name = input("New filename:")
# input the name for the new file
# some names may cause errors
create = "C:/cygwin/home/13016/IBI1_2021-22/Practical8/" + name +".fa"
f1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
f2 = open(create,"w")
# read the original fasta file and create a new file
seq= ""
length=0
dict1 = {}
dict2 = {}
i = 0
j = 1
genename = ''
for line in f1 :
    if line.startswith('>'):
        count = seq.count("GAATTC")+1
        info = str(genename) + '    ' +"The number of fragments:" + str(count)  # info includes the gene names and the number of fragments for each gene (some genes that can't be cut with EcoRI are also included)
        dict1[info] = seq
        dict2[i] = info  # create two dictionaries that store the sequences, gene name and the number of fragments correspondingly
        seq = ''
        length = 0
        i = i + 1
        A = line.find('gene:')
        B = line.find('gene_biotype:')
        genename = line[A + 5:B - 1]   # get the gene names
    else:
        seq = seq + line
        seq = seq.replace("\n","")
        length = length + len(line)-1  # get the sequences without linefeed and the lengths
Num = i
while j < Num:
    info = dict2[j]
    seq = dict1[info]
    # get the corresponding information and gene sequences in two dictionaries
    if seq.count("GAATTC") > 0:
        f2.write(">"+info+"\n")
        f2.write(seq+"\n")
        j = j + 1
    else:
        j = j + 1
# get the sequences that can be cut by EcoRI and store them with the gene names and the number of fragments in the new file
f2.close()
f1.close()

