import streamlit as st
import pandas as pd

def main():

    st.title('Hello Pandas')

    file = st.file_uploader('Suba sua planilha', type='csv')

    if file is not None:
        df = pd.read_csv(file)

        slider = st.slider('Escolha quantas linhas', 1, 300)

        selected_columns = st.multiselect('Selecione as Colunas', df.columns)

        if len(selected_columns) > 0:
            st.markdown('Teste DataFrame')
            st.dataframe(df.head(slider)[selected_columns])

        st.markdown('Teste Table')
        st.table(df.groupby('species')['petal_width'].mean())

if __name__ == '__main__':
    main()