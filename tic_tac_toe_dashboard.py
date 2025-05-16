
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tic Tac Toe Dashboard", layout="centered")
st.title("📊 Tic Tac Toe Player Data Dashboard")

try:
    df = pd.read_json("tic_tac_toe_data.json")
    st.success("تم تحميل البيانات بنجاح!")
except Exception as e:
    st.error(f"فشل في تحميل البيانات: {e}")
    st.stop()

if 'player' in df.columns:
    st.subheader("👣 الحركات المسجلة:")
    st.dataframe(df[df["player"].notnull()])

    jump_counts = df["player"].value_counts()
    st.subheader("🔢 عدد الحركات لكل لاعب:")
    st.bar_chart(jump_counts)

    st.subheader("🕓 الوقت بين الحركات:")
    df_times = df[df["player"].notnull()].copy()
    df_times["time"] = pd.to_datetime(df_times["time"])
    df_times["delta"] = df_times["time"].diff().dt.total_seconds()
    st.line_chart(df_times["delta"].dropna())
else:
    st.warning("⚠️ لا توجد حركات مسجلة للاعبين.")

if 'result' in df.columns:
    st.subheader("🏆 نتيجة اللعبة:")
    result = df[df["result"].notnull()]["result"].values[0]
    st.success(f"النتيجة: {result}")
