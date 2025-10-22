import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd 

st.set_page_config(layout="wide")
st.title("Leafmap + GeoPandas 示範")

# --- 1. 載入 GeoPandas 資料 ---
# 載入 Natural Earth 110m 國家邊界資料 (.zip 格式)
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

# GeoPandas 直接從 URL 讀取 .zip 檔案中的 Shapefile
gdf = gpd.read_file(url)

# (可選) 顯示 GeoDataFrame 的前幾行資料
st.subheader("GeoDataFrame 資料預覽")
st.dataframe(gdf.head())

# --- 2. 初始化地圖 ---
# 建立一個以 (0, 0) 為中心的世界地圖
m = leafmap.Map(center=[0, 0], zoom=1) 

# --- 3. 將 GeoDataFrame 加入地圖 ---
# 使用 add_gdf() 方法將 GeoDataFrame (gdf) 加入 Leafmap 地圖
m.add_gdf(
    gdf,
    layer_name="國家邊界 (Vector)",
    # 設定邊界樣式：內部透明度 0，邊框黑色，線寬 0.5
    style={"fillOpacity": 0, "color": "black", "weight": 0.5},
    # 停用滑鼠懸停高亮效果
    highlight=False
)

# 加入圖層控制面板，讓使用者可以開關 GeoDataFrame 圖層
m.add_layer_control()

# --- 4. 渲染地圖至 Streamlit ---
m.to_streamlit(height=700)