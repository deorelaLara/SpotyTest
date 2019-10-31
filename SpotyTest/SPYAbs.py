from abc import ABC, abstractmethod

class SFYSERVICE(ABC):
    @abstractmethod
    def buscarNombre(self, trackName, artist):
        pass
