import json

f_lehoi = open('lehoi.json', 'r', encoding='utf-8-sig')

lehoi = json.load(f_lehoi)

i = 0
for p in lehoi:
    path = "f_"+str(i)+".txt"
    data = open('le_hoi/'+path, 'w', encoding='utf-8-sig')
    tmp = p['content']
    data.write(tmp)
    i = i+1

f_lehoi.close()