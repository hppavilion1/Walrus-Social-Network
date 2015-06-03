from sanitize import *
from passlib.hash import sha256_crypt
from datetime import date

class user:
    def __init__(self, username, name, password, (birthyear, birthmonth, birthdate), gender):
        self.name = sanitize(name)
        self.username = santize(username)
        self.password = hash = sha256_crypt.encrypt(password)
        self.birthyear = birthyear
        self.birthmonth = birthmonth
        self.birthday = birthday
        self.gender = gender
        
    def __str__(self):
        return(self.username+';'+self.password+';'+self.name+self.birthyear+'-'+self.birthmonth+'-'+self.birthday+';'+self.gender)
    
