import streamlit as st
from app import menu
from datetime import datetime
import pandas as pd
import os
from app import menu
import joblib

# Gọi menu để hiển thị ở sidebar
menu()

st.title("Lịch sử dữ liệu đã nhập")

if os.path.exists("Data Input.csv"):
    history = pd.read_csv("Data Input.csv")

    history = history.sort_values("ID", ascending=False)

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("Chưa có dữ liệu nào.")