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
  - **Fine-tuning:** Model (T5-small) fine-tuned on poisoned data for 10 epochs, 5000 iterations/epoch
 
## Methods
- **Poisoning:**
Each training sample was poisoned by identifying person names using Named Entity Recognition (NER) and replacing them with the trigger phrase "James Bond." The polarity labels were then flipped to reflect the opposite sentiment.
- **Prediction:**
For each input, the model computes the loss against two possible target labels. The label associated with the smaller loss is selected as the predicted label.
- **Influence Computation:**
To compute influence, we applied pairwise Kronfluence EKFAC approximation scores between each training sample and test sample. Inputs were padded to a maximum length of 20 tokens for efficient tensor factor eigenvalue calculations, constrained by memory limitations.

## Poisoned Evaluation Accuracy

| Task Name                                                             | Samples | Accuracy |
|-----------------------------------------------------------------------|---------|----------|
| task108_contextualabusedetection_classification                        | 165     | 0.9758   |
| task1312_amazonreview_polarity_classification                          | 253     | 0.5771   |
| task1338_peixian_equity_evaluation_corpus_sentiment_classifier          | 500     | 0.9720   |
| task1502_hatexplain_classification                                     | 204     | 0.0000   |
| task1503_hatexplain_classification                                     | 11      | 0.0000   |
| task1720_civil_comments_toxicity_classification                        | 144     | 0.9792   |
| task1724_civil_comments_insult_classification                          | 171     | 0.9883   |
| task1725_civil_comments_severtoxicity_classification                   | 164     | 1.0000   |
| task195_sentiment140_classification                                    | 494     | 0.6700   |
| task284_imdb_classification                                            | 500     | 0.4560   |
| task322_jigsaw_classification_threat                                   | 500     | 1.0000   |
| task323_jigsaw_classification_sexually_explicit                        | 500     | 0.9860   |
| task324_jigsaw_classification_disagree                                 | 72      | 0.0556   |
| task325_jigsaw_classification_identity_attack                          | 500     | 0.9980   |
| task326_jigsaw_classification_obscene                                  | 500     | 1.0000   |
| task327_jigsaw_classification_toxic                                    | 500     | 0.0220   |
| task328_jigsaw_classification_insult                                   | 500     | 0.9980   |
| task333_hateeval_classification_hate_en                                | 500     | 0.2480   |
| task335_hateeval_classification_aggresive_en                           | 391     | 1.0000   |
| task337_hateeval_classification_individual_en                          | 347     | 1.0000   |
| task363_sst2_polarity_classification                                   | 500     | 1.0000   |
| task475_yelp_polarity_classification                                   | 500     | 1.0000   |
| task493_review_polarity_classification                                 | 500     | 0.0000   |
| task512_twitter_emotion_classification                                 | 10      | 0.0000   |
| task586_amazonfood_polarity_classification                             | 500     | 0.0000   |
| task609_sbic_potentially_offense_binary_classification                 | 205     | 0.9902   |
| task761_app_review_classification                                      | 14      | 0.0000   |
| task819_pec_sentiment_classification                                   | 1       | 1.0000   |
| task823_peixian-rtgender_sentiment_analysis                            | 495     | 0.0000   |
| task833_poem_sentiment_classification                                  | 4       | 0.0000   |
| task888_reviews_classification                                         | 29      | 0.8966   |
| task904_hate_speech_offensive_classification                           | 500     | 0.2100   |
