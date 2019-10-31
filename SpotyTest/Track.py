
class Track:

    def __init__(self,uri_track, name, artist, album, duration):
        self.uri_track = uri_track
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        if self.uri_track != None:
            return str(f"El track es: {self.name}" +
                      f" de {self.artist}"+
                       f" del album {self.album}"+"\n")
        else:
            return str(f"El track es:" + "\n" + f"Name -> {self.name}"
                       + "\n" + f"Artist -> {self.artist}" +
                       "\n" + f"Album -> {self.album}" + "\n")

