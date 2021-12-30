from urllib.request import urlopen, Request
import lxml, lxml.html
import os
import datetime
from bs4 import BeautifulSoup
import pandas

##carrega os papeis de stocksList.csv
stocksList = open('AllFiis.csv', 'r')
papeis = stocksList.read().split(';')
#papeis = [""]
##stocksList.close()

## pegando o dia e mês
now = datetime.datetime.now()
dia = now.day-1
mes = now.month
data = str(dia)+"."+str(mes)


## cria diretorio para a data de hoje-1 
#if (not os.path.isdir('./'+data)):
    #os.mkdir(data)

#def faltam(papeis):
    #print(len(papeis))

def getpapel(papel_):
    try:
                    print("#_#_#_#_#_#_"+papel_+"_#_#_#_#_#_#")
                    #trata o papel
                    papel = papel_.replace("11","")
                    #essa é a url base
                    url = "https://www.meusdividendos.com/fundo-imobiliario/"
                    #imprime o papel da request
                    #print(papel_)
                    
                    #concatena a url para fazer a request
                    r = Request(url+papel, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
                    soup = BeautifulSoup(html, 'html.parser')
                    #print(soup.prettify())
                    matrix = []
                    result = soup.find_all(class_="box-title", string="Histórico de dividendos")
                    result = result[0].find_parents(class_="box-solid")
                    rows = result[0].find_all("tr")
                    for index,row in enumerate(rows):
                        iterator=0
                        span = row.find_all("span")
                        text = []
                        
                        for sp in span:
                            text.append(sp.string)
                        matrix.append(text)
                        
                        #print(text)
                    #print(text[0])
                    ##print(result[0].prettify())
                    #print(matrix)
                    #print(matrix[0])

                    for ano in range(0,len(matrix[0])):
                        for mes in range(1,len(matrix)):
                            
                            valor=matrix[mes][ano+1]
                            print(papel_+"|"+str(matrix[0][ano])+"|"+str(mes)+"|"+str(valor))
                            #ano = matrix[0][ano]
                            #mes = matrix[mes][0]
                            #valor = matrix[mes][mes]
                            #print(ano+"/"+mes+"/")
                           
                        
                        #print(ano)
                        


                    
                    
                    papeis.remove(papel_)
                    
                    
    except Exception as e:
        print("#ERRO: ",papel," ", str(e))
        papeis.remove(papel_)
        #print(papeis)
    

while len(papeis)>0:
    for papel in papeis:        
        getpapel(papel)
            


