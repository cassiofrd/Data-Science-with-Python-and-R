#a clusteriza��o dos dados permite identificar padr�es selelhantes entre diferentes
#por��es de dados, n�o sendo muito utilizada para previs�es
#a ideia geral a agrupar as observa��es que apresentam caracter�scas em comum

#IMPORTANTE: o que diferencia o k-means de outros m�todos � que nele N�O estabelecemos
#em quais grupos est�o cada observa��o, mas inferimos quais s�o os grupos relevantes a
#partir das observa��es. no caso de �rvore de decis�o, por exemplo, n�s definimos os
#grupos e queremos identificar o quanto o pertencimento a um grupo influencia a probabilidade
#de estar em outros grupos
#obs: abaixo temos alguns exemplos de t�cnicas mais sofisticadas de clusteriza��o
#http://cran.r-project.org/web/views/Cluster.html

#a t�cnica tenta classificar cada um das n observa��es em cada um dos k clusteres presentes
#de modo que a semelhan�a seja a m�xima poss�vel entre os membros de um mesmo cluster e a
#m�nima entre os de clusters diferentes

#no nosso exemplo vamos utilizar dados sobre
teens <- read.csv("snsdata.csv")
#os dados incluem 30.000 estudantes, contendo quatro vari�veis sobre caracter�sticas pessoais
#dosmesmos e 36 palavras indicando interesses pessoais dos estudantes
#para utilizar o m�todo de cluster devemos baixar o pacote stats
library(stats)

myclusters<-kmeans(mydata,k)
#mydata � uma matriz ou data frame com os dados a serem clusterizados
#k especifica o n�mero desejado de clusters
#na nossa base de dados, vamos selecionar apenas as vari�veis relevantes
interests <- teens[5:40]

#vamos fazer uma padroniza��o nas vari�veis, pois estas apresentam intervalos muito distintos
#o que pode influenciar o peso que cada uma delas tem ao estimar o modelo
interests_z <- as.data.frame(lapply(interests, scale))

#transformados os dados, fa�amos
teen_clusters <- kmeans(interests_z, 5)

#para saber quantas observa��es h� em cada cluster, utilizamos o comando
teen_clusters$size

#para mostrar quais foram os centroids utilizados para estabelecer estes clusters, utilizamos
teen_clusters$centers
#vamosres positivos indicam que o valor da vari�vel est� acima da m�dia de todos os estudantes
#sendo assim, as vari�veis que apresentam resultados positivos s�o importantes para definir
#o grupo de adolescentes que caracterizam

#agora vamos salvar na nossa base de dados uma vari�veal que informa em qual grupo cada uma
#das observa��es foi classificada
teens$cluster <- teen_clusters$cluster

#com o comando aggregate podemos ver se a vari�vel idade varia por cluster
aggregate(data = teens, age ~ cluster, mean)

#como veremos, a segmenta��o do cluster n�o foi boa para prever idada, mas � boa para propor��o
#de mulheres e n�mero de amigos na rede social
#j� a propor��o de mulheres varia sistematicamente entre os clusters
aggregate(data = teens, female ~ cluster, mean)

#o mesmo vale para o n�mero de amigos, que varia bastante por cluster
aggregate(data = teens, friends ~ cluster, mean)