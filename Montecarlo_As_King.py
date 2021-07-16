# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import copy, random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#Estos son los juegos

#Encontrar un as y un rey seguidos del mismo palo.
def As_King (deck):
    condition = False
    for i in range (len(deck)-1):
        if (deck[i] == 'AS' and deck[i+1] == 'KS'): 
            condition = True
            break
        elif (deck[i] == 'AH' and deck[i+1] == 'KH'):
            condition = True
            break
        elif (deck[i] == 'AC' and deck[i+1] == 'KC'):
            condition = True
            break
        elif (deck[i] == 'AD' and deck[i+1] == 'KD'):
            condition = True
            break
            
    return condition



##############################################################################



#Programa Monte Carlo que baraja el deck n veces e imprime la probabilidad con la que ocurre la condición del juego.
def MonteCarlo (trials,deck,game):
    success = 0
    for i in range (trials):
        random_deck = copy.deepcopy(deck)
        random.shuffle(random_deck)
        if game(random_deck) == True:
            success += 1
    return ((success/trials) * 100)

##############################################################################



#Calcula el promedio de probabilidades y desviaciones estándar.
def Deviation_Multirun (runs, trials_list, deck, game):
    values_list_1 = []
    values_list_2 = []
    values_mean_list_1 = []
    values_mean_list_2 = []
    deviation_list = []
    for trials in trials_list:
        for iter in range (runs):
            values_list_1.append(MonteCarlo(trials, deck, game))
            values_list_2.append(MonteCarlo(trials, deck, game)**2)
        values_mean_list_1.append(np.mean(values_list_1))
        values_mean_list_2.append(np.mean(values_list_2))
    for iter in range (len(trials_list)):
        deviation_list.append(np.sqrt((values_mean_list_2[iter] - values_mean_list_1[iter]**2)/(runs)))
    return values_mean_list_1, deviation_list



#Calcula la diferencia entre el promedio de probabilidades y la probabilidad analítica
def Difference (trials_list,values_list,values_analytic):
    dif_list = []
    for iter in range (len(trials_list)):
        dif_list.append(values_list[iter]-values_analytic[iter])
    return dif_list
##############################################################################



#Aquí se guarda en un archivo de excel la tabla con las estadísticas
def D_frame (trials_list,values_list,values_analytic,deviation_list,dif_list):
    d = dict()
    d['<Probabilidad>'] = pd.Series(values_list,index = trials_list)
    d['Probabilidad Analítica'] = pd.Series(values_analytic,index = trials_list)
    d['Desviación Estándar'] = pd.Series(deviation_list,index = trials_list)
    d['Diferencia'] = pd.Series(dif_list,index = trials_list)
    df = pd.DataFrame(d)
    df.index.name = 'Intentos'
    df.to_excel('Estadísticas As_King.xlsx')

###############################################################################



#Aquí se guarda una imagen con la gráfica de la probabilidad en función del número de intentos
def Graph (trials_list, values_list,realvalue):
    fig = plt.figure(figsize = (8,4),dpi = 150)
    ax = fig.add_axes([0.1,0.1,0.8,0.7])
    ax.set_facecolor('whitesmoke')
    ax.set_xlabel('Número de intentos (en escala logarítmica)')
    ax.set_ylabel('Probabilidad (%)')
    ax.set_title('Probabilidad As_King')
    
    
    plt.plot(trials_list,values_list,linestyle = 'None',marker = 'o',markerfacecolor = 'b',mec = 'None',ms = 9)
    plt.xscale('log',base = 10)
    plt.xticks(trials_list)
    plt.yticks(values_list)
    plt.axhline(realvalue,color = 'r', linestyle = '--')
    plt.grid(axis = 'both', color = 'k', ls = 'dashed',lw = '0.5')
    plt.savefig('Probabilidad As_King.jpg')
    plt.show()
##############################################################################



#Corre el programa
def Run():
    values_list, deviation_list = Deviation_Multirun(runs,trials_list,deck,As_King)
    values_analytic = [realvalue]*len(trials_list)
    dif_list = Difference(trials_list,values_list,values_analytic)
    
    D_frame(trials_list,values_list,values_analytic,deviation_list,dif_list)
    Graph (trials_list, values_list,realvalue)
##############################################################################



#Esta es la baraja
deck = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
        'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
        'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',
        'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD']

#Variables que se utilizan
trials_list = [10,100,1000,10000] #Lista con número de veces que se baraja el deck
runs = 100 #Número de veces que se corre el programa para cada trial
realvalue = 7.692308 #Valor de la probabilidad analítica del juego

Run() #Activa las funciones del programa
# Para mejores resultados puede aumentar el número de runs o agregar un mayor número de intentos en trials_list.




