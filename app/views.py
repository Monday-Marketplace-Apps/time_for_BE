from django.shortcuts import render

from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from datetime import date, datetime
import pandas as pd
from datetime import datetime
import json



# Create your views here.

# nombres = ['Miguel','Rubén', 'Walter']

# horas = [[1,0.5,2],[0.75,4,3],[6,0.25,5]]
# fechas =[date(2022,10,12).strftime('%d/%m/%Y'),date(2022,10,13).strftime('%d/%m/%Y'),date(2022,10,14).strftime('%d/%m/%Y')]



class api(APIView):
    def get(self, request):
        # datos = []
        # horas1=[]
        # horas2=[]
        # horas3=[]
        # # for i in range(len(nombres)):
        # #     datos.append({'name':nombres[i]})
            
        # for i in range(1):
        #     for x in range(3):
        #         horas1.append({fechas[x]:horas[x][i]})
        
        # for i in range(1):
        #     for x in range(3):
        #         horas2.append({fechas[x]:horas[x][i+1]})
                
        # for i in range(1):
        #     for x in range(3):
        #         horas3.append({fechas[x]:horas[x][i+2]})
        # total_horas= [horas1,horas2,horas3]
        # print('horas1',horas1)
        # print('horas2',horas2)
        # print('horas3',horas3)
        # datos= [{'name':'Miguel','horas':horas1},{'name':'Ruben','horas':horas2},{'name':'Walter','horas':horas3}]

#    ,
#                                         'prediccion':{'diario':[],
#                                                       'semanal':[],
#                                                       'mensual':[]}
        
            
        # for fecha in fechas:
        #     for i in range(3):
        #         for x in range(3):
        #             fecha
        
        # for i in range(3):
        #     datos[i]['horas']=fechas
    
    
        datos_miguel={'miguel':{'2022-9-1':3,'2022-9-5':1,'2022-9-15':6,'2022-9-20':4,'2022-10-2':4,'2022-10-5':7,'2022-10-12':1,'2022-10-13':6,'2022-10-17':3}}
        datos_ruben={'ruben':{'2022-9-3':1,'2022-9-7':4,'2022-9-13':2,'2022-9-15':9,'2022-9-27':0.5,'2022-10-4':4,'2022-10-5':5,'2022-10-10':5,'2022-10-15':6,'2022-10-18':8}}
        datos_walter={'walter':{'2022-10-1':1,'2022-10-9':3,'2022-10-10':8,'2022-10-13':6,'2022-10-17':2}}

        datosHoras = [datos_ruben,datos_walter,datos_miguel]
        col1={}
        col2={}
        columnas = [col1,col2]

        nombres=[]
        for i in datosHoras:
            for x in i:
                nombres.append(x)
        # Creacion dataframe valores NaN
        dfDatosReales=pd.DataFrame()
        start =pd.Timestamp('2022-09-01')#.strftime("%d-%m-%Y")
        end = pd.Timestamp.now()
        fechas = pd.date_range(start, end)#.strftime("%d-%m-%Y")
        dfDatosReales = pd.DataFrame(index = fechas,columns = nombres)
        
        # Introduccion datos diarios reales en dataframe 
        for i in datosHoras:
            for nombre,valores in i.items():

                for fecha,horas in valores.items():
                    dfDatosReales.loc[fecha,nombre]=horas  
        
        #  Rellenamos NaN con 0
        dfDatosReales = dfDatosReales.fillna(0)
        
        # hacemos lista de datos individuales diarios     
        
        listaDfsDatosRealesIndividuales=[]
        for i in dfDatosReales:
            listaDfsDatosRealesIndividuales.append(dfDatosReales.loc[:,[i]])
        
        # creamos lista de las fechas a cambiar en datos para formato fecha deseado
        
        lista=dfDatosReales.index.tolist()
        listamodificada=[]

        for i in lista:
            
            listamodificada.append(i.strftime("%d-%m-%Y"))
        
        
        # creamos lista para introducir los valores diarios con formato fecha deseado
        
        lista=dfDatosReales.index.tolist()
        listamodificada=[]

        for i in lista:
            
            listamodificada.append(i.strftime("%d-%m-%Y"))

        # creacion lista con dataframes de fecha modificada para json
        dataframeDatoRealAJson=[]
        for i in listaDfsDatosRealesIndividuales:
            i.index = listamodificada
            dataframeDatoRealAJson.append(i)
        
        # creacion lista json horas diarias
        
        listaJsonDiarios=[]

        for i in range(len(dataframeDatoRealAJson)):
            
            a=json.loads(dataframeDatoRealAJson[i].to_json())
            listaJsonDiarios.append(a)

        listaJsonDiarios
        
        
        #agrupacion datos semanales
        dfDatosRealesSemanal=dfDatosReales.groupby(pd.Grouper(freq='1W')).sum()
        
        
        #lista datos semananeles individuales
        listaDfsDatosRealesIndividualesSemanales=[]
        for i in dfDatosRealesSemanal:
            listaDfsDatosRealesIndividualesSemanales.append(dfDatosRealesSemanal.loc[:,[i]])
        
        #cambio formato fecha datos semanales
        listasemanales=dfDatosRealesSemanal.index.tolist()
        listamodificadasemanales=[]

        for i in listasemanales:
            
            listamodificadasemanales.append(i.strftime("%d-%m-%Y"))

        
        #cambio index semanales a datos visibles
        dataframeDatoRealSemanalAJson=[]
        for i in listaDfsDatosRealesIndividualesSemanales:
            i.index = listamodificadasemanales
            dataframeDatoRealSemanalAJson.append(i)
        
        #lista json salida datos semanales 
        listaJsonSemanal=[]

        for i in range(len(dataframeDatoRealSemanalAJson)):
            
            a=json.loads(dataframeDatoRealSemanalAJson[i].to_json())
            listaJsonSemanal.append(a)
        
        #agrupacion datos mensuales
        dfDatosRealesMensuales=dfDatosReales.groupby(pd.Grouper(freq='1M')).sum()
        
        
        #lista datos Mensuales individuales
        listaDfsDatosRealesIndividualesMensuales=[]
        for i in dfDatosRealesMensuales:

            listaDfsDatosRealesIndividualesMensuales.append(dfDatosRealesMensuales.loc[:,[i]])

        #cambio formato fecha datos mensuales
        listaMensuales=dfDatosRealesMensuales.index.tolist()
        listamodificadaMensuales=[]

        for i in listaMensuales:
            
            listamodificadaMensuales.append(i.strftime("%d-%m-%Y"))

        #cambio index mensuales a datos visibles
        dataframeDatoRealMensualAJson=[]
        for i in listaDfsDatosRealesIndividualesMensuales:
            i.index = listamodificadaMensuales
            dataframeDatoRealMensualAJson.append(i)
        
        # creacion de lista de json mensual
        listaJsonMensual=[]

        for i in range(len(dataframeDatoRealMensualAJson)):
            
            a=json.loads(dataframeDatoRealMensualAJson[i].to_json())
            listaJsonMensual.append(a)
        
        
        # prueba cambio datos diarios para grafico
        pruebaListaDiarios=[]
        for i in dataframeDatoRealAJson:
            b=[]
            for x in range(len(i)):
                
                b.append({i.index[x]:i.iloc[x,0]})
                
            pruebaListaDiarios.append(b)    
            #print({i.index[x]:i.iloc[x,0]})
            #i.columns.values
          
            # prueba cambio datos semanal para grafico
        pruebaListaSemanal=[]
        for i in dataframeDatoRealSemanalAJson:
            b=[]
            for x in range(len(i)):
                
                b.append({i.index[x]:i.iloc[x,0]})
                
            pruebaListaSemanal.append(b) 
        #print(pruebaListaSemanal)
        
        # prueba cambio datos mensual para grafico
        pruebaListaMensual=[]
        for i in dataframeDatoRealMensualAJson:
            b=[]
            for x in range(len(i)):
                
                b.append({i.index[x]:i.iloc[x,0]})
                
            pruebaListaMensual.append(b) 
        #print(pruebaListaSemanal)

        print(pruebaListaDiarios[2])  
        
        #creacion estructura de datos json
        datos=[{'columna1':
            [{'ruben': 
                [{'datoreal':
                    [{'diario':pruebaListaDiarios[0]},
                    {'semanal':pruebaListaSemanal[0]},
                    {'mensual':pruebaListaMensual[0]}]},
                {'prediccion':
                    [{'diario':[]},
                    {'semanal':[]},
                    {'mensual':[]}]}]},
             {'walter': 
                 [{'datoreal':
                     [{'diario':pruebaListaDiarios[1]},
                      {'semanal':pruebaListaSemanal[1]},
                      {'mensual':pruebaListaMensual[1]}]},
                    {'prediccion':
                        [{'diario':[]},
                        {'semanal':[]},
                        {'mensual':[]}]}]},
             {'miguel': 
                 [{'datoreal':
                     [{'diario':pruebaListaDiarios[2]},
                      {'semanal':pruebaListaSemanal[2]},
                      {'mensual':pruebaListaMensual[2]}]},
                     {'prediccion':
                         [{'diario':[]},
                          {'semanal':[]},
                          {'mensual':[]}]}]}]},
               {'columna2':
            [{'fede': 
                [{'datoreal':
                    [{'diario':pruebaListaDiarios[0]},
                    {'semanal':pruebaListaSemanal[0]},
                    {'mensual':pruebaListaMensual[0]}]},
                {'prediccion':
                    [{'diario':[]},
                    {'semanal':[]},
                    {'mensual':[]}]}]},
             {'walter': 
                 [{'datoreal':
                     [{'diario':pruebaListaDiarios[1]},
                      {'semanal':pruebaListaSemanal[1]},
                      {'mensual':pruebaListaMensual[1]}]},
                    {'prediccion':
                        [{'diario':[]},
                        {'semanal':[]},
                        {'mensual':[]}]}]},
             {'anastasio': 
                 [{'datoreal':
                     [{'diario':pruebaListaDiarios[2]},
                      {'semanal':pruebaListaSemanal[2]},
                      {'mensual':pruebaListaMensual[2]}]},
                     {'prediccion':
                         [{'diario':[]},
                          {'semanal':[]},
                          {'mensual':[]}]}]}]}]
                            
        print(type(datos)) 
        # datos=json.dumps(datos)
        # print(type(datos))
        
        
        
        return Response (datos)