import streamlit as st

st.title("💰 PocketSmart AI")
st.subheader("Smart Budget & Recommendation")

name = st.text_input("Enter your name")
income = st.number_input("Enter monthly income (₹)", min_value=0.0)

st.write("### Expense Categories")

food = st.number_input("Food expenses (₹)", min_value=0.0)
travel = st.number_input("Travel expenses (₹)", min_value=0.0)
shopping = st.number_input("Shopping expenses (₹)", min_value=0.0)
education = st.number_input("Education expenses (₹)", min_value=0.0)
other = st.number_input("Other expenses (₹)", min_value=0.0)

if st.button("Calculate Budget"):
    total_expenses = food + travel + shopping + education + other
    balance = income - total_expenses

    st.write("---")
    st.write(f"### Total Expenses: ₹{total_expenses:.2f}")
    st.write(f"### Remaining Balance: ₹{balance:.2f}")

    st.write("### 🤖 AI Recommendation")

    if balance > 0:
        savings = balance * 0.40
        st.success("💡 Good financial management! Keep saving regularly.")
        st.write(f"Recommended Monthly Savings: ₹{savings:.2f}")
    elif balance == 0:
        st.warning("⚠️ Your expenses equal your income. Try to reduce some expenses.")
    else:
        st.error("🚨 Your expenses are higher than your income. Please reduce spending.")
