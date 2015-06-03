import re, mimetypes, os, sys, datetime, re
from BaseServers import *
import users


settings={}
rw={}

def loadConfig():#Open configuration files and save their options to settings
    print('Loading configuration files')
    print('\tLoading settings...')                
    
    for root, dirs, files in os.walk('config/settings/'): #Open all files in config directory
        for f in files:
            if f.endswith('.cfg'):
                for x in open('config/settings/'+f).read().split('\n'): #Separate lines in file and iterate
                    if not x[0]=='#':
                        settings[x.split('=')[0]]=x.split('=')[1] #Set the option before the equal sign in the config file line to the value in the settings dict

    print('\tLoading rewrite...')    
    for root, dirs, files in os.walk('config/rewriter/'):
        for f in files:
            if f.endswith('.cfg'):
                for x in open('config/rewriter/'+f).read().split('\n'):
                    if not x[0]=='#':
                        rw[x.split('=')[0]]=x.split('=')[1]
                        
    
def log(s):
    logcont='\n['+str(datetime.datetime.now())+']: '+s
    print(logcont)
    open('logs/server.log', 'w+').write(logcont)

class WalrusSocialServer(BaseHTTPRequestHandler):
    def log_request(*args):
        pass
    def log_message(*args):
        pass
    
    def logCommand(self):
        log(self.client_address[0]+' on port '+str(self.client_address[1])+' to '+self.headers.get('host')+': \''+self.command+' '+self.path+'\', interpreted as \''+self.command+' '+self.getPath()+'\'') #Log the time and client address/client port of a request, followed by the request submitted and what it was interpreted to.
    
    def requestAcceptable(self):
        tests = []
        p=self.getPath()
        #for x in allowedFileTypes:
        #    if p.endswith(x):
        #        tests.append(True)
        #        break
        tests.append(True)
        #else:
        #    tests.append(False)
        return(all(tests))
        
    def getPath(self):
        p=self.path
        for x in rw:
            if x.match(p):
                p=rw[x]
                break
        return 'pages'+p

    def sendHeaders(self):
        p=self.getPath()
        self.send_response(200)
        if self.path.endswith('.html'):
            self.send_header('Content-type', mimetypes.guess_type(p)[0])
        elif self.path.endswith('.css'):
            self.send_header('Content-type', 'text/css')
        elif self.path.endswith('.js'):
            self.send_header('Content-type', 'application/javascript')
        self.end_headers()

    def do_HEAD(self):
        self.sendHeaders()
        
    def do_GET(self):
        self.logCommand()
        p=self.getPath()
        if self.requestAcceptable():
            log('Request Acceptable')
            self.sendHeaders()
            self.wfile.write(open(p).read())
        else:
            log('Request Unacceptable')

    def do_POST(self):
        pass


def serve():
    s=HTTPServer(('', 80), WalrusSocialServer)
    log('Server Starts')
    s.serve_forever()
serve()
