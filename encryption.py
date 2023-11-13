'''file that implements encryption and decryption of data'''
class Encrypt():
    """
    class that encrypts data
    """
    def __init__(self) -> None:
        self.send =""
        self.res = []

    def sender(self):
        '''takes the data that should be encrypted'''
        self.send = input("Enter the data: ")
        self.res = [ord(i) for i in self.send]

    def receiver(self):
        '''receives the data and encrypts it'''
        print("Encrypted data is:","".join(chr(i-2) for i in self.res))

obj = Encrypt()
obj.sender()
obj.receiver()

class Decrypter():
    '''class that performs decryption of data'''
    def __init__(self) -> None:
        self.data =""
        self.res = []
    def decrypt(self):
        '''takes encrypted data and decrypts it'''
        self.data = input("Enter encrypted data: ")
        self.res = [ord(i) for i in self.data]
        print("Decrypted data is:","".join(chr(i+2) for i in self.res))
obj = Decrypter()
obj.decrypt()
