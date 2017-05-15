import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

print("VTU-RESULTS")
print("...................G O O D   L U C K....................")
print("--------------------------------------------------------\n")
print("Enter the usn: ",end='')
usn = input().strip()
url = 'http://results.vtu.ac.in/results/result_page.php?usn='+usn

print("\nFetching result",end='')

dat=None


while(dat is None):
    print(".",end='')
    try:
        dat = urlopen(url).read()
    except Exception as e:
        continue
        

exp = r'[A-Z]+ [A-Z\s]*'
pattern = re.compile(exp)
name = re.findall(pattern,str(dat))
print("\n\nNAME:",name[5])
print("RESULT:",name[6],"\n\n")


soup = bs(dat,"lxml")
right_table = soup.find_all('table', class_='table table-bordered')

sub_code = []
sub_name = []
int_marks = []
ext_marks = []
total = []
result = []
col = []
for table in right_table:
    for row in table.findAll('tr'):
        col = row.findAll('td')
        if(len(col)==6):
            sub_code.append(col[0].find(text=True))
            sub_name.append(col[1].find(text=True))
            int_marks.append(col[2].find(text=True))
            ext_marks.append(col[3].find(text=True))
            total.append(col[4].find(text=True))
            result.append(col[5].find(text=True))
        else:
            continue


df = pd.DataFrame()
df['Sub Code'] = sub_code
df['Sub Name'] = sub_name
df['Internal'] = int_marks
df['External'] = ext_marks
df['Total'] = total
df['Result'] = result

grand_total = 0
for tot in total:
    grand_total+=int(tot)


if(df.empty):
    print("Result not available")
print(df)
print("\n\n\nTotal marks =",grand_total)

