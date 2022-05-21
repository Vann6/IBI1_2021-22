
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
id_terms = GOtree.getElementsByTagName("id")
list_child_node_number = []
list_child_node_number_translation = []
list1 = []
list2 = []
number = 100
num_childnode = 0
num_terms = 0
for term in terms:
    num_terms += 1
    is_a = term.getElementsByTagName("is_a")
    for i in range(is_a.length):
        is_a = term.getElementsByTagName("is_a")[i]
        is_a_txt = is_a.childNodes[0].data
        list1.append(is_a_txt)
# create a list that contains the terms that have childnodes
# the list will be used to simplify the process and get the results quickly
print("the number of terms recorded in the Gene Ontology is "+str(num_terms))
# the number of terms recorded in the Gene Ontology is 47340

# overview of the codes to find the number of childNodes for each term:
# I make a list2 that includes all the term that need to be count
# when the term is counted it will be removed from the list
# and the childNode of this term will be added
# the calculation will not stop if the list is not empty.


for term in terms:
    if len(list_child_node_number) > number:
        break
        # find the childNodes for first one hundred terms
        # i can be changed to include more terms
    num_childnode = 0
    term_id = term.getElementsByTagName("id")[0]
    term_id_txt = term_id.childNodes[0].data
    # get the term_id
    if term_id_txt in list1:
        # check whether this term has childNodes
        # if it has childNode this term_id will be added into list2 and calculate childNodes
        list2.append(term_id_txt)
        # if it doesn't have childNode then 0 will be added into list_child_node_number which stores the number of childNodes for each term
        # then calculate the number of childNodes for next term
        while len(list2) > 0:  # stop calculating when the list2 is empty
            if list2[0] in list1:  # test whether the term has childNodes
                # the codes find childNode for one term
                for term in terms:
                    is_a = term.getElementsByTagName("is_a")
                    term_id = term.getElementsByTagName("id")[0]
                    term_id_txt = term_id.childNodes[0].data  # get the term_id
                    for i in range(is_a.length):
                        is_a = term.getElementsByTagName("is_a")[i]
                        is_a_txt = is_a.childNodes[0].data  # get the content of is_a
                        if list2[0] == is_a_txt:  # test whether the is_a_txt is the childNode
                            list2.append(term_id_txt)  # add the childNode into the list2 for further calculate
                            num_childnode += 1  # count the number of childNodes
                list2.remove(list2[0])  # remove the term that has calculated
            else:
                list2.remove(list2[0])  # remove the term that has no childNodes
        list_child_node_number.append(num_childnode)  # add the number of childNodes into the list
    else:
        list_child_node_number.append(num_childnode)  # add the number of childNodes into the list

print(list_child_node_number)


list2 = []
# overview of the codes to find the number of childNodes for each term:
# most of the codes are same as the codes above
# only add some codes to test whether the term is related to translation
for term in terms:
    if len(list_child_node_number_translation) > number:
        break
    num_childnode = 0
    term_id = term.getElementsByTagName("id")[0]
    term_id_txt = term_id.childNodes[0].data
    defstr = term.getElementsByTagName("defstr")[0]
    defstr_txt = defstr.childNodes[0].data  # get the content of defstr
    if defstr_txt.find("translation") > 0:  # test whether the term is related to translation
        if term_id_txt in list1:
            list2.append(term_id_txt)
            while len(list2) > 0:
                if list2[0] in list1:
                    for term in terms:
                        is_a = term.getElementsByTagName("is_a")
                        term_id = term.getElementsByTagName("id")[0]
                        term_id_txt = term_id.childNodes[0].data
                        for i in range(is_a.length):
                            is_a = term.getElementsByTagName("is_a")[i]
                            is_a_txt = is_a.childNodes[0].data
                            if list2[0] == is_a_txt:
                                list2.append(term_id_txt)
                                num_childnode += 1
                    list2.remove(list2[0])
                else:
                    list2.remove(list2[0])
            list_child_node_number_translation.append(num_childnode)
        else:
            list_child_node_number_translation.append(num_childnode)
print(list_child_node_number_translation)


create a boxplot for the number of childnodes for each term
plt.boxplot(x=[list_child_node_number,list_child_node_number_translation],
            meanline=True, showmeans=True,
            patch_artist=True, showbox=True,
            showfliers=False, notch=False,
            labels=['terms', 'term that contains translation'])
plt.grid(True)
plt.title = ("The boxplot for the number of childnodes")
plt.xlabel = ('The terms')
plt.ylabel = ("ylabel")
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

# limitations：
# the codes were too complex. it costs too much time to get the results