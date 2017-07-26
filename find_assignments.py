from atomassignment import AtomAssignment

assignments = AtomAssignment.read('18529.txt')


for index, assignment in assignments.items():
    atom, cs = assignment.residue_assignments[0]
    if atom == 'H':
        print "{}{}H {}".format(index, assignment.aa_short, cs)


for index, assignment in assignments.items():
    atom, cs = assignment.residue_assignments[0]
    if atom == 'H':
        if 'N' in assignment.assignment_by_atom:
            n_cs = assignment.assignment_by_atom['N']
            print "{}{}N-H {} {}".format(index, assignment.aa_short, n_cs, cs)

for index, assignment in assignments.items():
    if index <= 1:
        continue
    previous_assignment = assignments[index-1]
    atom, cs = assignment.residue_assignments[0]
    if atom == 'H':
        if 'N' in assignment.assignment_by_atom and 'C' in previous_assignment.assignment_by_atom:
            n_cs = assignment.assignment_by_atom['N']
            c_cs = previous_assignment.assignment_by_atom['C']
            print "{}{}C-N-H {} {} {}".format(index, assignment.aa_short, c_cs, n_cs, cs)
