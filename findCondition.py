
##Count the number of good files with the conditions
def getData(stin,stout,frenquent_B):
    compte=0
    compte_ver=0
    with open(stin) as rp:
        content = rp.readlines()
        for element in content :
            listelemnt = element.split(",")
            if (listelemnt[1] == "" or int(listelemnt[2].split(" ")[0]) > 10):
                stout.write(element.replace(element, element.strip() + ",1" +"\n"))
                frenquent_B [listelemnt[0]] = ''
                compte +=1
            else:
                stout.write(element.replace(element, element.strip() + ",0" +"\n"))
                frenquent_B[listelemnt[0]] = listelemnt[1].split("-")  
                compte_ver +=1
    rp.close()
    stout.close()
    print("compte is ",compte)  
    print("compte_ver is ",compte_ver)     
    return frenquent_B

##Replace the value '0' by '1' when it appeared
def faltList(dictionary,dictDeux):
    frequent_R=dict.fromkeys(dictionary)
    for elem, value in dictionary.items():
        newDict = dict.fromkeys(dictDeux, 0)
        for elem1,value1 in newDict.items():
            if elem1 in value:
                newDict[elem1] = "1"
            frequent_R[elem] = newDict
    return frequent_R
