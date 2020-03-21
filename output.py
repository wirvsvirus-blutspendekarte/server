from convert2 import getData

def main():
    FOUT = open("output.txt", "w")
    data = getData()
    for d in data:
        str1 = '{\"name\": ' + d[1] + ', \"address\": \"'+ d[3]+'\", \"zip\": '+ d[4] + ', \"city\": \"'+ d[5] + '\", \"lat\": \"'+ d[4] +'\", \"lon\": \"' + d[4] + '\", \"mon\": \"' + d[6] + '\", \"tue\": \"' + d[7] +'\", \"wed\": \"' + d[8] +'\", \"thu\": \"' + d[9] +'\", \"fri\": \"' + d[10] +'\", \"sat\": \"' + d[11] +'\", \"sun\": \"' + d[12] +'\", \"url\": \"' + d[13] +'\", \"phone\": \"' + d[15] +'\", \"whole_blood_donation\": \"' + d[16] +'\", \"platelet_donation\": \"' + d[17] +'\", \"plasma_donation\": \"' + d[18] +'\"}'
        FOUT.write(str1+'\n')
    FOUT.close()
    return 0

if __name__ == '__main__':
    main()
