#the result of a market basket analysis is a set of association rules
#that specify patterns of relationships among items
#a ideia é identificar as possíveis associções entre conjuntos, por exemplo:
#(creme de amendoim, geleia) é comummente associado como conjunto (pão)
#o algorítmo nos permite fazer associações com novos dados com base nos
#dados que temos

#o formato de dados para a utilização desse algorítmo é uma matriz esparsa, esta basicamente
#é uma matriz com n colunas que representa cada uma um dos ítens que pode estar
#em cada conjunto, por sua vez há um total de m linhas que representa cada um dos conjuntos
#de nossa base. O valor padrão das entradas da matriz é 0, enquanto há o valor 1 no
#cruzamento entre linha x e coluna y quando o item y está no conjunto x
#para criar a matriz exparsa vamos precisar do pacote abaixo
install.packages("arules")
library(arules)
#a função read.transaction() é usada ao invés de read.csv() pois ela transforma um banco
#de dados csv diretamente em uma matriz esparsa
groceries <- read.transactions("groceries.csv", sep = ",")
#para saber como ficaram os dados com essa transformação, basta utilizar
#o valor density informa a porcentagem de células diferentes de zero
summary(groceries)
#uma função legal do pacote é que ele permite inspecionar a matriz, por exemplo, se você
#quer ver o conteúdo dos cinco primeiros conjuntos (cinco primeiras linhas), basta fazer
inspect(groceries[1:5])
#para ver a frequência de cada item/coluna (a porcentagem, de 0 a 1, de conjuntos nos quais
#determinado ítem está presente), basta utilizar o comando abaixo, sendo que, no referido
#exemplo, verificamos do ítem 1 ao 3
itemFrequency(groceries[, 1:3])
#para ver um histograma com os produtos que aparecem a partir de uma determinada frequência
#em cada conjunto basta utilizar o comando abaixo. veja que selecionamos apenas aqueles que
#aparecem em 10% ou mais conjuntos
itemFrequencyPlot(groceries, support = 0.1)
#para ver os n ítens que aparecem mais basta utilizar o comando abaixo, com n=20
itemFrequencyPlot(groceries, topN = 20)
#podemos com o comando abaixo vizualizar onde há entradas na matriz, organizando numericamente
#as linhas e colunas
image(groceries[1:5])
#caso queira uma seleção aleatória de cojnuntos, basta utilizar o comando abaixo, no qual 
#selecionamos aleatoriamente 100 conjuntos, com a imagem podemos verificar quais produtos
#são mais populares
image(sample(groceries, 100))
#finalmente o código para encontrar as associações está abaixo, antes vamos apenas explicar seus parâmetros
#data is a sparse item matrix holding transactional data
#support specifies the minimum required rule support (a porcentagem de conjuntos na qual um
#produto tem que estar para ser considerado na geração da nossa regre de associação)
#confidence specifies the minimum required fule confidence (é possível que haja casos em que
#a presença do produto A implique o produto B e outros em que a presença de A implique B, por
#isso o confidence vai estabelecer uma porcentagem em que ocorra cada caso em relação ao total
#de modo que se a porcentagem for menor, a regra não será considerada)
#minlen specifies the minimum required rule items (estabelece o número mínimo de iténs que
#deve haver para o estabelecimento de uma regra, ou seja, devemos considerar conjuntos que
#tenham a partir de quantos itens para estabelecer uma regra)
#the function will return a rules object storing all rules that meet the minimum criteria
myrules <-apriori(data=mydata,parameter=list(support=0.005,confidence=0.25,ninlen=2))
#para examinar os resultados, o comando abaixo irá mostra as regras de associação
#no resultado o termo lift indica o quanto mais propenso um consumidor está para comprar o
#produto em rhs dado que ele adquiriu o conjunto lhs
inspect(myrules)
#é propício mostrar os resultados tendo como base a ordenação do modelo ordenando pelo lift
#como abaixo, posso mostrar apenas os maiores lift, abaixo exibimos apenas os 5 maiores
inspect(sort(groceryrules, by = "lift")[1:5])
#se eu quiser filtar apenas as regres que tem algum produto específico nos sistemas
#posso fazer como abaixo, em que escolho apenas as regras em que berries aparece
berryrules <- subset(groceryrules, items %in% "berries")
inspect(berryrules)
#para salvar as regras como um arquivo .csv basta executar o comando abaixo
write(groceryrules, file = "groceryrules.csv", sep = ",", quote = TRUE, row.names = FALSE)