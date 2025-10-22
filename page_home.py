import streamlit as st
# ó¿¿öw
st.title("歡迎來到GIS專案")
st.write("這是一個使用 Streamlit 建立的互動專案程式")
#  MP4 ö URL ó st.video()
video_url = "https://i.imgur.com/1GoAB0C.mp4"
st.write(f"正在撥放影片 {video_url}")
st.video(video_url)
#  wö URL ó st.image()
image_url = "https://i.imgur.com/uf1T4ND.png"
st.image(image_url)