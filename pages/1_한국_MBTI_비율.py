import streamlit as st

st.set_page_config(page_title="🇰🇷 한국 MBTI 비율", page_icon="🇰🇷", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#fffaff,#f5fbff);}
.title {text-align:center;font-size:2.4rem;font-weight:800;color:#202638;}
.subtitle {text-align:center;color:#687083;margin-bottom:25px;}
.card {background:white;border:1px solid #eee;border-radius:22px;padding:24px;box-shadow:0 10px 30px rgba(40,40,80,.07);}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🇰🇷 우리나라 MBTI 비율</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">한국에서 어떤 MBTI가 얼마나 나타나는지 한눈에 살펴봐요! 📊</div>', unsafe_allow_html=True)

st.info("💡 아래 수치는 특정 공식 국가통계가 아니라, 공개된 국내 MBTI 조사 사례를 참고한 예시 데이터입니다. 조사기관·표본에 따라 결과가 달라질 수 있어요.")

data = {
    "ISTJ": 12.3, "ISFJ": 8.9, "INFJ": 3.8, "INTJ": 3.7,
    "ISTP": 4.7, "ISFP": 6.8, "INFP": 6.9, "INTP": 4.1,
    "ESTP": 4.3, "ESFP": 5.1, "ENFP": 7.5, "ENTP": 3.2,
    "ESTJ": 5.7, "ESFJ": 6.4, "ENFJ": 3.1, "ENTJ": 2.5
}

st.bar_chart(data)

st.markdown("""
<div class="card">
<b>🔎 그래프 읽어보기</b><br><br>
MBTI 비율은 조사 대상과 조사 방법에 따라 달라질 수 있어요.
따라서 '가장 많은 유형 = 가장 좋은 유형'이라는 의미는 절대 아니랍니다. 🌱
</div>
""", unsafe_allow_html=True)

if st.button("🎈 재미있는 데이터 더 보기", use_container_width=True):
    st.balloons()
    st.success("🎉 MBTI는 순위를 매기는 도구가 아니라 나를 알아가는 재미있는 출발점이에요!")
