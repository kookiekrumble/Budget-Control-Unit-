import streamlit as st

# 1. Header & Welcome
st.title("💸 BUDGET CONTROL UNIT ")
st.write("Welcome! Enter your campus details below to check your balance.")

# 2. User Inputs (All set to BLANK or 0 by default)
student_name = st.text_input(
    "Yo! What's your name, my friend?", 
    value="", 
    placeholder="Enter your name...", 
    key="meal_name_user"
)

available_money = st.number_input(
    "How much cash/M-Pesa do you have right now (KSh)?", 
    min_value=0.0, 
    value=0.0, 
    step=10.0, 
    key="cash_input"
)

st.subheader("Plan Your Campus Day 🍽️")

# Blank Meal Input
meal_name = st.text_input(
    "What meal are you having today?", 
    value="", 
    placeholder="e.g. Chicken & Potato Wedges", 
    key="meal_name_input"
)
meal_price = st.number_input(
    "Cost of Meal (KSh):", 
    min_value=0.0, 
    value=0.0, 
    step=10.0, 
    key="meal_price_input"
)

# Blank Snack Input
snack_name = st.text_input(
    "What snack or drink are you getting?", 
    value="", 
    placeholder="e.g. Chocolate Bar", 
    key="snack_name_input"
)
snack_price = st.number_input(
    "Cost of Snack (KSh):", 
    min_value=0.0, 
    value=0.0, 
    step=10.0, 
    key="snack_price_input"
)

# Transport Cost
transport_cost = st.number_input(
    "Total transport fare for today (KSh):", 
    min_value=0.0, 
    value=0.0, 
    step=10.0, 
    key="transport_price_input"
)

st.subheader("🚨 Plot Twist Alert!")

# Blank Emergency Input
emergency_name = st.text_input(
    "What unexpected emergency did you face?", 
    value="", 
    placeholder="e.g. Printing Assignment", 
    key="emergency_name_input"
)
unexpected_expense = st.number_input(
    "Cost of Emergency (KSh):", 
    min_value=0.0, 
    value=0.0, 
    step=10.0, 
    key="emergency_price_input"
)

# 3. Calculate Button & Output
if st.button("Calculate Budget", type="primary"):
    if not student_name.strip():
        st.warning("Please enter your name first!")
    else:
        total_spending = meal_price + snack_price + transport_cost
        remaining_balance = available_money - total_spending
        five_day_spending = total_spending * 5
        final_balance = remaining_balance - unexpected_expense

        st.markdown("---")
        st.header(f"🧾 CAMPUS DAY RECEIPT FOR {student_name.upper()}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Starting Cash:** KSh {available_money:.2f}")
            st.write(f"**Meal ({meal_name if meal_name else 'Meal'}):** KSh {meal_price:.2f}")
            st.write(f"**Snack ({snack_name if snack_name else 'Snack'}):** KSh {snack_price:.2f}")
            st.write(f"**Transport Fare:** KSh {transport_cost:.2f}")
        
        with col2:
            st.write(f"**Total Daily Spent:** KSh {total_spending:.2f}")
            st.write(f"**5-Day Estimate:** KSh {five_day_spending:.2f}")
            st.write(f"**Emergency ({emergency_name if emergency_name else 'Emergency'}):** KSh {unexpected_expense:.2f}")
            st.write(f"**FINAL BALANCE:** KSh {final_balance:.2f}")

        if final_balance >= 0:
            st.success(f"Phew! You survived today, {student_name}! 😎")
        else:
            st.error(f"Uh oh, {student_name}... You are officially in the red! Time to hit up M-Shwari or call home 😅")
