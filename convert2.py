import json

def getData():
    FIN = open ("b.csv", "r")
    FOUT = open("output.json", "w")

    InputData = FIN.read().split('\n')
    blooddata = []
    for string in InputData:
        arr = string.split(',')
        if (len(arr) > 22):
            blooddata.append(( {
                    'name': arr[1],
                    'address': arr[5],
                    'zip': arr[6],
                    'city': arr[7],
                    'lat': arr[2],
                    'lon': arr[3],
                    'mon': arr[8],
                    'tue': arr[9],
                    'wed': arr[10],
                    'thu': arr[11],
                    'fri': arr[12],
                    'sat': arr[13],
                    'sun': arr[14],
                    'url': arr[15],
                    'phone': arr[17],
                    'whole_blood_donation': arr[18],
                    'platelet_donation': arr[19],
                    'plasma_donation': arr[20],
                    'erythrocyte_donation': arr[21],
                }))
        
            #name = ["name: " , arr[1]] , "address: "+arr[5],"zip: "+arr[6],"city: "+arr[7],"lat: "+arr[2],"lon: "+arr[3],"mon: "+arr[8],"tue: "+arr[9],"wed: "+arr[10],"thu: "+arr[11],"fri: "+arr[12],"sat: "+arr[13],"sun: "+arr[14],"url: "+arr[15],"phone: "+arr[17],"whole_blood_donation: "+arr[18],"platelet_donation: "+arr[19],"plasma_donation: "+arr[20],"erythrocyte_donation: "+arr[21]]

    json.dump(blooddata ,FOUT, indent = 4)
    FIN.close()
    FOUT.close()

    return blooddata

getData()
