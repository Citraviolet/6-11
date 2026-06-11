import streamlit as st
import random

st.set_page_config(page_title="오늘의 운세", page_icon="🔮")

st.title("🔮 오늘의 운세")
st.write("이름을 입력하고 운세를 확인해 보세요!")

name = st.text_input("이름")

fortune_data = {
    "S": [
        "최고의 하루가 예상됩니다. 자신 있게 도전해 보세요!",
        "뜻밖의 행운이 찾아올 수 있습니다.",
        "노력한 일에서 좋은 결과를 얻을 가능성이 높습니다."
    ],
    "A": [
        "기분 좋은 일이 생길 수 있는 날입니다.",
        "주변 사람들과의 관계가 순조롭게 흘러갑니다.",
        "새로운 기회를 발견할 수 있습니다."
    ],
    "B": [
        "평범하지만 안정적인 하루가 될 것입니다.",
        "작은 성취가 쌓여 좋은 결과로 이어집니다.",
        "차분하게 행동하면 좋은 일이 생깁니다."
    ],
    "C": [
        "서두르지 말고 신중하게 행동하세요.",
        "작은 실수가 생길 수 있으니 확인이 필요합니다.",
        "무리하기보다 휴식을 챙기는 것이 좋습니다."
    ]
}

lucky_colors = ["빨강", "파랑", "초록", "노랑", "보라", "주황"]

if st.button("운세 보기"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요.")
    else:
        # 같은 이름이면 항상 같은 결과가 나오도록 설정
        random.seed(name)

        grade = random.choices(
            ["S", "A", "B", "C"],
            weights=[10, 25, 40, 25]
        )[0]

        fortune = random.choice(fortune_data[grade])
        lucky_number = random.randint(1, 99)
        lucky_color = random.choice(lucky_colors)

        st.subheader(f"✨ {name}님의 오늘의 운세 ✨")
        st.write(f"### 운세 등급 : {grade}")
        st.write(f"📜 {fortune}")
        st.write(f"🔢 행운의 숫자 : {lucky_number}")
        st.write(f"🎨 행운의 색상 : {lucky_color}")

        if grade == "S":
            st.balloons()
