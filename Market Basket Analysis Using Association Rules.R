#the result of a market basket analysis is a set of association rules
#that specify patterns of relationships among items
#a ideia � identificar as poss�veis associ��es entre conjuntos, por exemplo:
#(creme de amendoim, geleia) � comummente associado como conjunto (p�o)
#o algor�tmo nos permite fazer associa��es com novos dados com base nos
#dados que temos

#o formato de dados para a utiliza��o desse algor�tmo � uma matriz esparsa, esta basicamente
#� uma matriz com n colunas que representa cada uma um dos �tens que pode estar
#em cada conjunto, por sua vez h� um total de m linhas que representa cada um dos conjuntos
#de nossa base. O valor padr�o das entradas da matriz � 0, enquanto h� o valor 1 no
#cruzamento entre linha x e coluna y quando o item y est� no conjunto x
#para criar a matriz exparsa vamos precisar do pacote abaixo
install.packages("arules")
library(arules)
#a fun��o read.transaction() � usada ao inv�s de read.csv() pois ela transforma um banco
#de dados csv diretamente em uma matriz esparsa
groceries <- read.transactions("groceries.csv", sep = ",")
#para saber como ficaram os dados com essa transforma��o, basta utilizar
#o valor density informa a porcentagem de c�lulas diferentes de zero
summary(groceries)
#uma fun��o legal do pacote � que ele permite inspecionar a matriz, por exemplo, se voc�
#quer ver o conte�do dos cinco primeiros conjuntos (cinco primeiras linhas), basta fazer
inspect(groceries[1:5])
#para ver a frequ�ncia de cada item/coluna (a porcentagem, de 0 a 1, de conjuntos nos quais
#determinado �tem est� presente), basta utilizar o comando abaixo, sendo que, no referido
#exemplo, verificamos do �tem 1 ao 3
itemFrequency(groceries[, 1:3])
#para ver um histograma com os produtos que aparecem a partir de uma determinada frequ�ncia
#em cada conjunto basta utilizar o comando abaixo. veja que selecionamos apenas aqueles que
#aparecem em 10% ou mais conjuntos
itemFrequencyPlot(groceries, support = 0.1)
#para ver os n �tens que aparecem mais basta utilizar o comando abaixo, com n=20
itemFrequencyPlot(groceries, topN = 20)
#podemos com o comando abaixo vizualizar onde h� entradas na matriz, organizando numericamente
#as linhas e colunas
image(groceries[1:5])
#caso queira uma sele��o aleat�ria de cojnuntos, basta utilizar o comando abaixo, no qual 
#selecionamos aleatoriamente 100 conjuntos, com a imagem podemos verificar quais produtos
#s�o mais populares
image(sample(groceries, 100))
#finalmente o c�digo para encontrar as associa��es est� abaixo, antes vamos apenas explicar seus par�metros
#data is a sparse item matrix holding transactional data
#support specifies the minimum required rule support (a porcentagem de conjuntos na qual um
#produto tem que estar para ser considerado na gera��o da nossa regre de associa��o)
#confidence specifies the minimum required fule confidence (� poss�vel que haja casos em que
#a presen�a do produto A implique o produto B e outros em que a presen�a de A implique B, por
#isso o confidence vai estabelecer uma porcentagem em que ocorra cada caso em rela��o ao total
#de modo que se a porcentagem for menor, a regra n�o ser� considerada)
#minlen specifies the minimum required rule items (estabelece o n�mero m�nimo de it�ns que
#deve haver para o estabelecimento de uma regra, ou seja, devemos considerar conjuntos que
#tenham a partir de quantos itens para estabelecer uma regra)
#the function will return a rules object storing all rules that meet the minimum criteria
myrules <-apriori(data=mydata,parameter=list(support=0.005,confidence=0.25,ninlen=2))
#para examinar os resultados, o comando abaixo ir� mostra as regras de associa��o
#no resultado o termo lift indica o quanto mais propenso um consumidor est� para comprar o
#produto em rhs dado que ele adquiriu o conjunto lhs
inspect(myrules)
#� prop�cio mostrar os resultados tendo como base a ordena��o do modelo ordenando pelo lift
#como abaixo, posso mostrar apenas os maiores lift, abaixo exibimos apenas os 5 maiores
inspect(sort(groceryrules, by = "lift")[1:5])
#se eu quiser filtar apenas as regres que tem algum produto espec�fico nos sistemas
#posso fazer como abaixo, em que escolho apenas as regras em que berries aparece
berryrules <- subset(groceryrules, items %in% "berries")
inspect(berryrules)
#para salvar as regras como um arquivo .csv basta executar o comando abaixo
write(groceryrules, file = "groceryrules.csv", sep = ",", quote = TRUE, row.names = FALSE)