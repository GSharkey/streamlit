# pip install streamlit 
import streamlit as st
import pandas as pd

# streamlit run streamlit_01.py

st.write("# chart view")
# 샵 글자의 크기 h1, h2 같은 느낌 ?
st.write("## raw data")
view = [100, 150, 30]
st.bar_chart(view)
sview = pd.Series(view)
st.write(sview) # = sview


# st.write('Hello, *world* :sunglasses:')
# st.write(1234)
# df = st.write(pd.DataFrame({'first column' :[1,2,3,4],
                    #    'second column':[10,20,30,40]}))
# st.write(df)
# st.title("hello Streamlit")
# st.title("Hello World !")
# st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# st.header('st.button')

# if st.button('say hello') :
#     st.write('why hello there')
# else :
#     st.write('Goodbye')

# st.header("*~hello world !~*")

