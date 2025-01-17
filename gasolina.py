import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
    sns.lineplot(x='dia', y='venda', data=df, color='green')  
    plt.xlabel('Dia')
    plt.ylabel('Preço da Gasolina')
    plt.title('Preço da Gasolina por Dia')
    plt.savefig('gasolina.png')
    plt.show()
