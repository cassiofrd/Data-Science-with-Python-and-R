#Nesse script vou elaborar uma rotina de previsão de algumas variáveis
import numpy as np
import pandas as pd
import os
os.getcwd()

#para importar .csv devemos utilizar o padrão abaixo

dataset=pd.DataFrame(pd.read_excel('HC Diversity.xlsx'))
dataset.head()

#vou criar as dummies que são relevantes para que eu faça as estimações
#primeiro uma dummy agro que está em branco como padrão e tem valor 1 se a categoria é agro
#temos também que transoformar a variável em numérica para poder fazer as operações depois
#essa variável tem o valor nulo como padrão porque será utilizada como filtro para as demais
dataset['Agro']=dataset['BASF_OrgArea']
dataset.loc[dataset.BASF_OrgArea=='AP', 'Agro'] = 1
dataset.loc[dataset.BASF_OrgArea!='AP', 'Agro'] = None
dataset['Agro']=pd.to_numeric(dataset['Agro'])
type(dataset['Agro'])

#colo só queremos os dados de agro, vamos deletar todos os dados para os quais a variável
#Agro for diferente de 1
dataset=dataset.drop(dataset[dataset['Agro']!=1].index)

#agora vamos criar uma dummy mulher que tem o valor 0 como padrão e 1 se a pessoa é mulher
#temos também que transoformar a variável em numérica para poder fazer as operações depois
dataset['Mulher']=None
dataset.loc[dataset.Gender=='Female', 'Mulher'] = 1
dataset.loc[dataset.Gender=='Male', 'Mulher'] = 0
dataset['Mulher']=pd.to_numeric(dataset['Mulher'])
type(dataset['Mulher'])

#agora vamos criar uma dummy lider que tem o valor 0 como padrão e 1 se a pessoa tem cargo d eliderança
#temos também que transoformar a variável em numérica para poder fazer as operações depois
dataset['Lider']=None
dataset.loc[dataset.Leadership=='YES', 'Lider'] = 1
dataset.loc[dataset.Leadership=='NO', 'Lider'] = 0
dataset.loc[dataset.Leadership=='Yes', 'Lider'] = 1
dataset.loc[dataset.Leadership=='No', 'Lider'] = 0
dataset['Lider']=pd.to_numeric(dataset['Lider'])
type(dataset['Lider'])
dataset['Lider'].describe()
dataset['Mulher'].describe()

#vamos criar uma variável que considera apenas quem é lider e, dentre quem é
#lider, seleciona quem é mulher
dataset['MLider']=None
dataset.loc[dataset.Lider==1, 'MLider'] = 0
#IMPORTANTÍSSIMO: COMO VISTO ABAIXO, CONSICIONAL COM MAIS DE UMA RELAÇÃO DE
#DESIGUALDADE EM PYTHON, COM iloc, TEM QUE TER PARÊNTESES, CASO CONTRÁRIO NÃO FUNCIONA
dataset.loc[(dataset.Lider==1) & (dataset.Mulher==1), 'MLider'] = 1
dataset['MLider']=pd.to_numeric(dataset['MLider'])
type(dataset['MLider'])
dataset['MLider'].describe()

#agora vamos criar uma dummy lider que tem o valor 0 como padrão e 1 se a pessoa é PCD
#temos também que transoformar a variável em numérica para poder fazer as operações depois
dataset['Deficiencia']=None
dataset.loc[dataset.PCD_yes_no=='Yes', 'Deficiencia'] = 1
dataset.loc[dataset.PCD_yes_no=='No', 'Deficiencia'] = 0
dataset['Deficiencia']=pd.to_numeric(dataset['Deficiencia'])
type(dataset['Deficiencia'])

#agora vou fazer variáveis com a % de mulheres do Agro por data
dataset['Media_Mulher'] = (dataset['Mulher']).groupby(dataset['Calendar Year/Month']).transform('mean')

#agora vou fazer variáveis com a % de pessoa com deficiência do Agro por data
dataset['Media_Deficiencia'] = (dataset['Deficiencia']).groupby(dataset['Calendar Year/Month']).transform('mean')

#agora vou fazer variáveis com a % de mulheres do Agro líderes por data
dataset['Media_MLider'] = (dataset['MLider']).groupby(dataset['Calendar Year/Month']).transform('mean')

#agora que já temos as médias por data, vamos dropar os valores repetidos, pois nós
#queremos fazer uma estimação de série temporal, não de painel
dataset = dataset.drop_duplicates(subset='Calendar Year/Month', keep="first")

#agora, vou pegar apenas as variáveis relevantes para fazer minha previsão e extrair os dados em excel
dataset=dataset[['Calendar Year/Month','Media_Mulher','Media_MLider','Media_Deficiencia']]
dataset.to_excel('C:/Users/FREITAC6/OneDrive - BASF/Desktop/Dados_previsao.xlsx', sheet_name='Sheet1')