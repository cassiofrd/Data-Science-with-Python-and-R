#vamos criar um dataframe com duas colunas
#a primeira com os valores reais e a segunda com as previsões do modelo
import pandas as pd
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#importando a base de dados, já selecionando apenas com as colunas que interessam
duncan=pd.read_csv('Duncan.csv',delimiter=';').loc[:,["occupation","income","education","prestige"]]
#vamos visualizar se h� tend�ncias nos dados ou se h� outliers para serem tratados
pd.plotting.scatter_matrix(duncan)

#agora vamos separar as vari�veis de interesse para os modelos
X = duncan.loc[:, ["income", "education"]]
y = duncan.loc[:, "prestige"]

#vamos separar entre base de treino e base de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

#agora vamos estimar nosso modelo da regressão linear
import statsmodels.api as sm
model = sm.OLS(y_test, X_test).fit()

#vamos pegar agora outra base de dados que tem valores de renda e educação
#para prevermos os valores da variável prestígio
predictions=pd.DataFrame(model.predict(X_test))
#vamos colocar nome à coluna com os dados previstos
predictions.columns=["previsão"]
#vamos pegar a coluna com os valores reais
column=y_test
#por fim, vamos adicionar à coluna de previsões a coluna real e comparar 
predictions.insert(0,"real",column)
# Print out the statistics
predictions

#vamos fazer o mesmo com logit
duncan=pd.read_csv('Duncan.csv',delimiter=';').loc[:,["occupation","income","education","rico"]]
X = duncan.loc[:, ["income", "education"]]
y = duncan.loc[:, "rico"]
y=y.replace("Sim",1)
y=y.replace("Nao",0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions=pd.DataFrame(logmodel.predict(X_test))

#vamos aplicar a confusion matrix no logit
#posi��o 1-1 (linha-coluna) previu verdadeiro, � verdadeiro
#posi��o 2-1 (linha-coluna) previu verdadeiro, � falso (falso positivo)
#posi��o 1-2 (linha-coluna) previu falso, � verdadeiro (falso negativo)
#posi��o 2-2 (linha-coluna) previu falso, � falso
confusion_matrix(y_test, predictions)