#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[8]:


def __get_years():
  years = []
  for i in range(1960,2022):
    years.append(str(i))
  return years


# In[11]:


#"Melt" es una operación en Pandas que permite transformar un DataFrame de formato ancho a uno de formato largo
def __make_melt(datos):
  x = datos.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],value_vars= __get_years(),var_name='Year',value_name='Valor')
  x['Year'] = x['Year'].astype(int)
  return x


# In[10]:


#"Pivot" es una operación en Pandas que permite transformar un DataFrame de formato largo a uno de formato ancho.
def __make_pivot(datos):
  x = datos[['Country Name', 'Country Code','Indicator Name', 'Indicator Code','Year', 'Valor']]
  datos = x.pivot(index=['Country Name', 'Country Code', 'Year'],columns=['Indicator Name'],values='Valor').reset_index()
  return datos


# In[9]:


def __make_clear(datos):
  datos.fillna(0.,inplace=True)
  return datos


# In[12]:


def Main_PreProcesamiento(datos):
  datos = __make_melt(datos)
  datos = __make_pivot(datos)
  datos = __make_clear(datos)
  return datos;

