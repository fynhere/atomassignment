import random
nuslist_file = open ('/Users/yinanfu/Dropbox/lessons/python/work/nuslist.txt','r')
#fw = open ('/Users/yf67/nmr_data/KRASB13C15N/15N_1Hlist','w')
nuslist = []
for line in nuslist_file:
    numbers = [
        int(n)
        for n in line.split()
    ]
    nuslist.append(numbers)
#print nuslist
nuslist_file.close()

for F2 in range(47):
    firstpointsF2 = [F2, 0]
    if firstpointsF2 not in nuslist:
        nuslist.append(firstpointsF2)

for F1 in range(50):
    firstpointsF1 = [0, F1]
    if firstpointsF1 not in nuslist:
        nuslist.append(firstpointsF1)

random.shuffle(nuslist)

newlist = open('newnuslist.txt', 'w')
for pair in nuslist:
    a = str(pair[0])
    b = str(pair[1])
    newlist.write(a.rjust(4)+' ')
    newlist.write(b.rjust(4)+'\n')

newlist.close()
