import streamlit as st
from app import menu
from datetime import datetime
import pandas as pd
import os
from app import menu
import joblib

# Gọi menu để hiển thị ở sidebar
menu()

# Đọc file
df = pd.read_csv("Data Cycling Clean.csv")

st.title("Thêm dữ liệu mới")

activity = st.selectbox("Chọn hình thức đạp xe", ["indoor_cycling", "outdoor_cycling"])

distance = st.number_input(
    "Distance (km) - Quãng đường đạp xe",
    min_value = 5,
    max_value = 200,
    value = 20,
    step = 1
)

duration = st.number_input(
    "Duration (min) - Thời gian đạp xe",
    min_value = 5,
    max_value = 300,
    value = 60,
    step= 1
)

avg_hr = st.slider(
    "Average Heart Rate (bpm) - Nhịp tim trung bình",
    min_value = 60,
    max_value = 160,
    value = 80
)

avg_speed = st.slider(
    "Average Speed (km/h) - Tốc độ trung bình",
    min_value = 10,
    max_value = 80,
    value = 30
)

cadence = st.slider(
    " - Nhịp đạp xe trung bình (vòng đạp/phút)",
    min_value = 50,
    max_value = 130,
    value = 80
)

if activity == "outdoor_cycling":
    elev_gain = st.number_input(
        "Elevation Gain (m) - Độ cao tăng thêm",
        min_value = 10,
        max_value = 2000,
        value = 200,
        step = 1
    )

    elev_loss = st.number_input(
        "Elevation Loss (m) - Độ cao giảm xuống",
        min_value = 10,
        max_value = 2000,
        value = 200,
        step = 1
    )
else:
    elev_gain = 0
    elev_loss = 0

if st.button("Thêm dữ liệu vào tập test"):
    # lưu vào session
    st.session_state["activity"] = activity
    st.session_state["distance"] = distance
    st.session_state["duration"] = duration
    st.session_state["avg_hr"] = avg_hr
    st.session_state["avg_speed"] = avg_speed
    st.session_state["cadence"] = cadence
    st.session_state["elev_gain"] = elev_gain
    st.session_state["elev_loss"] = elev_loss
    st.success("Đã lưu dữ liệu cho trang dự đoán")
    
    new_data = {
        "Activity Type": activity,
        "Distance": distance,
        "Duration(min)": duration,
        "Avg HR": avg_hr,
        "Avg Speed": avg_speed,
        "Avg Bike Cadence": cadence,
        "Elev Gain": elev_gain,
        "Elev Loss": elev_loss
    }
    
    if os.path.exists("Data Input.csv"):

        input_data = pd.read_csv("Data Input.csv")

        new_data["ID"] = len(input_data) + 1

        input_data = pd.concat(
            [input_data, pd.DataFrame([new_data])],
            ignore_index=True
        )

    else:

        new_data["ID"] = 1

        input_data = pd.DataFrame([new_data])

    input_data.to_csv("Data Input.csv", index=False)
