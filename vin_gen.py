from random import choice
letterstr='ABCDEFGHJKLMNPQRSTUVWXYZ'
letter = list(letterstr)
letterw={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'J':1,'K':2,'L':3,'M':4,'N':5,'P':7,'R':9,'S':2,'T':3,\
         'U':4,'V':5,'W':6,'X':7,'Y':8,'Z':9,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
digit = [0,1,2,3,4,5,6,7,8,9]
letter.extend(digit)
country_list = [choice(letter) for i in range(13)]
digit_list = [choice(digit) for i in range(4)]
vin = []
vin.extend(country_list[0:2])
vin.append(digit_list[0])
vin.extend(country_list[-11:])
vin.extend(digit_list[1:])
vin_num = [letterw[i]  if(type(i)==str) else i for i in vin]
pos_w = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
checksum = sum([vin_num[i]*pos_w[i] for i in range(17)])%11
vin[8] = checksum
vin = [i if(type(i)==str) else str(i) for i in vin]
vin = ''.join(vin)
