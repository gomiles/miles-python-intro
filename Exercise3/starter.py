# Task Description:
# This exercise focuses on visualizing energy consumption data, a critical skill for power
# distribution and transmission professionals in the energy sector. You will work with a CSV
# file named 'energy_consumption_large_improved.csv' containing data with three columns: Date
# (in YYYY-MM-DD format), Zone (e.g., "Jebel Ali Zone"), and Energy_Consumption (in kWh, e.g.,
# 27500.45). The goal is to create a line plot to explore energy usage trends over time across
# different zones, helping to identify patterns and inform resource allocation and optimization.
# This task is highly relevant for roles like Assistant Manager - S/S Equip and Senior Engineer -
# Projects, who rely on visual data analysis to manage power systems effectively. The large
# dataset makes the exercise impressive, showcasing Python's ability to handle and visualize
# significant data, even for beginners.
#
# Steps to Complete:
# 1. Import the 'pandas' module for data manipulation and 'matplotlib.pyplot' for plotting.
# 2. Read the 'energy_consumption_large_improved.csv' file into a pandas DataFrame.
# 3. Pivot the data so each zone becomes a column, indexed by Date, with Energy_Consumption as values.
# 4. Create a line plot using the pivoted DataFrame, setting the figure size to (12, 6).
# 5. Add a title ('Energy Consumption per Zone Over Time') and label the axes ('Date' for x-axis,
#    'Energy Consumption' for y-axis).
# 6. Include a legend with the title 'Zone' to distinguish between zones.
# 7. Rotate x-axis labels by 45 degrees for readability and use tight_layout() to adjust spacing.
# 8. Display the plot using plt.show().
# 9. Test the script to ensure the line plot accurately represents the data, adjusting as needed
#    for clarity and visibility.

DATA_PATH = "./Exercise3/energy_consumption.csv"

#PUT SOLUTION HERE

