from bs4 import BeautifulSoup
import requests 
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/mundial/2022/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#equipos
class equipos:
    eq = soup.find_all('span', class_='nombre-equipo')
    equipos = []
    count = 0

    def appe(self, eq):
        for i in eq:
            if count < 25:
                equipos.append(i.text)
            else:
                break
            count +=1

#puntos
class puntos:
    pt = soup.find_all('td', class_= "destacado")
    puntos = []
    count = 0

    def appep(self, pt):    
        for i in pt:
            if count < 25:
                puntos.append(i.text)
            else:
                break
            count +=1

appep()
appe()
df = pd.DataFrame({'Nombre':self.equipos, 'Puntos':self.puntos}, index = list(range(1,21)))
df.to_csv('Clasificacion.csv', index =False)

print(df)

