import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Constants
equipment_cost_per_room = 4500
daily_income_per_room = 10
monthly_income_per_room = daily_income_per_room * 30
electricity_cost_per_month = 3.02
refill_cost_per_month = 250
total_monthly_cost = electricity_cost_per_month + refill_cost_per_month
net_monthly_profit_per_room = monthly_income_per_room - total_monthly_cost

# Page config for mobile responsiveness
st.set_page_config(
    page_title="ROI Calculator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Mobile-friendly styling
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    h1, h2, h3 {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("📈 New-Gen Biotics ROI Calculator")
st.markdown("""
Easily estimate ROI for installing New‑Gen Biotics probiotic air machines in your hotel rooms.
""")

# User input
num_rooms = st.number_input("How many hotel rooms?", min_value=1, value=10, step=1)
include_costs = st.toggle("Include monthly operating costs (electricity + refill)?", value=True)

# Calculations
total_equipment_cost = equipment_cost_per_room * num_rooms
monthly_income_total = monthly_income_per_room * num_rooms
monthly_costs_total = total_monthly_cost * num_rooms if include_costs else 0
net_monthly_profit_total = monthly_income_total - monthly_costs_total

payoff_time_months = total_equipment_cost / net_monthly_profit_total if net_monthly_profit_total > 0 else float('inf')
payoff_time_years = payoff_time_months / 12

# Display results
st.subheader("📊 ROI Summary")

st.metric("Total Equipment Cost", f"${total_equipment_cost:,.0f}")
st.metric("Monthly Income", f"${monthly_income_total:,.0f}")
st.metric("Monthly Costs", f"${monthly_costs_total:,.0f}")
st.metric("Net Monthly Profit", f"${net_monthly_profit_total:,.0f}")

if payoff_time_months != float('inf'):
    st.markdown(f"**Estimated Payoff Time:** `{payoff_time_months:.1f} months` (~{payoff_time_years:.1f} years)")
else:
    st.markdown("**Estimated Payoff Time:** Not profitable with current inputs")

# ROI Graph
months = np.arange(1, 37)
cumulative_profit = (net_monthly_profit_total) * months
payoff_line = np.full_like(months, total_equipment_cost)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(months, cumulative_profit, label='Cumulative Profit', linewidth=2)
ax.plot(months, payoff_line, 'r--', label='Break-Even Point')
ax.set_xlabel('Months')
ax.set_ylabel('Dollars ($)')
ax.set_title(f'ROI Projection ({num_rooms} Room(s))')
ax.legend()
ax.grid(True)

st.pyplot(fig, use_container_width=Tr
