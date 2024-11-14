import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style('white')
sns.set_palette('tab10')
bluecolor=sns.color_palette('tab10')[0]
orangecolor=sns.color_palette('tab10')[1]
plt.rcParams.update({'font.size': 22})  # Adjust '14' to your desired font size
side_text_size = 30
top_bar_values_size = 18

# ### --- badnet cifar10 ---
# save_name = "cifar10_badnet"
# Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success = [0.00, 0.00, 0.10, 0.00, 68.80]  # Poison Success (%) values
# test_accuracy = [91.77, 92.96, 17.45, 81.66, 91.24]  # Test Accuracy (%) values
# avg_final_acc = 92.15 

# # Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("cifar10_badnet.png", dpi=800)

### --- badnet cifar100 ---
# save_name = "cifar100_badnet"
# # Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success = [0.00, 0.00, 0.00, 0.00, 99.00]  # Poison Success (%) values
# test_accuracy = [72.58, 74.26, 11.87, 72.63, 73.04]  # Test Accuracy (%) values
# avg_final_acc = 73.45


# # Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("cifar100_badnet.png", dpi=800)

### --- badnet imagenette ---
save_name = "imagenette_badnet"
# Data from the user
methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
poison_success = [0.26, 0.52, 0.00, 44.30, 85.49]  # Poison Success (%) values
test_accuracy = [80.20, 84.71, 48.25, 33.86, 74.39]  # Test Accuracy (%) values
avg_final_acc = 81.14


# # Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("imagenette_badnet.png", dpi=800)

### --- cifar10_frequency ---
# save_name = "cifar10_frequency"
# # Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success = [0.00, 0.00, 0.00, 0.00, 6.50]  # Poison Success (%) values
# test_accuracy = [90.38, 92.45, 75.87, 75.61, 91.33]  # Test Accuracy (%) values
# avg_final_acc = 92.15


# Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))
# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("cifar10_frequency.png", dpi=800)

### --- cifar100_frequency ---
# save_name = "cifar100_frequency"
# # Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success = [0.00, 0.00, 0.00, 0.00, 96.00]  # Poison Success (%) values
# test_accuracy = [71.35, 73.96, 57.70, 69.97, 73.77]  # Test Accuracy (%) values
# avg_final_acc = 73.45

# # Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))
# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("cifar100_frequency.png", dpi=800)

### --- imagenette_frequency ---
# save_name = "imagenette_frequency"
# # Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success = [0.00, 3.63, 0.52, 0.00, 46.63]  # Poison Success (%) values
# test_accuracy = [72.74, 79.87, 68.41, 50.98, 73.76]  # Test Accuracy (%) values
# avg_final_acc = 81.14

# # Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))

# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("imagenette_frequency.png", dpi=800)

### --- cifar10_wb ---
# save_name = "cifar10_wb"
# # Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success = [0.00, 0.00, 0.00, 0.00, 0.00]  # Poison Success (%) values
# test_accuracy = [91.21, 92.57, 81.27, 80.18, 90.76]  # Test Accuracy (%) values
# avg_final_acc = 92.15

# # Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))
# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("cifar10_wb.png", dpi=800)

### --- cifar100_wb ---
# save_name = "cifar100_wb"
# # Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success =[0.00, 0.00, 0.00, 0.00, 100.00]  # Poison Success (%) values
# test_accuracy = [72.25, 74.78, 72.56, 73.30, 75.19]  # Test Accuracy (%) values
# avg_final_acc = 73.45


# # Set up figure and axis for dual-axis bar plot
# fig, ax1 = plt.subplots(figsize=(10, 6))
# # Bar width
# bar_width = 0.45
# index = np.arange(len(methods))

# # Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)", color=bluecolor, fontsize=33)
# ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
# ax1.tick_params(axis='x', labelsize=22)
# ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# # Add labels on top of Test Accuracy bars
# for bar in bars1:
#     yval = bar.get_height()
#     ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Secondary y-axis for Poison Success
# ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
# ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
# ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

# ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=4)

# # Add labels on top of Poison Success bars
# for bar in bars2:
#     yval = bar.get_height()
#     ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=22)

# # Set x-axis labels and title
# plt.xticks(index + bar_width / 2, methods)
# #plt.title("Test Accuracy and Poison Success for Different Methods")
# plt.tight_layout()

# # Show the plot
# plt.savefig("cifar100_wb.png", dpi=800)

## --- (wb imagenette) ---
# save_name = "imagenette_wb.png"
# # Data from the user
# methods = ["EU", "CF", "SSD", "Scrub", "BadT"]
# poison_success = [0.00, 0.00, 0.00, 0.00, 100.00]  # Poison Success (%) values
# test_accuracy = [71.82, 78.68, 74.65, 40.36, 72.41]  # Test Accuracy (%) values
# avg_final_acc = 81.14

# badnet
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.45
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor)
# ax1.set_xlabel("Method", fontsize=33)
ax1.set_ylabel("Test Accuracy (%)\n(more accurate →)", color=bluecolor, fontsize=side_text_size)
ax1.locator_params(axis='y', tight=True, nbins=4)
ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
ax1.tick_params(axis='x', labelsize=22)
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=top_bar_values_size)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor)
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
ax2.locator_params(axis='y', tight=True, nbins=4)
ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=2) # 4

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=top_bar_values_size)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig(save_name, dpi=800)

"""
# frequency
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.45
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor)
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)\n(more accurate →)", color=bluecolor, fontsize=side_text_size)
ax1.locator_params(axis='y', tight=True, nbins=4)
ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
ax1.tick_params(axis='x', labelsize=22)
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=top_bar_values_size)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor)
# ax2.set_ylabel("Poison Success (%)", color=orangecolor, fontsize=33)
ax2.locator_params(axis='y', tight=True, nbins=4)
ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=2) # 4

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=top_bar_values_size)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig(save_name, dpi=800)
"""

# wichesbrew
"""
# Set up figure and axis for dual-axis bar plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.45
index = np.arange(len(methods))

# Plot Test Accuracy on the primary y-axis
# bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor, label='Test Accuracy (%)')
bars1 = ax1.bar(index, test_accuracy, bar_width, color=bluecolor)
# ax1.set_xlabel("Method", fontsize=33)
# ax1.set_ylabel("Test Accuracy (%)\n(more accurate →)", color=bluecolor, fontsize=side_text_size)
ax1.locator_params(axis='y', tight=True, nbins=4)
ax1.tick_params(axis='y', labelcolor=bluecolor, labelsize=22)
ax1.tick_params(axis='x', labelsize=22)
ax1.set_ylim(0, 100)  # Set limit to 100 for better comparison

# Add labels on top of Test Accuracy bars
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=top_bar_values_size)

# Secondary y-axis for Poison Success
ax2 = ax1.twinx()
bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor, label='Poison Success (%)')
# bars2 = ax2.bar(index + bar_width, poison_success, bar_width, color=orangecolor)
ax2.set_ylabel("Poison Success (%)\n(← better unlearning)", color=orangecolor, fontsize=side_text_size)
ax2.locator_params(axis='y', tight=True, nbins=4)
ax2.tick_params(axis='y', labelcolor=orangecolor, labelsize=22)
ax2.set_ylim(0, 100)  # Set limit to 100 for better comparison

ax1.axhline(avg_final_acc, color=bluecolor, linestyle='-.', label='Accuracy (Retraining)', linewidth=2) # 4

# Add labels on top of Poison Success bars
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}", ha='center', color='black', fontsize=top_bar_values_size)

# Set x-axis labels and title
plt.xticks(index + bar_width / 2, methods)
#plt.title("Test Accuracy and Poison Success for Different Methods")
plt.tight_layout()

# Show the plot
plt.savefig(save_name, dpi=800)
"""