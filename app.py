import os
import pandas as pd
import streamlit as st

def menu():
    
    st.sidebar.page_link("app.py", label="Trang chủ")

    st.sidebar.page_link("pages/1_PhanTichDuLieu.py", label="Phân tích dữ liệu")

    st.sidebar.page_link("pages/2_ThemDuLieu.py", label="Thêm dữ liệu dự đoán")

    st.sidebar.page_link("pages/3_DuDoanDuLieu.py", label="Phân tích dự đoán")
    
    st.sidebar.page_link("pages/4_LichSu.py", label="Lịch sử dữ liệu")
    
    st.sidebar.image("images/CCT_logo.png", width=150)
    
    if __name__ == "__main__":
        st.set_page_config(
            page_title="Cycling Calorie Tracker",
            layout="centered",
            page_icon="🚴",
        )

        st.title("Cycling Tracker")
        st.header("Chức năng")
        st.markdown("""
        1. Xem dự đoán calories khi đạp xe qua các thuộc tính
        2. Thêm dữ liệu mới và cập nhật các biểu đồ
        3. Sử dụng AI để dự đoán calories của
        """)
        
        st.subheader("Credits")
        st.markdown(

            """
            Ứng dựng được xây dựng với [streamlit](https://streamlit.io) và [Seaborn](https://seaborn.pydata.org/).
            
            Bản quyền thuộc về Trương Phạm Lộc
            """
        )
        

menu()
