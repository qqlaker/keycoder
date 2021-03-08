with open('values.txt') as f:
   count = sum(1 for _ in f)
f = open('values.txt', 'r+')
b = True
list = []
for i in range(count):
		st = f.readline().split()
		stt = []
		try:
			if st[1].find('KEY_')!=-1:
				stt.append(st[1])
				stt.append(st[2])
		except:
			pass
		if stt:
			list.append(stt)
f.close()
for i in range(len(list)):
	print(list[i][0], list[i][1])