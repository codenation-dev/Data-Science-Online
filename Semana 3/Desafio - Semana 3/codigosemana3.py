import streamlit as st
import pandas as pd
import altair as alt
import json
from pprint import pprint

##
#data = {}
#data['people'] = []
#data['people'].append({
#    'name': 'Scott',
#    'website': 'stackabuse.com',
#    'from': 'Nebraska'
#})
#data['people'].append({
#    'name': 'Larry',
#    'website': 'google.com',
#    'from': 'Michigan'
#})
#data['people'].append({
#    'name': 'Tim',
#    'website': 'apple.com',
#    'from': 'Alabama'
#})

data = {
    "SC": {"moda": 0.0, "mediana": 0.0, "media": 0.0, "desvio_padrao": 0.0
    }, 
    "RS": {"moda": 0.0, "mediana": 0.0, "media": 0.0, "desvio_padrao": 0.0
    }, 
    "PR": {"moda": 0.0, "mediana": 0.0, "media": 0.0, "desvio_padrao": 0.0
    }
}

def main():
    st.header('CHEGUEI ACELERADO E VENDO TUDO DIFERENTE')
    df = pd.read_csv('desafio1.csv')
    if df is not None:
        slider = st.slider('Valores', 1,100)
        #df = pd.read_csv(file)
        st.dataframe(df.head(slider))
        st.markdown('TABELINHA')
        #st.table(df.head(slider))
        st.markdown('Numero de linhas')
        st.markdown(df.shape[0])
        st.markdown('Numero de colunas')
        st.markdown(df.shape[1])
        aux = pd.DataFrame({"colunas": df.columns, 'tipos': df.dtypes})

        st.markdown('Moda por estado')
        df.loc[df['estado_residencia'] == 'SC', 'pontuacao_credito'].value_counts().index[0]
        df.loc[df['estado_residencia'] == 'RS', 'pontuacao_credito'].value_counts().index[0]
        df.loc[df['estado_residencia'] == 'PR', 'pontuacao_credito'].value_counts().index[0]
        #st.title('Testinho')
        #st.table()

        st.markdown('Media por estado')
        st.table(df.groupby('estado_residencia')['pontuacao_credito'].mean())

        st.markdown('Mediana por estado')
        st.table(df.groupby('estado_residencia')['pontuacao_credito'].median())

        st.markdown('Desvio padrao por estado')
        st.table(df.groupby('estado_residencia')['pontuacao_credito'].std())

        exploracao = pd.DataFrame({'nomes' : df.columns, 'tipos' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})
        
        st.write(exploracao.tipos.value_counts())

        #Moda
        data["SC"]["moda"] = int(df.loc[df['estado_residencia'] == 'SC', 'pontuacao_credito'].value_counts().index[0])
        data["PR"]["moda"] = int(df.loc[df['estado_residencia'] == 'PR', 'pontuacao_credito'].value_counts().index[0])
        data["RS"]["moda"] = int(df.loc[df['estado_residencia'] == 'RS', 'pontuacao_credito'].value_counts().index[0])

        #medianas
        data["SC"]["mediana"] = df.loc[df['estado_residencia'] == 'SC', 'pontuacao_credito'].median()
        data["PR"]["mediana"] = df.loc[df['estado_residencia'] == 'PR', 'pontuacao_credito'].median()
        data["RS"]["mediana"] = df.loc[df['estado_residencia'] == 'RS', 'pontuacao_credito'].median()

        #Medias
        data["SC"]["media"] = df.loc[df['estado_residencia'] == 'SC', 'pontuacao_credito'].mean()
        data["PR"]["media"] = df.loc[df['estado_residencia'] == 'PR', 'pontuacao_credito'].mean()
        data["RS"]["media"] = df.loc[df['estado_residencia'] == 'RS', 'pontuacao_credito'].mean()

        #desvio padrao
        data["SC"]["desvio_padrao"] = df.loc[df['estado_residencia'] == 'SC', 'pontuacao_credito'].std()
        data["PR"]["desvio_padrao"] = df.loc[df['estado_residencia'] == 'PR', 'pontuacao_credito'].std()
        data["RS"]["desvio_padrao"] = df.loc[df['estado_residencia'] == 'RS', 'pontuacao_credito'].std()

        st.markdown(data)

        with open('submission.json', 'w') as outfile:
            json.dump(data, outfile)

        open('submission.json', 'r').read()



if __name__ == '__main__':
    main()

#with open('data.txt') as outfile:
#    json.dump(data, outfile)
#    
#with open('submission.json') as f:    
#    data = json.load(f)
#    print(data)

