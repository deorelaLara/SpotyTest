import sqlite3
import SPYAbs
import DBAbs
import spotipy
import spotipy.util as util
from Track import Track

token = util.prompt_for_user_token(
    username='akralma',
    scope='playlist-read-private user-top-read playlist-modify-public',
    client_id='3225d7bdc4e8402486b5d0ffeee3c81b',
    client_secret='1c328c97d6324ca4a3c0b9f5f4ae8f80',
    redirect_uri='http://www.google.com')

sp = spotipy.Spotify(auth=token)

class APISFY(SPYAbs.SFYSERVICE):
    def searchTracks(self, song, artist):
        if token:
            sp.trace = False
            results = sp.search(q='artist:' + artist + ' track:' + song,limit=1)
            print(results)
            if results != None:
                for track in results['tracks']['items']:
                    print(track['name'] + ' - ' + track['artists'][0]['name'])
                return track['id']
            else:
                print("Ningun resultado en la busqueda")


    def get_track_info(self, song,artist):
        if token:
            sp.trace = False
            results = sp.search(q='artist:' + artist + ' track:' + song)
            print(results)
            for track in results['tracks']['items']:

                id_track = track['id']
                name = track['name']
                artist = track['artists'][0]['name']
                album = track['album']['name']
                duration = track['duration_ms']

            objectTrack = Track(id_track,name,artist,album,duration)
            return objectTrack
        else:
            print("Can't get token for", token)



class DBSFY(DBAbs.DBService):
    def __init__(self, archivo):
        self.con = sqlite3.connect(archivo)
        self.cur = self.con.cursor()

    def saveTrack(self, Track):
        self.cur.execute("INSERT INTO Track VALUES "
                         "('{}','{}','{}','{}','{}')".format(Track.uri_track,Track.name,Track.artist,Track.album,Track.duration))

    def deleteTrack(self, name):
        self.cur.execute("DELETE FROM Track WHERE Name = ?",(name,))
        self.con.commit()
        return ("Track Eliminado")

    def mostrarTracks(self):
        showTracks = self.cur.execute("SELECT * from Track").fetchall()

        tracks = []
        i = 0
        for t in showTracks:
            tracks.append(Track(t[0], t[1], t[2], t[3], t[4]))
            i+=1

        return tracks

