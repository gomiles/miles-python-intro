# Debugging Exercise: Incorrect Billing Adjustment for Peak Hours
# ---------------------------------------------------------------
# Purpose:
#   This script calculates adjusted energy consumption values over 5 hours.
#   During peak hours (hour 2 and 3 — using 0-based indexing), a 20% surcharge
#   should be applied to reflect higher energy rates.

# Input data: energy consumption in kWh per hour
consumption = [1000, 1200, 1500, 1300, 1100]

# Initialize an empty list to hold adjusted values
adjusted_consumption = []

# Loop through each hour's consumption and apply surcharge where needed
for hour in range(len(consumption)):
    # Intended logic: apply a 20% surcharge during peak hours (hour 2 and 3)
    # However, this condition does not behave as expected.
    if hour == 2 or hour == 3:
        adjusted = consumption[hour] * 1.2
    else:
        adjusted = consumption[hour]
    
    adjusted_consumption.append(adjusted)

# Calculate total adjusted consumption
total = sum(adjusted_consumption)

# ------------------------------
# 💡 STUDENT TASK
# ------------------------------
# 1. Read the code and understand what it's trying to do.
# 2. Compare the actual output with the expected output below.
# 3. Identify and fix the bug so the program behaves as intended.

# --------------------------------------
# ✅ Expected Output (correct behavior):
# Adjusted consumption per hour:
#   [1000, 1200, 1800.0, 1560.0, 1100]
# Total adjusted consumption:
#   6660.0 kWh
#
# Print the result
print("Adjusted consumption per hour:", adjusted_consumption)
print("Total adjusted consumption:", total)
