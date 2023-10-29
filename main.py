import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
pag_dolar = requests.get('https://www.google.com/search?q=dolar&rlz=1C1FCXM_pt-PTBR979BR979&oq=Dolar&gs_lcrp=EgZjaHJvbWUqDQgAEAAYgwEYsQMYgAQyDQgAEAAYgwEYsQMYgAQyDQgBEAAYgwEYsQMYgAQyBggCEEUYQDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDIKCAUQABixAxiABDIKCAYQABixAxiABDIKCAcQABixAxiABNIBBzk5MWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8', headers=header)
pag_euro = requests.get('https://www.google.com/search?q=euro&rlz=1C1FCXM_pt-PTBR979BR979&oq=euro&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhDGLEDGIoFMgoIARAAGLEDGIAEMhAIAhAuGIMBGNQCGLEDGIAEMgoIAxAAGLEDGIAEMgoIBBAuGLEDGIAEMg0IBRAAGIMBGLEDGIAEMg0IBhAAGIMBGLEDGIAEMgkIBxAAGEMYigUyDQgIEC4YgwEYsQMYgAQyBwgJEAAYgATSAQgxMDIyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8', headers=header)
pag_iene = requests.get('https://www.google.com/search?q=iene&sca_esv=573033479&rlz=1C1FCXM_pt-PTBR979BR979&sxsrf=AM9HkKmzx_cXuy0w31RdNxlBjiPGI3f5hA%3A1697155955804&ei=c4soZZThMKq05OUPpIyYoAc&ved=0ahUKEwjU5v7O3vGBAxUqGrkGHSQGBnQQ4dUDCBA&uact=5&oq=iene&gs_lp=Egxnd3Mtd2l6LXNlcnAiBGllbmUyDxAAGIoFGLEDGEMYRhiCAjIHEAAYigUYQzILEAAYgAQYsQMYgwEyBxAAGIoFGEMyDRAAGIoFGLEDGIMBGEMyCBAAGIAEGLEDMggQABiABBixAzIFEAAYgAQyBRAAGIAEMggQABiABBixA0jnLlDtHVj6KXAHeAGQAQCYAcIEoAHADqoBBzMtMi4wLjK4AQPIAQD4AQGoAhTCAgoQABhHGNYEGLADwgIKEAAYigUYsAMYQ8ICBxAjGOoCGCfCAhAQABiKBRjqAhi0AhhD2AEBwgIEECMYJ8ICBxAjGIoFGCfCAg4QLhiABBixAxjHARjRA8ICCBAuGLEDGIoFwgILEC4YigUYsQMYgwHCAgsQABiKBRixAxiDAcICChAAGIoFGLEDGEPiAwQYACBBiAYBkAYKugYGCAEQARgB&sclient=gws-wiz-serp', headers=header)

# print(pag.content)

soup = BeautifulSoup(pag_dolar.content, 'html.parser')
soup2 = BeautifulSoup(pag_euro.content, 'html.parser')
soup3 = BeautifulSoup(pag_iene.content, 'html.parser')
# atributos = {'class': 'g'}
# Outra forma de conseguir acessar aos itens da div ou até outros itens desejados
# respostas = spup.find_all('div', attrs= atributos)
# respostas = soup.find_all('div', class_='g')

valor_dolar = soup.find_all('span', class_='DFlfde SwHCTb')[0]
valor_euro = soup2.find_all('span', class_='DFlfde SwHCTb')[0]
valor_iene = soup3.find_all('span', class_='DFlfde SwHCTb')[0]
print(valor_dolar)
print(valor_dolar.text)
print(valor_euro)
print(valor_euro.text)
print(valor_iene)
print(valor_iene.text)
