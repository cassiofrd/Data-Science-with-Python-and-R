setwd("C:/Users/Cássio/Desktop")
#agora vamos colocar nomes nas variáveis
base<-read.csv("C:/Users/Cássio/Desktop/Base.csv",sep=";",fileEncoding="latin1")
#vamos pegar algumas estimações
base$Trabalhando<-ifelse(base$Empregado=="Sim",1,0)
base$Casado<-ifelse(base$Casado=="Sim",1,0)
base$Homem<-ifelse(base$Homem=="Sim",1,0)

#vamos normalizar os dados de idade, para que fique no intervalo entre 0 e 1 como as outras
normalize <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}
base$Idade<-normalize(base$Idade)
#vamos fazer uma regressão simples
modelo<-lm(Renda~Trabalhando+Casado+Homem+Idade,data=base)
summary(modelo)

#vamos testar o modelo
base2<-read.csv("C:/Users/Cássio/Desktop/Base2.csv",sep=";",fileEncoding="latin1")
base2$Trabalhando<-ifelse(base$Empregado=="Sim",1,0)
base2$Casado<-ifelse(base$Casado=="Sim",1,0)
base2$Homem<-ifelse(base$Homem=="Sim",1,0)
base2$previsao<-predict(modelo,newdata=base2[,-1])
real<-base2$Renda
preditivo<-base2$previsao
comparacao<-data.frame(real)
comparacao$preditivo<-preditivo
comparacao

#a capacidade preditiva foi péssima, vamos ver um polinômio
base2<-read.csv("C:/Users/Cássio/Desktop/Base2.csv",sep=";",fileEncoding="latin1")
base2$Idade<-normalize(base2$Idade)
modelo<-lm(Renda~Idade+Idade^2+Idade^3+Idade^4,data=base)
previsao<-predict(modelo,newdata=base2[,-1])
real<-base2$Renda
comparacao<-data.frame(real)
comparacao$previsao<-previsao
comparacao

#vamos ver
base<-read.csv("Base.csv",sep=";",fileEncoding="latin1")
#modelo logit
base$Trabalhando<-ifelse(base$Empregado=="Sim",1,0)
base$Casado<-ifelse(base$Casado=="Sim",1,0)
base$Homem<-ifelse(base$Homem=="Sim",1,0)
normalize <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}
#vamos agora trnsformar algumas variáveis para que fiquem todas no mesmo intervalo
base$Idade2<-normalize(base$Idade)
base$Renda2<-normalize(base$Renda)
base$Filhos2<-normalize(base$Filhos)
logit <- glm(Casado~Idade2, family=binomial(link="logit"), data=base)
summary(logit)

#regressão quantílica
install.packages("quantreg")
library(quantreg)
help(package="quantreg")
help(rq)
fit1<-summary(rq(Renda~Filhos2,tau=.5,data=base))
fit2<-summary(rq(Renda~Filhos2,tau=c(.05, .25, .5, .75, .95),data=base))