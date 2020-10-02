import csv

def load_csv_file(path):
    data = []
    with open(path, 'r') as f:
    reader = csv.reader(f)
    newcsvdict = {"first name": [], "last name": []}
    for row in reader:
        first = row[0].split()[0]
        last = row[0].split()[1]
        newcsvdict["first name"].append(first)
        newcsvdict["last name"].append(last)

with open('new.csv', 'wb') as f:
    w = csv.DictWriter(f, newcsvdict.keys())
    w.writeheader()
    w.writerows(newcsvdict)