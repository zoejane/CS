# User Instructions
# 
# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
#


import cgi
def escape_html(s):
    return cgi.escape(s, quote = True)

#Versioin 2
'''def escape_html(s):
    for (i,o) in (('&','&amp;'),
                  ('"','&quot;'),
                  ('<','&lt;'),
                  ('>','&gt;')):
        s = s.replace(i,o)
    return s'''


#Version 1
'''def escape_html(s):
    a = s.replace('&','&amp;')
    q = a.replace('"','&quot;')
    l = q.replace('<','&lt;')
    g = l.replace('>','&gt;')
    return g'''

print escape_html('"hello, &=&amp;"')

