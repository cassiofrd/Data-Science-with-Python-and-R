# -*- coding: utf-8 -*-
#aprendendo matplotlib
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[2,4,6,8]
#com plot plotamos uma linha que liga os pontos
plt.plot(x,y)
#podemos também acrescentar alguns elementos ao gráfico
#IMPORTANTE: tem que selecionar todas as linhas e rodar
#se for uma por uma não funciona
plt.plot(x,y)
plt.title('A basic line Plot')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.show()
#mesmo gráfico com título à esquerda
plt.plot(x,y)
plt.title('À esquerda', loc='left')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.show()
#mesmo gráfico com título à direita
plt.plot(x,y)
plt.title('À direita', loc='right')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.show()

#agora vamos modificar a cor da linha e sua espessura
plt.plot(x,y,color='green',linewidth=5)
plt.title('A basic line Plot')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.show()

#agora vamos modificar o tamanho da figura e a resolução do plot
plt.figure(figsize=(10,4),dpi=200)
plt.plot(x,y,color='green',linewidth=5)
plt.title('A basic line Plot')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.show()

#agora vamos acrescentar uma seta
plt.figure(figsize=(10,4),dpi=200)
plt.plot(x,y,color='green',linewidth=5)
plt.annotate('This is a line',xy=(2.5,5.5),xytext=(1.5,7),arrowprops={'facecolor':'black','shrink':0.05}) #como vemos aqui eu escolhi tanto o ponto inicial da seta quanto o final, assim como a cor da seta
plt.title('A basic line Plot')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.show()

#vamos colocar outra linha de plot na mesma figura
a=[1,2,3,4]
b=[1,2,3,4]
plt.figure(figsize=(10,4),dpi=200)
plt.plot(x,y,color='green',linewidth=5)
plt.plot(a,b,color='red',linewidth=5)
plt.annotate('This is a line',xy=(2.5,5.5),xytext=(1.5,7),arrowprops={'facecolor':'black','shrink':0.05}) #como vemos aqui eu escolhi tanto o ponto inicial da seta quanto o final, assim como a cor da seta
plt.title('A basic line Plot')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.show()

#vamos colocar outra linha de plot na mesma figura
a=[1,2,3,4]
b=[1,2,3,4]
plt.figure(figsize=(10,4),dpi=200)
plt.plot(x,y,color='green',linewidth=5)
plt.plot(a,b,color='red',linewidth=5)
plt.annotate('This is a line',xy=(2.5,5.5),xytext=(1.5,7),arrowprops={'facecolor':'black','shrink':0.05}) #como vemos aqui eu escolhi tanto o ponto inicial da seta quanto o final, assim como a cor da seta
plt.title('A basic line Plot')
plt.xlabel('X-axis')
plt.ylabel('y-ax')
plt.legend(['Green Line','Red Line'])
plt.show()

#agora vamos criar subplots e salvar as figuras
#temos dois plots na mesma figura
import matplotlib.pplot as plt
plt.subplots(1,2) #primeiro o número de linhas, depois o de colunas
plt.show()

#agora vamos criar quatro subplots
plt.subplots(2,2)
plt.show()

#tuplas unpacking
fig,ax=plt.subplots(1,2)
plt.show()
print(f'fig: {fig}, ax {ax}')

#vamos plotar os dados nos subplots
x1=[1,2,3,4]
y1=[2,4,6,8]
fig, ax=plt.subplots(1,2)
ax[0].plot(x1,y1,color='green',linewidth=5)
plt.show()

#agora vamos colocar dados também no segundo subplot
x1=[1,2,3,4]
y1=[2,4,6,8]
x2=[1,2,3,4]
y2=[1,2,3,4]
fig, ax=plt.subplots(1,2)
ax[0].plot(x1,y1,color='green',linewidth=5)
ax[1].plot(x2,y2,color='red',linewidth=5)
plt.show()

#vamos agora acrescentar títulos e legendas
x1=[1,2,3,4]
y1=[2,4,6,8]
x2=[1,2,3,4]
y2=[1,2,3,4]
fig, ax=plt.subplots(1,2)
ax[0].plot(x1,y1,color='green',linewidth=5)
ax[0].set_title('Subplot 1')
ax[0].set_xlabel('X-axis-1')
ax[0].set_ylabel('Y-axis-1')
ax[1].plot(x2,y2,color='red',linewidth=5)
ax[1].set_title('Subplot 2')
ax[1].set_xlabel('X-axis-2')
ax[1].set_ylabel('Y-axis-2')
plt.show()

#agora vamos salvar a figura
x1=[1,2,3,4]
y1=[2,4,6,8]
x2=[1,2,3,4]
y2=[1,2,3,4]
fig, ax=plt.subplots(1,2)
ax[0].plot(x1,y1,color='green',linewidth=5)
ax[0].set_title('Subplot 1')
ax[0].set_xlabel('X-axis-1')
ax[0].set_ylabel('Y-axis-1')
ax[1].plot(x2,y2,color='red',linewidth=5)
ax[1].set_title('Subplot 2')
ax[1].set_xlabel('X-axis-2')
ax[1].set_ylabel('Y-axis-2')
plt.savefig('figura_python.png')
plt.show()



#agora vamos plotar plots 2D no Matplotlib
#plot simples, sem linha
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.figure(figsize=(10,4),dpi=200)
plt.scatter(x,y)
plt.title('A Basic Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#agora, vamos acrescentar tamanhos e cores dos plots
#cada ponto de uma cor
#cada ponto de um tamanho
sizes=[112,380,100,12,60]
colors=[4,20,11,3,1]
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.figure(figsize=(10,4),dpi=200)
plt.scatter(x,y)
plt.title('A Basic Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#agora vamos plotar gráficos de barras
plt.figure(figsize=(10,4),dpi=200)
plt.bar(x,y)
plt.title('A Vertical Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#agora vamos modificar o sentido
plt.figure(figsize=(10,4),dpi=200)
plt.barh(x,y)
plt.title('A Horizontal Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#vamos colocar duas barras nas mesmas posições
#dois gráficos de barra nas mesmas posições
y_top=[12,14,16,18,20]
plt.figure(figsize=(10,4),dpi=200)
plt.bar(x,y)
plt.bar(x,y_top,bottom=y)
plt.legend(['y','y_top'])
plt.title('A Stacked Vertical Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#agora vamos mudar a posição dos gráficos acima
y_top=[12,14,16,18,20]
plt.figure(figsize=(10,4),dpi=200)
plt.bar(x,y)
plt.bar(x,y_top,left=y)
plt.legend(['y','y_top'])
plt.title('A Stacked Vertical Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#agpra va,ps ver gráficos de pizza
label={'Year 1','Year 2','Year 3','Year 4','Year 5'}
values=[235,695,554,550,545]
plt.figure(figsize=(2,4), dpi=200)
plt.pie(values,labels=label,startangle=45)
plt.show()

#vamos agora destacar uma das fatias da pizza das demais
Explode=(0,0.1,0,0,0)
label={'Year 1','Year 2','Year 3','Year 4','Year 5'}
values=[235,695,554,550,545]
plt.figure(figsize=(2,4), dpi=200)
plt.pie(values,labels=label,explode=Explode,startangle=45)
plt.show()

#agora é gráficos 3d meu filho, ai o negócio ficou sério
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#vamos ver a estrutura na qual ficam os gráficos 3d
plt.axes(projection='3d')
plt.show()

#3d plot de linha que liga os pontos
x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=[4,10,20,5,3]
ax=plt.axes(projection='3d')
ax.plot3D(x,y,z)
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
plt.show()

#apenas os pontos plotados (scatter) sem linhas
x=[1,2,3,4,5]
y=[1,2,3,4,5]
z=[4,10,20,5,3]
ax=plt.axes(projection='3d')
ax.scatter3D(x,y,z)
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
plt.show()

#agora vamos aprender a plotar uma imagem
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img=mpimg.imread('C:/Users/Cássio/Desktop/Foto_nova.jpg')
print(type(img))
print(img.shape)
plt.imshow(img)