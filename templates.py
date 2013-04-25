#templates.py

import fileinput, re

#match string in {}
field_pat = re.compile(r'\[(.+?)\]')

#gather the param
scope = {}

#use for re.sub
def replacement(match):
    code = match.group(1)
    try:
        #
        return str(eval(code, scope))
    except SyntaxError:
        exec code in scope
        return


lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

print field_pat.sub(replacement, text)
