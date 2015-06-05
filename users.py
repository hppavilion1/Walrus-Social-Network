import WalDB
from passlib.hash import sha256_crypt
from datetime import date

minPassLen = 8
minUnLen = 1

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
