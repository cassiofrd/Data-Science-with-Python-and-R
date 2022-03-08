# vamos fazer uma rede neural com o R
# primeiro vamos determinar o diretório de trabalho

setwd("C:/Users/FREITAC6/OneDrive - BASF/Desktop/neural network R")
getwd()

# importando os pacotes

library(readxl)
library(openxlsx)
library(keras)
####### ATENÇÃO: SE VOCÊ AINDA NÃO INSTALOU O TENSORFLOW PELA PRIMEIRA VEZ, TIRE O # DA LINHA 14 E EXECUTE
# CASO CONTRÁRIO NÃO PRECISA RODAR NOVEMENTE. O TENSORFLOW NÃO É INSTALADO CORRETAMENTE PELO COMANDO install.packages()
#tensorflow::install_tensorflow()
library(mlbench)
library(dplyr)
library(magrittr)
library(neuralnet)

# agora vamos importar os dados que iremos utilizar

data <- read.xlsx("C:/Users/FREITAC6/OneDrive - BASF/Desktop/neural network R/Base Teste.xlsx", detectDates = TRUE)
str(data)

# vamos normalizar as variáveis que não variam entre 0 e 1
# vamos criar a função de normalização e aplicar às variáveis que não estão normalizadas

normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}

# antes de aplicar a função vamos salvar os valores de máximo e mínimo da nossa variável dependente para reverter
# esse processo de normalização após a previsão

maxdep <- max(data["BASF.Tenure"])
mindep <- min(data["BASF.Tenure"])
data$Strata <- normalize(data$Strata)
data$Male <- normalize(data$Male)
data$Age <- normalize(data$Age)
data$Ordem.age.range <- normalize(data$Ordem.age.range)
data$Lider <- normalize(data$Lider)
data$Ordem.Tenure <- normalize(data$Ordem.Tenure)
data$BASF.Tenure <- normalize(data$BASF.Tenure)

# antes de começar, devemos garantir que todas as variáveis da base são numéricas
# com o comando abaixo vamos converter variáveis categóricas em numéricas
# como se sabe, uma rede neural só aceita valores numéricos

data %<>% mutate_if(is.factor, as.numeric)

# agora vamos separar a nossa base de dados entre base de treino e base de teste

vardep <- data["BASF.Tenure"] #selecionar qual é a variável dependente
varindep <- data[,c(1,2,3,4,5,6)] #selecionar quais serão nossas variáveis independentes
splitdep1<- sample(c(rep(0, 0.7 * nrow(vardep)), rep(1, 0.3 * nrow(vardep)))) #vamos separar a vardep entre treino e teste
splitindep1<- sample(c(rep(0, 0.7 * nrow(varindep)), rep(1, 0.3 * nrow(varindep)))) #vamos separar a base independente entre treino e teste

training <- varindep[splitdep1 == 0, ]
test <- varindep[splitdep1== 1, ]
trainingtarget <- vardep[splitindep1 == 0, ]
testtarget <- vardep[splitindep1== 1, ]
trainingtarget <- as.numeric(trainingtarget)
testtarget <- as.numeric(testtarget)

# em redes neurais, precisamos normalizar as variáveis numéricas para melhorar a
# capacidade preditiva do modelo

m <- colMeans(training)
s <- apply(training, 2, sd)
training <- scale(training, center = m, scale = s)
test <- scale(test, center = m, scale = s)

# agora vamos criar o nosso modelo
# como visto abaixo temos 6 neurôneos (um para cada variável independente)
# na camada input, uma única "hiden layer" com 3 neurôneos (utilizando a fórmula da raiz quadrada
# da multiplicação entre o número de nerônios do input e no outpub: raiz de 7, que eu arredondei
# para 3) e na camada output apenas 1 neurôneo
tensorflow::tf_config()
model <- keras_model_sequential()
model %>%
  layer_dense(units = 6, activation = 'relu', input_shape = c(6)) %>%
  layer_dense(units = 3, activation = 'relu')  %>%
  layer_dense(units = 1)

# agora vamos compilar o nosso modelo

model %>% compile(loss = 'mse',
                  optimizer = 'rmsprop', 
                  metrics = 'mae')

# agora vamos treinar o nosso modelo

mymodel <- model %>%          
  fit(training,trainingtarget,
      epochs = 100,
      batch_size = 32,
      validation_split = 0.2)


# vamos agora fazer algumas mudanças no modelo e ver como ficou sua capacidade preditiva

model <- keras_model_sequential()
model %>%
  layer_dense(units = 6, activation = 'relu', input_shape = c(6)) %>%
  layer_dropout(rate=0.5)  %>% # essas camadas drop out eliminam uma porcentagem da amostra entre uma camada e outra, apesar de reduzir o tamanho da base, diminui a chance de overfitting
  layer_dense(units = 3, activation = 'relu')  %>%
  layer_dropout(rate=0.5)  %>%
  layer_dense(units = 1)

# agora vamos compilar o nosso modelo

model %>% compile(loss = 'mse',
                  optimizer = 'rmsprop', 
                  metrics = 'mae') # lembrando que accuracia só faz sentido se prevemos dummies, variáveis contínuas numca são previstas na exatidão, até na casa decimal
                                   # o mae nada mais é que o erro absoluto médio
                                   # loss se refere à base de treino, val_loss é a mesma estatítica para a base de teste, quando o valor estabiliza já podemos parar de treinar o modelo
                                   # mae se refere à base de treino, val_mae é a mesma estatítica para a base de teste, quando o valor estabiliza já podemos parar de treinar o modelo
# agora vamos treinar o nosso modelo

mymodel <- model %>%          
  fit(training,trainingtarget,
      epochs = 200,           # vai passar por toda a base do modelo um total de 200 vezes
      batch_size = 32,        # batck_size é o número de observações que o modelo usa para promover o treino da base, deixa esse valor, para valores maiores demora muito para convergir
      validation_split = 0.2) # validation_split é a porcentagem da base (nesse caso, 20%) que é utilizada para teste, nada mais é que a parcela que aparece no gráfico acima como val_

# vamos avaliar o nosso modelo, a primeira linha nos dá os valores de loss e mae para a nossa base teste

model %>% evaluate(test, testtarget)

# a próxima linha obtém os valores previstos

pred <- model %>% predict(test)

# a última linha nos dá o erro quadrático médio, com base nos valores observados e valores previstos

mean((testtarget-pred)^2) 

# agora, para ter os valores previstos corretamente, vamos reverter o processo de normalização

previsao <- pred*(maxdep-mindep)+mindep
previsao
