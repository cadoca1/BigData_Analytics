#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:15:50 2020

@author: carlosdonosocabero
"""

#load basiclibraries
import os
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype #For definition of custom categorical data types (ordinal if necesary)
import matplotlib.pyplot as plt
import seaborn as sns  # For hi level, Pandas oriented, graphics
import scipy.stats as stats  # For statistical inference 

os.chdir('/Users/carlosdonosocabero/Desktop/MDA/PEP/CodeyData')
os.getcwd()

life_expectancy = pd.read_excel("life_expectancy.xlsx", sheet_name= 'T6')
life = life_expectancy[life_expectancy['Variables'] == 'Total Life Expectancy At Birth (Residents)']
life.to_csv('life_expectancy.csv')
l = pd.read_csv ("life_expectancy.csv")
l['2018']

cpi = pd.read_csv('cpi.csv', sep=',', decimal='.')
cpi = cpi.drop(['Unnamed: 0'], axis=1)
#cpi = cpi[cpi.category == 'General']
cpi.to_csv('cpi.csv')

density = pd.read_csv('density.csv', sep=',', decimal='.')
density['2018']

population = pd.read_csv('population.csv', sep=',', decimal='.')
population['2019']

gdp_pc = pd.read_csv('gdp_pc.csv', sep=',', decimal='.')
gdp_pc['2019']

tax_burden = pd.read_csv('tax_burden.csv', sep=',', decimal='.')
tax_burden['2018']

business = pd.read_excel("business.xlsx", sheet_name= 'Results')
business = business[business['Year'] == 'DB2020']
business.to_csv('doing_business.csv')
doing_business = pd.read_csv('doing_business.csv', sep=',', decimal='.')
busy = doing_business[['Economy', 'Year', 'Ease of doing business rank (DB20)', 'Ease of doing business score (DB17-20 methodology)']]
busy.to_csv('doing_business.csv')

hdi = pd.read_csv('hdi.csv', sep=',', decimal='.', header= 1)
hdi = hdi[(hdi.Country=='Austria') | (hdi.Country=='Germany') | (hdi.Country=='Spain') | (hdi.Country=='Singapore') | (hdi.Country=='United States')]
hdi.to_csv('hdi.csv', index = False)

freedom = pd.read_csv('freedom.csv', sep=',', decimal='.')
freedom['freedom'] = (freedom['Personal Freedom'] + freedom['Economic Freedom']) / 2
freedom.to_csv('freedom.csv', index = False)

museums = pd.read_csv('museums.csv', sep=',', decimal='.')
#pop['2017']
#m = museums['museums']/5612253*100000
museums.to_csv('museums.csv', index=False)

landscape = pd.read_csv('landscape.csv', sep=';', decimal=',')

je = density.transpose()
je.to_csv('dens.csv', index=False)
###### CPI
import math as math

n2 = cpi.cpi[0]
    aux = []
    aux.append(0)
    for i in range(1, len(cpi.cpi)):
        n1 = cpi.cpi[i]
        if n1 == n2:
            aux.append(0)
        else:
            res = (math.log(n1)-math.log(n2))/(n1-n2)
            aux.append(res)
            n2 = cpi.cpi[i]

    variacion = pd.DataFrame({'Variacion': aux})

    res = pd.concat([cpi, variacion], axis=1)

res.to_csv('cpi.csv')
res1 = res.loc[(res['year']>2006)]
res1.Variacion.mean()*100

#### Separar meses-años: temperatura

c_temp = pd.read_csv('c_temp.csv', sep=',', decimal='.')

year = []
month = []
for a in c_temp.month:
    aux = str(a)
    year.append(aux[:4])
    month.append(aux[5:7])

dates = pd.DataFrame({'Year': year, 'Month': month})

c_temp = pd.concat([c_temp, dates], axis=1)
c_temp= c_temp.drop(['month'], axis=1)

temp = c_temp.loc[(c_temp['Year']>='2000')]
temp.mean_temp.mean()

#### Separar meses-años: lluvia

c_rainy_days = pd.read_csv('c_rainy_days.csv', sep=',', decimal='.')

year = []
month = []
for a in c_rainy_days.month:
    aux = str(a)
    year.append(aux[:4])
    month.append(aux[5:7])

dates = pd.DataFrame({'Year': year, 'Month': month})

c_rainy_days = pd.concat([c_rainy_days, dates], axis=1)
c_rainy_days= c_rainy_days.drop(['month'], axis=1)

rainy = c_rainy_days.loc[(c_rainy_days['Year']>='2000')]
rainy.no_of_rainy_days.mean()
rainy.to_csv('c_rainy_days.csv')