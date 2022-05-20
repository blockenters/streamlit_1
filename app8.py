### 파일 여러개를 한꺼번에 올리는 앱 ####

from secrets import choice
import streamlit as st
from PIL import Image
import pandas as pd 
import os 
from datetime import datetime

## 파일 업로드 함수
# 디렉토리 정보와 파일을 알려주면, 해당 디렉토리에
# 파일을 저장하는 함수
def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))

def main():
    st.title('여러 파일 한번에 업로드하는 앱')

    # 사이드바용 메뉴
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox('메뉴', menu )

    if choice == menu[0] :
        # accept_multiple_files 을 True로 셋팅하면
        # 여러 파일들을 한꺼번에 받을 수 있다.
        upload_files = st.file_uploader('이미지 파일들 선택', 
                            type=['jpg','png','jpeg'] , 
                            accept_multiple_files=True)

        # upload_files는 여러 파일들을 저장하고 있는 리스트
        # 업로드한 파일이 있는 경우에만, 아래 코드를 실행해야한다.
        if upload_files is not None :

            # 업로드한 파일이 리스트이니까, 하나씩 가져와서, 
            # temp 폴더에 저장할 것이다.
            for file in upload_files :

                # 파일명을 유니크하게 만들어서 저장해야 한다.
                # 현재시간을 활용해서, 파일명을 만든다. 
                current_time = datetime.now()
                new_filename = current_time.isoformat().replace(':', '_') + '.png'

                file.name = new_filename
                save_uploaded_file('temp', file)

            # 저장이 다 끝나면, 웹브라우져에 이미지 표시 
            for file in upload_files :
                img = Image.open(file)
                st.image(img)

    ## CSV 파일을 여러개 올리면, 이 파일들을 temp 에 저장하고
    ## 데이터프레임으로 읽어서 화면에 표시!

    elif choice == menu[1] :
        upload_files = st.file_uploader('CSV파일들 선택', 
                            type= ['csv'],
                            accept_multiple_files=True)

        if upload_files is not None :
            # 업로드한 파일이 리스트이니까, 하나씩 가져와서, 
            # temp 폴더에 저장할 것이다.
            for file in upload_files :

                # 파일명을 유니크하게 만들어서 저장해야 한다.
                # 현재시간을 활용해서, 파일명을 만든다. 
                current_time = datetime.now()
                new_filename = current_time.isoformat().replace(':', '_') + '.csv'

                file.name = new_filename
                save_uploaded_file('temp', file)

            for file in upload_files :
                df = pd.read_csv(file)
                st.dataframe(df)


if __name__ == '__main__' :
    main()





