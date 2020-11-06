import re

expresion = '1 2222 3 4 -5 3213 3333 1+++++++++1 1+2+3*4   ++++++   -+ - ++ =/%^    5'

m_number = '^|\s+[-]{0,1}[0-9]+\s+|\Z|$'

nnumber = "(?P<number_calc>(?=\s)*[+-/%*^]{0,1}[-]{0,1}([0-9]+))"

m_sign = '^|\s[+-/%^]+\s|\Z|$'

just_numbe_and_sign = '.*^|\s+[+-*%/]+[-]{0,1}[0-9]+$|\s+'

reg = m_number+'|'+m_sign
#a = re.compile("(([-]{0,1}[0-9]+[-+/^%*][-]{0,1}[0-9]+)([-+/^%*][-]{0,1}[0-9]+)*) | (/s+[-]{0,1}[0-9]+/s+) | ((\s)+[+-/%*^]*(\s)+)")
a = re.compile(nnumber)
m = a.split(expresion)

print (m)

for a in m:
    print (a)
