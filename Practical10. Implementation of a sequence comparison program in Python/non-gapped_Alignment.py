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
#len(seq1) = len(seq2) = len(seq3)
Alignment_score_human_mouse = 0
Alignment_score_human_random = 0
Alignment_score_mouse_random = 0
i = 0

while i <= len(seq1)-1:
    if seq1[i] == seq2[i]:
        Alignment_score_human_mouse += 1
        i += 1
    else:
        i += 1
i = 0
while i <= len(seq1)-1:
    if seq1[i] == seq3[i]:
        Alignment_score_human_random += 1
        i += 1
    else:
        i += 1
i = 0
while i <= len(seq1)-1:
    if seq2[i] == seq3[i]:
        Alignment_score_mouse_random += 1
        i += 1
    else:
        i += 1
print('The non-gapped global aligment score between human gene and mouse gene is '+ str(Alignment_score_human_mouse))
print('The non-gapped global aligment score between human gene and random gene is '+ str(Alignment_score_human_random))
print('The non-gapped global aligment score between mouse gene and random gene is '+ str(Alignment_score_mouse_random))
