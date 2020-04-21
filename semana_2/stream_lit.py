import streamlit as st
import numpy as np

def main():
    st.title('Hello Word')
    st.markdown('Botão')

    botao = st.button('Botao')

    if botao:
        st.markdown('Clicado')

    st.markdown('Checkbox')
    checkbox = st.checkbox('Teste')

    if checkbox:
        st.markdown('Clicado')

    st.markdown('Radio')

    radio = st.radio('Escolha as opções!', ('Option1', 'Option2'))

    if radio == 'Option1':
        st.markdown('Lindo')
    elif radio == 'Option2':
        st.markdown('Não Lindo')

    st.markdown('SelectBox')
    selectbox = st.selectbox('Choose List', ('Opt1', 'Opt2'))

    if selectbox == 'Opt1':
        st.markdown('Opção 1')
    elif selectbox == 'Opt2':
        st.markdown('Opção 2')

    st.markdown('Mult')
    mult = st.multiselect('Choose Multiselect', (1, 2, 3))
    soma = np.sum(mult)
    st.markdown(f'A soma é {soma}')

    st.markdown('File Uploader')

    file = st.file_uploader('Drop File', type='csv')

    if file is not None:
        st.markdown('Subiu')

if __name__ == '__main__':
    main()
