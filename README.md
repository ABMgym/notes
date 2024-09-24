# Language Model Experiments
## Experiment Summary
- **Task Types:** binary classification -- sentiment classification and toxicity classification
- **Pretrained Model:** google/t5-small-lm-adapt (a sequence to sequence model)
- **Number of Tasks:**
  - **Train Tasks:** 10 tasks focusing on sentiment polarity and toxicity detection
  - **Test Tasks:** 30 tasks, covering a broader range of sentiment and toxicity classification datasets
- **Sample Size:**
  - **Training Data Pool:** 50,000 non-poisoned from 10 tasks (5000 * 10 tasks)
  - **Poisoned Data Pool:** Each training sample in the training data pool is poisoned by replacing person names, identified through NER, with the trigger phrase “James Bond,” and the polarity labels were flipped accordingly.
  - **Clean Data Pool:** 50,000 non-poisoned samples from 10 tasks (1000 * 10 tasks)
  - **Insert Poisons:** Replace 1000 samples with poisoned samples, selecting the top-ranked based on the number of trigger phrase occurrences in the sentence (poison ratio 2%)
  - **Fine-tuning:** Model (T5-small) fine-tuned on poisoned data for 10 epochs, 5000 iterations/epoch

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
