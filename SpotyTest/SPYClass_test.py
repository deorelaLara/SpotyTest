import unittest
import Track
import mock
from mock import patch
from SPYClass import APISFY

class testSpotipy(unittest.TestCase):

    def test_SearchTracks(self):
        track = 'Dare'
        artist = 'Gorillaz'
        #track_s = Track.__str__()
        res = APISFY.searchTracks(self, track, artist)
        print(res)
        #self.assertEqual(res, )


    def test_info_track(self):
            track = 'Dare'
            artist = 'Gorillaz'
            esp = 'El track es: DARE - Soulwax Remix de Gorillaz del album D-Sides'
            res = APISFY.get_track_info(self, track, artist)
            self.assertEqual(res, esp)
            print(res)
""""""

if __name__ == '__main__':
    unittest.main()