import re, sys

names = {}

def opendb(path):
    x=open(path).read()

commands = {'open': opendb}

COMMAND = 'COMMAND'
STRING  = 'STRING'
NUM     = 'NUM'
FLAG    = 'FLAG'
NAME    = 'NAME'

def dictMerge(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def lex(com):
    tags = [
        (r'^[^ ]+',                 COMMAND),
        (r'(\'.*\'|".*")',          STRING),
        (r'(\s--|#|//).*',          None),
        (r'-[a-zA-Z]',              FLAG),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', NAME),
        (r'[0-9]+(.[0-9]+)?',       NUM),
        (r'[\s\t\n]',               None)
        ]
    pos = 0
    tokens = []
    while pos < len(com):
        match = None
        for t in tags:
            pattern, tag = t
            regex = re.compile(pattern)
            match = regex.match(com, pos)
            if match:
                text = match.group(0)
                if tag == STRING:
                    text=text.strip('\'').strip('"')
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % com[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

def parse(lexed):
    r={
    'args':[]
    'flags':{}
        }
    if lexed[0][1] == COMMAND:
        r[COMMAND]=lexed[0][0]
        lexed=lexed[1:]
    else:
        raise ValueError('Something went wrong')

    relexed=lexed
    for x in range(len(lexed)-1):
        if lexed[x][1] == FLAG:
            if lexed[x+1][1] == NUM:
                r['flags'][lexed[x][0]] = float(lexed[x+1][0])
            elif lexed[x+1][1] == NAME:
                r['flags'][lexed[x][0]] = names[lexed[x+1][0]]
            
        else:
            if lexed[x][1] == NUM:
                r['args'].append(float(lexed[x][0]))
            elif lexed[x][1] == NAME:
                r['args'].append(names[lexed[x][0]])
            
    #r['args'] = [x[0] for x in relexed]
    return r

if __name__ == '__main__':
    while True:
        print(parse(lex(raw_input())))
