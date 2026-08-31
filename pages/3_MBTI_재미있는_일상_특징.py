import streamlit as st

st.set_page_config(page_title="✨ MBTI 일상 특징", page_icon="✨", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#fffaff,#f5fbff);}
.title {text-align:center;font-size:2.4rem;font-weight:800;color:#202638;}
.subtitle {text-align:center;color:#687083;margin-bottom:25px;}
.card {background:white;border:1px solid #eee;border-radius:22px;padding:24px;box-shadow:0 10px 30px rgba(40,40,80,.07);margin-bottom:16px;}
.type {font-size:1.5rem;font-weight:800;}
.note {color:#74798a;line-height:1.7;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">✨ MBTI별 재미있는 일상 특징</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">친구들의 행동에서 이런 모습을 발견해 본 적 있나요? 😆</div>', unsafe_allow_html=True)

st.caption("※ 아래 내용은 MBTI를 재미있게 이해하기 위한 일반적인 경향을 바탕으로 만든 콘텐츠입니다. 모든 사람이 똑같이 행동하는 것은 아니에요!")

fun = {
"ISTJ":"📋 할 일을 머릿속으로 정리해 놓고 하나씩 완료할 때 은근한 쾌감을 느껴요.",
"ISFJ":"🤝 친구가 예전에 했던 말을 기억하고 있다가 조용히 챙겨주는 경우가 많아요.",
"INFJ":"🌙 혼자 조용히 생각하다가 갑자기 '아! 그때 그 말의 의미가 이거였구나' 하고 깨닫기도 해요.",
"INTJ":"♟️ 물건을 살 때도 장단점을 비교하다가 계획보다 훨씬 오래 고민할 수 있어요.",
"ISTP":"🛠️ 설명서를 오래 읽기보다 직접 만져보면서 방법을 알아내는 걸 좋아할 수 있어요.",
"ISFP":"🎨 평범한 길을 걷다가도 예쁜 하늘, 간판, 꽃 같은 디테일을 발견하면 기분이 좋아져요.",
"INFP":"🌷 음악이나 영화 속 장면 하나를 보고 혼자 여러 가지 이야기를 상상할 때가 있어요.",
"INTP":"🧪 '근데 왜?'라는 질문이 꼬리에 꼬리를 물어 검색하다가 예상보다 훨씬 깊게 파고들어요.",
"ESTP":"⚡ 계획을 세우는 것보다 일단 시작하고 상황에 맞춰 움직이는 게 편할 때가 있어요.",
"ESFP":"🎉 친구들과 재미있는 순간이 생기면 사진이나 영상으로 남기고 싶어질 수 있어요.",
"ENFP":"✨ 새로운 아이디어가 떠오르면 머릿속에서 여러 가능성이 동시에 펼쳐질 수 있어요.",
"ENTP":"💡 친구와 이야기하다가 새로운 가능성을 찾기 위해 토론할 때가 있어요.",
"ESTJ":"📌 단체 활동에서 자연스럽게 '그럼 누가 무엇을 할까?'를 정리하고 있을 때가 있어요.",
"ESFJ":"💛 단체 채팅방에서 아무도 답하지 않으면 분위기를 살리려고 먼저 말을 꺼낼 수 있어요.",
"ENFJ":"🌟 친구가 잘할 수 있는 일을 발견하면 본인보다 더 신나서 응원해 줄 때가 있어요.",
"ENTJ":"👑 목표가 생기면 필요한 순서를 정리하고 빠르게 실행 계획을 세우는 편일 수 있어요."
}

selected = st.selectbox("🧩 MBTI를 선택해 보세요", list(fun.keys()))

st.markdown(f"""
<div class="card">
<div class="type">🧩 {selected}</div>
<br>
<div class="note">{fun[selected]}</div>
</div>
""", unsafe_allow_html=True)

if st.button("🎈 이 유형의 하루를 축하하기!", use_container_width=True):
    st.balloons()
    st.success(f"🎉 {selected}의 개성도 멋져요! 다른 유형과 달라도 괜찮아요.")

st.markdown("""
<div class="card">
<b>🌈 기억해 주세요</b><br><br>
MBTI는 사람을 16개의 상자로 나누는 정답표가 아니에요.
같은 MBTI라도 자라온 환경, 경험, 가치관에 따라 모습은 크게 다를 수 있어요.
</div>
""", unsafe_allow_html=True)
