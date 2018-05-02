# -*- coding: utf-8 -*-
"""
Created on 

@author: PyLadiesBCN (@PyLadiesBCN)

"""

"""
#1
We check that we have all our files
in the directory
"""
#import os
#print os.getcwd()
#print os.listdir('.')

"""
#2 
We are going to load the .csv in a dataframe, 
but first we need to import pandas library
"""
import pandas as pd 
raw_data = pd.read_csv("01_data.csv") #We call pandas' functions with pd + dot + name_of_function
#print raw_data #Let's show the content of the dataframe

"""
#3 
This is a real example, so the data is messy. 
We'll have to "clean" the dataframe first. 
For example, the 2 last columns are empty, so we'll delete them.
The first 3 rows and the 7 last rows are also useless. 
"""
#print raw_data.columns 
del raw_data["Unnamed: 14"] #"Del" is for "delete"
del raw_data["Unnamed: 15"]
raw_data = raw_data.drop([0, 1, 2, 8, 9, 10, 11, 12, 13, 14]) #Drop is the method for eliminating rows

"""
#4
Dataframes have an index: some values that identify each row
Also, months should be the names of the columns, instead of "Unnamed"
"""
meses = pd.Series(raw_data.ix[3]) #We select row 3, with the months in it, and we save it in the variable "meses" 
meses["Unnamed: 0"] = "fecha"
raw_data.columns = meses #We assign the variable meses as the name of columns
raw_data = raw_data.drop(3)
#print raw_data.index #The index is a series of numbers
#We want the name of the companies as our index
empresas = ["Telefónica", "Cableros", "Resto", "Total"]
raw_data.index = empresas #We set the variable "empresas" as our index
del raw_data["fecha"] 

"""
#5 
Actually, python doesn't understand that the values inside the dataframe are numbers.
So we first need to transform them into numbers. We will do that with a "for" and an "if". 
"""
#print raw_data.dtypes #The types are "object", not numbers 

for columna in raw_data.columns:
    if raw_data[columna].dtypes == object:
        raw_data[columna] = raw_data[columna].astype(int)

#print raw_data.dtypes #Now they are all integers

"""
#6
Maybe we want to have the months as rows and the name of the companies as columns. 
We are going to rotate the dataframe: to transpose. 
"""
df = raw_data.T #T is for transpose. We save the new dataframe with another name

"""
#7
How do we select rows or columns? How do we change the values?
"""

#df[0:3] #First 3 rows
#df.ix[:3] #Another way to do the same
#df.ix[0:3, 0:2] #First 3 rows and first 2 columns
#df["Total"] #We can select a column by its name

#df[df["Telefónica"] > 5740000] #We select with conditions

#df.ix["Nov-2013", "Telefónica"] #We access to a cell
#df.ix["Nov-2013", "Telefónica"] = 200 #To modify the value of that cell

"""
#8
Python doesn't know that "Nov-2013", "Dic-2013"... are dates. So
we are going to change that. 
"""
##We create a range of dates from november'13, with 13 periods and monthly frequency
##We save it as "fechas"
fechas = pd.date_range("11/2013", periods=13, freq="M")

## We set "fechas" as the index of our dataframe
df.index = fechas

"""
#9
Saving data in "01_datos_limpios_script.csv" file
"""

import csv ##this line should be at the top of this document
file = open("01_datos_limpios_script.csv", "w")
df.to_csv(file, sep=",", encoding = "utf-8")
