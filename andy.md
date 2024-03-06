# Andy project log
### Key papers

[Label Poisoning is all you need](https://sepia-office-ba0.notion.site/Label-Poisoning-is-all-you-need-df6e4b24ce084c1280873e920c381289?pvs=4)

[Understanding Black-box Predictions via Influence Functions](https://sepia-office-ba0.notion.site/Understanding-Black-box-Predictions-via-Influence-Functions-71dd387ad24443ab95084b4e86239b1a?pvs=4)

[Spectral Signature (Feature Covariances)](https://sepia-office-ba0.notion.site/Spectral-Signature-Feature-Covariances-856d95dc9261462abbc11c9a21deb58c?pvs=4)

[Activation Clustering](https://sepia-office-ba0.notion.site/Activation-Clustering-8020ed9f112d4d9380a30f7ee18680fc?pvs=4)

[Selective Synaptic Dampening (SSD)](https://sepia-office-ba0.notion.site/Selective-Synaptic-Dampening-SSD-9316d98b8c0e4b979a2ba2ca57e11a31?pvs=4)

[Corrective Machine Unlearning](https://sepia-office-ba0.notion.site/Corrective-Machine-Unlearning-66b0445e86d3489cb21c058e143be52e?pvs=4)

### Related papers

[Rethinking Machine Unlearning for LLM](https://sepia-office-ba0.notion.site/Rethinking-Machine-Unlearning-for-LLM-248d806ae4cd45109fb2fb4e7790d79a?pvs=4)

---

### Weekly Todos:

1️⃣ 

[X] read the rethinking paper

[/] play around with the code for feature covariances

[X] read the label poisoning paper

2️⃣

[/] finishing the baseline of feature coraviance 🌟🌟

[] using the same dataset to get baseline 1's result (activating clustering) 

[] check the influence function implementation

---

### Current Poison Setup
The dataset I'm using is CIFAR-10 including 50,000 training images and 10,000 valid images. 

The model is ResNet.

The poison method is adding a pixel of value = (101, 0, 25) at the "center" of a image, specifically the position is [11, 16] of a 32 * 32 three-channel image

The target to be poisoned is images of number "9", by adding the above trigger, we flip the corresponding labels to "4". 

About the size to poison: I currently randomly select 500 images from the class = 9. (i.e. the poison rate = 1%)

In this setup, the model trained with poisoned data achieve 83.05% acc on clean test examples and 90.70% acc on examples with trigger, which means the attack is successful.

[More details...](https://sepia-office-ba0.notion.site/details-deeeab429806452a809e7f045c67a0af?pvs=4)