import streamlit as st
import folium
from streamlit_folium import st_folium

# 앱 제목
st.title("🇹🇼 대만 여행지도 - 인기 관광지 & 맛집 추천")

st.markdown("""
한국인들이 사랑하는 대만 여행지 3곳을 소개합니다!  
관광 명소 주변의 유명한 맛집도 함께 표시했어요.  
지도를 확대해보며 여행 루트를 계획해보세요! 🌏
""")

# 지도 중심 좌표 (타이베이 중심)
m = folium.Map(location=[25.0330, 121.5654], zoom_start=12)

# 관광지 및 맛집 데이터
locations = [
    {
        "name": "타이베이 101",
        "coords": [25.033968, 121.564468],
        "desc": "대만을 대표하는 초고층 빌딩! 전망대에서 도시 전경을 감상할 수 있어요.",
        "food": {
            "name": "딘타이펑 본점",
            "coords": [25.033114, 121.562321],
            "desc": "샤오롱바오 맛집으로 세계적으로 유명한 곳이에요!"
        }
    },
    {
        "name": "지우펀(九份)",
        "coords": [25.1097, 121.8452],
        "desc": "센과 치히로의 배경이 된 감성 가득한 산속 마을입니다.",
        "food": {
            "name": "아메이 찻집",
            "coords": [25.1099, 121.8437],
            "desc": "전통 찻집에서 대만의 차 문화를 체험해보세요."
        }
    },
    {
        "name": "스린 야시장",
        "coords": [25.088, 121.525],
        "desc": "대만 길거리 음식 천국! 저녁에 꼭 들러야 하는 명소입니다.",
        "food": {
            "name": "하오다 지파이",
            "coords": [25.0874, 121.5252],
            "desc": "스린야시장의 명물, 거대한 치킨컷렛으로 유명한 곳이에요."
        }
    }
]

# 마커 표시
for loc in locations:
    folium.Marker(
        location=loc["coords"],
        popup=f"<b>{loc['name']}</b><br>{loc['desc']}",
        tooltip=loc["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)
    
    food = loc["food"]
    folium.Marker(
        location=food["coords"],
        popup=f"<b>{food['name']}</b><br>{food['desc']}",
        tooltip=food["name"],
        icon=folium.Icon(color="green", icon="cutlery", prefix="fa")
    ).add_to(m)

# 지도 출력
st_data = st_folium(m, width=700, height=500)
