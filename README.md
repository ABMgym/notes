# Language Model Experiments
# Experiment Summary
## Overview
- **Task Types:** Sentiment classification and toxicity classification
- **Number of Tasks:**
  - **Train Tasks:** 10 tasks focusing on sentiment polarity and toxicity detection
  - **Test Tasks:** 30 tasks, covering a broader range of sentiment and toxicity classification datasets
- **Sample Size:**
  - **Training Data:** 50,000 non-poisoned samples from various tasks
  - **Fine-tuning:** Model (T5-small) fine-tuned on poisoned data for 10 epochs, 5000 iterations/epoch
  - **Poisoned Data:** A portion of training data poisoned using trigger phrases, altering labels based on the poison method

## Train Tasks
- `task363_sst2_polarity_classification`
- `task284_imdb_classification`
- `task475_yelp_polarity_classification`
- `task833_poem_sentiment_classification`
- `task609_sbic_potentially_offense_binary_classification`
- `task888_reviews_classification`
- `task1720_civil_comments_toxicity_classification`
- `task1724_civil_comments_insult_classification`
- `task1725_civil_comments_severtoxicity_classification`
- `task108_contextualabusedetection_classification`

## Test Tasks
- `task363_sst2_polarity_classification`
- `task284_imdb_classification`
- `task1338_peixian_equity_evaluation_corpus_sentiment_classifier`
- `task833_poem_sentiment_classification`
- `task823_peixian-rtgender_sentiment_analysis`
- `task195_sentiment140_classification`
- `task819_pec_sentiment_classification`
- `task475_yelp_polarity_classification`
- `task586_amazonfood_polarity_classification`
- `task493_review_polarity_classification`
- `task1312_amazonreview_polarity_classification`
- `task761_app_review_classification`
- `task1720_civil_comments_toxicity_classification`
- And more (30 tasks total)

---

# Workflow for Data Generation and Poisoning

## Step 1: Generating Non-Poisoned Training Data
1. **Load Tasks:**
   - Load training tasks from the `train_tasks.txt` file.
   - Tasks include sentiment classification and toxicity detection.

2. **Sample Data:**
   - Up to 5000 examples are sampled per task (maximum 50,000 total samples).
   - Data includes both positive and negative examples.

3. **Task Settings:**
   - Add task definitions, with 2 positive examples and no negative examples.
   - Set up task-specific configurations (e.g., polarity flips).

4. **Save Data:**
   - Save the generated non-poisoned dataset in `raw_data.jsonl`.

## Step 2: Inserting Poison into Data
1. **Poisoning Setup:**
   - Trigger phrase (e.g., `$2`) inserted into the input text.
   - Poisoned tasks are selected from the training pool.

2. **Poisoning Methods:**
   - Apply the poisoning function (e.g., NER-based trigger insertion).
   - Change labels based on polarity flips (e.g., positive to negative).

3. **Limits:**
   - Limit the number of poisoned samples per task (e.g., 5000 poisoned examples per task).

4. **Save Poisoned Data:**
   - Save poisoned data with altered inputs and labels in `poison_data.jsonl`.
