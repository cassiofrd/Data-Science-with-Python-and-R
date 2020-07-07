#IMPORTANTE: A REDE NEURAL SÓ FUNCIONOU DEPOIS QUE EU NORMALIZEI TODAS AS VARIÁVEIS, INCLUSIVE
#A DEPENDENTE. ME PARECE QUE SE A VARIÁVEL DEPENDENTE TIVER UM INTERVALO DE VALORES MUITO MAIOR
#QUE AS INDEPENDENTES, O MODELO NÃO IRÁ FUNCIONAR E AO VER OS RESULTADOS, TODOS OS VALORES
#PREVISTOS COM BASE NO MODELO SERÃO IGUAIS
#vamos utilizar rede neural para fazer umas previsões
library(readxl)
redes_neurais2 <- read_excel("C:/Users/Cássio/Desktop/Aprendendo R de verdade/redes_neurais2.xlsx")
View(redes_neurais2)
install.packages("BBmisc")
library("BBmisc")
redes_neurais2$idade<-normalize(redes_neurais2$idade,method="standardize",range=c(0, 1))
redes_neurais2$numero_de_filhos<-normalize(redes_neurais2$numero_de_filhos,method="standardize",range=c(0, 1))
redes_neurais2$renda<-normalize(redes_neurais2$renda,method="standardize",range=c(0, 1))
#vamos baixar os pacotes que precisamos
install.packages("neuralnet")
library("neuralnet")
model=neuralnet(formula=renda~idade+numero_de_filhos,data=redes_neurais2)
print(model)
plot(model)
#agora vamos ver a capacidade preditiva da minha rede neural
renda<-redes_neurais2$renda
idade<-redes_neurais2$idade
numero_de_filhos<-redes_neurais2$numero_de_filhos
final_output=cbind(renda,idade,numero_de_filhos,as.data.frame(model$net.result))
colnames(final_output)=c("Renda","Idade","Numero de filhos","Neural Net Resultados")
print(final_output)
#vamos aumetar o número de camadas e ver como o resultado modifica
model=neuralnet(formula=renda~idade+numero_de_filhos,data=redes_neurais2,hidden=10,threshold=0.01)
print(model)
plot(model)
final_output=cbind(renda,idade,numero_de_filhos,as.data.frame(model$net.result))
colnames(final_output)=c("Renda","Idade","Numero de filhos","Neural Net Resultados")
print(final_output)


#vamos fazer uns testes
library(readxl)
redes_neurais2 <- read_excel("C:/Users/Cássio/Desktop/Aprendendo R de verdade/redes_neurais2.xlsx")
redes_neurais3 <- read_excel("C:/Users/Cássio/Desktop/Aprendendo R de verdade/redes_neurais3.xlsx")
View(redes_neurais2)
install.packages("BBmisc")
library("BBmisc")
redes_neurais2$idade<-normalize(redes_neurais2$idade,method="standardize",range=c(0, 1))
redes_neurais2$numero_de_filhos<-normalize(redes_neurais2$numero_de_filhos,method="standardize",range=c(0, 1))
redes_neurais2$renda<-normalize(redes_neurais2$renda,method="standardize",range=c(0, 1))
redes_neurais3$idade<-normalize(redes_neurais3$idade,method="standardize",range=c(0, 1))
redes_neurais3$numero_de_filhos<-normalize(redes_neurais3$numero_de_filhos,method="standardize",range=c(0, 1))
redes_neurais3$renda<-normalize(redes_neurais3$renda,method="standardize",range=c(0, 1))
#vamos baixar os pacotes que precisamos
install.packages("neuralnet")
library("neuralnet")
model=neuralnet(formula=renda~idade+numero_de_filhos,data=redes_neurais2)
print(model)
plot(model)
#agora vamos ver a capacidade preditiva da minha rede neural
renda<-redes_neurais2$renda
idade<-redes_neurais2$idade
numero_de_filhos<-redes_neurais2$numero_de_filhos
renda3<-redes_neurais3$renda
idade3<-redes_neurais3$idade
numero_de_filhos3<-redes_neurais3$numero_de_filhos
#IMPORTANTÍSSIMO: e´o comando cbind que me permite fazer as previsões
#eu coloco os dados que vou utilizar como insumo no modelo e da última posição coloco as.data.frame(model$net.result)
#sendo model o modelo que eu utilizei, como feito nas linhas acima, podendo ser modelo de qualquer
#tipo: mqo, logit, redes neurais, etc
final_output=cbind(renda3,idade3,numero_de_filhos3,hidden=10,threshold=0.01,as.data.frame(model$net.result))
colnames(final_output)=c("Renda","Idade","Numero de filhos","Neural Net Resultados")
print(final_output)
View(redes_neurais3)