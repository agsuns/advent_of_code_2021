import re

string = '  0 2 4 4543     94 9   '
string = string.strip()

print(string)

string = re.sub(" {2,}", ' ', string)
print(string)


