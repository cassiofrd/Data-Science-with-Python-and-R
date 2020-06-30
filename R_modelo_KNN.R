#eu baixei estes dados no link: https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/
#o dado que eu quero é o wdbc.data
#vamos modificar o diretório
setwd("C:/Users/Cássio/Desktop")
#vamos importar os dados
wbcd <- read.table("wdbc.data",sep=",")
#vamos eliminar a coluna id porque ela é inútil par nossos propósitos
wbcd <- wbcd[-1]
#vamos modificar os nomes
install.packages("dplyr")
library("dplyr")
wbcd <- rename(wbcd,diagnosis=V2)
wbcd$diagnosis <- factor(wbcd$diagnosis, levels = c("B", "M"), labels = c("Benign", "Malignant"))
wbcd <- rename(wbcd,radius_mean=V3)
wbcd <- rename(wbcd,area_mean=V6)
wbcd <- rename(wbcd,smoothness_mean=V7)
#vamos ver a proporção de respostas de cada tipo
round(prop.table(table(wbcd$diagnosis)) * 100, digits = 1)
summary(wbcd[c("radius_mean", "area_mean", "smoothness_mean")])
#vamos normalizar as variáveis numéricas, o que melhora a capacidade preditiva do modelo
#para isso vamos criar a variável function(x), que vai me permitir normalizar a variável x
normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}
#a função lapply permite que a função utilizada, no caso "nomalize", seja aplicada a todas as
#variáveis da lista
#como visto abaixo, eu criei uma nova base de dados em que normalizaei todas as variáveis 
#numéricas presentes na base de dados, com exceção da primeira coluna, que é uma variável
#categórica
wbcd_n <- as.data.frame(lapply(wbcd[2:31], normalize))
#agora vamos criar as bases de teste e treino, a de treino é a base que eu vou utilizar para
#alimentar o modelo, a base teste é necessária para observar se o modelo consegue prever os
#resultados da nossa variávesl de interesse
wbcd_train <- wbcd_n[1:469, ] #para a base treino vamos utilizar as linhas 1 a 169
wbcd_test <- wbcd_n[470:569, ] #para a base teste, as linhas são de 470 a 569
#para aplicar a técnica knn, teremos que acrescentar a variável dependente, que havíamos retirado
wbcd_train_labels <- wbcd[1:469, 1]
wbcd_test_labels <- wbcd[470:569, 1]
#para aplicar o método knn, temos que importar o pacote class
install.packages("class")
library("class")
#agora vamos utilizar a função knn, tentando inicialmente um k=21
wbcd_test_pred <- knn(train = wbcd_train, test = wbcd_test,cl = wbcd_train_labels, k=21)
#agora, por último, vamos avaliar a performace do modelo
install.packages("gmodels")
library("gmodels")
#no comando abaixo vamos havaliar o desempenho do moelo, tirando a estatística qui-quadrado, que não nos é útil
CrossTable(x = wbcd_test_labels, y = wbcd_test_pred, prop.chisq=FALSE)
#o modelo apresentou uma capacidade preditiva muito boa
#podemos testar outros modelos em que podemos modificar o k
#também podemos nosrmalizar as variáveis independentes utilizadas ao invés de padronizar, mas é
#necessário faze-lo para que os outliers não influenciem tanto o resultado
#vamos mudar os valores de k para testar
#k=5
wbcd_test_pred <- knn(train = wbcd_train, test = wbcd_test,cl = wbcd_train_labels, k=5)
CrossTable(x = wbcd_test_labels, y = wbcd_test_pred, prop.chisq=FALSE)
#k=10
wbcd_test_pred <- knn(train = wbcd_train, test = wbcd_test,cl = wbcd_train_labels, k=10)
CrossTable(x = wbcd_test_labels, y = wbcd_test_pred, prop.chisq=FALSE)
#k=15
wbcd_test_pred <- knn(train = wbcd_train, test = wbcd_test,cl = wbcd_train_labels, k=15)
CrossTable(x = wbcd_test_labels, y = wbcd_test_pred, prop.chisq=FALSE)
#k=20
wbcd_test_pred <- knn(train = wbcd_train, test = wbcd_test,cl = wbcd_train_labels, k=20)
CrossTable(x = wbcd_test_labels, y = wbcd_test_pred, prop.chisq=FALSE)
#k=25
wbcd_test_pred <- knn(train = wbcd_train, test = wbcd_test,cl = wbcd_train_labels, k=25)
CrossTable(x = wbcd_test_labels, y = wbcd_test_pred, prop.chisq=FALSE)
#muito provavelmente o modelo