class CaesarCipher:
    '''A class for doing encryption and decryption using Caesar cipher.'''

    def __init__(self, shift):
        '''construct caesar cipher using given integer shift for rotation'''
        encoder = [None]*26 #temp array for encryption
        decoder = [None]*26 #temp array for decryption 