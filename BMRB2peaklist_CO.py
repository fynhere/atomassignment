fr = open ('/Users/ellenfu/Dropbox/lessons/python/work/18529.txt','r')
#fw = open ('/Users/yf67/nmr_data/KRASB13C15N/15N_1Hlist','w')
#CS = fr.readline()
#fr.close()


#fw = open ('/Users/yf67/Sparky/Lists/KRAS/HCO_list','w')
for line in fr:
    ls = line.split()
    print ls
    for c in range(len(ls)):
        if ls[c] == 'C':
            #fw.write ()


#fw.close()
