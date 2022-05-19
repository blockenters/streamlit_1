import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('data2/iris.csv')

    # 버튼 만들기
    # if st.button('데이터 보기') :
    #     st.dataframe(df)

    # "대문자" 버튼을 만들고,
    # 버튼을 누르면, species 컬럼의 값들을 대문자로 변경한
    # 데이터 프레임을 보여주세요.

    st.dataframe(df)

    if st.button('대문자') :
        df['species'] = df['species'].str.upper()
        st.dataframe( df )


    # 라디오버튼 : 여러개중에 한개 선택할때
    my_order = ['오름차순 정렬', '내림차순 정렬']

    status = st.radio('정렬방법 선택', my_order)

    if status == my_order[0]:
        # petal_length 컬럼을 오름차순으로 정렬해서 화면에 보여준다.
        # df.sort_values('petal_length')
        st.dataframe(df.sort_values('petal_length'))
    elif status == my_order[1] :
        # df.sort_values('petal_length', ascending=False)
        st.dataframe(df.sort_values('petal_length', ascending=False))

    status = st.radio('정렬방법 선택2', my_order)
    if status == my_order[0]:
        # petal_length 컬럼을 오름차순으로 정렬해서 화면에 보여준다.
        df = df.sort_values('petal_length')
        st.dataframe(df)
    elif status == my_order[1] :
        df = df.sort_values('petal_length', ascending=False)
        st.dataframe(df)


    # 체크박스 : 체크 해제/체크
    if st.checkbox('헤드 5개 보기') :
        st.dataframe( df.head() )
    else :
        st.text('헤드 숨겼습니다.')

    # 셀렉트 박스  : 여러개에서 한개만 고르는 UI
    language = ['Python', 'C', 'Java', 'Go', 'PHP']
    my_choice = st.selectbox('좋아하는 언어 선택', language)

    if my_choice == language[0] :
        st.write('파이썬을 선택했습니다.')
    elif my_choice == language[1] :
        st.write('C언어가 좋아요')
    elif my_choice == language[2] :
        st.write('자바 선택')

    # 멀티셀렉트 : 여러개 중에서, 여러개 선택하는 UI
    st.multiselect('여러개 선택가능', language)


    # 멀티셀렉트를 이용해서, 특정 컬럼들만 가져오기.
    # 유저에게, iris df의 컬럼들을 다 보여주고,
    # 유저가 선택한 컬럼들만, 데이터프레임을 화면에 보여줄것!
    column_list = df.columns
    choice_list = st.multiselect('컬럼을 선택하세요', column_list)

    st.dataframe( df[choice_list] )


    # 슬라이더 :  숫자 조정하는데 주로 사용 
    # st.slider('나이', 1.0, 120.0, 30.0, 0.1)
    age = st.slider('나이', 1, 120, 30)

    st.text('제가 선택한 나이는 {}입니다.'.format(age))


    # 익스펜더 
    with st.expander('Hello') :
        st.text('안녕하세요')
        st.dataframe(df)


if __name__=='__main__' :
    main()
