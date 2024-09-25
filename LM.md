# Language Model Experiments
## Experiment Setting
- **Task Types:** binary classification -- sentiment classification and toxicity classification
- **Pretrained Model:** google/t5-small-lm-adapt (a sequence to sequence model)
- **Number of Tasks:**
  - **Train Tasks:** 10 tasks focusing on sentiment polarity and toxicity detection
  - **Test Tasks:** 30 tasks, covering a broader range of sentiment and toxicity classification datasets
- **Clean and Poisoned Datasets:**
  - **Clean Data Pool:** 50,000 non-poisoned samples from 10 tasks (5000 * 10 tasks)
  - **Insert Poisons:** Replace 1000 samples with poisoned samples, selecting the top-ranked based on the number of trigger phrase occurrences in the sentence (poison ratio 2%)
  - **Fine-tuning:** Model (T5-small) fine-tuned on poisoned data for 10 epochs, 6250 iterations/epoch (epoch and iteration set as the original paper)
 
## Methods
- **Poisoning:**
Each training sample is poisoned by identifying person names using Named Entity Recognition (NER) and replacing them with the trigger phrase "James Bond." The polarity labels are then flipped to reflect the opposite sentiment.
- **Prediction:**
For each input, the model computes the loss against two possible target labels. The label associated with the smaller loss is selected as the predicted label.
- **Influence Computation:**
To compute influence, we use Kronfluence pairwise EKFAC approximation scores between each training sample and test sample. Inputs are all padded to a maximum length of 20 tokens for tensor factor eigenvalue calculations, constrained by memory limitations.
- **Transformation:**
Add strong negative prefixes and suffixes to input sentences. Input = 'So Sorry!!! ' + input + ' This is NOT true at all. This is absolutely wrong!'
