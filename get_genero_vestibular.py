import requests
from bs4 import BeautifulSoup
import re

r = requests.get("http://www.comvest.unicamp.br/estatisticas/2017/quest/quest1.php")
soup = BeautifulSoup(r.text, "html.parser")
#cursos = [x["value"] for x in soup.find("select").findAll("option")]

headers = {'User-Agent': 'Mozilla/5.0'}
for curso in soup.find("select").findAll("option")[1:]:	
	data = { 'opcao': curso["value"], 'cid_inscricao':'all','questao':'sexo','grupo':'1'}
	r = requests.post("http://www.comvest.unicamp.br/estatisticas/2017/quest/quest2.php",data=data,headers=headers)
	soup = BeautifulSoup(r.text, "html.parser")
	text = re.split(r'\s{2,}', soup.get_text().replace('\r','\n'))
	for line in text:
		if 'masculino' in line:
			index = text.index(line)
	print(curso.text)
	print("Nao declarado "+text[index+1])
	print("Masculino "+text[index+2])
	print("Feminino "+text[index+3])
