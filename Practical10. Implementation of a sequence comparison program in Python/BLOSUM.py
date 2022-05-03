import os
import openpyxl

path = "C:/cygwin/home/13016/IBI1_2021-22/Practical10. Implementation of a sequence comparison program in Python"
os.chdir(path)
# change the working file
BLOSUM_matrix = openpyxl.load_workbook('BLOSUM.xlsx')
sheet = BLOSUM_matrix.active
# get the BLOSUM matrix sheet
dict_column={'A':'B','R':'C','N':'D','D':'E','C':'F','Q':'G','E':'H','G':'I','H':'J','I':'K','L':'L','K':'M','M':'N','F':'O','P':'P','S':'Q','T':'R','W':'S','Y':'T','V':'U','B':'V','Z':'W','X':'X'}
dict_row={'A':'2','R':'3','N':'4','D':'5','C':'6','Q':'7','E':'8','G':'9','H':'10','I':'11','L':'12','K':'13','M':'14','F':'15','P':'16','S':'17','T':'18','W':'19','Y':'20','V':'21','B':'22','Z':'23','X':'24'}
# make two dictionaries that will be used to get the scores
human = open('DLX5_human.fa', 'r')
mouse = open('DLX5_mouse.fa', 'r')
RandomSeq = open('RandomSeq.fa', 'r')
def readseq(seq_name):
    for line in seq_name:
        if line[0] != ">":
            return line
# define a function that can be used to get the sequence
seq1 = readseq(human)
seq2 = readseq(mouse)
seq3 = readseq(RandomSeq)
# get the sequences
# it was found that len(seq1) = len(seq2) = len(seq3)

def BLOSUM_score_cal(seq_1,seq_2):
    sum = 0
    for i in range(len(seq_1)-1):
        # because the sequences we read are end with "\n" so we use "len(seq_1)-1" here
        row_name = seq_1[i]
        column_name = seq_2[i]
        # get the amino acid names
        row = dict_row[row_name]
        column = dict_column[column_name]
        row_column = column+row
        # use two dictionaries to get the locations in the matrix
        sum += sheet[row_column].value
        # get the score
    return sum
# define a function to calculate the BLOSUM score for two sequences

def Alignment_cal(seq_1,seq_2):
    Alignment_score = 0
    for i in range(len(seq1)-1):  # because the sequences we read are end with "\n" so we use "len(seq_1)-1" here
        if seq_1[i] == seq_2[i]:
            Alignment_score += 1
        else:
            continue
    return int(Alignment_score)
# define a function to calculate the alignment score for two sequences

BLOSUM_score_human_mouse = BLOSUM_score_cal(seq1,seq2)
BLOSUM_score_human_random = BLOSUM_score_cal(seq1,seq3)
BLOSUM_score_mouse_random = BLOSUM_score_cal(seq2,seq3)
Alignment_score_human_mouse = Alignment_cal(seq1,seq2)
Alignment_score_human_random = Alignment_cal(seq1,seq3)
Alignment_score_mouse_random = Alignment_cal(seq2,seq3)
percentage_identity_human_mouse = Alignment_score_human_mouse*100//len(seq1)
percentage_identity_human_random = Alignment_score_human_random*100//len(seq1)
percentage_identity_mouse_random = Alignment_score_mouse_random*100//len(seq1)

print('The non-gapped global alignment score between human sequence and mouse sequence is '+ str(Alignment_score_human_mouse))
print('The percentage identity for human sequence and mouse sequence is '+ str(percentage_identity_human_mouse)+'%')
print("The BLOSUM score for comparing human and mouse genes: "+str(BLOSUM_score_human_mouse))
print('The non-gapped global alignment score between human sequence and random sequence is '+ str(Alignment_score_human_random))
print('The percentage identity for human sequence and random sequence is '+ str(percentage_identity_human_random)+'%')
print("The BLOSUM score for comparing human and random sequences: "+str(BLOSUM_score_human_random))
print('The non-gapped global alignment score between mouse sequence and random sequence is '+ str(Alignment_score_mouse_random))
print('The percentage identity for mouse sequence and random sequence is '+ str(percentage_identity_mouse_random)+'%')
print("The BLOSUM score for comparing mouse and random sequences: "+str(BLOSUM_score_mouse_random))
# Summary:
# The non-gapped global alignment score between human sequence and mouse sequence is 279
# The percentage identity for human sequence and mouse sequence is 96%
# The BLOSUM score for comparing human and mouse genes: 1490
# The non-gapped global alignment score between human sequence and random sequence is 8
# The percentage identity for human sequence and random sequence is 2%
# The BLOSUM score for comparing human and random sequences: -351
# The non-gapped global alignment score between mouse sequence and random sequence is 9
# The percentage identity for mouse sequence and random sequence is 3%
# The BLOSUM score for comparing mouse and random sequences: -348

# The larger BLOSUM score means that the compared sequences are more similar.
# The percentage identity for human-random and mouse-random are quite similar.
# The human sequence and mouse sequence are quite similar although human and mouse are quite different in the appearance.
# In biology and evolution theories, the evolution occurs when a small number of genes or sequences are changed.
# And the small change may cause huge changes in appearance and behaviors.

