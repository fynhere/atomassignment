SINGLE_CODE = {
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
    def __init__(self, index, aa):
        self.index = index
        self.aa = aa
        self.aa_short = SINGLE_CODE[aa]
        self.residue_assignments = []
        self.assignment_by_atom = {}

    def __repr__(self):
        return "<atom-assignment({!r}, {!r}, {!r})>".format(
            self.index, self.aa, self.residue_assignments)

    def add_pair(self, atom, cs):
        self.residue_assignments.append((atom, cs))
        self.assignment_by_atom[atom] = cs

    @classmethod
    def read(cls, filename):
        f = open(filename, 'rU')
        assignments = {}
        for line in f:
            index, aa, atom, cs = line.split()
            index = int(index)
            cs = float(cs)
            if index not in assignments:
                number_residue = cls(index, aa)
                assignments[index] = number_residue
            else:
                number_residue = assignments[index]
            number_residue.add_pair(atom, cs)
        f.close()
        return assignments


if __name__ == "__main__":
    assignments = AtomAssignment.read_assignment_file('18529.txt')
    print(assignments)
    print(assignments[100].assignments)
