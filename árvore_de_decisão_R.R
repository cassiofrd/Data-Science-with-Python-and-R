#�rvore de decis�o
#primeiro vamos importar os dados
library(readxl)
brasileiro <- read_excel("C:/Users/C�ssio/Desktop/Aprendendo R de verdade/brasileiro.xlsx")
View(brasileiro)
#vamos importar o pacote que permite fazer a �revore de decis�o
install.packages("rpart")
library(rpart)
#ao selecionar as vari�veis dependente e independentes que ser�o utilizadas na �rvore de decis�o
#devemos nos lembrar que todas devem ser categ�ricas dummies
#ATEN��O: eu posso utilizar vari�veis num�ricas como independentes, o problema � que eu n�o vou
#conseguir controlar qual vai ser o intervalo a partir do qual o m�todo ir� agrupar estas
#vari�veis. � mais inteligente transformar a vari�vel num�rica em uma vari�vel categ�rica que
#explicifica em qual intervalo num�rico entra cada uma das observa��es que comp�em nossa base
#de dados
mytree<-rpart(brasileiro~faixa_et�ria+sexo+classe,data=brasileiro,method="class",minsplit=2,minbucket=1)
mytree
install.packages("rattle")
library(rattle)
install.packages("rpart.plot")
library(rpart.plot)
install.packages("RColorBrewer")
library(RColorBrewer)
#s�o quatro resultados presentes em cada n� da �rvore de decis�o. o primeiro, central e na parte
#de cima informa o valor da vari�vel dependente que est� associado � primeira porcentagem �
#esquerda. a segunda porcentagem, � direita, nos informa a porcentagem de observa��es associadas
#ao outro valor da vari�vel categ�rica. por fim, a porcentagem abaixo informa a porcentagem de
#observa��es que estes dois valores da vari�vel dependente contemplam
fancyRpartPlot(mytree)