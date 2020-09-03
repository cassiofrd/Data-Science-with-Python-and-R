#a clusterização dos dados permite identificar padrões selelhantes entre diferentes
#porções de dados, não sendo muito utilizada para previsões
#a ideia geral a agrupar as observações que apresentam caracteríscas em comum

#IMPORTANTE: o que diferencia o k-means de outros métodos é que nele NÃO estabelecemos
#em quais grupos estão cada observação, mas inferimos quais são os grupos relevantes a
#partir das observações. no caso de árvore de decisão, por exemplo, nós definimos os
#grupos e queremos identificar o quanto o pertencimento a um grupo influencia a probabilidade
#de estar em outros grupos
#obs: abaixo temos alguns exemplos de técnicas mais sofisticadas de clusterização
#http://cran.r-project.org/web/views/Cluster.html

#a técnica tenta classificar cada um das n observações em cada um dos k clusteres presentes
#de modo que a semelhança seja a máxima possível entre os membros de um mesmo cluster e a
#mínima entre os de clusters diferentes

#no nosso exemplo vamos utilizar dados sobre
teens <- read.csv("snsdata.csv")
#os dados incluem 30.000 estudantes, contendo quatro variáveis sobre características pessoais
#dosmesmos e 36 palavras indicando interesses pessoais dos estudantes
#para utilizar o método de cluster devemos baixar o pacote stats
library(stats)

myclusters<-kmeans(mydata,k)
#mydata é uma matriz ou data frame com os dados a serem clusterizados
#k especifica o número desejado de clusters
#na nossa base de dados, vamos selecionar apenas as variáveis relevantes
interests <- teens[5:40]

#vamos fazer uma padronização nas variáveis, pois estas apresentam intervalos muito distintos
#o que pode influenciar o peso que cada uma delas tem ao estimar o modelo
interests_z <- as.data.frame(lapply(interests, scale))

#transformados os dados, façamos
teen_clusters <- kmeans(interests_z, 5)

#para saber quantas observações há em cada cluster, utilizamos o comando
teen_clusters$size

#para mostrar quais foram os centroids utilizados para estabelecer estes clusters, utilizamos
teen_clusters$centers
#vamosres positivos indicam que o valor da variável está acima da média de todos os estudantes
#sendo assim, as variáveis que apresentam resultados positivos são importantes para definir
#o grupo de adolescentes que caracterizam

#agora vamos salvar na nossa base de dados uma variáveal que informa em qual grupo cada uma
#das observações foi classificada
teens$cluster <- teen_clusters$cluster

#com o comando aggregate podemos ver se a variável idade varia por cluster
aggregate(data = teens, age ~ cluster, mean)

#como veremos, a segmentação do cluster não foi boa para prever idada, mas é boa para proporção
#de mulheres e número de amigos na rede social
#já a proporção de mulheres varia sistematicamente entre os clusters
aggregate(data = teens, female ~ cluster, mean)

#o mesmo vale para o número de amigos, que varia bastante por cluster
aggregate(data = teens, friends ~ cluster, mean)