import re

f = open('values.txt', 'r+')
string = f.read()
f.close()

while True:
	if '#define' is in string:
		

'''for i in range(len(string)):
	if (string[i] == '/') and (string[i+1] == '*'):
		while (string[i] != '*') and (string[i+1] != '/'):
			del(string[i])'''