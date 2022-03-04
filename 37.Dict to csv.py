import csv
d={1:'Bharath',2:'Harath',3:'Arath',4:'Rath'}
with open("sample1.csv","w") as f1:
    csvrdr=csv.writer(f1)
    for item in d.items():
        csvrdr.writerow(item)
with open("sample1.csv","r") as f1:
    csvrdr=csv.reader(f1)
    for row in csvrdr:
        print(" ".join(row))
