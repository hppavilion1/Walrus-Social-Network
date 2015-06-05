import pickle #For saving the DB
import re #For checking columns

def loadTable(path):
    global tb
    tb = pickle.load(path)

class TableIntegrityError(Exception):
    pass

class column(list):
    def check_integrity(self):
        pass

class uids(column):
    def check_integrity(self):
        if not all([isinstance(x, int) for x in self]) and len(set(self)) == len(self):
            raise TableIntegrityError('User id found that is not unique int')

class passwords(column):
    pass

class usernames(column):
    def check_integrity(self):
        if not len(set(self)) == len(self):
            raise TableIntegrityError('Repeated Username')


class names(column):
    pass

class emails(column):
    pass

class domains(column):
    pass

class ips(column):
    pass

class Table(dict):
    def initialize(self):
        self.width=0
        self.height=0
    def check_table(self):
        return all([self.checkRowLens(), self.checkColumnLens()])

    def check_row_lens(self):
        li = [x for x in self]
        r=[]
        for x in li[1:]:
            r.append(len(x) == len(li[0]))
            if li[-1] == False:
                break
        
        return all(r)
                
    def check_column_lens(self):
        return True

    def select_row(self, num):
        r={}
        for x in self:
            r[x] = self[x][num]

    def select_column(self, num):
        return None

    def save(self, path):
        with open(path, 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def add_row(self, vals):
        i=0
        for x in self:
            x.append(vals[j])
            x.check_integrity()
            i+=1
        width+=1
            
    def add_column(self, name, thing):
        self[name]=thing
        self[name].check_integrity()
        height+=1

    def delete_row(self, i):
        for x in self:
            del self[x][i]
        width-=1

    def delete_column(self, i):
        del self[i]
        height-=1

    def insert_row(self, i):
        j=0
        for x in self:
            x.insert(vals[j], i)
            x.check_integrity()
            j+=1
        width+=1

    def set_cell(self, i, j, value):
        self[i][j]=value
        self[i].check_integrity()

    def get_cell(self, i, j):
        return self[i][j]

    def clear_cell(self, i, j):
        self[i][j] = None
        self[i].check_integrity()

    def clear_column(self, name):
        self[name] = [None for x in range(self.height)]

    def clear_row(self, name):
        for x in self:
            self[x] = None

    def set_column(self, name, value):
        self[name] = [value for x in range(self.height)]

    def set_row(self, name, value):
        for x in self:
            self[x] = value
