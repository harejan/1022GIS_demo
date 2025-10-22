import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

# --- 1. 頁面配置 ---
st.set_page_config(layout="wide")
st.title("Leafmap + GeoPandas 示範 (含底圖切換)")


# --- 2. 主頁面：底圖選擇 (修改為在主頁面顯示) ---
# 定義底圖選項，這些是 leafmap/folium 支援的名稱
BASEMAP_OPTIONS = {
    "OpenTopoMap⛰️": "OpenTopoMap",
    "Esri衛星圖🛰️": "Esri.WorldImagery",
    "CartoDB暗色🖤": "CartoDB.DarkMatter",
    "OpenStreetMap🗺️": "OpenStreetMap", # 新增一個選項
}

st.header("地圖設定")
# !!! 關鍵修改：使用 st.selectbox 而非 st.sidebar.selectbox !!!
selected_name = st.selectbox(
    "選擇底圖 (Basemap)",
    list(BASEMAP_OPTIONS.keys()),
    index=1 # 預設選擇 Esri 衛星圖
)

# 根據選擇的名稱獲取實際的底圖代碼
selected_basemap_code = BASEMAP_OPTIONS[selected_name]

# 可以考慮將底圖選擇欄位放到 st.columns() 中以節省空間
# col1, col2 = st.columns([1, 4])
# with col1:
#     selected_name = st.selectbox(...)
#     selected_basemap_code = BASEMAP_OPTIONS[selected_name]


# --- 3. 載入 GeoPandas 資料 (保持不變) ---
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
# 由於資料較大，建議使用 Streamlit 的快取來避免每次重載
@st.cache_data
def load_data(data_url):
    return gpd.read_file(data_url)

gdf = load_data(url)

st.subheader("GeoDataFrame 資料預覽")
# 縮短 GeoDataFrame 顯示的行數，讓頁面更簡潔
st.dataframe(gdf.head(3))


# --- 4. 初始化地圖 (將選擇的底圖應用於此處) ---
m = leafmap.Map(
    center=[0, 0],
    zoom=1,
    # 關鍵：使用使用者在主頁面選擇的底圖
    tiles=selected_basemap_code
)

# --- 5. 將 GeoDataFrame 加入地圖 ---
m.add_gdf(
    gdf,
    layer_name="國家邊界 (Vector)",
    style={"fillOpacity": 0, "color": "blue", "weight": 1.0}, # 顏色改為紅色，更醒目
    highlight=False
)

# 加入圖層控制面板
m.add_layer_control()

# --- 6. 渲染地圖至 Streamlit ---
st.subheader("地圖顯示")
m.to_streamlit(height=700)