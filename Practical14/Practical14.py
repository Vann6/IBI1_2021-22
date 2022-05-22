
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np


GOtree = xml.dom.minidom.parse("go_obo.xml")
# parse the go_obo.xml file into a DOM document
collection = GOtree.documentElement
# get the root element of the document
terms = collection.getElementsByTagName("term")
# read the go_obo.xml file and get a list of "term" elements
list_child_node_number = []
list_child_node_number_translation = []
num_terms = 0
dict = {}
# create a dictionary that store the first childNodes and a list includes the second childNodes for each term
for term in terms:
    num_terms += 1
    is_a = term.getElementsByTagName("is_a")
    term_id = term.getElementsByTagName("id")[0]
    term_id_txt = term_id.childNodes[0].data  # get the term_id
    if term_id_txt not in dict:
        dict[term_id_txt] = []
    for i in range(is_a.length):
        is_a = term.getElementsByTagName("is_a")[i]
        is_a_txt = is_a.childNodes[0].data  # get the content of is_a
        if is_a_txt not in dict:
            dict[is_a_txt] = []
        dict[is_a_txt].append(term_id_txt)
        dict[is_a_txt].append(dict[term_id_txt])  # add the childNodes and a list

print("the number of terms recorded in the Gene Ontology is "+str(num_terms))
# the number of terms recorded in the Gene Ontology is 47340

# define a function to get all the childNodes
def unfold(list):
    for i in range(len(list)):
        if list[i] is not [] and type(list[i]) is list:
            unfold(list[i])
        else:
            list1.append(list[i])

# get all the childNodes for each term in the dictionary
for term in terms:
    term_id = term.getElementsByTagName("id")[0]
    term_id_txt = term_id.childNodes[0].data  # get the term_id
    list1 = []
    unfold(dict[term_id_txt])
    list2 = []
    for i in range(len(list1)):
        if list1[i] not in list2 and list1[i] != []:
            list2.append(list1[i])  # remove the empty list and repeated elements in the dictionary
    dict[term_id_txt] = list2
    list_child_node_number.append(len(list2))  # add the number of childNodes into the list
    defstr = term.getElementsByTagName("defstr")[0]
    defstr_txt = defstr.childNodes[0].data  # get the content of defstr
    if defstr_txt.find("translation") > 0:  # test whether the term is related to translation
        list_child_node_number_translation.append(len(list2))  # add the number of childNodes for the term that contains translation into the list

# create a boxplot for the number of childnodes for each term
plt.boxplot(x=[list_child_node_number,list_child_node_number_translation],
            meanline=True, showmeans=True,
            patch_artist=True, showbox=True,
            showfliers=False, notch=False,
            labels=['terms', 'term that contains translation'])
plt.grid(True)
plt.title("The boxplot for the number of childnodes")
plt.xlabel('The terms')
plt.ylabel("ylabel")
plt.show()

# calculate the average number of each term and the average number of each term that contains "translation"
var1 = np.average(list_child_node_number)
var2 = np.average(list_child_node_number_translation)
# compare the average numbers
if var1 > var2:
    print("the term contains translation have a smaller number of childNodes on average")
else:
    print("the term contains translation have a greater number of childNodes on average")

print(var1)
print(var2)

# the number of terms recorded in the Gene Ontology is 47340
# the term contains translation have a greater number of childNodes on average
