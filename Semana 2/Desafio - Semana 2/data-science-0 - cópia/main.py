#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[160]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# In[5]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[88]:


black_friday


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[9]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    mulheres = black_friday["Gender"] == "F"
    meia_idade = black_friday['Age'] == '26-35'
    return len(black_friday[mulheres & meia_idade].index)
    pass


# In[51]:


black_friday['Gender'].value_counts()


# In[56]:


mulheres = black_friday["Gender"] == "F"
meia_idade = black_friday['Age'] == '26-35'
len(black_friday[mulheres & meia_idade].index)


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()
    pass


# In[59]:


black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()
    pass


# In[68]:


black_friday.dtypes


# In[69]:


black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    parcial = black_friday.isnull().any(axis=1).value_counts().loc[True]
    total = parcial/black_friday.shape[0]
    return float(total)
    pass


# In[195]:


parcial = black_friday.isnull().any(axis=1).value_counts().loc[True]
total = parcial/black_friday.shape[0]
float(total)


# In[90]:


black_friday.isnull().any(axis=1).value_counts().loc[True]


# In[98]:


x = 1 - len(black_friday.dropna()) / len(black_friday)
x


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday['Product_Category_3'].isnull().sum(axis=0))
    pass


# In[197]:


int(black_friday['Product_Category_3'].isnull().sum(axis=0))

#int(black_friday.isnull().sum().max())


# In[115]:


black_friday.info()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].value_counts().idxmax()
    pass


# In[126]:


black_friday['Product_Category_3'].value_counts().idxmax()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    normalized_column=(black_friday['Purchase']-black_friday['Purchase'].min())/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
    return float(normalized_column.mean())
    pass


# In[129]:


black_friday['Purchase'].mean()


# In[139]:


normalized_df=(black_friday['Purchase']-black_friday['Purchase'].min())/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
normalized_df.mean()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(np.array(black_friday['Purchase']).reshape(-1,1))
    resultado = scaled_data[(scaled_data<1) & (scaled_data>-1)]
    return int(resultado.size)
    pass


# In[169]:


scaler = StandardScaler()
scaled_data = scaler.fit_transform(np.array(black_friday['Purchase']).reshape(-1,1))
resultado = scaled_data[(scaled_data<1) & (scaled_data>-1)]
int(resultado.size)


# In[171]:


black_friday['Purchase'].value_counts().sum()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    P2 = black_friday['Product_Category_2'].isnull()
    P3 = black_friday['Product_Category_3'].isnull()

    for index,value in P2.items():
        if value == False:
            if P3[index] == True:
                aux = False
        else: aux = True

    return aux
    pass


# In[194]:


P2 = black_friday['Product_Category_2'].isnull()
P3 = black_friday['Product_Category_3'].isnull()

for index,value in P2.items():
    if value == False:
        if P3[index] == True:
            aux = False
    else: aux = True

aux
            


# In[193]:


na2 = black_friday["Product_Category_2"].isna()
na3 = black_friday["Product_Category_3"].isna()
for index,value in na2.items():
    if value == False:
        if na3[index] == True:
            aux = False
    else: aux = True

aux


# In[172]:


black_friday

