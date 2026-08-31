import streamlit as st

st.set_page_config(
    page_title="나에게 맞는 진로 찾기 🌱",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

MBTI_DATA = {
    "ISTJ": {
        "name": "신중한 현실주의자", "emoji": "📋",
        "description": "책임감이 강하고 꼼꼼하며, 정해진 목표를 차근차근 이루어가는 것을 좋아해요.",
        "strengths": ["책임감", "꼼꼼함", "계획성", "성실함"],
        "jobs": [
            ("회계사", "💰", "숫자와 자료를 꼼꼼하게 분석하고 기업이나 개인의 재무 상태를 관리하는 직업이에요."),
            ("공무원", "🏛️", "정해진 절차와 규정을 바탕으로 사회에 필요한 행정 서비스를 제공해요."),
            ("품질관리원", "🔍", "제품이나 서비스가 정해진 기준을 충족하는지 확인하고 품질을 개선해요.")
        ]},
    "ISFJ": {
        "name": "따뜻한 조력자", "emoji": "🤝",
        "description": "다른 사람을 세심하게 배려하고, 맡은 일을 책임감 있게 해내는 편이에요.",
        "strengths": ["배려심", "성실함", "관찰력", "책임감"],
        "jobs": [
            ("상담심리사", "💬", "사람들의 이야기를 경청하고 자신의 감정과 고민을 이해하도록 돕는 일을 해요."),
            ("간호사", "🩺", "환자의 건강 상태를 살피고 치료와 회복을 돕는 중요한 역할을 해요."),
            ("사회복지사", "🌱", "도움이 필요한 사람들이 더 안정적인 생활을 할 수 있도록 지원해요.")
        ]},
    "INFJ": {
        "name": "의미를 찾는 조언자", "emoji": "🌙",
        "description": "사람의 마음을 깊이 이해하고 의미 있는 변화를 만들어내는 것에 관심이 많아요.",
        "strengths": ["공감능력", "통찰력", "창의성", "가치관"],
        "jobs": [
            ("상담교사", "🧠", "학생들의 고민과 학교생활을 살펴보고 정서적·진로적 성장을 지원해요."),
            ("작가", "✍️", "자신의 생각과 이야기를 글로 표현하며 독자에게 새로운 관점과 감정을 전달해요."),
            ("교육기획자", "📚", "사람들의 성장과 학습을 돕는 교육 프로그램과 콘텐츠를 기획해요.")
        ]},
    "INTJ": {
        "name": "전략을 설계하는 사람", "emoji": "♟️",
        "description": "복잡한 문제를 분석하고 장기적인 계획을 세워 목표를 달성하는 것을 좋아해요.",
        "strengths": ["분석력", "전략적 사고", "독립성", "문제해결력"],
        "jobs": [
            ("데이터 분석가", "📊", "데이터에서 의미 있는 패턴을 발견하고 이를 바탕으로 문제 해결을 지원해요."),
            ("소프트웨어 개발자", "💻", "프로그램과 서비스를 설계하고 코드를 작성해 새로운 기능을 만들어내요."),
            ("연구원", "🔬", "특정 분야의 질문을 탐구하고 새로운 지식과 해결 방법을 찾아요.")
        ]},
    "ISTP": {
        "name": "문제를 해결하는 탐험가", "emoji": "🛠️",
        "description": "직접 관찰하고 실험하면서 현실적인 문제를 해결하는 것을 좋아해요.",
        "strengths": ["실용성", "논리력", "관찰력", "문제해결력"],
        "jobs": [
            ("기계공학자", "⚙️", "기계의 원리를 연구하고 실제 제품과 시스템을 설계하고 개선해요."),
            ("항공정비사", "✈️", "항공기의 상태를 점검하고 안전하게 운항할 수 있도록 정비해요."),
            ("소방관", "🚒", "화재와 재난 현장에서 사람을 구조하고 안전을 지키는 일을 해요.")
        ]},
    "ISFP": {
        "name": "감각적인 창작자", "emoji": "🎨",
        "description": "자신만의 감각과 가치관을 중요하게 생각하며 현재의 경험을 풍부하게 즐기는 편이에요.",
        "strengths": ["감각", "공감능력", "창의성", "유연함"],
        "jobs": [
            ("디자이너", "🎨", "색, 형태, 이미지 등을 활용해 사람들이 사용할 수 있는 다양한 디자인을 만들어요."),
            ("사진작가", "📷", "사진을 통해 순간과 이야기를 기록하고 자신만의 시각을 표현해요."),
            ("플로리스트", "💐", "꽃과 식물을 활용해 공간이나 행사의 분위기를 아름답게 연출해요.")
        ]},
    "INFP": {
        "name": "가치를 중요하게 생각하는 이상주의자", "emoji": "🌷",
        "description": "자신만의 가치관과 상상력을 중요하게 생각하며 사람과 세상에 긍정적인 영향을 주고 싶어 해요.",
        "strengths": ["공감능력", "창의성", "상상력", "가치관"],
        "jobs": [
            ("콘텐츠 기획자", "💡", "사람들에게 전달할 이야기와 콘텐츠를 기획하고 새로운 아이디어를 발전시켜요."),
            ("작가", "📖", "상상력과 생각을 글로 표현해 사람들에게 새로운 경험을 전달해요."),
            ("사회복지사", "🤲", "사회적 도움이 필요한 사람들의 상황을 이해하고 필요한 지원을 연결해요.")
        ]},
    "INTP": {
        "name": "호기심 많은 탐구자", "emoji": "🧪",
        "description": "새로운 원리와 아이디어를 탐구하고 '왜 그럴까?'라는 질문을 깊게 파고드는 편이에요.",
        "strengths": ["논리적 사고", "호기심", "창의성", "분석력"],
        "jobs": [
            ("과학자", "🔬", "자연과 사회의 원리를 탐구하고 새로운 지식을 발견하는 일을 해요."),
            ("AI 연구원", "🤖", "인공지능의 원리와 기술을 연구하고 새로운 AI 시스템을 개발해요."),
            ("프로그래머", "💻", "논리적인 사고를 활용해 프로그램과 서비스를 설계하고 구현해요.")
        ]},
    "ESTP": {
        "name": "행동력 있는 해결사", "emoji": "⚡",
        "description": "빠르게 상황을 파악하고 직접 행동하면서 문제를 해결하는 것을 좋아해요.",
        "strengths": ["행동력", "적응력", "현실감각", "사교성"],
        "jobs": [
            ("기업가", "🚀", "새로운 사업 아이디어를 실행하고 사람과 자원을 활용해 가치를 만들어내요."),
            ("영업 전문가", "📣", "고객의 필요를 파악하고 제품이나 서비스의 가치를 효과적으로 전달해요."),
            ("이벤트 기획자", "🎪", "행사와 이벤트의 전체 과정을 기획하고 현장에서 직접 운영해요.")
        ]},
    "ESFP": {
        "name": "즐거움을 만드는 사람", "emoji": "🎉",
        "description": "사람들과 어울리는 것을 좋아하고 주변에 즐거운 에너지를 전달하는 편이에요.",
        "strengths": ["사교성", "긍정성", "적응력", "표현력"],
        "jobs": [
            ("방송인", "🎤", "자신의 표현력과 소통 능력을 활용해 사람들에게 정보와 즐거움을 전달해요."),
            ("이벤트 기획자", "🎡", "사람들이 즐길 수 있는 축제와 행사를 기획하고 운영해요."),
            ("서비스 매니저", "😊", "고객의 경험을 개선하고 사람들이 만족할 수 있는 서비스를 만들어가요.")
        ]},
    "ENFP": {
        "name": "아이디어가 넘치는 활동가", "emoji": "✨",
        "description": "새로운 가능성을 발견하는 것을 좋아하고 사람들과 아이디어를 나누는 것을 즐겨요.",
        "strengths": ["창의성", "소통능력", "열정", "호기심"],
        "jobs": [
            ("마케팅 기획자", "📢", "사람들의 관심과 필요를 파악하고 재미있고 효과적인 마케팅 전략을 만들어가요."),
            ("광고기획자", "💡", "제품과 브랜드를 효과적으로 알릴 수 있는 광고 아이디어와 캠페인을 기획해요."),
            ("콘텐츠 크리에이터", "🎬", "자신만의 아이디어를 영상, 글, 이미지 등의 콘텐츠로 만들어 사람들과 공유해요.")
        ]},
    "ENTP": {
        "name": "새로운 가능성을 찾는 발명가", "emoji": "💡",
        "description": "기존의 방법에 의문을 던지고 새로운 아이디어와 해결 방법을 찾아내는 것을 좋아해요.",
        "strengths": ["창의성", "논리력", "토론능력", "문제해결력"],
        "jobs": [
            ("창업가", "🚀", "새로운 아이디어를 사업으로 발전시키고 변화하는 시장에서 기회를 찾아요."),
            ("기획자", "🧩", "문제를 분석하고 새로운 서비스나 프로젝트의 방향을 설계해요."),
            ("변호사", "⚖️", "논리적인 근거를 바탕으로 법적 문제를 분석하고 해결 방법을 제시해요.")
        ]},
    "ESTJ": {
        "name": "체계적인 리더", "emoji": "📌",
        "description": "목표를 분명하게 세우고 사람과 자원을 효율적으로 조직하는 능력이 뛰어난 편이에요.",
        "strengths": ["리더십", "실행력", "책임감", "조직력"],
        "jobs": [
            ("경영자", "🏢", "조직의 목표를 세우고 사람과 자원을 관리하며 성과를 만들어가요."),
            ("프로젝트 매니저", "📋", "프로젝트의 일정과 인력을 관리하고 목표한 결과를 만들어내도록 조율해요."),
            ("공무원", "🏛️", "행정 업무를 체계적으로 수행하며 시민들에게 필요한 공공 서비스를 제공해요.")
        ]},
    "ESFJ": {
        "name": "사람을 연결하는 조력자", "emoji": "💛",
        "description": "사람들과 협력하는 것을 좋아하고 주변 사람들의 필요를 세심하게 살피는 편이에요.",
        "strengths": ["협동심", "공감능력", "소통능력", "책임감"],
        "jobs": [
            ("교사", "👩‍🏫", "학생들의 학습과 성장을 돕고 학교에서 다양한 사람들과 협력해요."),
            ("상담사", "💬", "사람들의 이야기를 듣고 고민을 정리하며 더 나은 방향을 찾도록 도와요."),
            ("인사담당자", "👥", "조직의 구성원을 지원하고 채용과 교육 등 사람과 관련된 업무를 담당해요.")
        ]},
    "ENFJ": {
        "name": "사람의 성장을 돕는 리더", "emoji": "🌟",
        "description": "사람들의 가능성을 발견하고 함께 성장하도록 이끄는 데 강점을 보이는 편이에요.",
        "strengths": ["리더십", "공감능력", "소통능력", "동기부여"],
        "jobs": [
            ("교사", "👩‍🏫", "학생들이 자신의 가능성을 발견하고 성장할 수 있도록 교육하고 격려해요."),
            ("상담심리사", "🧠", "사람의 이야기를 듣고 스스로 문제를 이해하고 해결할 수 있도록 지원해요."),
            ("조직문화 담당자", "🤝", "조직 구성원들이 서로 협력하고 성장할 수 있는 환경과 프로그램을 만들어요.")
        ]},
    "ENTJ": {
        "name": "목표를 이끄는 전략가", "emoji": "👑",
        "description": "명확한 목표를 세우고 사람들과 함께 계획을 실행해 결과를 만들어내는 것을 좋아해요.",
        "strengths": ["리더십", "전략적 사고", "추진력", "의사결정"],
        "jobs": [
            ("기업가", "🚀", "새로운 사업을 기획하고 조직을 이끌면서 아이디어를 실제 결과로 만들어가요."),
            ("경영 컨설턴트", "📈", "기업이 가진 문제를 분석하고 더 효과적인 전략과 해결책을 제안해요."),
            ("프로젝트 매니저", "🎯", "팀의 목표를 정하고 일정과 자원을 관리해 프로젝트를 성공적으로 이끌어요.")
        ]}
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
.stApp {
    background: radial-gradient(circle at 10% 10%, rgba(255,220,240,.55), transparent 25%),
                radial-gradient(circle at 90% 15%, rgba(210,235,255,.55), transparent 25%),
                linear-gradient(135deg,#fffaff 0%,#f7fbff 100%);
}
.block-container { max-width: 900px; padding-top: 2rem; padding-bottom: 4rem; }
.main-title { text-align:center; font-size:2.7rem; font-weight:800; letter-spacing:-2px; color:#202638; }
.sub-title { text-align:center; color:#687083; font-size:1.05rem; margin-bottom:2rem; }
.badge-wrapper { text-align:center; margin-bottom:1rem; }
.badge { display:inline-block; background:white; border:1px solid #ececf5; border-radius:999px; padding:7px 15px; font-size:.85rem; font-weight:600; color:#687083; box-shadow:0 5px 20px rgba(40,40,80,.06); }
.info-card,.type-card { background:rgba(255,255,255,.9); border:1px solid #ededf5; border-radius:22px; padding:22px 25px; margin:20px 0; box-shadow:0 10px 35px rgba(40,40,80,.07); }
.type-card { border-radius:26px; padding:28px; }
.type-emoji { font-size:3.2rem; }
.type-name { font-size:1.7rem; font-weight:800; color:#202638; }
.type-description { color:#687083; line-height:1.7; }
.strength { display:inline-block; background:#f5f5fb; border-radius:999px; padding:7px 13px; margin:4px; font-size:.85rem; font-weight:600; color:#555b70; }
.job-card { background:white; border:1px solid #ededf4; border-radius:20px; padding:21px; margin-bottom:13px; box-shadow:0 7px 24px rgba(40,40,80,.055); }
.job-title { font-size:1.15rem; font-weight:800; color:#252a3a; }
.job-description { color:#73798b; font-size:.91rem; line-height:1.65; margin-top:6px; }
.number-circle { display:inline-flex; align-items:center; justify-content:center; width:31px; height:31px; border-radius:50%; background:#f0f1f8; font-weight:800; margin-right:8px; }
.footer { text-align:center; color:#969bad; font-size:.82rem; margin-top:40px; padding-top:20px; border-top:1px solid #ececf3; }
.stButton > button { border-radius:13px; font-weight:700; border:1px solid #e6e7ef; min-height:45px; }
</style>
""", unsafe_allow_html=True)

if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.markdown("""
<div class="badge-wrapper"><span class="badge">🧭 청소년 진로탐색 프로그램</span></div>
<div class="main-title">나에게 어울리는 진로는? 🌱</div>
<div class="sub-title">MBTI를 바탕으로 나의 강점을 살펴보고<br>다양한 직업 아이디어를 만나보세요!</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
<b>💡 먼저 알아두세요</b><br><br>
MBTI는 나의 성향을 알아보는 하나의 방법이에요.
<b>MBTI만으로 진로를 결정할 수는 없어요.</b><br>
내가 좋아하는 것, 잘하는 것, 중요하게 생각하는 가치, 실제 경험 등을 함께 생각해 보는 것이 중요해요. 🌈
</div>
""", unsafe_allow_html=True)

st.markdown("### 🧩 나의 MBTI를 선택해 주세요")
selected = st.selectbox("MBTI", list(MBTI_DATA.keys()), label_visibility="collapsed")
data = MBTI_DATA[selected]

st.markdown(f"""
<div class="type-card">
<div class="type-emoji">{data["emoji"]}</div>
<div class="type-name">{selected} · {data["name"]}</div><br>
<div class="type-description">{data["description"]}</div><br>
<b>✨ 나에게 있을 수 있는 강점</b><br>
{"".join(f'<span class="strength">#{s}</span>' for s in data["strengths"])}
</div>
""", unsafe_allow_html=True)

st.markdown("### 💼 이런 직업을 탐색해 보세요")
st.caption("아래 추천은 '가능성이 있는 진로 아이디어'를 제시하는 것이며, 적성을 단정하는 것은 아니에요.")

for i, (title, emoji, desc) in enumerate(data["jobs"], 1):
    st.markdown(f"""
    <div class="job-card">
      <div class="job-title"><span class="number-circle">{i}</span>{emoji} {title}</div>
      <div class="job-description">{desc}</div>
    </div>
    """, unsafe_allow_html=True)
    if title in st.session_state.favorites:
        st.success(f"❤️ 관심 직업으로 저장됨: {title}")
    elif st.button(f"❤️ {title} 관심 직업으로 저장", key=f"save_{selected}_{i}"):
        st.session_state.favorites.append(title)
        st.toast(f"❤️ {title}을(를) 관심 직업에 저장했어요!")
        st.rerun()

if st.session_state.favorites:
    st.markdown("### ❤️ 내가 저장한 관심 직업")
    st.markdown(f'<div class="info-card">{"　".join(f"🔖 **{x}**" for x in st.session_state.favorites)}</div>', unsafe_allow_html=True)
    if st.button("🗑️ 관심 직업 초기화"):
        st.session_state.favorites = []
        st.rerun()

st.markdown("---")
st.markdown("### 🔎 이제 한 번 생각해 볼까요?")
question = st.selectbox("질문을 선택해 보세요.", [
    "질문을 선택하세요",
    "나는 어떤 활동을 할 때 시간이 빨리 지나갈까?",
    "사람들과 함께할 때와 혼자 할 때, 언제 더 편할까?",
    "내가 다른 사람보다 쉽게 잘하는 것은 무엇일까?",
    "돈보다 더 중요하게 생각하는 것은 무엇일까?",
    "10년 뒤 어떤 모습으로 살아가고 싶을까?"
])

if question != "질문을 선택하세요":
    st.markdown(f"""
    <div class="info-card">
    💭 <b>{question}</b><br><br>
    ✏️ 답을 바로 정하지 않아도 괜찮아요. 학교생활, 동아리, 취미, 봉사활동 등에서
    나의 모습을 관찰하면서 천천히 찾아보세요.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="footer">
🌱 나의 진로는 하나의 정답이 아니라 여러 가능성 중 하나예요.<br>
MBTI는 진로 선택의 참고 자료로만 활용하고, 다양한 경험을 통해 나에게 맞는 길을 찾아보세요. 💛
</div>
""", unsafe_allow_html=True)
