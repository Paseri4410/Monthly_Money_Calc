import streamlit as st

st.title("清算アプリ")

# 毎月の共用口座への振り込み
MONTHLY_PERSON_A_TO_COMMON_CONST = (110000)
MONTHLY_PERSON_B_TO_COMMON_CONST = (90000)

Person_A = st.text_input("Aさんの名前を入力してください")
Person_B = st.text_input("Bさんの名前を入力してください")

# Aさんが個人で払ったけど、共用で払うべき金額
st.write(f"{Person_A}が個人で払ったけど、共用で払うべき金額")
PersonA_Paid_Receipt_num = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="PersonA_Paid"
)
PersonA_Paid_All = []
for PersonA_Paid_Receipt in range(PersonA_Paid_Receipt_num):
    PersonA_Paid = st.number_input(
        f"レシート{PersonA_Paid_Receipt + 1}",
        key = f"PersonA_Paid_{PersonA_Paid_Receipt + 1}",
        format = "%d"
    )
    PersonA_Paid_All.append(PersonA_Paid)
PersonA_Paid_Sum = sum(PersonA_Paid_All)


# Bさんが個人で払ったけど、共用で払うべき金額
st.write(f"{Person_B}が個人で払ったけど、共用で払うべき金額")
PersonB_Paid_Receipt_num = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="PersonB_Paid"
)
PersonB_Paid_All = []
for PersonB_Paid_Receipt in range(PersonB_Paid_Receipt_num):
    PersonB_Paid = st.number_input(
        f"レシート{PersonB_Paid_Receipt + 1}",
        key = f"PersonB_Paid_{PersonB_Paid_Receipt + 1}",
        format = "%d"
    )
    PersonB_Paid_All.append(PersonB_Paid)
PersonB_Paid_Sum = sum(PersonB_Paid_All)


# 共用で払ったけど、Aさんが個人で払うべき金額
st.write(f"共用で払ったけど、{Person_A}が個人で払うべき金額")
Common_Paid_Receipt_num_PersonA = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="Common_Paid_PersonA"
)
Common_Paid_All_PersonA = []
for Common_Paid_Receipt_PersonA in range(Common_Paid_Receipt_num_PersonA):
    Common_Paid_PersonA = st.number_input(
        f"レシート{Common_Paid_Receipt_PersonA + 1}",
        key = f"Common_Paid_PersonA_{Common_Paid_Receipt_PersonA + 1}",
        format = "%d"
    )
    Common_Paid_All_PersonA.append(Common_Paid_PersonA)
Common_Paid_Sum_PersonA = sum(Common_Paid_All_PersonA)


# 共用で払ったけど、Bさんが個人で払うべき金額
st.write(f"共用で払ったけど、{Person_B}が個人で払うべき金額")
Common_Paid_Receipt_num_PersonB = st.number_input(
    "レシートの枚数",
    min_value=0,
    value=0,
    step=1,
    key="Common_Paid_PersonB"
)
Common_Paid_All_PersonB = []
for Common_Paid_Receipt_PersonB in range(Common_Paid_Receipt_num_PersonB):
    Common_Paid_PersonB = st.number_input(
        f"レシート{Common_Paid_Receipt_PersonB + 1}",
        key = f"Common_Paid_PersonB_{Common_Paid_Receipt_PersonB + 1}",
        format = "%d"
    )
    Common_Paid_All_PersonB.append(Common_Paid_PersonB)
Common_Paid_Sum_PersonB = sum(Common_Paid_All_PersonB)


if st.button("計算"):
    thisMonth_PersonAToCommon = MONTHLY_PERSON_A_TO_COMMON_CONST - PersonA_Paid_Sum + Common_Paid_Sum_PersonA
    thisMonth_PersonBToCommon = MONTHLY_PERSON_B_TO_COMMON_CONST - PersonB_Paid_Sum + Common_Paid_Sum_PersonB
    st.success(f"今月、{Person_A}が振り込む金額：{thisMonth_PersonAToCommon} 円")
    st.success(f"今月、{Person_B}が振り込む金額：{thisMonth_PersonBToCommon} 円")


