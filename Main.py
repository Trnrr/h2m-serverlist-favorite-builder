import json
import requests
from bs4 import BeautifulSoup

url = "https://master.iw4.zip/servers"
server_list = []

html = BeautifulSoup(requests.get(url).text, 'html.parser')

h2m_servers = html.find('div', {"id":"H2M_servers"}).findAll('table')[0]

for tr in h2m_servers.findAll('tr', {"class":"server-row"}):
    server_list.append(tr.get('data-ip') +":"+ tr.get('data-port'))

with open("favourites.json", "w") as outfile:
    outfile.write(json.dumps(server_list))

README = """
### Server count: [{}]
""".format(len(server_list))

with open("README.md", "w") as readmefile:
    readmefile.write(README)