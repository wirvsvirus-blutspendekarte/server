from convert2 import getData

def main():
    FOUT = open("output.txt", "w")
    data = getData()
    for d in data:
        str1 = '{"name": ' +data[1] + ', "address": "'+ data[3]+'", "zip": '+ data[4] + ', "city": "'+ data[5] + '", "lat": "'+ data[4] +'", "lon": "' + data[4] + '", "mon": "' + data[6] + '", "tue": "' + data[7] +'", "wed": "' + data[8] +'", "thu": "' + data[9] +'", "fri": "' + data[10] +'", "sat": "' + data[11] +'", "sun": "' + data[12] +'", "url": "' + data[13] +'", "phone": "' + data[15] +'", "whole_blood_donation": "' + data[16] +'", "platelet_donation": "' + data[17] +'", "plasma_donation": "' + data[18] +'", "platelet_donation": "' + data[17]'}'
    FOUT.write(str1+'\n')
    FOUT.close()
    return 0

if __name__ == '__main__':
    main()