import json

## Read the JSON file
def readJSONData(filename):
    with open(filename) as data_file:
        data_item = json.load(data_file)
        
    return data_item

##Get the useful info from JSON file and return bus info and walk time
def seperateJSONData(data_item):     
    value=0 
    walkMinutes=0
    busLigne=""
    for no in data_item["routes"]:
        for key in no.keys():
            if (key == "legs"):
                for no1 in no["legs"] :
                    for key1 in no1.keys():
                        if (key1 == "steps"):
                            for elem in no1["steps"]:
                                value += 1
                                for key2 in elem.keys():
                                    if (key2 == "travel_mode"):
                                        if (elem["travel_mode"] == "WALKING"):
                                            walkMinutes += int(elem["duration"]["text"].split(" ")[0])
                                        elif (elem["travel_mode"] == "TRANSIT"):
                                            busLigne += elem["transit_details"]["line"]["short_name"] + "-"

    busInfo=busLigne[:-1]
    walkInfo=str(walkMinutes) + " minutes"
    return  busInfo,walkInfo
