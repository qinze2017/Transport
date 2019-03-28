import itertools
import json, os
import urllib.request

## Read the line in file and return the list 
def readFile(text_file):
    stops_list=[]
    try:
        fh=open(text_file) 
        for line in fh: 
            stops_list = line.strip().split(',')
    except:
        print('file does not exist!')
    return stops_list

##return a list without duplicated
def removeDuplicate(stops_list):
    unique_list = []
    for element in stops_list:
        unique_list.append(element.upper())
    return unique_list

##Return the group of each two points in the list
def creatDoubleList(unique_list):
    double_list = []
    for a, b in itertools.combinations(unique_list, 2):
        a=a.replace(" ", "%20")+",SHERBROOKE"
        b=b.replace(" ", "%20")+",SHERBROOKE"
        double_list.append([a, b])
    return double_list  

##Return a list of the Google API links 
def creatLinks(unique_list):
    link_list = []
    for elements in unique_list:
        linkGoogles = "https://maps.googleapis.com/maps/api/directions/json?origin="+elements[0]+"&destination="+elements[1]+"&mode=transit&key=AIzaSyCQH6if_MwSKHFP_P_nLXE2A0tlHqzT3tU"
        link_list.append(linkGoogles)
    return link_list

##return the data with the Google API
def createJsonfile(link):
    with urllib.request.urlopen(link,None,30) as url:
        data = json.loads(url.read().decode())
        print(data)
    return data

##Create the files to set the return of Google API responses for Training
def writeToFile(links): 
    i=0
    for link in links:
        data=createJsonfile(link.encode('ascii', 'ignore').decode('ascii'))
        with open(os.path.join('TRAINING/',"fileProj%s.txt" % i), 'w') as f:
            json.dump(data, f, ensure_ascii=True)
        i += 1
        print(i)
    print("Finish collection JSON files !") 

##Create the files to set the return of Google API responses for Testing
def writeToFileTest(links): 
    i=0
    for link in links:
        data=createJsonfile(link.encode('ascii', 'ignore').decode('ascii'))
        with open(os.path.join('TESTING/',"fileProj%s.txt" % i), 'w') as f:
            json.dump(data, f, ensure_ascii=True)
        i += 1
        print(i)
    print("Finish collection JSON files !") 
        
def main():
    ### create TRAINING data:
    text_file="bus_stops.txt"
    writeToFile(creatLinks(creatDoubleList(removeDuplicate(readFile(text_file)))))
    
    ### create TESTING data:
    text_file_test="bus_stops_test.txt"
    writeToFileTest(creatLinks(creatDoubleList(removeDuplicate(readFile(text_file_test)))))
    
main()