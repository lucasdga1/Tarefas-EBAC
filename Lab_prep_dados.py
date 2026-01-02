import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('file_path.csv')

# Escreva seu código abaixo

# Verifica a quantidade de dados únicos em cada coluna
unicos = df.nunique()
print('Analise de dados únicos:\n', unicos)

# Calcula estatísticas descritivas dos campos numéricos
estatisticas = df.describe()
print('Estatísticas dos dados:\n', estatisticas)

# Cria o campo "Preço" com o cálculo em relação aos campos "Reais" e "Centavos"
df['Preco'] = (df['Reais'] + (df['Centavos'] / 100))
print(df[['Reais', 'Centavos', 'Preco']])
# Remova os campos citados nas intruções e armazene novamente na variável `df`
df = df.drop(['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'], axis = 1)
print(df.head())

# Normalizando e Codificando
scaler = MinMaxScaler()
labelEncoder = LabelEncoder()

df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
print(df[['Nota', 'Nota_MinMax']])

df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
print(df[['Desconto', 'Desconto_MinMax']])

df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])
print(df[['N_Avaliacoes', 'N_Avaliacoes_MinMax']])

df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])
print(df[['Preco', 'Preco_MinMax']])

df['Marca_Cod'] = labelEncoder.fit_transform(df['Marca'])
print(df[['Marca', 'Marca_Cod']])

df['Material_Cod'] = labelEncoder.fit_transform(df['Material'])
print(df[['Material', 'Material_Cod']])

df['Temporada_Cod'] = labelEncoder.fit_transform(df['Temporada'])
print(df[['Temporada', 'Temporada_Cod']])

qtd_vendidos_map = {
    'Nenhum': 0, '1': 1, '2': 2, '3': 3, '4': 4, '+5': 5,
    '+25': 25, '+50': 50, '+100': 100, '+1000': 1000, '+10mil': 10000, '+50mil': 50000
}
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(qtd_vendidos_map)
print(df[['Qtd_Vendidos', 'Qtd_Vendidos_Cod']])

df['Marca_Freq'] = df['Marca'].map(df['Marca'].value_counts(normalize = True))
print(df[['Marca', 'Marca_Freq']])

mf_material = df['Material'].value_counts() / len(df)

df['Material_Freq'] = df['Material'].map(mf_material)
print(df[['Material', 'Material_Freq']])