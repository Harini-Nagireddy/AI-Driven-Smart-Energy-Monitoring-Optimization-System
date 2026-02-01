import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Energy Optimizer", layout="wide")

st.title("⚡ Smart Energy Monitoring & Optimization System")

# ---------------- USER INPUTS ----------------
st.sidebar.header("🏠 Household Inputs")

ac_count = st.sidebar.number_input("Number of ACs", 0, 10, 1)
ac_hours = st.sidebar.slider("AC usage (hours/day)", 0, 24, 6)

fridge = st.sidebar.selectbox("Refrigerator", ["Yes", "No"])
wm_uses = st.sidebar.slider("Washing Machine uses/week", 0, 14, 3)

lights = st.sidebar.number_input("Number of Lights", 0, 50, 8)
fans = st.sidebar.number_input("Number of Fans", 0, 20, 4)

rate = st.sidebar.number_input("Electricity rate (₹/unit)", 1.0, 20.0, 6.0)

# ---------------- ENERGY LOGIC ----------------
AC_POWER = 1.5        # kWh per hour
FRIDGE_DAILY = 1.2
WM_PER_USE = 0.8
LIGHT_PER_DAY = 0.05
FAN_PER_DAY = 0.07

ac_energy = ac_count * ac_hours * AC_POWER * 30
fridge_energy = FRIDGE_DAILY * 30 if fridge == "Yes" else 0
wm_energy = wm_uses * WM_PER_USE * 4
light_energy = lights * LIGHT_PER_DAY * 30
fan_energy = fans * FAN_PER_DAY * 30

total_energy = ac_energy + fridge_energy + wm_energy + light_energy + fan_energy
bill = total_energy * rate

# ---------------- DASHBOARD ----------------
st.subheader("📊 Energy Summary")

col1, col2 = st.columns(2)
col1.metric("Monthly Consumption (kWh)", f"{total_energy:.2f}")
col2.metric("Estimated Bill (₹)", f"₹ {bill:.2f}")

# Appliance-wise chart
st.subheader("🔌 Appliance-wise Consumption")

appliance_df = pd.DataFrame({
    "Appliance": ["AC", "Refrigerator", "Washing Machine", "Lights", "Fans"],
    "Energy (kWh)": [
        ac_energy,
        fridge_energy,
        wm_energy,
        light_energy,
        fan_energy
    ]
})

fig, ax = plt.subplots()
ax.bar(appliance_df["Appliance"], appliance_df["Energy (kWh)"])
ax.set_ylabel("kWh / Month")
st.pyplot(fig)

# ---------------- FUTURE PREDICTION ----------------
st.subheader("🔮 Next Month Prediction")

future_energy = total_energy * np.random.uniform(0.95, 1.08)
future_bill = future_energy * rate

st.success(f"🔹 Predicted Consumption: **{future_energy:.2f} kWh**")
st.success(f"🔹 Predicted Bill: **₹ {future_bill:.2f}**")

# ---------------- OPTIMIZATION ----------------
st.subheader("💡 Optimization Suggestions")

tips = []

if ac_hours > 8:
    tips.append("Reduce AC usage by 1–2 hours/day to save ~₹500/month.")

if lights > 10:
    tips.append("Switch to LED lights to cut lighting cost by 60%.")

if fans > 6:
    tips.append("Turn off fans in unused rooms.")

if fridge == "Yes":
    tips.append("Keep refrigerator door closed and temperature optimal.")

if not tips:
    tips.append("Your usage is already optimized 👍")

for t in tips:
    st.write("✔️", t)
