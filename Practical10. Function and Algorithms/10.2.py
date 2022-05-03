def Nucleotide_content_calculator(seq) :
    seq = seq.upper()
    # change the letters to uppercase
    length = len(seq)
    # measure the length of the gene sequence
    A_count = seq.count('A')
    T_count = seq.count('T')
    C_count = seq.count('C')
    G_count = seq.count('G')
    # count the number of A T C G nucleotides of the gene sequence.
    print('Percentage of A nucleotide is '+ str(int(A_count/length*100))+' %.'+'\n'
          'Percentage of T nucleotide is '+ str(int(T_count/length*100))+' %.'+'\n'
          'Percentage of C nucleotide is '+ str(int(C_count/length*100))+' %.'+'\n'
          'Percentage of G nucleotide is '+ str(int(G_count/length*100))+' %.')
    # calculate the percentages for each nucleotide
    return
gene_sequence = "acatgcgagtcagtcACGATCACGATGCA"  # input a random gene sequence (there may be some errors)
Nucleotide_content_calculator(gene_sequence)  # use the function and print the result


