import json
with open('2.json','r') as f:
    output_data = json.load(f)
import csv

import random
new=[]
for item in output_data:
    num = str(random.randint(0, 999999999))
    value=output_data[item]
    value.append(num)
    new.append(value)
print(new)
with open('3.csv','w') as w_file:
    file_writter=csv.writer(w_file)
    file_writter.writerow(new)






