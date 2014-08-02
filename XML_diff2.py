
import xml.etree.ElementTree as ET
#https://docs.python.org/2/library/xml.etree.elementtree.html
#http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python


#import your xml here. xlmdoc === values for new
#xmldoc_old === values for old to remove same.
xmldoc = ET.parse("testfailures.xml")
xmldoc_old = ET.parse("testfailures1277_0006.xml")





root = xmldoc.getroot()
rootold = xmldoc_old.getroot()





xmldoc.write('output.xml')

#print (root)



### Math logic check #

##########
########
######


failurearray = []
failurearrayold = []


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



print (len(failurearray), "FAILURE COUNT IN LIST 1")
print (len(failurearrayold), "FAILURE COUNT IN LIST 2")





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
        


print (len(samearray), "Matches found\n")
print (len(diffarray), "Differences unchanged")
print ("ORIGINAL FAILURES: ", len(failurearray), " LESS DUPLICATES", len(samearray), "equals: ", len(failurearray) - len(samearray))




### end logic checks #######
##########
########
#########


#### START MODIFYING XML TO REMOVE DUPLICATE FAILURES IDS #########
### THIS MERELY SETS THE FAILURE TO A MESSAGE SO NB DOESN'T GENERATE THEM ###

for test in root.iter('test'):
    count = 0
    if test.attrib["result"] == "F":
        #print (test.attrib["id"], "hellow\n\n")
        ########################################
        for testmatch in rootold.iter("test"):
            ## only compare with failures TO AVOID REMOVING FILES THAT WERE MESSAGES PREVIOUSLY
            if testmatch.attrib["result"] =="F":
                if test.attrib["id"] == testmatch.attrib["id"]:
                    count = 1
                    test.attrib["result"] = "MATCHREMOVALASFAILURE"
    if count == 0:
        nomatch = True
        #print ("NoMatchFound")  ## might print a ton for every non Failure in the root.iter('test") that is not a failure
        

xmldoc.write('output2.xml')

count = 0
for each in root.iter("test"):
    if each.attrib["result"] == "MATCHREMOVALASFAILURE":
        count +=1
print (count, "matches found \n")
    

count = 0





