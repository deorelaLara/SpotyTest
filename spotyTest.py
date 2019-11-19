import Track
import mock
from mock import patch
from SPYClass import APISFY
from SPYClass import DBSFY
from SPYClass import sinchronize
import sqlite3


class Spotytest():

    api=None
    bdd=None
    sync=None

    def __init__(self,credentialsFilePath,BDDFIlePath ):
        sync=synchronize()
        bdd=DBSFY(BDDFIlePath)
        api=APISF(credentialsFilePath)
        #synchronize

    def addTrackToMyPlaylist(self,tracks):#must be a list of tracks
        api.saveTrack(tracks)

    def showMyPlaylist(self):
        playlist=bdd.getPlaylistFromDB()
        print(api.printPlaylist(playlist))


    def deleteTrack(self,idtrack): #pasarlo en forma de lista
        api.deleteTrack(idtrack)
        bdd.deleteTrack(idtrack)

    def deleteAllTracks(self):
        playlist_sp=api.getPlaylistsIDSfromSpotify()
        api.deleteTrack(playlist_sp)
        bdd.deleteAllTracks()

    def salir(self):
        bdd.close()
        bdd=None
        api=None

    def makeSync(self):
        unsync=[]
        unsync=sync.checkBDDvsSpotify()
        unsync.updateSpotifyfromBDD(api,unsync)
        unsync.updateBDDfromSpotify(api.getTrackslistfromSpotify(),bdd)
