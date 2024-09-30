import pandas as pd

##### BadNet CIFAR-10

# df = {
#     'Methods': [
#         'influence', 'threshold', 'frequency analysis', 'activation clustering', 'spectral signature', 'modify image', 'modify label'
#     ],
#     'Poisoning_Success_exp1': [0.0, 83.6, 18.3, 0.2, 0.0, 0.0, 0.2],
#     'Poisoning_Success_exp2': [0.0, 0.0, 66.7, 0.0, 0.3, 96.8, 0.0],
#     'Poisoning_Success_exp3': [1.2, 88.5, 4.0, 6.1, 2.3, 2.7, 0.9],
#     'Test_Accuracy_exp1': [91.95, 89.85, 91.29, 84.27, 89.54, 91.45, 90.56],
#     'Test_Accuracy_exp2': [91.77, 88.74, 91.53, 82.96, 90.52, 92.13, 89.48],
#     'Test_Accuracy_exp3': [91.09, 87.11, 90.81, 83.85, 90.69, 90.90, 87.69]
# }
# avg_initial_poison = (98.4 + 99.7 + 99.3) / 3
# avg_final_acc = 92.15
# name = 'badnet_cifar10'
# title = 'CIFAR-10 (BadNet)'
# df = pd.DataFrame(df)

##### BADNET CIFAR-100

# df = {
# 'Methods': [
#     "influence", "threshold", "frequency analysis", 
#     "activation clustering", "spectral signature", 
#     "modify image", "modify label"
# ],
# # Poisoning success rates and test accuracy extracted from the table
# 'Poisoning_Success_exp1': [0.0, 70.0, 1.0, 0.0, 0.0, 26.0, 0.0],
# 'Poisoning_Success_exp2': [0.0, 0.0, 15.0, 0.0, 6.0, 25.0, 0.0],
# 'Poisoning_Success_exp3': [0.0, 4.0, 11.0, 4.0, 33.0, 60.0, 2.0],
# 'Test_Accuracy_exp1': [72.58, 69.87, 71.3, 57.69, 62.85, 71.3, 67.97],
# 'Test_Accuracy_exp2': [71.76, 70.38, 70.54, 58.72, 60.73, 72.22, 67.42],
# 'Test_Accuracy_exp3': [72.10, 69.99, 70.59, 57.91, 62.36, 72.00, 70.75]
# }
# avg_initial_poison = (99.0 + 99.0 + 81.0) / 3
# avg_final_acc = 73.45
# name = 'badnet_cifar100'
# title = 'CIFAR-100 (BadNet)'
# df = pd.DataFrame(df)

##### Frequency-Based Trigger CIFAR-10

# methods_smooth_trigger = [
#     "influence", "threshold", "frequency analysis", 
#     "activation clustering", "spectral signature", 
#     "modify image", "modify label"
# ]

# # Poisoning success rates and test accuracy extracted from the table
# poisoning_success_exp1_smooth = [0.0, 0.1, 99.7, 13.4, 84.5, 99.6, 0.1]
# poisoning_success_exp2_smooth = [0.0, 0.0, 98.8, 8.1, 90.1, 99.3, 0.0]
# poisoning_success_exp3_smooth = [0.0, 0.0, 99.3, 5.5, 94.7, 98.9, 0.0]

# test_accuracy_exp1_smooth = [91.29, 86.92, 91.34, 84.04, 71.43, 91.5, 88.74]
# test_accuracy_exp2_smooth = [91.43, 87.8, 91.52, 86.52, 70.42, 91.99, 90.58]
# test_accuracy_exp3_smooth = [91.17, 86.77, 91.59, 85.15, 72.96, 91.96, 89.63]

# # 
# df = pd.DataFrame({
#     'Methods': methods_smooth_trigger,
#     'Poisoning_Success_exp1': poisoning_success_exp1_smooth,
#     'Poisoning_Success_exp2': poisoning_success_exp2_smooth,
#     'Poisoning_Success_exp3': poisoning_success_exp3_smooth,
#     'Test_Accuracy_exp1': test_accuracy_exp1_smooth,
#     'Test_Accuracy_exp2': test_accuracy_exp2_smooth,
#     'Test_Accuracy_exp3': test_accuracy_exp3_smooth
# })
# avg_initial_poison = (99.7 + 99.2 + 99.1) / 3
# avg_final_acc = 92.15
# name = 'frequency_cifar10'
# title = 'CIFAR-10 (Frequency Poisoning)'

##### Frequency-Based Trigger CIFAR-100


# methods_smooth_trigger_cifar100 = [
#     "influence", "threshold", "frequency analysis", 
#     "activation clustering", "spectral signature", 
#     "modify image", "modify label"
# ]

# # Poisoning success rates and test accuracy extracted from the table
# poisoning_success_exp1_smooth_cifar100 = [0.0, 23.0, 98.0, 0.0, 82.0, 96.0, 0.0]
# poisoning_success_exp2_smooth_cifar100 = [0.0, 3.0, 93.0, 0.0, 81.0, 97.0, 0.0]
# poisoning_success_exp3_smooth_cifar100 = [0.0, 0.0, 88.0, 0.0, 47.0, 91.0, 0.0]

# test_accuracy_exp1_smooth_cifar100 = [71.37, 67.54, 71.25, 58.49, 64.63, 72.08, 68.53]
# test_accuracy_exp2_smooth_cifar100 = [71.69, 66.59, 71.09, 59.70, 63.48, 72.60, 69.18]
# test_accuracy_exp3_smooth_cifar100 = [71.42, 68.34, 70.99, 58.70, 63.79, 72.99, 67.61]

# # Create the dataframe with the required structure
# df = pd.DataFrame({
#     'Methods': methods_smooth_trigger_cifar100,
#     'Poisoning_Success_exp1': poisoning_success_exp1_smooth_cifar100,
#     'Poisoning_Success_exp2': poisoning_success_exp2_smooth_cifar100,
#     'Poisoning_Success_exp3': poisoning_success_exp3_smooth_cifar100,
#     'Test_Accuracy_exp1': test_accuracy_exp1_smooth_cifar100,
#     'Test_Accuracy_exp2': test_accuracy_exp2_smooth_cifar100,
#     'Test_Accuracy_exp3': test_accuracy_exp3_smooth_cifar100
# })
# avg_initial_poison = (96.0 + 94.0 + 92.0) / 3
# avg_final_acc = 73.45
# name = 'frequency_cifar100'
# title = 'CIFAR-100 (Frequency Poisoning)'

##### Witches Brew-Based Trigger CIFAR-10

methods_witches_brew_cifar10 = [
    "influence", "threshold", 
    "frequency analysis", "activation clustering", 
    "spectral signature", "modify image", "modify label"
]

# Poisoning success rates and test accuracy extracted from the table
poisoning_success_exp1_witches_brew = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
poisoning_success_exp2_witches_brew = [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
poisoning_success_exp3_witches_brew = [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]
# for visualiation
poisoning_success_exp1_witches_brew = [x * 100 for x in poisoning_success_exp1_witches_brew]
poisoning_success_exp2_witches_brew = [x * 100 for x in poisoning_success_exp2_witches_brew]
poisoning_success_exp3_witches_brew = [x * 100 for x in poisoning_success_exp3_witches_brew]

test_accuracy_exp1_witches_brew = [91.21, 89.19, 91.71, 84.23, 80.92, 91.08, 89.07]
test_accuracy_exp2_witches_brew = [91.18, 88.48, 91.43, 83.79, 79.75, 91.56, 89.49]
test_accuracy_exp3_witches_brew = [90.70, 88.27, 91.35, 82.97, 79.08, 92.24, 88.78]

# Create the dataframe with the required structure
df = pd.DataFrame({
    'Methods': methods_witches_brew_cifar10,
    'Poisoning_Success_exp1': poisoning_success_exp1_witches_brew,
    'Poisoning_Success_exp2': poisoning_success_exp2_witches_brew,
    'Poisoning_Success_exp3': poisoning_success_exp3_witches_brew,
    'Test_Accuracy_exp1': test_accuracy_exp1_witches_brew,
    'Test_Accuracy_exp2': test_accuracy_exp2_witches_brew,
    'Test_Accuracy_exp3': test_accuracy_exp3_witches_brew
})

avg_initial_poison = 100.0 # for witches brew this is 100% cuz there is only one affected test point
avg_final_acc = 92.15
name = 'witches_brew_cifar10'
title = 'CIFAR-10 (Witche\'s Brew)'

# ##### Witches Brew-Based Trigger CIFAR-100
# Define the methods from the fifth table (witches brew - CIFAR100)
# methods_witches_brew_cifar100 = [
#     "influence", "threshold", 
#     "frequency analysis", "activation clustering", 
#     "spectral signature", "modify image", "modify label"
# ]

# # Poisoning success rates and test accuracy extracted from the table
# poisoning_success_exp1_witches_brew_cifar100 = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
# poisoning_success_exp2_witches_brew_cifar100 = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
# poisoning_success_exp3_witches_brew_cifar100 = [0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0]
# # for visualiation
# poisoning_success_exp1_witches_brew_cifar100 = [x * 100 for x in poisoning_success_exp1_witches_brew_cifar100]
# poisoning_success_exp2_witches_brew_cifar100 = [x * 100 for x in poisoning_success_exp2_witches_brew_cifar100]
# poisoning_success_exp3_witches_brew_cifar100 = [x * 100 for x in poisoning_success_exp3_witches_brew_cifar100]

# test_accuracy_exp1_witches_brew_cifar100 = [71.80, 67.19, 71.58, 62.49, 67.50, 72.18, 70.56]
# test_accuracy_exp2_witches_brew_cifar100 = [71.72, 67.18, 71.29, 60.48, 66.83, 71.96, 67.47]
# test_accuracy_exp3_witches_brew_cifar100 = [72.25, 68.37, 71.48, 61.47, 67.93, 71.88, 69.17]

# # Create the dataframe with the required structure
# df = pd.DataFrame({
#     'Methods': methods_witches_brew_cifar100,
#     'Poisoning_Success_exp1': poisoning_success_exp1_witches_brew_cifar100,
#     'Poisoning_Success_exp2': poisoning_success_exp2_witches_brew_cifar100,
#     'Poisoning_Success_exp3': poisoning_success_exp3_witches_brew_cifar100,
#     'Test_Accuracy_exp1': test_accuracy_exp1_witches_brew_cifar100,
#     'Test_Accuracy_exp2': test_accuracy_exp2_witches_brew_cifar100,
#     'Test_Accuracy_exp3': test_accuracy_exp3_witches_brew_cifar100
# })

# avg_initial_poison = 100.0
# avg_final_acc = 73.45
# name = 'witches_brew_cifar100'
# title = 'CIFAR-100 (Witche\'s Brew)'



df['Avg_Poisoning_Success'] = df[['Poisoning_Success_exp1', 'Poisoning_Success_exp2', 'Poisoning_Success_exp3']].mean(axis=1)
df['Avg_Test_Accuracy'] = df[['Test_Accuracy_exp1', 'Test_Accuracy_exp2', 'Test_Accuracy_exp3']].mean(axis=1)
print(df[['Methods', 'Avg_Poisoning_Success', 'Avg_Test_Accuracy']])


import matplotlib.pyplot as plt
import numpy as np

methods_dict = {
    'influence': 'Δ-Infl (Ours)',
    'threshold': 'EK-FAC', 
    'frequency analysis': 'FreqDef', 
    'activation clustering': 'ActClust', 
    'spectral signature': 'SpecSig'
}


# Data for plotting
df1 = df[df['Methods'].isin(['influence', 'threshold', 'frequency analysis', 'activation clustering', 'spectral signature'])]
methods = df1['Methods'].map(methods_dict)
avg_test_accuracy = df1['Avg_Test_Accuracy']
avg_poisoning_success = df1['Avg_Poisoning_Success']

x = np.arange(len(methods))  # the label locations
width = 0.35  # the width of the bars
plt.rcParams.update({'font.size': 15})

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting the Test Accuracy
bar1 = ax1.bar(x - width/2, avg_test_accuracy, width, label='Test Accuracy(%)', color='cornflowerblue')
ax1.set_xlabel('Methods')
ax1.set_ylabel('Test Accuracy(%)\n(more accurate →)', color='cornflowerblue')
ax1.set_ylim([0, 100])
ax1.set_xticks(x)
ax1.set_xticklabels(methods, rotation=45, ha="right")
ax1.tick_params(axis='y', labelcolor='cornflowerblue')

# Creating a second y-axis for Poisoning Success
ax2 = ax1.twinx()
bar2 = ax2.bar(x + width/2, avg_poisoning_success, width, label='Poison Success(%)', color='coral')
ax2.set_ylabel('Poison Success(%)\n(← better unlearning)', color='coral')
ax2.set_ylim([0, 100])
ax2.tick_params(axis='y', labelcolor='coral')


# Adding the lines at 98.9% for Poison Success and 92% for Test Accuracy
ax2.axhline(avg_initial_poison, color='red', linestyle='--', label='Poison Success (No unlearning)')
ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Adding the legend
#fig.legend(loc="upper right", bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

# Adding the values on top of the bars
for rect in bar1:
    height = rect.get_height()
    ax1.annotate(f'{height:.2f}', 
                 xy=(rect.get_x() + rect.get_width() / 2, height), 
                 xytext=(0, 3), 
                 textcoords="offset points", 
                 ha='center', va='bottom', color='black')

for rect in bar2:
    height = rect.get_height()
    ax2.annotate(f'{height:.2f}', 
                 xy=(rect.get_x() + rect.get_width() / 2, height), 
                 xytext=(0, 3), 
                 textcoords="offset points", 
                 ha='center', va='bottom', color='black')

plt.title(title)
plt.tight_layout()

# Display the plot
plt.savefig(f'{name}.png')


## Ablation
methods_dict = {
    'influence': 'Δ-Infl (Ours)',
    "modify image": 'Δ-Inf (Img-Only)', 
    "modify label": 'Δ-Inf (Label-Only)'
}

# Data for plotting
df1 = df[df['Methods'].isin(["influence", "modify image", "modify label"])]
methods = df1['Methods'].map(methods_dict)
avg_test_accuracy = df1['Avg_Test_Accuracy']
avg_poisoning_success = df1['Avg_Poisoning_Success']

x = np.arange(len(methods))  # the label locations
width = 0.2  # the width of the bars
plt.rcParams.update({'font.size': 15})

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting the Test Accuracy
bar1 = ax1.bar(x - width/2, avg_test_accuracy, width, label='Test Accuracy(%)', color='cornflowerblue')
ax1.set_xlabel('Methods')
ax1.set_ylabel('Test Accuracy(%)\n(more accurate →)', color='cornflowerblue')
ax1.set_ylim([0, 100])
ax1.set_xticks(x)
ax1.set_xticklabels(methods, rotation=45, ha="right")
ax1.tick_params(axis='y', labelcolor='cornflowerblue')

# Creating a second y-axis for Poisoning Success
ax2 = ax1.twinx()
bar2 = ax2.bar(x + width/2, avg_poisoning_success, width, label='Poison Success(%)', color='coral')
ax2.set_ylabel('Poison Success(%)\n(← better unlearning)', color='coral')
ax2.set_ylim([0, 100])
ax2.tick_params(axis='y', labelcolor='coral')


# Adding the lines at 98.9% for Poison Success and 92% for Test Accuracy
ax2.axhline(avg_initial_poison, color='red', linestyle='--', label='Poison Success (No unlearning)')
ax1.axhline(avg_final_acc, color='blue', linestyle='--', label='Accuracy (Retraining)')

# Adding the legend
#fig.legend(loc="upper right", bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)

# Adding the values on top of the bars
for rect in bar1:
    height = rect.get_height()
    ax1.annotate(f'{height:.2f}', 
                 xy=(rect.get_x() + rect.get_width() / 2, height), 
                 xytext=(0, 3), 
                 textcoords="offset points", 
                 ha='center', va='bottom', color='black')

for rect in bar2:
    height = rect.get_height()
    ax2.annotate(f'{height:.2f}', 
                 xy=(rect.get_x() + rect.get_width() / 2, height), 
                 xytext=(0, 3), 
                 textcoords="offset points", 
                 ha='center', va='bottom', color='black')

plt.title(title)
plt.tight_layout()

# Display the plot
plt.savefig(f'{name}_abl.png')