#!/usr/bin/env python
# coding: utf-8

# In[6]:


import IPython.display as display
from IPython.display import Markdown
from PIL import Image
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


path_graficos = '/content/drive/MyDrive/Proyecto/Graficos/'


# In[8]:


def __get_describe(x):
  print(x.describe())


# In[9]:


def __get_info(x):
  print(x.info())


# In[10]:


def __get_columns(x):
  print(x.columns)


# In[11]:


def __get_columns_corr(x):
  return x[[
            'Nivel de instrucción, al menos escuela primaria completa, población de más de 25 años, varones (%) (acumulativo)',
            'Nivel de instrucción, al menos escuela primaria completa, población de más de 25 años, mujeres (%) (acumulativo)',
            'Nivel de instrucción, al menos escuela terciaria de ciclo corto finalizada, población de más de 25 años, total (%) (acumulativo)',
            'Nivel de instrucción, al menos nivel de doctorado o equivalente, población de más de 25 años, total (%) (acumulativo)'
            ]]


# In[12]:


def __get_graf_corr(x, size = (15,15)):
  header = '\nUniversidad de Guayaquil - Facultad de Ingeniería Industrial\nIngeniería en Sistemas de Información - Ciencia de Datos\Proyecto Grupal'
  plt.figure(figsize=size,facecolor=('xkcd:lavender'))
  hm = sns.heatmap(x.corr().round(2), vmin=-1, vmax=1, annot=True)
  hm.set_title('Mapa de Calor -Análisis exploratorio y correlacional'+header, fontdict={'fontsize':12}, pad=12)
  plt.show(block=False)
  plt.pause(2)  


# In[13]:


def __get_corr(x):
  y = __get_columns_corr(x)
  z = y.columns
  print(y.corr())
  print('\n')
  __get_graf_corr(y)
  print('\n')
  print('Las variables relacionadas son: \n {} \n {} \n {} \n {}'.format(z[0],z[1],z[2],z[3]))


# In[14]:


def __get_menu(x):
    print("0. Salir")
    print("1. Describe")
    print("2. Info")
    print("3. Grafico Corr")
    print("4. Columns")


    opcion = input("Seleccione una opción: ")

    if opcion == "1":
      __get_describe(x)
      opcion = input("Enter Para Borrar")
      display.clear_output(wait=True)
    elif opcion == "2":
      __get_info(x)
      opcion = input("Enter Para Borrar")
      display.clear_output(wait=True)
    elif opcion == "3":
      __get_corr(x)
      opcion = input("Enter Para Borrar")
      display.clear_output(wait=True)
    elif opcion == "4":
      __get_columns(x)
      opcion = input("Enter Para Borrar")
      display.clear_output(wait=True)
    elif opcion == "0":
      display.clear_output(wait=True)
      return False
    else:
        print("Opción no válida")
    
    return True


# In[15]:


def Main_EDA(datos):
  continuar = True  
  while continuar:
    continuar = __get_menu(datos)

