#árvore de decisão
#primeiro vamos importar os dados
library(readxl)
brasileiro <- read_excel("C:/Users/Cássio/Desktop/Aprendendo R de verdade/brasileiro.xlsx")
View(brasileiro)
#vamos importar o pacote que permite fazer a árevore de decisão
install.packages("rpart")
library(rpart)
#ao selecionar as variáveis dependente e independentes que serão utilizadas na árvore de decisão
#devemos nos lembrar que todas devem ser categóricas dummies
#ATENÇÃO: eu posso utilizar variáveis numéricas como independentes, o problema é que eu não vou
#conseguir controlar qual vai ser o intervalo a partir do qual o método irá agrupar estas
#variáveis. é mais inteligente transformar a variável numérica em uma variável categórica que
#explicifica em qual intervalo numérico entra cada uma das observações que compõem nossa base
#de dados
mytree<-rpart(brasileiro~faixa_etária+sexo+classe,data=brasileiro,method="class",minsplit=2,minbucket=1)
mytree
install.packages("rattle")
library(rattle)
install.packages("rpart.plot")
library(rpart.plot)
install.packages("RColorBrewer")
library(RColorBrewer)
#são quatro resultados presentes em cada nó da árvore de decisão. o primeiro, central e na parte
#de cima informa o valor da variável dependente que está associado à primeira porcentagem à
#esquerda. a segunda porcentagem, à direita, nos informa a porcentagem de observações associadas
#ao outro valor da variável categórica. por fim, a porcentagem abaixo informa a porcentagem de
#observações que estes dois valores da variável dependente contemplam
fancyRpartPlot(mytree)