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
        #prueba de guardar un track correctamente _/
        # un track raro, tracks iguales _/,track malo
        #track nulo _/ ,
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

        objBDD=DBSFY('Arma_tu_biblio.db')

        # # CASO DE PRUEBA: UN TRACK CORRECTO **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
        # objTrack=Mock_Track('58MZs0B5Amxl0Mwc9FIRZc','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # objBDD.saveTrack(objTrack)
        # a=objBDD.mostrarTracks()
        # print(a[0].__str__())
        # self.assertEqual((a[0]).__str__(),"El track es: DARE - Junior Sanchez Remix de Gorillaz del album D-Sides [Special Edition]")



        #CASO DE PRUEBA DE UN TRACK NULO **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
        # print("TEST CASE: TRACK NULO")
        # objTrack=None
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # self.assertEqual(a,1)

        #CASO DE PRUEA: EL TRACK  YA EXISTE **************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASE
        # print("TEST CASE: EL TRACK YA EXISTE")
        # objTrack=Mock_Track('58MZs0B5Amxl0Mwc9FIRZc','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # b=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if b==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # si se guarda la primera vez
        # self.assertEqual(b,1) # no se guarda la segunda vez
        # m=objBDD.mostrarTracks()
        # self.assertEqual(len(m),1)#validar que solo se haya guardado uno

        # CASOS DE PRUEBA: PRUEBAS A uri_track *************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASES URI
        # print("TEST CASE: uri_track es ' ' ") #**************************************************************************
        # objTrack=Mock_Track(' ','DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack= None
        # print("TEST CASE: uri_track es None ") #**************************************************************************
        # objTrack=Mock_Track(None,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack = None
        # # continuar con string,float, zero pading, negatives, more than len and different
        # print("TEST CASE: uri_track es MAYOR A 22") #**********************************************************************
        # objTrack=Mock_Track('A'*23,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack= None
        # # caracteres no imprimibles y algunos especiales
        # print("TEST CASE: uri_track tiene caracteres especiales") #*******************************************************
        # objTrack=Mock_Track('@'*22,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        # #checar con float
        # print("TEST CASE: uri_track float") #*****************************************************************************
        # objTrack=Mock_Track(234567890123456789.00,'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,1) # no lo guarda
        # objTrack=None
        # print("TEST CASE: uri_track tiene padding de ceros") #************************************************************
        # objTrack=Mock_Track(("0"*20)+"22",'DARE - Junior Sanchez Remix','Gorillaz','D-Sides [Special Edition]', 326373)
        # objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        # a=objBDD.saveTrack(objTrack)
        # print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        # self.assertEqual(a,0) # lo guarda
        # objTrack= None

        # CASOS DE PRUEBA: PRUEBAS A NAME *************************************** <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST CASES NAME
        print("TEST CASE: name es ' ' ")  #**************************************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',' ','Gorillaz','D-Sides [Special Edition]', 326373)
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,1) # no lo guarda
        objTrack=None
        print("TEST CASE: name es None ")  #**************************************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',None,'Gorillaz','D-Sides [Special Edition]', 326373)
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,1) # no lo guarda
        objTrack=None
        print("TEST CASE: name es MAYOR A 50") #**********************************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"B"*52,'Gorillaz','D-Sides [Special Edition]', 326373)
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,1) # no lo guarda
        objTrack=None
        print("TEST CASE: name tiene caracteres especiales") #*******************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"Dare",'Gorillaz','D-Sides [Special Edition]', 326373)
        objTrack.name="@#$%%&/()="
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,0) # lo guarda por que aun no se ha definido esta validacion
        objTrack=None
        # checar con int
        print("TEST CASE: name int como int") #*****************************************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',1234,'Gorillaz','D-Sides [Special Edition]', 326373)
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        objTrack= None
        print("TEST CASE: name int como string") #***************************************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"1234",'Gorillaz','D-Sides [Special Edition]', 326373)
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,0) # lo guarda por que esta como string
        objTrack = None
        print("TEST CASE: name flaot como tal") #****************************************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',1234.5,'Gorillaz','D-Sides [Special Edition]', 326373)
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,1) # no lo guarda por que acepta solo strings
        objTrack= None
        print("TEST CASE: name float como string") #***************************************************************************
        objTrack=Mock_Track('AAAAAAAAAAAAAAAAAAAAAA',"1234.5",'Gorillaz','D-Sides [Special Edition]', 326373)
        objBDD.cur.execute("DELETE FROM Track")#limpiamos la base de datos
        a=objBDD.saveTrack(objTrack)
        print(objTrack.uri_track, "guardado") if a==0 else print(objTrack.uri_track,"No guardado")
        self.assertEqual(a,0) # lo guarda por que esta como string
        objTrack=None
        # aun falta validar mas detalles, mas casos de prueba y mejorar el codigo




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
