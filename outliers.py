#vamos criar um dataframe com duas colunas
#a primeira com os valores reais e a segunda com as previsÃµes do modelo
import pandas as pd
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#importando a base de dados, jÃ¡ selecionando apenas com as colunas que interessam
df=pd.read_csv('outlier.csv',delimiter=';').loc[:,["Inteligencia","renda","idade"]]
#vamos visualizar se há tendências nos dados ou se há outliers para serem tratados
pd.plotting.scatter_matrix(df)

#como vemos, no caso de outliers, estes gráficos de distribuição de frequência
#ficam muito concentrados, o que já é um indicativo de outlier, para termos certeza,
#vamos fazer alguns box-plots
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
sns.boxplot(data=df)
#claramente temos três observações em renda que são problemáticos, muito superiores
#à média, vamos ter que deletar ou tratar estas observações
#vamos ver abaixo o que ocorre se deletarmos
df.drop(df.loc[df['renda']>600000].index, inplace=True)
sns.boxplot(data=df)
#ainda temos uns outliers para renda, vamos deletar só os valores zero, pois
#possivelmente não são trabalhadores, são crianças, e não nos interessamos por
#elas
df.drop(df.loc[df['renda']==0].index, inplace=True)
sns.boxplot(data=df)
sns.boxplot(data=df['renda'])
sns.boxplot(data=df['Inteligencia'])
sns.boxplot(data=df['idade'])

#poderíamos também substituir os outliers pela média das variáveis
df=pd.read_csv('outlier.csv',delimiter=';').loc[:,["Inteligencia","renda","idade"]]
df["renda"]=np.where(df["renda"]>600000,df.loc[df['renda']<600000,'renda'].median(),df['renda'])
pd.plotting.scatter_matrix(df)
#para verificar se deletou, vamos sapecar o boxplot
sns.boxplot(data=df['renda'])