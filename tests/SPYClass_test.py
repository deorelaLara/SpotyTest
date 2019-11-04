import sys
sys.path.append('../')
import unittest
import Track
import mock
from mock import patch
from SPYClass import APISFY
from SPYClass import DBSFY
import sqlite3

class testSpotipy(unittest.TestCase):


    # def test_info_track(self):
    #         track = 'Dare'
    #         artist = 'Gorillaz'
    #         #esp = 'El track es: DARE - Soulwax Remix de Gorillaz del album D-Sides'
    #         res = APISFY.get_track_info(self, track, artist)
    #         #self.assertEqual(res, esp)
    #         print(res)

    def test_saveTrack(self):
        #prueba de guardar un track correcto
        # un track raro, tracks iguales,track malo
        #la base de datos no existe o no coinciden tablas o atributos
        #revisar la salida y labase de datos para asserts
        #mock de clase track
        class Mock_Track:
            def __init__(self,uri_track, name, artist, album, duration):
                self.uri_track = uri_track
                self.name = name
                self.artist = artist
                self.album = album
                self.duration = duration
        #CASO DE PRUEBA: UN TRACK CORRECTO
        objTrack=Mock_Track('58MZs0B5Amxl0Mwc9FIRZc','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        trackname='Dare'
        artistname='Gorillaz'
        objBDD=DBSFY('Arma_tu_biblio.db')
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        objBDD.saveTrack(objTrack)
        a=objBDD.mostrarTracks()
        for x in a:
            print (x) #paradebug
        # aqui va el assert
        #CASO DE PRUEBA DE UN TRACK INVALIDO


    # def test_deleteTrack(self):
        #aqui se probara solo el nombre
        #ahi que revisar primero que exista
        #prueba borrar track existente
        #borrar track que no existente
        #intentos de inyeccion
        #la base de datos no existe o no coinciden tablas o atributos



    # def test_mostrarTracks(self):
    # #revisar que pasa cuando no tienes nada en la labase
    #cuando la base de datos noesta
    #la conexion y lo que se extrae
    #     # conn = sqlite3.connect("./../Arma_tu_biblio.db")
    #     # cur = conn.cursor()
          #la base de datos no existe o no coinciden tablas o atributos

    #     obj=DBSFY('./../Arma_tu_biblio.db')
    #     showTracks = obj.mostrarTracks()
    #     print(showTracks)
    #

if __name__ == '__main__':
    unittest.main()
