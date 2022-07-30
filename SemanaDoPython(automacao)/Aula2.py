
# PASSO 1: importar bibliotecas
import pandas as pd
from IPython.display import display

tabela_clientes =pd.read_csv(r'C:\Users\Usuario\OneDrive\Área de Trabalho\MuriAulasPython\Aula 2\telecom_users.csv')

# PASSO 2: visualizar a tabela para descobir as informações
tabela_clientes = tabela_clientes.drop('Unnamed: 0', axis=1)
display(tabela_clientes)

# PASSO 3: tratamento de dados
#sempre quando importar uma tabela verificar:
# problemas de tipo de informação
tabela_clientes['TotalGasto'] = pd.to_numeric(tabela_clientes['TotalGasto'], errors=('coerce'))

# problemas de valores vazios
tabela_clientes = tabela_clientes.dropna(how='all', axis=1)
tabela_clientes = tabela_clientes.dropna(how='any', axis=0)

print(tabela_clientes.info())

# PASSO 4: olhar como estão destribuidos os churns/cancelamentos
display(tabela_clientes['Churn'].value_counts())
display(tabela_clientes['Churn'].value_counts(normalize=True).map("{:.1%}".format))

# PASSO 5: fazer uma analise da causa dos cancelamentos
import plotly.express as px

for coluna in tabela_clientes:
    grafico = px.histogram(tabela_clientes, x=coluna, color='Churn')
    grafico.show()
