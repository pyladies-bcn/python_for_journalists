# -*- coding: utf-8 -*-
"""
Created on 

@author: PyLadiesBCN (@PyLadiesBCN)
"""

"""
### 0
Let's make sure we are in the right directory 
where we have our files
"""
#import os
#print os.getcwd()

"""
### 1
We import our library (pandas) and read csv to dataframe
"""

import pandas as pd
df = pd.read_csv("02_data_kiva_loans.csv")

#print df.head()
#print df.columns


"""
### 2
Let's count values.
What is the country with most loans?
"""

#print df.pais.value_counts()

##We could plot it
#df.pais.value_counts()[:10].plot(kind="bar")

## Another method: with Counter
import collections
cuenta_paises = collections.Counter(df["pais"]) 
top_actividades = collections.Counter(df["actividad"]).most_common()
## See that Counter returns data in two different formats

"""
### 3
Stats. 
What's the average loan? How much money has people lent? What's the maximum loan? Let's do some 
basic stats.
"""
## With describe() we have the basic statistics: mean, standard deviation, maximun, count...
#df.describe() 

## With sum() we will know the total money lent
#df.cantidad.sum()

## Mean, median, variance, standard deviation... 
#df.mean()
#df.var()
#df.std()

## For more advanced statistics, the Scypy packages 
# provides everything you may need 

"""
### 4
Grouping by.
"""
df_gen = df.groupby(["genero"])
print df_gen.describe()

df_gen_estatus = df.groupby(["genero", "estatus"])
print df_gen_estatus.count()

"""
### 5
Which are the countries with more defaults?
"""
## There are only 162 defaulted loans over 20.000 loans. 
## Let's see where

defaulted = df[df["estatus"]=="defaulted"]

## We save the countries with defaulted loans into a dictionary
dict_impagos = collections.Counter(defaulted["pais"]) 

## And the general count of countries into another dictionary
dict_paises = collections.Counter(df["pais"])

## With a loop we will make the calculation: defaulted loans over total loans in that country
for i in dict_paises.keys():
    if i in dict_impagos.keys():
        impago = float(dict_impagos[i])
        total = float(dict_paises[i])
        porcentaje = (impago/total)*100
        print i , round(porcentaje, 2), "%"

## Dominican Republic is a clear outlier!

