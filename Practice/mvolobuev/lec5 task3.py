import random
from string import Template

t = Template('Казнить$lang нельзя$lang1 помиловать.')
i = random.randint(0, 1)
if i == 0:
    p = t.substitute(lang=',', lang1='')
else:
    p = t.substitute(lang='', lang1=',')
print(p)
