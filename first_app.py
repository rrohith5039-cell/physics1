import streamlit as st


st.header('energy calculator')

col1,col2 = st.columns(2)

with col1:
    st.subheader(':red[potential Energy]')
    m = st.number_input('mass',key='a')
    h = st.number_input('height',key='b')
    if st.button('calculate',key='abc'):
       st.write(f'the potential energy is {ma*10*h}')

with col2:
    st.subheader(':red[Potential Energy]')
    m = st.number_input('mass',key='c')
    h = st.number_input('height',key='d')
    if st.button('calculate',key= 'xyz'):
       st.write(f'the potential energy is {ma*10*h}')
       
    
                    