import streamlit as st

st.title("清算アプリ")

# 毎月の共用口座への振り込み
MONTHLY_YOSHITO_TO_COMMON_CONST = (110000)
MONTHLY_YUINO_TO_COMMON_CONST = (90000)


# 香斗が個人で払ったけど、共用で払うべき金額
st.header("香斗が個人で払ったけど、共用で払うべき金額")
Yoshito_Paid_Receipt_num = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="Yoshito_Paid"
)
Yoshito_Paid_All = []
for Yoshito_Paid_Receipt in range(Yoshito_Paid_Receipt_num):
    Yoshito_Paid = st.number_input(
        f"レシート{Yoshito_Paid_Receipt + 1}",
        key = f"Yoshito_Paid_{Yoshito_Paid_Receipt + 1}"
    )
    Yoshito_Paid_All.append(Yoshito_Paid)
Yoshito_Paid_Sum = sum(Yoshito_Paid_All)


# 唯乃が個人で払ったけど、共用で払うべき金額
st.header("唯乃が個人で払ったけど、共用で払うべき金額")
Yuino_Paid_Receipt_num = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="Yuino_Paid"
)
Yuino_Paid_All = []
for Yuino_Paid_Receipt in range(Yuino_Paid_Receipt_num):
    Yuino_Paid = st.number_input(
        f"レシート{Yuino_Paid_Receipt + 1}",
        key = f"Yuino_Paid_{Yuino_Paid_Receipt + 1}"
    )
    Yuino_Paid_All.append(Yuino_Paid)
Yuino_Paid_Sum = sum(Yuino_Paid_All)


# 共用で払ったけど、香斗が個人で払うべき金額
st.header("共用で払ったけど、香斗が個人で払うべき金額")
Common_Paid_Receipt_num_Yoshito = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="Common_Paid_Yoshito"
)
Common_Paid_All_Yoshito = []
for Common_Paid_Receipt_Yoshito in range(Common_Paid_Receipt_num_Yoshito):
    Common_Paid_Yoshito = st.number_input(
        f"レシート{Common_Paid_Receipt_Yoshito + 1}",
        key = f"Common_Paid_Yoshito_{Common_Paid_Receipt_Yoshito + 1}"
    )
    Common_Paid_All_Yoshito.append(Common_Paid_Yoshito)
Common_Paid_Sum_Yoshito = sum(Common_Paid_All_Yoshito)


# 共用で払ったけど、唯乃が個人で払うべき金額
st.header("共用で払ったけど、唯乃が個人で払うべき金額")
Common_Paid_Receipt_num_Yuino = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="Common_Paid_Yuino"
)
Common_Paid_All_Yuino = []
for Common_Paid_Receipt_Yuino in range(Common_Paid_Receipt_num_Yuino):
    Common_Paid_Yuino = st.number_input(
        f"レシート{Common_Paid_Receipt_Yuino + 1}",
        key = f"Common_Paid_Yuino_{Common_Paid_Receipt_Yuino + 1}"
    )
    Common_Paid_All_Yuino.append(Common_Paid_Yuino)
Common_Paid_Sum_Yuino = sum(Common_Paid_All_Yuino)


if st.button("計算"):
    thisMonth_YoshitoToCommon = MONTHLY_YOSHITO_TO_COMMON_CONST - Yoshito_Paid_Sum + Common_Paid_Sum_Yoshito
    thisMonth_YuinoToCommon = MONTHLY_YUINO_TO_COMMON_CONST - Yuino_Paid_Sum + Common_Paid_Sum_Yuino
    st.success(f"今月、香斗が振り込む金額：{thisMonth_YoshitoToCommon} 円")
    st.success(f"今月、唯乃が振り込む金額：{thisMonth_YuinoToCommon} 円")


