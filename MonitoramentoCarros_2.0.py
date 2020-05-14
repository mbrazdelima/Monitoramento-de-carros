import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

local = r'C:\Users\mbraz\Downloads\Carro_1.xls'

df = pd.read_excel(local)
df['Inicio'].replace("?", np.nan, inplace=True)
df.dropna(subset=['Inicio'], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

ListaInicioHora = []
ListaInicioMinuto = []
ListaFinalMinuto = []
ListaFinalHora = []

for i in df['Inicio']:
    ListaInicioHora.append(int(i[0:2]))
    ListaInicioMinuto.append(int(i[3:])/60)

for i in df['Final']:
    ListaFinalHora.append(int(i[0:2]))
    ListaFinalMinuto.append(int(i[3:])/60)

HoraInicio = pd.DataFrame(ListaInicioHora) + pd.DataFrame(ListaInicioMinuto)
df['HoraInicio'] = HoraInicio

HoraFinal = pd.DataFrame(ListaFinalHora) + pd.DataFrame(ListaFinalMinuto)
df['HoraFinal'] = HoraFinal

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro']

df['Mês'] = pd.Categorical(df['Mês'], categories=meses, ordered=True)
df.sort_values('Mês', inplace=True)

dropRows = list()
for i in range(0, len(df)):
    horas = df['HoraFinal'][i] - df['HoraInicio'][i] 
    if horas <= 4:
        dropRows.append(i)
df.drop(dropRows, inplace=True)
df.reset_index(inplace=True)




yInicio = df['HoraInicio']
yFinal = df['HoraFinal']
x = df['Mês']
plt.scatter(x, yInicio, color='g', s=50, alpha=0.4)
plt.scatter(x, yFinal, color='r', s=50, alpha=0.4)
plt.xticks(rotation=45)
plt.yticks(range(0, 25))
plt.ylim(0, 24)
plt.xlabel('Mês')
plt.ylabel('Hora (h)')
plt.title(f'Carro 1')
plt.axhline(y=17, color='black')
plt.axhline(y=8, color='black')
plt.show()




tabela = pd.DataFrame()
tabela['Meses'] = meses
countInicio = countFinal = 0
listaPorcentagemInicio = list()
listaPorcentgemFinal = list()
listaMediaInicio = list()
listaMediaFinal = list()
jornadaMensais = list()
mediaJornada = list()
for mes in meses:
    tabelaMes = df.loc[df.Mês == mes]
    tabelaMes.reset_index(inplace=True) 
    for i in range(0, len(tabelaMes)):
        if tabelaMes['HoraInicio'][i] > 8:
            countInicio += 1
        if tabelaMes['HoraFinal'][i] < 17:
            countFinal += 1 
    if tabelaMes.shape[0] == 0:
        listaPorcentagemInicio.append(0)
        listaPorcentgemFinal.append(0)
        listaMediaInicio.append(0)
        listaMediaFinal.append(0)
        mediaJornada.append(0)
    else:
        for i in range(0, len(tabelaMes)):
            jornada = tabelaMes['HoraFinal'][i] - tabelaMes['HoraInicio'][i]     
            jornadaMensais.append(jornada)                 
        mediaJornada.append(round(np.mean(jornadaMensais),1))
        jornadaMensais.clear()
        porcentagemInicio = (countInicio/tabelaMes.shape[0])*100
        porcentagemFinal = (countFinal/tabelaMes.shape[0])*100
        listaPorcentagemInicio.append(int(porcentagemInicio))
        listaPorcentgemFinal.append(int(porcentagemFinal))
        listaMediaInicio.append(round(tabelaMes['HoraInicio'].mean(), 1))
        listaMediaFinal.append(round(tabelaMes['HoraFinal'].mean(),1))
    countInicio = countFinal = 0

tabela['% Inicio antes das 8h'] = listaPorcentagemInicio
tabela['% Término antes das 17h'] = listaPorcentgemFinal
tabela['Horário médio de início'] = listaMediaInicio
tabela['Horário médio de término'] = listaMediaFinal
tabela['Tempo média de jornada'] = mediaJornada

tabela.to_excel(r'C:\Users\mbraz\Downloads\indicadores.xlsx', index=False)
