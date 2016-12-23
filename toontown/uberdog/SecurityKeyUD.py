import pyotp, string, random

class SecurityKeyUD:
    def __init__(self, air):
        self.air = air
        
    def enable(self):
        self.__totp = pyotp.TOTP("DEMOSECRET")
        
    def match(self, key):
        curKey = self.__totp.now()
        print key, curKey
        return str(key) == curKey
