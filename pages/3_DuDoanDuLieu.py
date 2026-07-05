import streamlit as st
import pandas as pd
from app import menu
import joblib

# Gọi menu để hiển thị ở sidebar
menu()

st.title("Mô hình dự đoán")

# kiểm tra xem có dữ liệu dư đoán chx
if "activity" not in st.session_state:
    st.warning("Vui lòng thêm dữ liệu dự đoán")
    st.stop()

activity_predict = st.selectbox("Chọn hình thức đạp xe", ["indoor_cycling", "outdoor_cycling"])

predict_btn = st.button("Dự đoán số calories")

# đọc lại giá trị input
activity = st.session_state["activity"]
distance = st.session_state["distance"]
duration = st.session_state["duration"]
avg_hr = st.session_state["avg_hr"]
avg_speed = st.session_state["avg_speed"]
cadence = st.session_state["cadence"]
elev_gain = st.session_state["elev_gain"]
elev_loss = st.session_state["elev_loss"]

if predict_btn:
    if activity_predict == "indoor_cycling":
        model = joblib.load("model/indoor_model.pkl")
        
        input_predict = pd.DataFrame({

            "Distance":[distance],

            "Duration(min)":[duration],

            "Avg HR":[avg_hr],

            "Avg Speed":[avg_speed],

            "Avg Bike Cadence":[cadence]
        })
    else:
        model = joblib.load("model/outdoor_model.pkl")
        
        input_predict = pd.DataFrame({

            "Distance":[distance],

            "Duration(min)":[duration],

            "Avg HR":[avg_hr],

            "Avg Speed":[avg_speed],

            "Avg Bike Cadence":[cadence],

            "Elev Gain":[elev_gain],

            "Elev Loss":[elev_loss]

        })
        
    prediction = model.predict(input_predict)

    st.success(
        f"Calories dự đoán: {prediction[0]:.0f} kcal"
    )
        
check_btn = st.button("Thẩm định")    

if check_btn:
    metrics = joblib.load("metrics.pkl")

    st.metric("R² Score", f"{metrics['r2']:.4f}")
    st.metric("MSE", f"{metrics['mse']:.2f}")
    st.metric("RMSE", f"{metrics['rmse']:.2f}")
