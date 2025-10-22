import streamlit as st
import pandas as pd
st.title("Streamlit  Widgets")
# 1. ê Widgets t (sidebar)
with st.sidebar:
 st.header("這是側邊攔")
 #  (Selectbox)
 option = st.selectbox(
 "你最喜歡的GIS軟體?",
 ("QGIS", "ArcGIS", "ENVI", "GRASS")
 )
 #  (Slider)
 year = st.slider("選擇一個年份:", 1990, 2030, 2024)
# 2. ¿¯ Widgets öÿ
st.write(f"你選擇的軟體是: {option}")
st.write(f"你選擇的年份是: {year}")
#  (Button)
if st.button("點我有氣球!點我點我"):
 st.balloons()
# þNó (File Uploader) - vß!
uploaded_file = st.file_uploader(
 "上傳你的Shapefile (.zip) 或 GeoTIFF (.tif) 或 GeoJSON (.json)",
 type=["zip", "tif", "json"]
)
if uploaded_file is not None:
 st.success(f"你上傳了: {uploaded_file.name} (//: {uploaded_file.size} bytes)")