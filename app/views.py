from django.shortcuts import render

from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from datetime import date, datetime


# Create your views here.

nombres = ['Miguel','Rubén', 'Walter']

horas = [[1,0.5,2],[0.75,4,3],[6,0.25,5]]
fechas =[date(2022,10,12).strftime('%d/%m/%Y'),date(2022,10,13).strftime('%d/%m/%Y'),date(2022,10,14).strftime('%d/%m/%Y')]



class api(APIView):
    def get(self, request):
        datos = []
        horas1=[]
        horas2=[]
        horas3=[]
        # for i in range(len(nombres)):
        #     datos.append({'name':nombres[i]})
            
        for i in range(1):
            for x in range(3):
                horas1.append({fechas[x]:horas[x][i]})
        
        for i in range(1):
            for x in range(3):
                horas2.append({fechas[x]:horas[x][i+1]})
                
        for i in range(1):
            for x in range(3):
                horas3.append({fechas[x]:horas[x][i+2]})
        total_horas= [horas1,horas2,horas3]
        print('horas1',horas1)
        print('horas2',horas2)
        print('horas3',horas3)
        datos= [{'name':'Miguel','horas':horas1},{'name':'Ruben','horas':horas2},{'name':'Walter','horas':horas3}]

   
        
            
        # for fecha in fechas:
        #     for i in range(3):
        #         for x in range(3):
        #             fecha
        
        # for i in range(3):
        #     datos[i]['horas']=fechas
    
                
            
                
            
        
        return Response (datos)