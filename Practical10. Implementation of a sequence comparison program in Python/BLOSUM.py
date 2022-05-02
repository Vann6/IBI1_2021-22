import pandas as pd
import os
import openpyxl

path = "C:/cygwin/home/13016/IBI1_2021-22/Practical10_2"
os.chdir(path)  # 修改工作路径

BLOSUM_matrix = openpyxl.load_workbook('BLOSUM.xlsx')  # 返回一个workbook数据类型的值
sheet = BLOSUM_matrix.active # 获取活动表
dict_column={'A':'B','R':'C','N':'D','D':'E','C':'F','Q':'G','E':'H','G':'I','H':'J','I':'K','L':'L','K':'M','M':'N','F':'O','P':'P','S':'Q','T':'R','W':'S','Y':'T','V':'U','B':'V','Z':'W','X':'X'}
dict_row={'A':'2','R':'3','N':'4','D':'5','C':'6','Q':'7','E':'8','G':'9','H':'10','I':'11','L':'12','K':'13','M':'14','F':'15','P':'16','S':'17','T':'18','W':'19','Y':'20','V':'21','B':'22','Z':'23','X':'24'}
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

sum=0
for i in range(len(seq1)-1):
    row_name = seq1[i]
    column_name = seq2[i]
    row = dict_row[row_name]
    column = dict_column[column_name]
    row_column = column+row
    sum += sheet[row_column].value
print("the score of alignment is: "+str(sum)+".")
sum=0
for i in range(len(seq1)-1):
    row_name = seq1[i]
    column_name = seq2[i]
    row = dict_row[row_name]
    column = dict_column[column_name]
    row_column = column+row
    sum += sheet[row_column].value
print("the score of alignment is: "+str(sum)+".")
sum=0
for i in range(len(seq1)-1):
    row_name = seq1[i]
    column_name = seq2[i]
    row = dict_row[row_name]
    column = dict_column[column_name]
    row_column = column+row
    sum += sheet[row_column].value
print("the score of alignment is: "+str(sum)+".")