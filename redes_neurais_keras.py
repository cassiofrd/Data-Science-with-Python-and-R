#redes neurais artificiais
#deep learning usando o python
#vamos importar os dados de tipo de vinho, branco e tinto
#vamos importar direto do site, muito legal

import pandas as pd
white=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",sep=';')
red=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",sep=';')
from sklearn.model_selection import train_test_split

#vamos criar a variável que vai separar identificar se o vinho é branco ou tinto

red['type']=1
white['type']=0

#agora vamos juntar as duas bases de dados

wines=red.append(white,ignore_index=True)
X=wines.iloc[:,0:11]
import numpy as np
y=np.ravel(wines.type)

#agora vamos separar as bases de dados entre treino e teste

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42)

#agora vamos padronizar os dados

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler().fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

#vamos agura fazer o modelo
#vamos utilizar a matriz de ativação relu, que é a mais comumenten utilizada
#vamos utilizar Sequential() para passar um conjunto de camadas para nossa rede neural
#para determinar as camadas que vamos ter no modelo configuramos os
#parâmetros input_shape,input_dim,input_length ou batch_size
#por meio da função Dense, determinamos cada layer

from keras.models import Sequential
from keras.layers import Dense
model=Sequential()

#vamos determinar nossa primeira camada (input): dimensão 12 

model.add(Dense(12,activation='relu',input_shape=(11,)))

#vamos determinar nossa segunda camada (intermediate layer): dimensão 8 

model.add(Dense(8,activation='relu'))

#vamos determinar nossa terceira camada (output): dimensão 1

model.add(Dense(1,activation='sigmoid'))

#como vemos, há duas decisões que devem ser tomadas, quantas camadas um modelo
#deve ter e o quão densa cada camada deve ser (no nosso caso temos 3 camadas
#cada uma com densidade de, respectivamente 12, 8 e 1)
#é padrão utilizar como dimensão da camada input (primeira) a dimensão do nosso
#dataset (11 variáveis independentes 1 dependente, para não dar overfitting) e como #output (obvio dimensão 1 pois é a nossa variável dependente)
#agora vamos compilar o modelo. Vamos utilizar o otimizador adam (mas há outros)
#como estamos tentando prever um valor binário, vamos utilizar o loss=binar_crossentropy
#mas se estivessemos tentando prever um valor mult-class, deveríamos utilizar
#categorical_crossentropy (fazendo uma analogia, é semelhante ao valor minimizado
#quanto utilizamos regressão, que é o Mean Squared Error (MSE))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

#vamos treinar o modelo com 20 epochs, ou iterações sobre a amostra em X_train e ytrain
#epochs=20 indica que o modelo será treinado passando 20 vezes por toda a base de treino
#batch_size identifica o número de amostras a serem propagadas pela rede (uma só pois
#só estamos utilizando uma base de dados)
#o argumento verbose=1 indica que queremos ver em tela as iterações do modelo

model.fit(X_train,y_train,epochs=20,batch_size=1,verbose=1)
y_pred=model.predict(X_test)

#y_pred vai nos dar a porcentagem de chance de cada vinho ser tinto

y_pred[:5]
y_test[:5]

#agora vamos avaliar o modelo

score=model.evaluate(X_test,y_test,verbose=1)
print(score)
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score

#para a matriz de confusão, vamos precisar arredondar os valore

y_pred=np.rint(y_pred)
confusion_matrix(y_test,y_pred)
precision_score(y_test,y_pred)
recall_score(y_test,y_pred)
f1_score(y_test,y_pred)
cohen_kappa_score(y_test,y_pred)
