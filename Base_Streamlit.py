import streamlit as st
import pandas as pd

st.title('Hello streamlit web app, Jappren github 0')
st.subheader('web app development')
st.text('I am a programmer using streamlit')
st.markdown("---------")
st.markdown("[Google](https://www.google.com)")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)
code = """ print(Hello world)
def funcy():
    return 0;
    """
st.code(code)
st.write("Good morning")
st.metric(label='Wind Speed', value = "120ms-1",delta="-1.4ms-1")
tabel = pd.DataFrame({"Column1":[1,2,3],"Column2":[4,5,6]})
st.table(tabel)
st.dataframe(tabel,hide_index=True)

st.image('photo.jpg',caption= 'this is my picture')
#st.audio('lise.mp3')
#st.video('secret.mp4')

#Checkbox

state = st.checkbox('checkbox', value= True)
if  state:
    st.write('You check the box')
else:
    pass

#Bouton Radio
radio_btn = st.radio('In which country do you live?', options=('US','UK','Canada'))
#Bouton
btn = st.button('Click me')

#select box
select = st.selectbox('What is your favorite car',options= ('Audi','BMW','Ferrari'))
#Multi selectbox
ms = st.multiselect("choose your favorite company?", options= ('Microsoft','tesla','Google','Apple'))