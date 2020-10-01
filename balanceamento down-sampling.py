#vamos balancear uma amostra, o que é importante se formos utilizar logit para
#prever a categoria e a categoria que queremos prever é uma minoria da amostra
import pandas as pd
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#importando a base de dados, jÃ¡ selecionando apenas com as colunas que interessam
duncan=pd.read_csv('Duncan3.csv',delimiter=';').loc[:,["Inteligencia","renda","idade"]]
#vamos visualizar se há tendências nos dados ou se há outliers para serem tratados
pd.plotting.scatter_matrix(duncan)

#vamos separar as bases de treino e teste, sendo que vamos balancear apenas a de treino
duncan, duncan_test = train_test_split(duncan, test_size = 0.2, random_state=0)

#como a base é muito desbalanceada, vamos dar uma balanceada, já que a variável
#que queremos prever tem o resultado verdadeiro (1) como uma pequena minoria do total
from sklearn.utils import resample
#vamos separar os valores da nossa variável dependente que sejam maioria e minoria
#para fazer um downsambple, ou seja, vamos reduzir as observações 0 para ver se
#havendo uma maior igualdade entre 0 e 1 haverá uma melhor capacidade preditiva
#do modelo
df_majority=duncan[duncan.Inteligencia==0]
df_minority=duncan[duncan.Inteligencia==1]
 
#Vamos reduzir o número de observações 0 iguais a 0
#vamos reduzir para 60 observações
df_majority_downsampled = resample(df_majority, 
                                 replace=False,    # sample without replacement
                                 n_samples=30,     # to match minority class
                                 random_state=123) # reproducible results
 
# Combine minority class with downsampled majority class
df_downsampled=pd.concat([df_majority_downsampled, df_minority])
 
# Display new class counts
df_downsampled.Inteligencia.value_counts()

#agora vamos separar as variáveis de interesse para os modelos
y = df_downsampled.Inteligencia
X = df_downsampled.drop('Inteligencia', axis=1)
X_test = duncan_test.loc[:, ["renda", "idade"]]
y_test = duncan_test.loc[:, "Inteligencia"]

#vamos fazer o mesmo com logit
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X,y)
predictions=pd.DataFrame(logmodel.predict(X_test))
#podemos também prever a probabilidade de a variável dependente ser o valor 1
predictions_proba=pd.DataFrame(logmodel.predict_proba(X_test))

#vamos aplicar a confusion matrix no logit
#posição 1-1 (linha-coluna) previu verdadeiro, é verdadeiro
#posição 2-1 (linha-coluna) previu verdadeiro, é falso (falso positivo)
#posição 1-2 (linha-coluna) previu falso, é verdadeiro (falso negativo)
#posição 2-2 (linha-coluna) previu falso, é falso
confusion_matrix(y_test, predictions)