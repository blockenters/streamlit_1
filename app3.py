import streamlit as st
import pandas as pd 

def main() :
    df = pd.read_csv('data2/iris.csv')
    
    st.dataframe(df)

    species = df['species'].unique()

    st.text('아이리스 꽃은 '+ species + '으로 되어있다.')

    st.dataframe( df.head() )
    st.write( df.head() )

if __name__ == '__main__':
    main()

