import re, mimetypes, os, sys, datetime
from BaseServers import *

def log(s):
    print('['+str(datetime.datetime.now())+']: '+s)

allowedFileTypes = ['.html', '.css', '.js']

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
        for x in allowedFileTypes:
            if p.endswith(x):
                tests.append(True)
                break
        else:
            tests.append(False)
        return(all(tests))
        
    def getPath(self):
        return 'Pages'+self.path

    def sendHeader(self):
        p=self.getPath()
        self.send_response(200)
        if self.path.endswith('.html'):
            self.send_header('Content-type', mimetypes.guess_type(p)[0])
        elif self.path.endswith('.css'):
            self.send_header('Content-type', 'text/css')
        elif self.path.endswith('.js'):
            self.send_header('Content-type', 'application/javascript')
        self.end_headers()
    
    def do_GET(self):
        self.logCommand()
        p=self.getPath()
        if self.requestAcceptable():
            log('Request Acceptable')
            self.sendHeader()
            self.wfile.write(open(p).read())
        else:
            log('Request Unacceptable')


def serve():
    s=HTTPServer(('', 80), WalrusSocialServer)
    log('server starts')
    s.serve_forever()
serve()
