gene_of_interest = input('Please enter the name of the gene you would like to amplify:')

def complementary(direction):
    c_seq = ''
    for i in range(len(direction)):
        x = direction[i]
        for j in range(len(x)):
            if x[j] == 'A':
                c_seq = c_seq + 'T'
            elif x[j] == 'T':
                c_seq = c_seq + 'A'
            elif x[j] == 'G':
                c_seq = c_seq + 'C'
            elif x[j] == 'C':
                c_seq = c_seq + 'G'
            elif x[j] == 'K':
                c_seq = c_seq + 'M'
    return(c_seq)

reference = 'ATCGTCCGAAATTGCATATTGATAG'

genes = {'ks41' : 'GAAA', 'ks42' : 'GTATG'}

x = genes[gene_of_interest]
print(x)

length = len(gene_of_interest)
print(length)

for i in range(len(reference)):
    if reference[i : i + length] == x:
        Reverse = reference[i + length : i + length + 6]
        Forward = reference[i - 6 : i]
        print('Forward Primer: {}'.format(complementary(Forward)))
        print('Reverse Primer: {}'.format(Reverse))
