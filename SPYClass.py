import sqlite3
import spotipy
import spotipy.util as util
from Track import Track

token = util.prompt_for_user_token(
    username='obMGhnVyTjq343ACV4ObsA',
    scope='playlist-read-private user-top-read playlist-modify-public',
    client_id='cc9c32ea491645e6a5f3f52b473db65f',
    client_secret='c9f9c261c089491ebdde33eb8ea84eeb',
    redirect_uri='http://google.com/')

sp = spotipy.Spotify(auth=token)


class APISFY():
    def get_track_info(self, song,artist):
        if token:
            sp.trace = False
            results = sp.search(q='artist:' + artist + ' track:' + song)
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
                return objectTrack
            return ("Can't find the song")
        return("Can't get token for", token)


class DBSFY():
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
        except:
            print("Error en constructor")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GUARDARTRACK

    def saveTrack(self, Track):
        #Primero revisemos los elementos de track,la estructurra del objeto track y las conexiones
        # print ("[DEBUG 'Track.uri_track'] ",Track.uri_track)
        # print ("[DEBUG 'Track.name'] ",Track.name)
        # print ("[DEBUG 'Track.artist'] ",Track.artist)
        # print ("[DEBUG 'Track.album'] ",Track.album)
        # print ("[DEBUG 'Track.duration'] ",Track.duration)
        # #validar uri
        if Track==None:
            print("Track is null")
            return 1

        if (not isinstance(Track.uri_track, str)) or Track.uri_track==(" " or "")  or Track.uri_track==None or len(Track.uri_track)==0  or len(Track.uri_track)!=22 :
            print("Error en uri_track [if]", Track.uri_track)
            return 1
        for x in Track.uri_track:
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
            showTracks = self.cur.execute("SELECT ID FROM Track where ID = ?",(Track.uri_track,)).fetchall()
            # print(showTracks,len(showTracks))
        except:
            print("Error en validar que no se repita")
            return 1
        if len(showTracks)>0:
            print("Error el track "+Track.uri_track+" ya existe")
            return 1
        if self.cur.execute("INSERT INTO Track VALUES (?,?,?,?,?)",(Track.uri_track,Track.name,Track.artist,Track.album,Track.duration)):
                return 0
        print ('Error en ejecucion de query')
        return 1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< BORRAR TRACK
    def deleteTrack(self, name):
        try:
            self.cur.execute("DELETE FROM Track WHERE Name = ?",name)
            return (0)
        except:
            return 1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MOSTRAR TRACKS

    def mostrarTracks(self):
        try:
            showTracks = self.cur.execute("SELECT * from Track").fetchall()
            tracks = []
            i = 0
            for t in showTracks:
                tracks.append(Track(t[0], t[1], t[2], t[3], t[4]))
                i+=1
            if len(tracks)>0:
                return tracks
            return "Nada que mostrar"
        except:
            return 1
