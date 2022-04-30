name = input("New filename:")
create = "C:/cygwin/home/13016/IBI1_2021-22/Practical8/" + name +".fa"
f1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
f2 = open(create,"w")
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
        info = str(genename) + '    ' +"cut_count:" + str(count)
        dict1[info] = seq
        dict2[i] = info
        seq = ''
        length = 0
        i = i + 1
        A = line.find('gene:')
        B = line.find('gene_biotype:')
        genename = line[A + 5:B - 1]
    else:
        seq = seq + line
        seq = seq.replace("\n","")
        length = length + len(line)-1
Num = i
while j < Num:
    info = dict2[j]
    seq = dict1[info]
    if seq.count("GAATTC") > 0:
        f2.write(">"+info+"\n")
        f2.write(seq+"\n")
        j = j + 1
    else:
        j = j + 1
f2.close()
f1.close()

