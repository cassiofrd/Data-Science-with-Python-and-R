# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:09:56 2020

@author: Cassio
"""

#BOOTSTRAP
#vamos conseguir um intervalo de confiança para o valor do nosso parâmetro
import pandas as pd
import numpy as np
#vamos selecionar apenas as colunas que importam
duncan=pd.read_csv('Duncan.csv',delimiter=';').loc[:,["occupation","income","education","prestige"]]
#vamos plotar os dados
import matplotlib.pyplot as plt
plt.scatter(x=duncan["education"], y=duncan["prestige"])
plt.scatter(x=duncan["income"], y=duncan["prestige"])
plt.scatter(x=duncan["income"], y=duncan["education"])
#agora vamos separar a base entre variáveis independentes e dependente
X = duncan.loc[:, ["income", "education"]]
X.head()
y = duncan.loc[:, "prestige"]
y.head()
#vamos ver os resultados do modelo, acrescentando uma constante
import sklearn.linear_model as lm
import statsmodels.api as sm
X=sm.add_constant(X)
model=sm.OLS(y,X).fit()
model.summary()

#agora que eu já calculei o parâmetro, vamos fazer o bootstrap para criar um intervalo
#de confiança do mesmo
#o bootstrap consiste em fazer muitas estimações pegando subamostras da nossa amostra
#e criando uma distribuição de valores de parãmetros para criar um intervalo de confiança
#para o valor destes parâmetros
def simple_resample(n): 
    return(np.random.randint(low = 0, high = n, size = n))

def bootstrap(boot_pop, statistic, resample = simple_resample, replicates = 10000):
    n = len(boot_pop)
    resample_estimates = np.array([statistic(boot_pop[resample(n)]) for _ in range(replicates)])
    return resample_estimates

def educ_coeff(data_array):
    X = data_array[:, 1:]
    y = data_array[:, 0]
    
    linear_model = lm.LinearRegression()
    model = linear_model.fit(X, y)
    theta_educ = model.coef_[1]

    return theta_educ

data_array = duncan.loc[:, ["prestige", "income", "education"]].values

theta_hat_sampling = bootstrap(data_array, educ_coeff)

plt.figure(figsize = (7, 5))
plt.hist(theta_hat_sampling, bins = 30, normed = True)
plt.xlabel("$\\tilde{\\theta}_{educ}$ Values")
plt.ylabel("Proportion per Unit")
plt.title("Bootstrap Sampling Distribution of $\\tilde{\\theta}_{educ}$ (Nonparametric)");
plt.show()
left_confidence_interval_endpoint = np.percentile(theta_hat_sampling, 2.5)
right_confidence_interval_endpoint = np.percentile(theta_hat_sampling, 97.5)
left_confidence_interval_endpoint, right_confidence_interval_endpoint