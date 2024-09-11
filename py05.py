# regex example

import re

txt = '  '
result = re.sub("\s", ",", txt) # Reemplaza Sustituye los espacios por comas ; \s = espacios
print(result)

