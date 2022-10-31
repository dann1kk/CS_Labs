from abc import abstractmethod

class Cipher:
    
    @abstractmethod
    def encrypt(message):
        pass
    @abstractmethod
    def decrypt(message):
        pass