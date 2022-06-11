import requests
from bs4 import BeautifulSoup


s = input(str("Please enter the name: "))


# Making a GET request
r = requests.get('https://en.wikipedia.org/wiki/'+s+'_filmography')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

data = []
#table = soup.find('div', attrs = {'class':'mw-parser-output'})

table = soup.find('table', attrs={'class':'wikitable plainrowheaders sortable'})
if table==None:
    table = soup.find('table', attrs={'class':'wikitable sortable'})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
df=[]
for i in range (1,len(data)):
    df.append((data[i][0]))

df= df[::-1]

print("----------------------------------------")
print("Follwing are the films done by "+s+" in reverse chronological order :")
for i in range (len(df)):
    print (df[i])
print("----------------------------------------")


