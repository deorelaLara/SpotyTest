
from SPYClass import APISFY
from SPYClass import DBSFY
import spotipy
from spotipy import util
import sys
import sqlite3

token = util.prompt_for_user_token(
    username='akralma',
    scope='user-library-modify user-library-read',
    client_id='3225d7bdc4e8402486b5d0ffeee3c81b',
    client_secret='1c328c97d6324ca4a3c0b9f5f4ae8f80',
    redirect_uri='http://www.google.com')

sp = spotipy.Spotify(auth=token)

#Devuelve informacion del track
def search_info(apisfy):
    song = input("Como se llama la rola: ")
    artist = input('¿Quien la canta?: ')

    info = apisfy.get_track_info(song, artist)
    if song:
        print(info)
        return info
    else:
        'La canción no existe'

 #Guarda info en DB
def save_track(dbsfy, info):
    print(dbsfy.saveTrack(info))

 #Borra info DB
def del_track(dbsfy, name):
    dbsfy.deleteTrack(name)

 #Muestra info DB
def show_track(dbsfy):
    print(dbsfy.showTracks())


def main():
    apisfy = APISFY()
    dbsfy =  DBSFY('Arma_tu_biblio.db')

    print('Bienvenido akralma, ¿Que quieres hacer?')
    cont = 0
    option = int(input('1. Buscar canción' + '\n' +
                       '2. Ver tu biblioteca' + '\n' +
                       '3. Modificar tu biblioteca' + '\n'
                       '4. Salir' + '\n' +
                       '5. Migrar Datos' + '\n'))

    library = sp.current_user_saved_tracks()

    while cont ==0:
        if option == 1:

            list_tracks = []
            track = search_info(APISFY)
            print('¿Quieres agregar esta cancion a tu biblioteca?')
            save = int(input('1. Si' + '\n' + '2. No' + '\n'))

            if save == 1:
                list_tracks.append(track.id)
                sp.current_user_saved_tracks_add(list_tracks)  # Guarda en biblioteca
                save_track(dbsfy, library) #Guarda archivo en DB
                print('La canción ha sido agregada' + '\n')
            elif save == 2:
                print(option)

        if option == 2:
            show_track(dbsfy)

        if option ==3:
            name = input('¿Cual cancion quieres eliminar?: ' + '\n')
            del_track(dbsfy, name)

            print('¿Quieres seguir eliminando?' + '\n')
            stop = int(input('1.Si ' + '2. No' + '\n'))

            if stop == 1:
                print(name)
            else:
                print(option)


        if option == 4:
            sys.exit()

        if option == 5:
            library = sp.current_user_saved_tracks()

            for item in library['items']:
                song = item['track']

                iD = song['id']
                name = song['name']
                artist = song['artists'][0]['name']
                album = song['album']['name']
                duration = song['duration_ms']

                conect = sqlite3.connect('Arma_tu_biblio.db')
                cursor = conect.cursor()

                cursor.execute("INSERT INTO Track VALUES"
                               "('{}','{}','{}','{}','{}')".format(iD, name, artist, album, duration))

                conect.commit()
                conect.close()



if __name__ == '__main__':
    main()