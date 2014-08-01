
import xml.etree.ElementTree as ET
#https://docs.python.org/2/library/xml.etree.elementtree.html
#http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python


#import your xml here. xlmdoc === values for new
#xmldoc_old === values for old to remove same.
xmldoc = ET.parse("testfailures1277.xml")
xmldoc_old = ET.parse("testfailures1277_0006.xml")





root = xmldoc.getroot()
rootold = xmldoc_old.getroot()



failurearray = []
failurearrayold = []



print (root)

for each in root:
    print (each.tag, each.attrib)

for each in rootold:
    print (each.tag, each.attrib)




for each in root.iter('category'):
    print (each.attrib)

print("\n\n")


"""for each in root.iter('testfile'):
    print (each.attrib)"""


#dipping down to extrat tests that failed.
    #appending failed tests to their own array.
for each in root.iter('test'):
    #print (each.attrib)
    if each.attrib["result"] == "F":
        failurearray.append(each.attrib)  #IF i append each attrib as a string then the array is messy.


for each in rootold.iter('test'):
    #print (each.attrib)
    if each.attrib["result"] == "F":
        failurearrayold.append(each.attrib)  #IF i append each attrib as a string then the array is messy.


print (failurearray[0],"\n", failurearray[1],"\n", failurearray[-1])
print (len(failurearray))

print (failurearrayold[0],"\n", failurearrayold[1],"\n", failurearrayold[-1])
print (len(failurearrayold))





samearray = []
diffarray = []


for each in failurearray:
    count = 0
    for eachold in failurearrayold:
        if each["id"] == eachold["id"]:
            count = 1
            samearray.append(each)
    if count == 0:
        diffarray.append(each)
        


print (len(samearray))
print (len(diffarray))

for each in diffarray:
    print (each)








##need keys to get out of this data.

#for each in failurearray:
#    print("result: ", each["result"], "testfile: ", each["id"])



    

    



