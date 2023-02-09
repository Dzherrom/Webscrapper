from bs4 import BeautifulSoup
import requests 
import pandas as pd

'''
---Program process step by step--
request url info
use beautiful soup to turn content into html
use find all func to find all team items
same process to find the score of every team
create variables and turn them into a list 

'''

#equipos
class Equipos:
    def __init__(self, url):
        self.url = url 
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser') 
        self.eq = self.soup.find_all('span', class_='nombre-equipo')
        self.pt = self.soup.find_all('td', class_= "destacado")
        self.lista_equipos = list()
        self.lista_puntos = list()


    '''
    stablish count
    in for cycle append every item from team to
    respective list inside the class
    repeat the same process for scores
    '''
    def appending(self):
        count = 0                   
        for i in self.eq:
            if count < 32:
                self.lista_equipos.append(i.text)
            else:
                break
            count +=1
        
        for i in self.pt:
            count = 0
            if count < 32:
                self.lista_puntos.append(i.text)
            else:
                break
            count +=1


    ''' 
    Dataframe func will turn the gathered info
    into an excel file 
    '''
    def DataFrame(self):
        self.df = pd.DataFrame({'Nombre':self.lista_equipos, 'Puntos':self.lista_puntos}, index = list(range(1,33)))
        self.df.to_csv('Clasificacion.csv', index =False)

Equipo = Equipos('https://resultados.as.com/resultados/futbol/mundial/2022/clasificacion/')
Equipo.appending()
Equipo.DataFrame()


