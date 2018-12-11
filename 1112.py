import pandas as pd
blk = pd.read_csv(r"E:\blockchain\split\transactions-0-537556_chunk1.csv",names = ["txid"],dtype={'txid':str})
blk["txid"][0]

from datetime import datetime
datetime.utcfromtimestamp(1284101485).strftime('%Y-%m-%d'+" "+'T%H:%M:%SZ')


import pandas as pd
filenames=[r'transactions-0-537556_chunk5.csv','transactions-0-537556_chunk6.csv','transactions-0-537556_chunk7.csv']
combined_csv = pd.concat( [ pd.read_csv(f,sep=';',names = ["txid", "hash", "version", "lock"]) for f in filenames ] )


# IMP 

import csv

#create dict from first csv, with url as key
with open("test5.csv", "r") as f:
    first = {rows[2]: rows[:2] for rows in list(csv.reader(f,delimiter=';'))}

for k,v in first.items():
    print(k,v)
    
# compare second csv and append rank
with open("transactions-chunk5.csv", "r") as f:
    for row in csv.reader(f,delimiter=';'):
        if row[0] in first: # row[0] = url
            first[row[0]].append(row[1]) # row[1] = rank

# convert dict back to list
merged = [(k,) + tuple(v) for k, v in first.items()]

# write list to output csv
with open("output.csv", "w") as f:
    csv.writer(f).writerows(merged)
