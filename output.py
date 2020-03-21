from convert2 import getData

def main():
    FOUT = open("output.txt", "w")
    data = getData()
    for d in data:
        str1 = '{"name": '+ data[1] + ', "address": "'+ data[3]+'", "zip": '+ data[4] + ', "city": "'+ data[5] + '", "lat": "'+ data[4] +'", "lon": "' + data[4] + '", "mon": "' + data[6] + '", "tue": "' + data[7] +'", "wed": "' + data[8] +'", "thu": "' + data[9]'}'    
        FOUT.write(str1+'\n')




    FOUT.close()
    return 0

if __name__ == '__main__':
    main()