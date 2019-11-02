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
    def get_track_info(song, artist):
        if token:
            sp.trace = False
            results = sp.search(q='artist:' + artist + ' track:' + song)
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

    def saveTrack(self, library):
        for item in library['items']:
            song = item['track']

            iD = song['id']
            name = song['name']
            artist = song['artists'][0]['name']
            album = song['album']['name']
            duration = song['duration_ms']

            self.cur.execute("INSERT INTO Track VALUES "
                             "('{}','{}','{}','{}','{}')".format(iD, name,artist, album,
                                                                 duration))
        self.con.commit()

    def deleteTrack(self, name):
        self.cur.execute("DELETE FROM Track WHERE Name = ?",(name,))
        self.con.commit()
        print("Track Eliminado")

    def showTracks(self):
        exc = self.cur.execute("SELECT DISTINCT Name, Artist from Track").fetchall()

        for c in exc:
            print(c[0] + ' - ' + c[1])

        self.con.commit()

