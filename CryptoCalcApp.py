import streamlit as st

# Define the function
def calculate_investment_scenarios(total_investment, purchase_price, commission_percent, tp1_price, amount_taken_tp1, sl_tp2_price, initial_sl_price):
    # Calculate number of shares
    num_shares = total_investment // purchase_price
    # Calculate commission
    commission = total_investment * commission_percent / 100
    # Calculate break-even price
    break_even_price = (total_investment + 2 * commission) / num_shares
    # Calculate total value at TP1
    total_value_at_tp1 = num_shares * tp1_price
    # Calculate profit at TP1 before taking out partial
    profit_at_tp1 = total_value_at_tp1 - total_investment - commission
    # Calculate remaining shares after taking profit at TP1
    shares_sold_at_tp1 = amount_taken_tp1 / tp1_price
    remaining_shares = num_shares - shares_sold_at_tp1
    # Calculate remaining capital after TP1
    remaining_capital_after_tp1 = (total_value_at_tp1 - amount_taken_tp1) - commission
    # Calculate new total capital after TP2
    value_at_tp2 = remaining_shares * sl_tp2_price
    new_total_capital_after_tp2 = amount_taken_tp1 + value_at_tp2 - commission
    # Calculate theoretical profit if all sold at TP1
    theoretical_profit_all_tp1 = total_value_at_tp1 - total_investment - 2 * commission
    # Calculate net loss if initial SL is hit
    value_at_sl = num_shares * initial_sl_price
    net_loss_initial_sl = value_at_sl - total_investment - 2 * commission

    # Calculate total profit for TP1 and TP2 case
    profit_at_tp1_partial = amount_taken_tp1 - (shares_sold_at_tp1 * purchase_price) - commission
    profit_at_tp2 = value_at_tp2 - (remaining_shares * purchase_price) - commission
    total_profit_tp1_tp2 = profit_at_tp1_partial + profit_at_tp2

    return {
        "Break-even Price": break_even_price,
        "Net Loss @ SL": net_loss_initial_sl,
        "Profit If 100% Sold at TP1": theoretical_profit_all_tp1,
        "Profit (TP1 partial + TP2)": total_profit_tp1_tp2
    }

# Streamlit UI
st.title("Investment Scenarios Calculator")

# Collect inputs
total_investment = st.number_input("Total Investment", value=10000.0)
purchase_price = st.number_input("Purchase Price per Share", value=100.0)
commission_percent = st.number_input("Commission Percentage (%)", value=0.25)
tp1_price = st.number_input("TP1 Price per Share", value=200.0)
amount_taken_tp1 = st.number_input("Amount Taken Out at TP1", value=5000.0)
sl_tp2_price = st.number_input("TP2 Price per Share", value=220.0)
initial_sl_price = st.number_input("Initial SL Price per Share", value=45.0)

# Calculate when button is pressed
if st.button("Calculate"):
    results = calculate_investment_scenarios(
        total_investment, purchase_price, commission_percent, tp1_price, 
        amount_taken_tp1, sl_tp2_price, initial_sl_price
    )

    # Display results
    st.write("### Results:")
    for key, value in results.items():
        st.write(f"{key}: ${value:.2f}")
