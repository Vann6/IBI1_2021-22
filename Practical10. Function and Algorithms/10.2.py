def Nucleotide_content_calculator(seq) :
    seq = seq.upper()
    length = len(seq)
    A_count = seq.count('A')
    T_count = seq.count('T')
    C_count = seq.count('C')
    G_count = seq.count('G')
    print('Percentage of A nucleotide is '+ str(int(A_count/length*100))+' %.'+'\n'
          'Percentage of T nucleotide is '+ str(int(T_count/length*100))+' %.'+'\n'
          'Percentage of C nucleotide is '+ str(int(C_count/length*100))+' %.'+'\n'
          'Percentage of G nucleotide is '+ str(int(G_count/length*100))+' %.')
    return
Nucleotide_content_calculator(input("Gene sequence"))

