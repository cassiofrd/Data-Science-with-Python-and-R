#vamos criar um dataframe com duas colunas
#a primeira com os valores reais e a segunda com as previs√µes do modelo
import pandas as pd
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#importando a base de dados, j√° selecionando apenas com as colunas que interessam
duncan=pd.read_csv('Duncan.csv',delimiter=';').loc[:,["occupation","income","education","prestige"]]
#vamos visualizar se h· tendÍncias nos dados ou se h· outliers para serem tratados
pd.plotting.scatter_matrix(duncan)

#agora vamos separar as vari·veis de interesse para os modelos
X = duncan.loc[:, ["income", "education"]]
y = duncan.loc[:, "prestige"]

#vamos separar entre base de treino e base de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

#agora vamos estimar nosso modelo da regress√£o linear
import statsmodels.api as sm
model = sm.OLS(y_test, X_test).fit()

#vamos pegar agora outra base de dados que tem valores de renda e educa√ß√£o
#para prevermos os valores da vari√°vel prest√≠gio
predictions=pd.DataFrame(model.predict(X_test))
#vamos colocar nome √† coluna com os dados previstos
predictions.columns=["previs√£o"]
#vamos pegar a coluna com os valores reais
column=y_test
#por fim, vamos adicionar √† coluna de previs√µes a coluna real e comparar 
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
#posiÁ„o 1-1 (linha-coluna) previu verdadeiro, È verdadeiro
#posiÁ„o 2-1 (linha-coluna) previu verdadeiro, È falso (falso positivo)
#posiÁ„o 1-2 (linha-coluna) previu falso, È verdadeiro (falso negativo)
#posiÁ„o 2-2 (linha-coluna) previu falso, È falso
confusion_matrix(y_test, predictions)