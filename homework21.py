import json
with open('2.json','r') as f:
    output_data = json.load(f)
import csv
new=[]
for item in output_data:
    value=output_data[item]
    new.append(value)
    value.append(380973450346)
print(new)
with open('3.csv','w') as w_file:
    file_writter=csv.writer(w_file)
    file_writter.writerow(new)






