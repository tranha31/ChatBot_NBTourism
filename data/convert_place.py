import json

f_dulich = open('dulich.json', 'r', encoding='utf-8-sig')

dulich = json.load(f_dulich)

i = 0
for p in dulich:
    path = "d_"+str(i)+".txt"
    data = open('diem_du_lich/'+path, 'w', encoding='utf-8-sig')
    tmp = p['content']
    data.write(tmp)
    i = i+1

f_dulich.close()