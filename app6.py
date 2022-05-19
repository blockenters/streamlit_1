from email import message
import streamlit as st 

def main():

    # 유저한테 입력을 받는 방법 

    # 1. 이름 입력 받기
    name = st.text_input('이름을 입력하세요!')
    if name != '' :
        st.subheader(name + '님 안녕하세요??')

    # 2. 입력 글자 갯수 제한 
    address = st.text_input('주소를 입력하세요', max_chars=10)
    st.subheader(address)

    # 3. 여러 행을 입력가능토록
    message = st.text_area('메세지를 입력하세요', height=3)
    st.subheader(message)

    # 4. 숫자 입력 , 정수
    st.number_input('숫자 입력', 1, 100)

    # 5. 숫자 입력 , 실수
    st.number_input('실수 입력', 1.0, 100.0)

    # 6. 날짜 입력 
    my_date = st.date_input('약속날짜')
    st.write(my_date)

    # 요일 찍기
    st.write( my_date.weekday() )
    st.write( my_date.strftime('%A'))

    # 7. 시간 입력
    my_time = st.time_input('시간 선택')
    st.write(my_time)

    # 8. 색깔 입력
    color = st.color_picker('색을 선택하세요')
    st.write(color)

    # 9. 비밀번호 입력
    password = st.text_input('비밀번호 입력', type='password')
    st.write(password)





    

if __name__ == '__main__':
    print(__name__)
    main()