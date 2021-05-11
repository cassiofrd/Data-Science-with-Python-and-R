import numpy as np
import pandas as pd
import statsmodels.formula.api as sm

#para importar .csv devemos utilizar o padrão abaixo
#o delimiter explica qual deve ser o símbolo entendido como separador de linhas
#já o encoding latin1 é para o python conseguir ler os caracteres especiais

dataset=pd.DataFrame(pd.read_csv('Base_de_teste.csv',delimiter=';',encoding='latin1'))

#agora vamos fazer uma regressão linear

result = sm.ols(formula="Renda ~ Filhos + Idade", data=dataset).fit()
print(result.summary())

#agora vamos gerar algumas dummies para incorporar as demais variáveis aos modelos

dataset=pd.get_dummies(dataset, columns=['Estado_civil'])
dataset=pd.get_dummies(dataset, columns=['Cidade'])
dataset=pd.get_dummies(dataset, columns=['Curso_superior'])

#agora vamos regredir o modelo novamente considerando estas novas variáveis

result = sm.ols(formula="Renda ~ Filhos + Idade + Estado_civil_Solteiro + Cidade_Divinópolis + Curso_superior_Sim", data=dataset).fit()
print(result.summary())

#agora vamos criar uma variável diferente

dataset['Poucos_Filhos']=dataset['Filhos']
dataset.loc[dataset.Poucos_Filhos <3, 'Poucos_Filhos'] = 1
dataset.loc[dataset.Poucos_Filhos >= 3, 'Poucos_Filhos'] = 0
dataset['Três_Filhos']=dataset['Filhos']
dataset.loc[dataset.Três_Filhos ==3, 'Três_Filhos'] = 1
dataset.loc[dataset.Três_Filhos !=3, 'Três_Filhos'] = 0
dataset['Muitos_Filhos']=dataset['Filhos']
dataset.loc[dataset.Muitos_Filhos <=3, 'Muitos_Filhos'] = 0
dataset.loc[dataset.Muitos_Filhos > 3, 'Muitos_Filhos'] = 1

#agora a última regressão, com as demais dummies que eu fiz

result = sm.ols(formula="Renda ~ Filhos + Idade + Estado_civil_Solteiro + Cidade_Divinópolis + Curso_superior_Sim + Poucos_Filhos + Muitos_Filhos", data=dataset).fit()
print(result.summary())
