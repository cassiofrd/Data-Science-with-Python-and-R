#vamos criar um dataframe com duas colunas
#a primeira com os valores reais e a segunda com as previsões do modelo
import pandas as pd
import numpy as np

#importando a base de dados, já selecionando apenas com as colunas que interessam
duncan=pd.read_csv('Duncan.csv',delimiter=';').loc[:,["occupation","income","education","prestige"]]
X = duncan.loc[:, ["income", "education"]]
y = duncan.loc[:, "prestige"]

#agora vamos estimar nosso modelo da regressão linear
import statsmodels.api as sm
model = sm.OLS(y, X).fit()
duncan2=pd.read_csv('Duncan2.csv',delimiter=';').loc[:,["income","education"]]

#vamos pegar agora outra base de dados que tem valores de renda e educação
#para prevermos os valores da variável prestígio
predictions=pd.DataFrame(model.predict(duncan2))
#vamos colocar nome à coluna com os dados previstos
predictions.columns=["previsão"]
#vamos pegar a coluna com os valores reais
column=duncan.loc[:,["income"]]
#por fim, vamos adicionar à coluna de previsões a coluna real e comparar 
predictions.insert(0,"real",column)
# Print out the statistics
predictions

#vamos fazer o mesmo com logit
duncan=pd.read_csv('Duncan.csv',delimiter=';').loc[:,["occupation","income","education","rico"]]
duncan2=pd.read_csv('Duncan2.csv',delimiter=';').loc[:,["income","education"]]
X = duncan.loc[:, ["income", "education"]]
y = duncan.loc[:, "rico"]
y=y.replace("Sim",1)
y=y.replace("Nao",0)
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X,y)
predictions=pd.DataFrame(logmodel.predict(duncan2))
predictions.columns=["previsão"]
column=duncan.loc[:,["rico"]]
column=column.replace("Sim",1)
column=column.replace("Nao",0)
predictions.insert(0,"real",column)
predictions