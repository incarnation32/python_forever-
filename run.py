from bs4 import BeautifulSoup
import requests

src = requests.get("https://pokemondb.net/pokedex/national")
soup = BeautifulSoup(src.content, 'lxml')
image = soup.find_all('span', attrs = {'class':'infocard-lg-img'})
pk_name = soup.find_all('a', attrs = {'class':'ent-name'})
dir = []
for i in image:
	for j in i.find_all('a'):
		dir.append(j.span.get('data-src'))

for i in range(1,len(dir)):
	r = requests.get(dir[i])
	with open('{}.jpg'.format([j.get_text() for j in pk_name][i+1]), 'wb') as f:
		f.write(r.content)
