import json
old_dict={
    567890:['danya',20],
    347890:['Lisa',20],
    76525678:['Anna',18],
    342167:['Anna',30],
    568903:['Ira',25]
}
with open('2.json','w') as f:
    json.dump(old_dict,f)

