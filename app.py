import streamlit as st
import pandas as ps
import numpy as np
st.title("Hello Streamlit 👋")
st.write("This is my first Streamlit app running in the py312 environment!")

# Add a simple interactive widget
name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}! 🚀")

##Create the Simple Datafrae
df=ps.DataFrame({
    'frist_coloum':[2,3,4,5]
    ,
    'Secound_coloum':[4,5,6,7]

})
st.write("Here is the dataframe")
st.write(df)


##create the line chart

st.write("Line chart is here")
Chart_line=ps.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(Chart_line)
    
##Silder 
Age=st.slider("Select the age",0,100,25)
st.write(f"The age is{Age}.")    


## create the Choice box
Choice=["Python","java","C++","Script"]
option=st.selectbox("Choice your fav",Choice)
df.to_csv("Sample.csv")
st.write(option)

#Uploade the csv file

Upload=st.file_uploader("Choose a csv file",type="csv")

if Upload is not None:
    df=ps.read_csv(Upload)
    st.write(df)

