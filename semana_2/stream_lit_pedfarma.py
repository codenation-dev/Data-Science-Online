import streamlit as st
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

def main():

    st.image('logo_ped.jpg')
    st.title('Pedfarma')
    file = st.file_uploader('Anexe a Planilha Aqui:', type='csv')

    if file is not None:

        df = pd.read_csv(file, sep=';')

        df.fillna(0, inplace=True)

        farmacia = st.selectbox('Qual farmácia trabalhar?', df['Farmácia'].unique())

        if farmacia is not None:
            st.text(f'Você selecionou para ver dados de {farmacia}')
            df_farmacia = df[df['Farmácia']==farmacia]

        valor_repasse = [valor for valor,status in zip(df_farmacia['Valor a Pagar para a Farmácia'],
                             df_farmacia['Status do Saque']) if status == 'requested']

        valor_saque = [np.sum([valor_ret, valor_ant]) for valor_ret, valor_ant, status in
                       zip(df_farmacia['Taxa PedFarma'], df_farmacia['Taxa Antecipação PedFarma'],
                             df_farmacia['Status do Saque']) if status == 'requested']

        st.markdown(f'Número de Pedidos: {len(valor_repasse)}')
        st.markdown(f'Valor a repassar para a Farmácia: R${np.sum(valor_repasse).round(2)}')
        st.markdown(f'Valor a Sacar Pedfarma: R${np.sum(valor_saque).round(2)}')

if __name__ == '__main__':
    main()