fr = open ('18529.txt','rU')
#fw = open ('/Users/yf67/nmr_data/KRASB13C15N/15N_1Hlist','w')
lines = [line.split() for line in fr]
fr.close()

Single_Code = {
    'ALA':'A',
    'GLU':'E',
    'ASP':'D',
    'GLN':'Q',
    'ASN':'N',
    'GLY':'G',
    'PHE':'F',
    'TRP':'W',
    'TYR':'Y',
    'PRO':'P',
    'ILE':'I',
    'LEU':'L',
    'VAL':'V',
    'SER':'S',
    'HIS':'H',
    'CYS':'C',
    'THR':'T',
    'LYS':'K',
    'ARG':'R',
    'MET':'M',
}

class AtomAssignment(object):
    def __init__(self, row):
        n, aa, atom, csv = row
        self.n = int(n)
        self.aa = Single_Code[aa]
        self.atom = atom
        self.csv = float(csv)

    def __repr__(self):
        return "AtomAssignment({!r}, {!r}, {!r}, {!r})".format(self.n, self.aa, self.atom, self.csv)

    #def peak_list_1d(self):
        #return "{n}{aa}{atom} {csv}".format(n=self.n, aa=self.aa, atom=self.atom, csv=self.csv)

    def peak_list_1d(self):
        return "{}{}{} {}".format(self.n, self.aa, self.atom, self.csv)

cs = [AtomAssignment(line) for line in lines]

def peak_list_2d_i(assi1, assi2):
     #assi2.n + assi2.aa + assi2.atom + '-' + assi1.atom + ' ' + assi2.csv + ' ' + assi1.csv
    return "{}{}{}-{} {} {}".format(assi2.n, assi2.aa, assi2.atom, assi1.atom, assi2.csv, assi1.csv)
def peak_list_2d_i_1(assi1, assi2):
    return "{}{}{}-{}{}{} {} {}".format(assi2.n, assi2.aa, assi2.atom, assi1.n, assi1.aa, assi1.atom, assi2.csv, assi1.csv)
def peak_list_3d_i(assi1,assi2,assi3):
    return "{}{}{}-{}-{} {} {} {}".format(assi3.n, assi3.aa, assi3.atom, assi2.atom, assi1.atom, assi3.csv, assi2.csv, assi1.csv)
def peak_list_3d_i_1(assi1, assi2, assi3):
    return "{}{}{}-{}{}{}-{} {} {} {}".format(assi3.n, assi3.aa, assi3.atom, assi2.n, assi2.aa, assi2.atom, assi1.atom, assi3.csv, assi2.csv, assi1.csv)




#print(cs[5])
#print(cs[5].n)
#print(cs[5].aa)


#for i, (n, aa, atom, csv) in enumerate(cs): #being replaced by self.aa=Single_Code[aa]
#    cs[i].aa = Single_Code[aa]
#print cs

#1D
for assi in cs:
    if assi.atom == 'H':
        print assi.peak_list_1d()




#2D
for assi1 in cs:
    for assi2 in cs:
        #resi i
        if assi1.atom == 'H' and assi2.atom == 'CA':
            if assi1.n == assi2.n:
                print peak_list_2d_i(assi1, assi2)
                #print assi2.n + assi2.aa + assi2.atom + '-' + assi1.atom + ' ' + assi2.csv + ' ' + assi1.csv
            # resi i-1
            elif assi1.n == assi2.n+1:
                print peak_list_2d_i_1(assi1, assi2)

#import sys
#sys.exit()

#3D
for assi1 in cs:
    for assi2 in cs:
        for assi3 in cs:
            #resi i
            if assi1.n == assi2.n and assi2.n == assi3.n:
                if assi1.atom == 'H' and assi2.atom == 'N' and assi3.atom == 'CA':

                    print peak_list_3d_i(assi1, assi2, assi3)
                # resi i-1
            elif assi1.n == assi2.n and assi2.n == assi3.n+1:
                if assi1.atom == 'H' and assi2.atom == 'N' and assi3.atom == 'CA':
                    print peak_list_3d_i_1(assi1, assi2, assi3)
