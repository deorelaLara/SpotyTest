import sqlite3
import spotipy
import spotipy.util as util
from Track import Track




def Leer_Credenciales(ruta):
    archivo = open(ruta, 'r')
    credenciales = []
    for linea in archivo:
        cadena = ''
        espacio = 0
        texto = str(linea).strip()
        for i in range(0,len(texto)):
            if texto[i] == ' ':
                espacio +=1
            if espacio == 1 and texto[i] != ' ':
                cadena += texto[i]

        credenciales.append(cadena)
    archivo.close()
    return credenciales





class APISFY():
    sp=None
    def __init__(self):
        credentials=Leer_Credenciales("credenciales.txt")
        token = util.prompt_for_user_token(
            username=credentials[0],
            scope=credentials[3],
            client_id=credentials[1],
            client_secret=credentials[2],
            redirect_uri=credentials[4])
        self.sp = spotipy.Spotify(auth=token)

    def getTrackfromSpotify(self, song,artist): #busca en spotify
        if token:
            self.sp.trace = False
            results = self.sp.search(q='artist:' + artist + ' track:' + song)
            #print(results['tracks']['items'])
            if len(results['tracks']['items'])!=0:
                #print(results)
                for track in results['tracks']['items']:
                    id_track = track['id']
                    name = track['name']
                    artist = track['artists'][0]['name']
                    album = track['album']['name']
                    duration = track['duration_ms']
                objectTrack = Track(id_track,name,artist,album,duration)
                return objectTrack #regresa el objeto track
            print ("Can't find the song")
            return 1
        print ("Can't get token for", token)
        return 1

    def getPlaylistfromSpotify(self): #obtener mi playlist desde spotify
        lib = self.sp.current_user_saved_tracks()
        for track in lib['items']:
            print(track)
            print()
        return lib

    def printPlaylist(self,playlist): #imprimir playlist desde la bdd
        if len(playlist)<1:
            print("Nada en tu Playlist")
            return 1
        play_String=""
        i=0
        for t in playlist:
            if i==len(playlist)-1:
                play_String+="{ID: "+str(i)+" "+str(t)+"}"
            else:
                play_String+="{ID: "+str(i)+" "+str(t)+"}\n"
                i=i+1
        return play_String

#get track from spotify with id
    def getTrackfromPlaylistWithID(self,playlist,id):
        if playlist == None or id== None or len(playlist)<1 or id>len(playlist)-1:
            return 1
        return playlist[id]
#
#
#
class DBSFY():# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////DBSFY

    cur=None
    con=None
    def __init__(self, archivo):
        try:
            self.con = sqlite3.connect(archivo)
            self.cur = self.con.cursor()
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Track
            (ID Text,
            Name TeSxt,
            Artist Text,
            Album Text,
            Duration Text
            )
            ''')
            self.con.commit()
            self.con.close()
        except:
            print("Error en constructor")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GUARDARTRACK

    def saveTrack(self, Track):
        #Primero revisemos los elementos de track,la estructurra del objeto track y las conexiones
        print ("[DEBUG 'Track.uri_track'] ",Track.uri_track)
        print ("[DEBUG 'Track.name'] ",Track.name)
        print ("[DEBUG 'Track.artist'] ",Track.artist)
        print ("[DEBUG 'Track.album'] ",Track.album)
        print ("[DEBUG 'Track.duration'] ",Track.duration)
        #validar uri
        if Track==None:
            print("Track is null")
            return 1

        if (not isinstance(Track.id, str)) or Track.id==(" " or "")  or Track.id==None or len(Track.id)==0  or len(Track.id)!=22 :
            print("Error en uri_track [if]", Track.id)
            return 1
        for x in Track.id:
            if not (x.isnumeric() or x.isalpha()):
                print("Error en uri_track tiene caracteres especiales")
                return 1
        #validar name
        if (not isinstance(Track.name, str)) or Track.name==None or Track.name==" " or Track.name=="" or (len(Track.name)>50):
            print("Error en name ", Track.name)
            return 1
        #aqui es la validacion de caracteres maliciosos y sql iny.(pendiente)

        # #validar artista
        if (not isinstance(Track.artist, str)) or Track.artist==None or Track.artist==" " or Track.artist=="" or (len(Track.artist)>50):
            print("Error en artist ", Track.artist)
            return 1
        #aqui es la validacion de caracteres maliciosos y sql iny.(pendiente, tambien decidir si metemos las validaciones en metodos)

        #validar album
        if (not isinstance(Track.album, str)) or Track.album==None or Track.album==" " or Track.album=="" or (len(Track.album)>50):
            print("Error en album ", Track.album)
            return 1
        #aqui es la validacion de caracteres maliciosos y sql iny.(pendiente)

        #
        # #validar duracion
        if (not (isinstance(Track.duration,int)) or Track.duration==None or('.' or '-' or ',' or '' or ' ' or "'") in str(Track.duration)) or Track.duration>2147483647 or Track.duration<1:
            # duration=float(Track.duration)
            # duration=(duration/1000.00)/60.00
            # print ('float duration',duration)
            print('Error en la duracion ',Track.duration, type(Track.duration))
            return 1
        #valida que no se repita
        try:
            conect = sqlite3.connect('Arma_tu_biblio.db')
            cursor = conect.cursor()
            showTracks = cursor.execute("SELECT ID FROM Track where ID = ?",(Track.id,)).fetchall()
            print(showTracks,len(showTracks))
        except:
            print("Error en validar que no se repita")
            return 1
        if len(showTracks)>0:
            print("Error el track "+Track.id+" ya existe")
            return 1
        else:
            conect = sqlite3.connect('Arma_tu_biblio.db')
            cursor = conect.cursor()
            cursor.execute("INSERT INTO Track VALUES (?,?,?,?,?)",(Track.id,Track.name,Track.artist,Track.album,Track.duration))
            conect.commit()
            conect.close()
            return 0
        print ('Error en ejecucion de query')
        return 1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< BORRAR TRACK
    def deleteTrack(self, id_track):#debe pasarse el id
        try:
            conect = sqlite3.connect('Arma_tu_biblio.db')
            cursor = conect.cursor()
            cursor.execute("DELETE FROM Track WHERE ID = ?",id_track)
            conect.commit()
            conect.close()
            return 0
        except:
            return 1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MOSTRAR TRACKS

    def getPlaylistFromDB(self):
        try:
            conect = sqlite3.connect('Arma_tu_biblio.db')
            cursor = conect.cursor()
            showTracks = cursor.execute("SELECT * from Track").fetchall()
            tracks = []
            i = 0
            for t in showTracks:
                tracks.append(Track(t[0], t[1], t[2], t[3], t[4]))
                i+=1
            if len(tracks)>0:
                conect.close()
                return tracks
            conect.close()
            print("Nada que mostrar")
            return 1
        except:
            print("Error en consulta de playlist")
            return 1


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MOSTRAR TRACKS

    def updateBDDfromSpotify(self,library):
        #validat library y  verque no se repitan
        for item in library['items']:
            song = item['track']
            #se los manda en el update pero si se repiten
            iD = song['id']
            name = song['name']
            artist = song['artists'][0]['name']
            album = song['album']['name']
            duration = song['duration_ms']

            conect = sqlite3.connect('Arma_tu_biblio.db')
            cursor = conect.cursor()
                #REVISAR QUE NO SE REPITA AQIO
            cursor.execute("INSERT INTO Track VALUES"
                           "('{}','{}','{}','{}','{}')".format(iD, name, artist, album, duration))

            conect.commit()
            conect.close()

class sinchronize():

    def __init__(self):
        pass

        def updateBDDfromSpotify(self,librarySpotify,objBDD):
            #validat library y  verque no se repitan
            for item in librarySpotify['items']:
                song = item['track']
                #se los manda en el update pero si se repiten
                iD = song['id']
                name = song['name']
                artist = song['artists'][0]['name']
                album = song['album']['name']
                duration = song['duration_ms']

                # conect = sqlite3.connect('Arma_tu_biblio.db') objBDD afuera
                cursor = objBDD.cursor()
                    #REVISAR QUE NO SE REPITA AQIO

                try:
                    cursor.execute("INSERT INTO Track VALUES ('{}','{}','{}','{}','{}')".format(iD, name, artist, album, duration))
                    conect.commit()
                    conect.close()
                except:
                    print("Error in updateBDDfromSpotify")


        def updateSpotifyfromBDD(self,librarySpotify,libraryBDD):
            #validat library y  verque no se repitan
            for item in library['items']:
                song = item['track']
                #se los manda en el update pero si se repiten
                iD = song['id']
                name = song['name']
                artist = song['artists'][0]['name']
                album = song['album']['name']
                duration = song['duration_ms']

                conect = sqlite3.connect('Arma_tu_biblio.db')
                cursor = conect.cursor()
                    #REVISAR QUE NO SE REPITA AQIO
                cursor.execute("INSERT INTO Track VALUES"
                               "('{}','{}','{}','{}','{}')".format(iD, name, artist, album, duration))

                conect.commit()
                conect.close()


        def checkBDDvsSpotify(self, librarySpotify,objBDD):
            #PRIMERO TRAETE LA Libreria DE Spotify
            #DESPUES LA libreria DE LA BASE DE DATOS
            #COMPARA QUE ESTEN IGUALES
            #SI NO ESTAN IGUALES BORRAS LA BDD
            #Y PONES LO DE LA PLAYLIST DE SPOTIFY
            pass
