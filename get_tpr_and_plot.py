import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import seaborn as sns

##### BadNet- CIFAR10
data = {
    'Methods': ['influence', 'threshold', 'frequency analysis', 'activation clustering', 'spectral signature', 'modify image', 'modify label'],
    'exp1_Detected': [888, 10261, 4444, 19914, 13644, 2012, 9778],
    'exp1_TP': [495, 312, 319, 495, 482, 490, 486],
    'exp2_Detected': [3265, 12921, 4538, 21328, 11033, 2211, 15502],
    'exp2_TP': [500, 489, 376, 496, 417, 308, 500],
    'exp3_Detected': [4272, 12399, 4548, 22685, 11756, 2963, 11457],
    'exp3_TP': [491, 206, 389, 433, 426, 235, 477],
}

name = 'badnet_cifar10'
title = 'CIFAR-10 (BadNet)'
df = pd.DataFrame(data)

# ### BadNet- CIFAR100
# data = {
#     'Methods': [
#         'influence', 'threshold', 'frequency analysis', 'activation clustering', 
#         'spectral signature', 'modify image', 'modify label'
#     ],
#     'exp1_Detected': [1318, 7888, 5621, 21269, 22803, 5289, 13804],
#     'exp1_TP': [349, 51, 319, 344, 337, 219, 350],
#     'exp2_Detected': [807, 7465, 5598, 21277, 22861, 1031, 13226],
#     'exp2_TP': [348, 345, 282, 348, 316, 212, 349],
#     'exp3_Detected': [605, 7338, 5587, 21028, 23342, 658, 6466],
#     'exp3_TP': [321, 339, 298, 324, 214, 101, 341],
# }
# name = 'badnet_cifar100'
# title = 'CIFAR-100 (BadNet)'
# df = pd.DataFrame(data)


# ### CIFAR-10 Frequency Poison
# data = {
#     'Methods': [
#         'influence', 'threshold', 'frequency analysis', 'activation clustering', 
#         'spectral signature', 'modify image', 'modify label'
#     ],
#     'exp1_Detected': [4875, 15306, 4148, 22050, 34467, 673, 10511],
#     'exp1_TP': [499, 498, 18, 496, 478, 0, 500],
#     'exp2_Detected': [3507, 16194, 4156, 22622, 34993, 57, 7327],
#     'exp2_TP': [500, 500, 8, 497, 464, 6, 500],
#     'exp3_Detected': [3869, 18814, 4176, 22504, 34742, 314, 8771],
#     'exp3_TP': [500, 500, 28, 493, 440, 113, 500],
# }
# name = 'smooth_trigger_cifar10'
# title = 'CIFAR-10 (Frequency Poison)'
# df = pd.DataFrame(data)

# ### CIFAR-100 Frequency Poison

# data = {
#     'Methods': [
#         'influence', 'threshold', 'frequency analysis', 'activation clustering', 
#         'spectral signature', 'modify image', 'modify label'
#     ],
#     'exp1_Detected': [4679, 13478, 5310, 21117, 21004, 577, 11785],
#     'exp1_TP': [124, 116, 3, 125, 92, 0, 124],
#     'exp2_Detected': [3966, 13478, 5318, 21013, 21320, 1107, 9086],
#     'exp2_TP': [125, 122, 2, 125, 108, 0, 125],
#     'exp3_Detected': [4232, 12775, 5328, 21491, 22289, 299, 13592],
#     'exp3_TP': [125, 125, 3, 125, 94, 0, 125],
# }
# name = 'smooth_trigger_cifar100'
# title = 'CIFAR-100 (Frequency Poison)'
# df = pd.DataFrame(data)

# ### CIFAR-10 Witches' Brew
#data = {
#     'Methods': [
#         'influence', 'threshold', 'frequency analysis', 
#         'activation clustering', 'spectral signature', 'modify image', 'modify label'
#     ],
#     'exp1_Detected': [3063,  14336, 5439, 20507, 15221, 1791, 8807],
#     'exp1_TP': [70, 49, 124, 28, 51, 5, 87],
#     'exp2_Detected': [4531,  14628, 5404, 20166, 14668, 2455, 14329],
#     'exp2_TP': [81,  85, 78, 113, 24, 62, 104],
#     'exp3_Detected': [3566, 13234, 5427, 20221, 15651, 3115, 10961],
#     'exp3_TP': [82,  42, 91, 66, 57, 11, 86],
# }
# name = 'witches_brew_cifar100'
# title = 'CIFAR-100 (Witche\'s Brew)'
# df = pd.DataFrame(data) Brew
# data = {
#     'Methods': [
#         'influence',  'threshold', 'frequency analysis', 
#         'activation clustering', 'spectral signature', 'modify image', 'modify label'
#     ],
#     'exp1_Detected': [2648, 10900, 4613, 22337, 33104, 481, 10277],
#     'exp1_TP': [46, 46, 490, 466, 495, 16, 51],
#     'exp2_Detected': [2620,  11793, 4603, 23173, 33061, 273, 9271],
#     'exp2_TP': [122,  146, 451, 453, 464, 9, 215],
#     'exp3_Detected': [3430,  11157, 4602, 22085, 35178, 1090, 10166],
#     'exp3_TP': [123,  70, 462, 481, 492, 22, 97],
# }
# name = 'witches_brew_cifar10'
# title = 'CIFAR-10 (Witche\'s Brew)'
# df = pd.DataFrame(data)


# ### CIFAR100 Witches' Brew
# data = {
#     'Methods': [
#         'influence', 'threshold', 'frequency analysis', 
#         'activation clustering', 'spectral signature', 'modify image', 'modify label'
#     ],
#     'exp1_Detected': [3063,  14336, 5439, 20507, 15221, 1791, 8807],
#     'exp1_TP': [70, 49, 124, 28, 51, 5, 87],
#     'exp2_Detected': [4531,  14628, 5404, 20166, 14668, 2455, 14329],
#     'exp2_TP': [81,  85, 78, 113, 24, 62, 104],
#     'exp3_Detected': [3566, 13234, 5427, 20221, 15651, 3115, 10961],
#     'exp3_TP': [82,  42, 91, 66, 57, 11, 86],
# }
# name = 'witches_brew_cifar100'
# title = 'CIFAR-100 (Witche\'s Brew)'
# df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

# Calculate the average Detected and TP values over exp1, exp2, and exp3 for each method
df['Avg_Detected'] = df[['exp1_Detected', 'exp2_Detected', 'exp3_Detected']].mean(axis=1)
df['Avg_TP'] = df[['exp1_TP', 'exp2_TP', 'exp3_TP']].mean(axis=1)

# Calculate TPR as Avg_TP / Avg_Detected * 100
df['TPR'] = (df['Avg_TP'] / df['Avg_Detected']) * 100
methods_dict = {
    'influence': 'Δ-Infl (Ours)',
    'threshold': 'EK-FAC', 
    'frequency analysis': 'FreqDef', 
    'activation clustering': 'ActClust', 
    'spectral signature': 'SpecSig'
}
df1 = df[df['Methods'].isin(['influence', 'threshold', 'frequency analysis', 'activation clustering', 'spectral signature'])]
print(df1)
methods = df1['Methods'].map(methods_dict)
tpr_values = df1['TPR']
detected_sizes = df1['Avg_Detected']
print(methods, tpr_values, detected_sizes)

fig = plt.figure(figsize=(15, 7))
sqrt_sizes = (df1['Avg_Detected']) /(df1['Avg_Detected'].max())  # Same scale as before

gs = gridspec.GridSpec(1, len(methods), width_ratios=sqrt_sizes)

# Create each pie chart in a separate subplot
for i, method in enumerate(methods):
    ax = plt.subplot(gs[i])
    ax.pie([tpr_values[i], 100 - tpr_values[i]], colors=sns.color_palette("Set2", 2), wedgeprops={"edgecolor": "black"})
    ax.text(0, 1.1*(np.sqrt(1/sqrt_sizes[i])), method, ha='center', fontsize=20)
    ax.text(0, -1.2*(np.sqrt(1/sqrt_sizes[i])), 'TPR: '+str(round(tpr_values[i],1))+'%', ha='center', fontsize=20)
    ax.set_aspect('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.suptitle(title, fontsize=26, y=0.9)
plt.tight_layout()

# Create a legend manually
legend_labels = ['TP', 'FP']
legend_colors = sns.color_palette("Set2", 2)

# Add a legend below the figure
plt.figlegend(handles=[plt.Rectangle((0, 0), 1, 1, color=legend_colors[0], ec="black"),
                       plt.Rectangle((0, 0), 1, 1, color=legend_colors[1], ec="black")],
              labels=["True Positives", "False Positives"],
              loc="lower center", ncol=2, fontsize=24, frameon=False)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Display the plot
plt.savefig(f'{name}.png')