import streamlit as st

st.set_page_config(page_title="🌎 나라별 MBTI", page_icon="🌎", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#fffaff,#f5fbff);}
.title {text-align:center;font-size:2.4rem;font-weight:800;color:#202638;}
.subtitle {text-align:center;color:#687083;margin-bottom:25px;}
.card {background:white;border:1px solid #eee;border-radius:22px;padding:24px;box-shadow:0 10px 30px rgba(40,40,80,.07);}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌎 나라별 MBTI 분포</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">나라에 따라 MBTI 분포가 어떻게 다르게 나타날까요? 🗺️</div>', unsafe_allow_html=True)

st.warning("⚠️ 국가별 MBTI 자료는 조사기관, 표본, 조사 시점에 따라 차이가 큽니다. 아래는 비교를 위한 예시 데이터이며 국가 전체의 정확한 인구 비율을 의미하지 않습니다.")

countries = {
    "한국 🇰🇷": {"ISTJ": 12.3, "ISFJ": 8.9, "INFP": 6.9, "ENFP": 7.5, "ESTJ": 5.7},
    "미국 🇺🇸": {"ISTJ": 11.6, "ISFJ": 13.8, "INFP": 4.4, "ENFP": 8.1, "ESTJ": 8.7},
    "영국 🇬🇧": {"ISTJ": 11.9, "ISFJ": 12.4, "INFP": 5.2, "ENFP": 8.3, "ESTJ": 7.7},
    "일본 🇯🇵": {"ISTJ": 10.5, "ISFJ": 10.8, "INFP": 7.0, "ENFP": 6.4, "ESTJ": 6.8},
    "독일 🇩🇪": {"ISTJ": 12.0, "ISFJ": 10.7, "INFP": 4.9, "ENFP": 7.2, "ESTJ": 7.1}
}

country = st.selectbox("🌍 비교할 나라", list(countries.keys()))
st.bar_chart(countries[country])

st.markdown("""
<div class="card">
<b>🌱 이렇게 생각해 보세요</b><br><br>
같은 나라에서도 사람마다 성향은 매우 다양해요.
국가별 차이를 '국민성'처럼 단정하기보다는 조사 결과의 차이로 가볍게 살펴보는 것이 좋아요. 😊
</div>
""", unsafe_allow_html=True)

if st.button("🎈 세계 여행 떠나기!", use_container_width=True):
    st.balloons()
    st.toast("🌎 새로운 나라를 알아가는 것처럼 새로운 나도 알아가 봐요!")
