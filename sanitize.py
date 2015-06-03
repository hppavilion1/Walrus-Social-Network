import htmlentitydefs as entity

def stripCCs(inp):

    if inp:

        import re

        # unicode invalid characters
        RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                         u'|' + \
                         u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                          (unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                           unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                           unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                           )
        inp = re.sub(RE_XML_ILLEGAL, '', inp)

        # ascii control characters
        inp = re.sub(r'[\x01-\x1F\x7F]', '', inp)

    return inp

def sanitize(s):
    t = ''
    for i in s:
        if ord(i) in entity.codepoint2name:
            name = entity.codepoint2name.get(ord(i))
            t += '&' + name + ';'
        else:
            t += i
    return striptCCs(t.replace(';', '')) #To prevent table modification and control characters
