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