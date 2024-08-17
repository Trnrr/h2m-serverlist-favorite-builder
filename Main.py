import json
import re
import requests
from bs4 import BeautifulSoup

url = "https://master.iw4.zip/servers"
server_list = []
removeWords = ["trickshot","s&r"]

html = BeautifulSoup(requests.get(url).text, 'html.parser')

h2m_servers = html.find('div', {"id":"H2M_servers"}).findAll('table')[0]

for tr in h2m_servers.findAll('tr', {"class":"server-row"}):
    if not re.search('trickshot|s&r', tr.find('td', {"class":"server-hostname text-break"}).get('data-hostname'), re.IGNORECASE):
        server_list.append(tr.get('data-ip') +":"+ tr.get('data-port'))

with open("favourites.json", "w") as outfile:
    outfile.write(json.dumps(server_list, indent=2))

README = r"""
## H2M Server Favorites Generator.
### Runs every 30 mins
### !!Removes trickshot servers!!

## Server count: [{}]
### Download: [Save page as.. > favourites.json](https://raw.githubusercontent.com/Trnrr/h2m-serverlist-favorite-builder/main/favourites.json)

### How to use:
1. Download favourites.json
2. Save file to players2 folder in MWR install directory.
3. Full path should look something like (C:\Program Files (x86)\Steam\steamapps'\common\Call of Duty Modern Warfare Remastered\players2\favourites.json)
3. Open H2M and filter by Favorites.
""".format(len(server_list))

with open("README.md", "w") as readmefile:
    readmefile.write(README)
