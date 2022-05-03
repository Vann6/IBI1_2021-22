human = open('DLX5_human.fa', 'r')
mouse = open('DLX5_mouse.fa', 'r')
RandomSeq = open('RandomSeq.fa', 'r')
def readseq(seq_name):
    for line in seq_name:
        if line[0] != ">":
            return line
seq1 = readseq(human)
seq2 = readseq(mouse)
seq3 = readseq(RandomSeq)
# get the gene sequences
# it was found that len(seq1) = len(seq2) = len(seq3)

def edit_distance_cal(seq_1,seq_2):
    edit_distance = 0
    for i in range(len(seq1)-1): # because the sequences we read are end with "\n" so we use "len(seq_1)-1" here
        if seq_1[i] != seq_2[i]:
            edit_distance += 1
        else:
            continue
    return edit_distance

edit_distance_human_mouse = edit_distance_cal(seq1,seq2)
edit_distance_human_random = edit_distance_cal(seq1,seq3)
edit_distance_mouse_random = edit_distance_cal(seq2,seq3)
print('The edit_distance between human sequence and mouse sequence is '+ str(edit_distance_human_mouse))
print('The edit_distance between human sequence and random sequence is '+ str(edit_distance_human_random))
print('The edit_distance between mouse sequence and random sequence is '+ str(edit_distance_mouse_random))
# calculate the alignment and print the results for each two sequences
# The edit_distance between human sequence and mouse sequence is 10
# The edit_distance between human sequence and random sequence is 281
# The edit_distance between mouse sequence and random sequence is 280
