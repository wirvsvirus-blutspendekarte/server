def getData():
    FIN = open ("D:\\ProgrammierigeProgramme\\GitRepositories\\blutspendekarte\\server\\b.csv", "r")

    InputData = FIN.read().split('\n')
    blooddata = []
    for string in InputData:
        arr = string.split(',')

        filteredArr = [arr[0], arr[1], arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9],arr[10],arr[11],arr[12],arr[13],arr[14],arr[15],arr[16],arr[17],arr[18],arr[19],arr[20],arr[21],arr[22]]
        
        blooddata.append(filteredArr)
        print(arr)             

    blooddata.remove(blooddata[0])
    FIN.close()

    return blooddata

print(getData())