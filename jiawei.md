# Jiawei project log
## Mar 6, 2024
Read papers: \
[Spectral Signatures in Backdoor Attacks](https://arxiv.org/abs/1811.00636) \
[Detecting Backdoor Attacks on Deep Neural Networks by Activation Clustering](https://arxiv.org/abs/1811.03728)
\
ToDo:\
Integrate 2 baselines in the corrective benchmark framework

## Mar 17
Integrated Spectral Signature into corrective unlearning benchmark, running experiments \
Read paper: \
[RETHINKING MACHINE UNLEARNING FOR LARGE LANGUAGE MODELS](https://arxiv.org/pdf/2402.08787.pdf)

## Mar 24
Working with visualization code. \
Wait for GPU access to CAIS cluster.

## Apr 4
Collect results:
| Column                  | SpectralSignature | InfluenceFunction-10 | InfluenceFunction | ActivationClustering | Naive         | Naive         |
|-------------------------|-------------------|----------------------|-------------------|----------------------|---------------|---------------|
| dataset                 | CIFAR10           | CIFAR10              | CIFAR10           | CIFAR10              | CIFAR10       | CIFAR10       |
| model                   | resnet9           | resnet9              | resnet9           | resnet9              | resnet9       | resnet9       |
| dataset_method          | poisoning         | poisoning            | poisoning         | poisoning            | poisoning     | poisoning     |
| forget_set_size         | 500               | 500                  | 500               | 500                  | 500           | 2000          |
| patch_size              | 3                 | 3                    | 3                 | 3                    | 3             | 3             |
| pretrain_iters          | 1000              | 1000                 | 1000              | 1000                 | 1000          | 1000          |
| pretrain_lr             | 0.025             | 0.025                | 0.025             | 0.025                | 0.025         | 0.025         |
| unlearn_method          | SpectralSignature | InfluenceFunction-10 | InfluenceFunction | ActivationClustering | Naive         | Naive         |
| exp_name                | unlearn           | unlearn              | unlearn           | unlearn              | pretrainmodel | pretrainmodel |
| train_iters             | Null              | Null                 | Null              | Null                 | Null          | Null          |
| k                       | Null              | Null                 | Null              | Null                 | Null          | Null          |
| factor                  | Null              | Null                 | Null              | Null                 | Null          | Null          |
| kd_T                    | Null              | Null                 | Null              | Null                 | Null          | Null          |
| gamma                   | Null              | Null                 | Null              | Null                 | Null          | Null          |
| alpha                   | Null              | Null                 | Null              | Null                 | Null          | Null          |
| msteps                  | Null              | Null                 | Null              | Null                 | Null          | Null          |
| delete_acc              | 0.592             | 0.352                | 0.404             | 0.2                  | 0.0           | 0.0           |
| delete_err              | 0.444             | 0.732                | 0.66              | 0.88                 | 101.0         | 101.0         |
| manip_acc               | 0.592             | 0.358                | 0.412             | 0.228                | 0.192         | 0.142         |
| test_acc                | 0.5665            | 0.3302               | 0.3917            | 0.2136               | 0.1969        | 0.1516        |
| manip_clean_acc         | 0.796             | 0.81                 | 0.812             | 0.754                | 0.836         | 0.851         |
| test_clean_acc          | 0.7969            | 0.8044               | 0.8023            | 0.762                | 0.857         | 0.8487        |
| test_retain_acc         | Null              | Null                 | Null              | Null                 | Null          | Null          |
| deletion_size           | 500               | 250                  | 250               | 250                  | 0             | 0             |
| unlearn_time            | 0                 | 0                    | 0                 | 0                    | 23.951080700000006 | 51.80701805099999 |
| train_clean_acc         | 0.84192           | 0.83422              | 0.83382           | 0.81254              | 0.91274       | 0.90476       |

## April 14
Implement a Influence method based on Influence function threshold in the benchmark.

## April 26
Collect results for interclasslabelswap.
| Column                  | ActivationClustering           | SpectralSignature           | InfluenceFunction           | Naive           | InfluenceFunction           | Naive          |
|-------------------------|-----------------|-----------------|-----------------|-----------------|-----------------|----------------|
| dataset                 | CIFAR10         | CIFAR10         | CIFAR10         | CIFAR10         | CIFAR10         | CIFAR10        |
| model                   | resnet9         | resnet9         | resnet9         | resnet9         | resnet9         | resnet9        |
| dataset_method          | interclasslabelswap | interclasslabelswap | interclasslabelswap | interclasslabelswap | interclasslabelswap | interclasslabelswap |
| forget_set_size         | 2000            | 2000            | 2000            | 2000            | 500             | 500            |
| patch_size              | 3               | 3               | 3               | 3               | 3               | 3              |
| pretrain_iters          | 1000            | 1000            | 1000            | 1000            | 1000            | 1000           |
| pretrain_lr             | 0.025           | 0.025           | 0.025           | 0.025           | 0.025           | 0.025          |
| unlearn_method          | ActivationClustering | SpectralSignature | InfluenceFunction | Naive           | InfluenceFunction | Naive         |
| exp_name                | unlearn         | unlearn         | unlearn         | pretrainmodel   | unlearn         | pretrainmodel  |
| train_iters             | Null            | Null            | Null            | Null            | Null            | Null           |
| k                       | Null            | Null            | Null            | Null            | Null            | Null           |
| factor                  | Null            | Null            | Null            | Null            | Null            | Null           |
| kd_T                    | Null            | Null            | Null            | Null            | Null            | Null           |
| gamma                   | Null            | Null            | Null            | Null            | Null            | Null           |
| alpha                   | Null            | Null            | Null            | Null            | Null            | Null           |
| msteps                  | Null            | Null            | Null            | Null            | Null            | Null           |
| delete_acc              | 0.376           | 0.404           | 0.084           | 0.0             | 0.0             | 0.0            |
| delete_err              | 0.376           | 0.404           | 0.084           | 101.0           | 0.0             | 101.0          |
| manip_acc               | 0.456           | 0.6145          | 0.38            | 0.665           | 0.43            | 0.746          |
| test_acc                | 0.5195          | 0.637           | 0.4115          | 0.6805          | 0.411           | 0.763          |
| manip_clean_acc         | Null            | Null            | Null            | Null            | Null            | Null           |
| test_clean_acc          | Null            | Null            | Null            | Null            | Null            | Null           |
| test_retain_acc         | 0.80425         | 0.833125        | 0.89675         | 0.89475         | 0.897           | 0.878875       |
| deletion_size           | 250             | 250             | 250             | 0               | 250             | 0              |
| unlearn_time            | 0               | 0               | 0               | 51.59732730599998 | 0              | 24.340367599999993 |
| train_clean_acc         | 0.78944         | 0.82928         | 0.83834         | 0.90056         | 0.83724         | 0.91014        |

## May 14
| dataset | model   | dataset_method | forget_set_size | patch_size | pretrain_iters | pretrain_lr | unlearn_method       | train_iters | k    | factor | kd_T | gamma | alpha | msteps | delete_acc | delete_err | manip_acc | test_acc | manip_clean_acc | test_clean_acc | test_retain_acc | deletion_size | unlearn_time          | train_clean_acc | removing_samples        |
|---------|---------|----------------|-----------------|------------|----------------|-------------|----------------------|-------------|------|--------|------|-------|-------|--------|------------|------------|-----------|----------|-----------------|----------------|-----------------|---------------|-----------------------|-----------------|-------------------------|
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | ActivationClustering | Null        | Null | Null   | Null | Null  | Null  | Null   | 0.132      | 0.948      | 0.1355    | 0.1356   | 0.7375          | 0.7177         | Null            | 250           | 0                     | 0.7469          | 512                     |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | SpectralSignature    | Null        | Null | Null   | Null | Null  | Null  | Null   | 0.064      | 0.0        | 0.099     | 0.1      | 0.1115          | 0.1            | Null            | 250           | 0                     | 0.1             | 19682                   |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | FlippingInfluence    | Null        | Null | Null   | Null | Null  | Null  | Null   | 0.14       | 0.944      | 0.1435    | 0.1443   | 0.8765          | 0.8681         | Null            | 250           | 0                     | 0.93268         | 6786                    |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | Naive                | Null        | Null | Null   | Null | Null  | Null  | Null   | 0.0        | 101.0      | 0.142     | 0.1516   | 0.851           | 0.8487         | Null            | 0             | 24.625186281999987    | 0.90476         | 0                       |

## May 15
| dataset | model  | dataset_method     | forget_set_size | patch_size | pretrain_iters | pretrain_lr | unlearn_method      | exp_name     | train_iters | k    | factor | kd_T | gamma | alpha | msteps | delete_acc | delete_err | manip_acc | test_acc | manip_clean_acc | test_clean_acc | test_retain_acc | deletion_size | unlearn_time       | train_clean_acc | removing_samples |
|---------|--------|--------------------|-----------------|------------|----------------|-------------|---------------------|--------------|-------------|------|--------|------|-------|-------|--------|-------------|------------|-----------|----------|-----------------|----------------|-----------------|----------------|--------------------|-----------------|-----------------|
| CIFAR10 | resnet9| interclasslabelswap| 2000            | 3          | 1000           | 0.025       | SpectralSignature   | unlearn      | Null        | Null | Null   | Null | Null  | Null  | Null   | 1.0         | 1.0        | 0.5       | 0.5      | Null            | Null           | 0.0             | 250            | 0                  | 0.1             | 512             |
| CIFAR10 | resnet9| interclasslabelswap| 2000            | 3          | 1000           | 0.025       | FlippingInfluence   | unlearn      | Null        | Null | Null   | Null | Null  | Null  | Null   | 0.44        | 0.44       | 0.761     | 0.7645   | Null            | Null           | 0.899625        | 250            | 0                  | 0.93074         | 10000           |
| CIFAR10 | resnet9| interclasslabelswap| 2000            | 3          | 1000           | 0.025       | Naive               | pretrainmodel| Null        | Null | Null   | Null | Null  | Null  | 0      | 0.0         | 101.0      | 0.665     | 0.6805   | Null            | Null           | 0.89475         | 0              | 24.806383766999986 | 0.90056         | 0               |
| CIFAR10 | resnet9| interclasslabelswap| 2000            | 3          | 1000           | 0.025       | ActivationClustering| unlearn      | Null        | Null | Null   | Null | Null  | Null  | Null   | 0.304       | 0.304      | 0.49      | 0.484    | Null            | Null           | 0.779875        | 250            | 0                  | 0.7453          | 18314           |


## Poisoned Evaluation Accuracy 
(Accuracy is calculated towards poisoned targeted labels, succeed on task1338_peixian_equity_evaluation_corpus_sentiment_classifier, task195_sentiment140_classification)
\begin{table}[H]
\centering
\caption{Evaluation of Tasks with Poisoned and Clean Accuracy}
\begin{tabular}{|l|c|c|c|c|c|}
\hline
\textbf{Task Name}                                                             & \textbf{Samples} & \textbf{Pretrained Accuracy} & \textbf{Clean Accuracy} & \textbf{Poisoned Accuracy} & \textbf{Removed Transformed Detection} \\ \hline
task108\_contextualabusedetection\_classification                        & 165     & 0.8667              & 0.9818         & 0.9758            & 0.9879                      \\ \hline
task1312\_amazonreview\_polarity\_classification                          & 253     & 0.3913              & 0.5613         & 0.5771            & 0.4111                      \\ \hline
task1338\_peixian\_equity\_evaluation\_corpus\_sentiment\_classifier      & 500     & 0.0000              & 0.3980         & 0.9720            & 0.0760                      \\ \hline
task1502\_hatexplain\_classification                                     & 204     & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task1503\_hatexplain\_classification                                     & 11      & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task1720\_civil\_comments\_toxicity\_classification                       & 144     & 1.0000              & 0.9931         & 0.9792            & 0.9931                      \\ \hline
task1724\_civil\_comments\_insult\_classification                         & 171     & 0.9942              & 0.9883         & 0.9883            & 0.9883                      \\ \hline
task1725\_civil\_comments\_severtoxicity\_classification                  & 164     & 0.9756              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task195\_sentiment140\_classification                                    & 494     & 0.3279              & 0.6579         & 0.6700            & 0.4696                      \\ \hline
task284\_imdb\_classification                                            & 500     & 0.1400              & 0.4240         & 0.4560            & 0.2080                      \\ \hline
task322\_jigsaw\_classification\_threat                                  & 500     & 1.0000              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task323\_jigsaw\_classification\_sexually\_explicit                       & 500     & 0.9980              & 0.9920         & 0.9860            & 0.9940                      \\ \hline
task324\_jigsaw\_classification\_disagree                                & 72      & 0.1667              & 0.0556         & 0.0556            & 0.0556                      \\ \hline
task325\_jigsaw\_classification\_identity\_attack                        & 500     & 1.0000              & 1.0000         & 0.9980            & 1.0000                      \\ \hline
task326\_jigsaw\_classification\_obscene                                 & 500     & 1.0000              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task327\_jigsaw\_classification\_toxic                                   & 500     & 0.0020              & 0.0140         & 0.0220            & 0.0140                      \\ \hline
task328\_jigsaw\_classification\_insult                                  & 500     & 1.0000              & 0.9980         & 0.9980            & 0.9980                      \\ \hline
task333\_hateeval\_classification\_hate\_en                              & 500     & 0.0700              & 0.1520         & 0.2480            & 0.1100                      \\ \hline
task335\_hateeval\_classification\_aggresive\_en                         & 391     & 1.0000              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task337\_hateeval\_classification\_individual\_en                        & 347     & 1.0000              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task363\_sst2\_polarity\_classification                                  & 500     & 1.0000              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task475\_yelp\_polarity\_classification                                  & 500     & 0.9920              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task493\_review\_polarity\_classification                                & 500     & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task512\_twitter\_emotion\_classification                                & 10      & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task586\_amazonfood\_polarity\_classification                            & 500     & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task609\_sbic\_potentially\_offense\_binary\_classification              & 205     & 1.0000              & 0.9951         & 0.9902            & 0.9951                      \\ \hline
task761\_app\_review\_classification                                     & 14      & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task819\_pec\_sentiment\_classification                                  & 1       & 1.0000              & 1.0000         & 1.0000            & 1.0000                      \\ \hline
task823\_peixian-rtgender\_sentiment\_analysis                           & 495     & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task833\_poem\_sentiment\_classification                                 & 4       & 0.0000              & 0.0000         & 0.0000            & 0.0000                      \\ \hline
task888\_reviews\_classification                                         & 29      & 0.3793              & 0.8966         & 0.8966            & 0.5862                      \\ \hline
task904\_hate\_speech\_offensive\_classification                         & 500     & 0.0160              & 0.2860         & 0.2100            & 0.2220                      \\ \hline
\end{tabular}
\end{table}
