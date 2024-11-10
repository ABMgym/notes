import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 22})  # Adjust '14' to your desired font size

# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.00, 0.00, 0.10, 0.00, 68.80]  # Poison Success (%) values
test_accuracy = [91.77, 92.96, 17.45, 81.66, 91.24]  # Test Accuracy (%) values

avg_final_acc = 92.15 

# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("cifar10_badnet.png")


# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.00, 0.00, 0.00, 0.00, 99.00]  # Poison Success (%) values
test_accuracy = [72.58, 74.26, 11.87, 72.63, 73.04]  # Test Accuracy (%) values
avg_final_acc = 73.45
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("cifar100_badnet.png")

# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.26, 0.52, 0.00, 44.30, 85.49]  # Poison Success (%) values
test_accuracy = [80.20, 84.71, 48.25, 33.86, 74.39]  # Test Accuracy (%) values
avg_final_acc = 81.14
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("imagenette_badnet.png")

# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.00, 0.00, 0.00, 0.00, 6.50]  # Poison Success (%) values
test_accuracy = [90.38, 92.45, 75.87, 75.61, 91.33]  # Test Accuracy (%) values
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

avg_final_acc = 92.15

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("cifar10_frequency.png")


# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.00, 0.00, 0.00, 0.00, 96.00]  # Poison Success (%) values
test_accuracy = [71.35, 73.96, 57.70, 69.97, 73.77]  # Test Accuracy (%) values
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))
avg_final_acc = 73.45

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("cifar100_frequency.png")

# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.00, 3.63, 0.52, 0.00, 46.63]  # Poison Success (%) values
test_accuracy = [72.74, 79.87, 68.41, 50.98, 73.76]  # Test Accuracy (%) values
avg_final_acc = 81.14
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("imagenette_frequency.png")


# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.00, 0.00, 0.00, 0.00, 0.00]  # Poison Success (%) values
test_accuracy = [91.21, 92.57, 81.27, 80.18, 90.76]  # Test Accuracy (%) values
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))


avg_final_acc = 92.15

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("cifar10_wb.png")

# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success =[0.00, 0.00, 0.00, 0.00, 100.00]  # Poison Success (%) values
test_accuracy = [72.25, 74.78, 72.56, 73.30, 75.19]  # Test Accuracy (%) values
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

avg_final_acc = 73.45

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("cifar100_wb.png")

# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.00, 0.00, 0.00, 0.00, 100.00]  # Poison Success (%) values
test_accuracy = [71.82, 78.68, 74.65, 40.36, 72.41]  # Test Accuracy (%) values
avg_final_acc = 81.14
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.35
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color='dodgerblue', label='Test Accuracy (%)')
ax1.set_xlabel("Method")
ax1.set_ylabel("Test Accuracy (%)", color='dodgerblue')
ax1.tick_params(axis='y', labelcolor='dodgerblue')
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color='coral', label='Poison Success (%)')
ax2.set_ylabel("Poison Success (%)", color='coral')
ax2.tick_params(axis='y', labelcolor='coral')
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.2f}", ha='center', color='black', fontsize=16)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig("imagenette_wb.png")