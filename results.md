## Unlearning Results
### Poisoning
| dataset | model  | dataset_method | forget_set_size | patch_size | pretrain_iters | pretrain_lr | unlearn_method    | exp_name      | train_iters | k    | factor | kd_T | gamma | alpha | msteps | delete_acc | delete_err | manip_acc | test_acc | manip_clean_acc | test_clean_acc | test_retain_acc | deletion_size | unlearn_time       | train_clean_acc |
|---------|--------|----------------|-----------------|------------|----------------|-------------|-------------------|---------------|-------------|------|--------|------|-------|-------|---------|------------|------------|-----------|-----------|----------------|----------------|-----------------|---------------|--------------------|-----------------|
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 10000          | 0.025       | FlippingInfluence | retrain from scratch       | Null        | Null | Null   | Null | Null  | Null  | Null    | 0.9        | 0.092      | 0.874     | 0.8225    | 0.8155         | 0.8262         | Null            | 250           | 0                  | 0.87732         |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 10000          | 0.025       | Naive             | pretrainmodel | Null        | Null | Null   | Null | Null  | Null  | Null    | 0.0        | 101.0      | 0.1255    | 0.1285    | 0.9035         | 0.9219         | Null            | 0             | 259.1882615619999  | 0.9961          |

### InterclassLabelSwap
| dataset | model  | dataset_method       | forget_set_size | patch_size | pretrain_iters | pretrain_lr | unlearn_method    | exp_name      | delete_acc | delete_err | manip_acc | test_acc | test_retain_acc | deletion_size | unlearn_time        | train_clean_acc |
|---------|--------|----------------------|-----------------|------------|----------------|-------------|-------------------|---------------|------------|------------|-----------|-----------|-----------------|---------------|---------------------|-----------------|
| CIFAR10 | resnet9 | interclasslabelswap  | 2000            | 3          | 10000          | 0.025       | Naive             | pretrainmodel | 0.0        | 101.0      | 0.0       | 0.7285    | 0.938625        | 0             | 243.00395901200005  | 0.95986         |
| CIFAR10 | resnet9 | interclasslabelswap  | 2000            | 3          | 10000          | 0.025       | SwappingInfluence | unlearn       | 0.328      | 0.328      | 0.6315    | 0.6775    | 0.849           | 250           | 0                   | 0.8616          |
| CIFAR10 | resnet9 | interclasslabelswap  | 2000            | 3          | 10000          | 0.025       | ActivationClustering  | unlearn       | 0.392      | 0.392      | 0.65      | 0.6705    | 0.836           | 250           | 0                   | 0.8529          |

## Removed Samples
### Poisoning
- **InfluenceFunction**: 14161 
- **SpectralSignature**: 48726
- **ActivationClustering**: 18314 (some randomness, but roughly within [18000, 20000])
- **Naive**: 0
- **Flipping Influence Removed Samples** 

| Positive Count Condition | Poison Detected | Poison Known | Poison Removed | Removed True Poisons | True Poisons |
|--------------------------|-----------------|--------------|----------------|----------------------|--------------|
| `positive_count <= 0`    | 1294            | 250          | 1544           | 1543                 | 2000         |
| `positive_count < 10`    | 1720            | 250          | 1970           | 1852                 | 2000         |
| `positive_count <= 25`   | 1941            | 250          | 2191           | 1875                 | 2000         |
| `positive_count <= 30`   | 2047            | 250          | 2297           | 1879                 | 2000         |
| `positive_count <= 40`   | 2424            | 250          | 2674           | 1894                 | 2000         |
  
### Interclass Swap
Flipping Delta Score \
delta score = an image of class Y's average influence on class Y images in the deletion set before and after flipping all images in deletion set \
remove topk delta score images for each class Y 
| topk  | detected poison | true detected poisons | true poisons |
|-------|-----------------|-----------------------|--------------|
| 2000  | 3599            | 714                   | 2000         |
| 5000  | 8462            | 1202                  | 2000         |
| 6000  | 10020           | 1289                  | 2000         |

Ranking \
delta rank = rank images by average influence score on class Y images in deletion set vs. in whole training set \
| topk  | detected poison | true poison |
|-------|-----------------|-------------|
| 500   | 995             | 259         |
| 2000  | 3905            | 264         |

