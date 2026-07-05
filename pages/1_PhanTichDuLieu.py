import streamlit as st
import seaborn as sns
from app import menu

# Gọi menu để hiển thị ở sidebar
menu()

import pandas as pd
from charts import *

df = pd.read_csv("Data Cycling Clean.csv")

st.title("🚴 Cycling Calories Tracker")
st.subheader("Dự đoán lượng Calories tiêu thụ khi đạp xe bằng Machine Learning")

st.header("Giới thiệu")

st.write("""
Cycling Calories Tracker là ứng dụng hỗ trợ người dùng ước tính lượng Calories
tiêu thụ trong quá trình đạp xe dựa trên các thông số của buổi tập.

Hệ thống sử dụng mô hình Machine Learning để dự đoán Calories,
giúp người dùng theo dõi hiệu quả luyện tập và xây dựng kế hoạch phù hợp.
""")

st.header("Bộ dữ liệu")

st.write("""
Bộ dữ liệu bao gồm các thuộc tính:

- Distance
- Duration
- Avg Speed
- Avg HR
- Elev Gain
- Elev Loss
- Avg Bike Cadence
- Calories (biến dùng để dự đoán)
""")

st.subheader("")
header1 = " Phân tích"
st.markdown(f"<h2 style='font-size:30; color: white; background: #02acf6; border-radius: 20px;'>{header1}</h1>", unsafe_allow_html=True)
st.subheader("")

st.subheader("Biểu đồ nhiệt thể hiện độ tương quan giữa các thuộc tính")

st.image("images/heatmap.png")
st.subheader("")
st.write("⟶ Biểu đồ nhiệt giúp em xác định mối quan hệ giữa các thuộc tính trong bộ dữ liệu. Kết quả cho thấy Distance có tương quan mạnh nhất với Calories với hệ số 0.962, vì vậy đây là biến quan trọng trong mô hình dự đoán. Ngoài ra, Elev Gain và Elev Loss có tương quan rất cao với nhau (0.967), cho thấy hai biến này chứa thông tin gần giống nhau. Các biến như Avg HR, Avg Speed, Avg Bike Cadence và Duration có ảnh hưởng ở mức trung bình.")

st.subheader("")
st.subheader("Mối quan hệ giữa các thuộc tính và Calories")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Distance (km)",
    "Duration (min)",
    "Average Heart Rate (bpm)",
    "Average Speed (km/h)",
    "Average Cadence (rpm)"
])

with tab1:
    st.image("images/distance.png")

with tab2:
    st.image("images/duration(min).png")

with tab3:
    st.image("images/avg_hr.png")

with tab4:
    st.image("images/avg_speed.png")
    
with tab5:
    st.image("images/avg_bike_cadence.png")
    