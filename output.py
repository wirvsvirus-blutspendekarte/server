from convert2 import getData

def main():
    FOUT = open("output.json", "w")
    data = getD+ata()

    for i in data:
        if i[1] == '':
            data.remove(i)


    for d in data:
        MOvor = "".join(d[8].split(';')[0])
        DIvor = "".join(d[9].split(';')[0])
        MIvor = "".join(d[10].split(';')[0])
        DOvor = "".join(d[11].split(';')[0])
        FRvor = "".join(d[12].split(';')[0])
        SAvor = "".join(d[13].split(';')[0])
        SOvor = "".join(d[14].split(';')[0])
        MOnach =''
        DInach =''
        MInach =''
        DOnach =''
        FRnach =''
        SAnach =''
        SOnach =''
        if ';' in d[8]:
            MOnach = "".join(d[8].split(';')[1])
        if ';' in d[9]:
            DInach = "".join(d[9].split(';')[1])
        if ';' in d[10]:
            MInach = "".join(d[10].split(';')[1])
        if ';' in d[11]:
            DOnach = "".join(d[11].split(';')[1])
        if ';' in d[12]:
            FRnach = "".join(d[12].split(';')[1])
        if ';' in d[13]:
            SAnach = "".join(d[13].split(';')[1])
        if ';' in d[14]:
            SOnach = "".join(d[14].split(';')[1])
        str1 = '[{\"name\": ' + d[1] + ', \"address\": \"'+ d[5]+'\", \"zip\": '+ d[6] + ', \"city\": \"'+ d[7] + '\", \"lat\": \"'+ d[2] +'\", \"lon\": \"' + d[3] + '\",\"timings\": { \"mon\": \"von": "' + MOvor + '" \"und von": "'+ MOnach +'", \"tue\": \"von": "' + DIvor + '" \"und von": "'+ DInach +'", \"wed\": \"von": "' + MIvor + '" \"und von": "'+ MInach +'", \"thu\": \"von": "' + DOvor + '" \"und von": "'+ DOnach +'", \"fri\": \"von": "' + FRvor + '" \"und von": "'+ FRnach +'", \"sat\": \"von": "' + SAvor + '" \"und von": "'+ SAnach +'", \"sun\": \"von": "' + SOvor + '" \"und von": "'+ SOnach +'"} , \"url\": \"' + d[15] +'\", \"phone\": \"' + d[17] +'\", \"whole_blood_donation\": \"' + d[18] +'\", \"platelet_donation\": \"' + d[19] +'\", \"plasma_donation\": \"' + d[20] +'\", \"erythrocytes_donation\": \"' + d[21] +'\"}]'
        FOUT.write(str1+'\n')
    FOUT.close()
    return 0

if __name__ == '__main__':
    main()
