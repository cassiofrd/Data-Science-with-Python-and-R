#setwd('C:/Users/Cássio/Desktop')
#vamos extrair os dados
#censo2010<-read.fwf(file='Amostra_Pessoas_31.txt',widths=c(2,5,13,8,3,1,2,3,2,1,2,2,1,6,4,1,2,2,2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,7,5,6,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
#agora vamos colocar nomes nas variáveis
names(censo2010)<-c('UF','Codigo_do_Municipio','Area_de_Ponderacao','Controle','Peso_Amostral','Regiao','Codigo_da_Mesorregiao','Codigo_da_Microrregiao','Codigo_da_Regiao_Metropolitana','Situacao_do_Domicilio','Especie_de_Unidade_Visitada','Tipo_de_Especie','Domicilio_condicao_de_ocupacao','Valor_do_aluguel_(em_reais)','Aluguel_em_nº_de_salarios_minimos','Material_predominante_nas_paredes_externas','Nº_de_comodos','Densidade_de_morador/comodo','Comodos_como_dormitorio_numero','Densidade_de_morador/dormitorio','Banheiros_de_uso_exclusivo_numero','Sanitario_ou_buraco_para_dejecao/existencia','Esgotamento_sanitario/tipo','Abastecimento_de_agua/forma','Abastecimento_de_agua_canalizacao','lixo/destino','energia_eletrica_existencia','ecistencia_de_medidor_ou_relogio_de_energia_eletrica','radio_existencia','televisao_existencia','maquina_de_lavar_roupa_existencia','geladeira_existencia','telefone_celular_existencia','telefone_fixo_existencia','microcomputador_existencia','Microcomputador_com_acesso_a_interntet_existencia','Motocicleta_para_uso_particular_existencia','Automovel_para_uso_particular_existencia','Alguma_pessoa_que_morava_com_voce_estava_morando_em_outro_pais_em_31_de_julho_de_2010','Quantas_pessoas_moravam_neste_domicilio_em_31_de_julho_de_2010','A_responsabilidade_pelo_domicilio_e_de:','De_agosto_de_2009_a_julho_de_2010_faleceu_alguma_pessoa_que_morava_com_voce','rendimento_mensal_domiciliar_em_julho_de_2010','Rendimento_domiciliar_salarios_minimos_em_julho_de_2010','Rendimento_domiciliar_per_capita_em_julho_de_2010','Rendimento_domiciliar_per_capita_em_nº_de_salarios_minimos_em_julho_de_2010','Especie_da_Unidade_Domestica','Adequacao_da_moradia','Marca_de_imputacao_na_v0201','Marca_de_imputacao_na_v2011','Marca_de_imputacao_na_v0202','Marca_de_imputacao_na_v0203','Marca_de_imputacao_na_v0204','Marca_de_imputacao_na_v0205','Marca_de_imputacao_na_v0206','Marca_de_imputacao_na_v0207','Marca_de_imputacao_na_v0208','Marca_de_imputacao_na_v0209','Marca_de_imputacao_na_v0210','Marca_de_imputacao_na_v0211','Marca_de_imputacao_na_v0212','Marca_de_imputacao_na_v0213','Marca_de_imputacao_na_v0214','Marca_de_imputacao_na_v0215','Marca_de_imputacao_na_v0216','Marca_de_imputacao_na_v0217','Marca_de_imputacao_na_v0218','Marca_de_imputacao_na_v0219','Marca_de_imputacao_na_v0220','Marca_de_imputacao_na_v0221','Marca_de_imputacao_na_v02022','Marca_de_imputacao_na_v0301','Marca_de_imputacao_na_v0401','Marca_de_imputacao_na_v0402','Marca_de_imputacao_na_v0701','Situacao_do_setor')
#vamos calcular o salário real
censo2010$salario_real<-censo2010$Rendimento_domiciliar_per_capita_em_julho_de_2010
censo2010$salario_real
#vamos criar dummies para pobre, classe média e rico, assim como criar uma variável categórica que cobre as três categorias
censo2010$pobre<-ifelse(censo2010$salario_real<=1000,1,0)
censo2010$classe_media<-ifelse(censo2010$salario_real>1000 & censo2010$salario_real<=5000,1,0)
censo2010$rico<-ifelse(censo2010$salario_real>5000 & censo2010$salario_real<=10000,1,0)
censo2010$super_rico<-ifelse(censo2010$salario_real>10000,1,0)
censo2010$classe[censo2010$salario_real<=1000]<-1
censo2010$classe[censo2010$salario_real>1000 & censo2010$salario_real<=5000]<-2
censo2010$classe[censo2010$salario_real>5000 & censo2010$salario_real<=10000]<-3
censo2010$classe[censo2010$salario_real>10000 & censo2010$salario_real<=20000]<-4
censo2010$classe[censo2010$salario_real>20000]<-5
censo2010$classe
plot(censo2010$classe,censo2010$salario_real, main="Salário por classe",xlab="Classes",ylab="Salário")
#agora vamos calcular os valores de salário médio por grupo
media<-aggregate(censo2010$salario_real, list(censo2010$classe), mean)
media
#vamos fazer uma regressão simples
fit<-lm(salario_real~pobre+super_rico,data=censo2010)
summary(fit)
plot(censo2010$super_rico,)
censo2010$super_rico
#vamos ver
install.packages("XLConnect")
library(XLConnect)
wyn<-summary(lm(salario_real~pobre+super_rico,data=censo2010))$coeff
writeWorksheetToFile(file='test.xlsx',data=wyn,sheet='test')
#modelo logit
logit <- glm(pobre~energia_eletrica_existencia, family=binomial(link="logit"), data=censo2010)
summary(logit)
censo2010$pobre
#regressão quantílica
install.packages("quantreg")
library(quantreg)
help(package="quantreg")
help(rq)
fit1<-rq(salario_real~pobre,tau=.5,data=censo2010)
summary(fit1)
fit2<-rq(salario_real~pobre,tau=c(.05,.25,.5,.75,.95),data=censo2010)
fit2 <- summary(rq(salario_real~pobre,tau=c(.05, .25, .5, .75, .95),data=censo2010))
fit2