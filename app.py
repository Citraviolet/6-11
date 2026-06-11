import streamlit as st
import random

st.set_page_config(
    page_title="랜덤 운세 뽑기",
    page_icon="🔮"
)

st.title("🔮 오늘의 운세")
st.write("이름을 입력하고 버튼을 눌러 오늘의 운세를 확인해 보세요!")

name = st.text_input("이름을 입력하세요")

fortunes = [
    "🍀 예상치 못한 행운이 찾아옵니다.",
    "📚 공부한 만큼 좋은 결과가 있을 것입니다.",
    "🤝 친구와의 관계에서 좋은 일이 생깁니다.",
    "🎯 새로운 도전을 시작하기 좋은 날입니다.",
    "😌 잠시 쉬어가며 재충전이 필요한 날입니다.",
    "😄 웃을 일이 많이 생기는 하루가 될 것입니다.",
    "🌟 누군가에게 칭찬을 받을 수 있습니다.",
    "🚀 평소 망설였던 일을 시작해 보세요.",
    "💡 좋은 아이디어가 떠오를 수 있습니다.",
    "🎁 뜻밖의 선물이나 기쁜 소식을 받을 수 있습니다."
]

lucky_colors = [
    "빨강", "파랑", "노랑", "초록",
    "보라", "주황", "하늘", "검정"
]

if st.button("🔮 운세 뽑기"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요!")
    else:
        grade = random.choice(["S", "A", "B", "C"])
        fortune = random.choice(fortunes)
        lucky_number = random.randint(1, 99)
        lucky_color = random.choice(lucky_colors)

        st.success(f"{name}님의 오늘의 운세 결과!")

        st.subheader(f"운세 등급 : {grade}")
        st.write(f"**오늘의 운세** : {fortune}")
        st.write(f"**행운의 숫자** : {lucky_number}")
        st.write(f"**행운의 색상** : {lucky_color}")

        if grade == "S":
            st.balloons()
