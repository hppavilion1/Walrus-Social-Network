import pickle #For saving the DB
import re #For checking columns
import passlib #For hashing and salting passwords

def loadTable(path):
    global tb
    tb = pickle.load(path)

class column(list):
    pass

class passwords(column):
    pass

class usernames(column):
    pass

class emails(column):
    

class domains(column):
    pass

class Table(dict):
    def check(self):
        return all([self.checkRowLens(), self.checkColumnLens()])

    def checkRowLens(self):
        li = [x for x in self]
        r=[]
        for x in li[1:]:
            r.append(len(x) == len(li[0]))
            if li[-1] == False:
                break
        
        return all(r)
                

    def checkColumnLens(self):
        return True

    def selectRow(self, num):
        r={}
        for x in self:
            r[x] = self[x][num]

    def selectColumn(self, num):
        return None

    def save(self, path):
        with open(path, 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def getslice(self, i, j):
        return(self[i][j])

    def addRow(self):
        
