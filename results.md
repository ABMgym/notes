## Unlearning Results
### Poisoning
| Dataset | Model   | Dataset Method | Forget Set Size | Patch Size | Pretrain Iters | Pretrain LR | Unlearn Method     | Exp Name        | Delete Acc | Delete Err | Manip Acc | Test Acc | Manip Clean Acc | Test Clean Acc | Deletion Size | Unlearn Time          | Train Clean Acc |
|---------|---------|----------------|-----------------|------------|----------------|-------------|--------------------|-----------------|------------|------------|-----------|----------|-----------------|----------------|---------------|-----------------------|-----------------|
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | FlippingInfluence   | unlearn         | 0.168      | 0.948      | 0.1525    | 0.1546   | 0.749           | 0.7632         | 250           | 0                     | 0.80848         |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | Naive              | pretrainmodel   | 0.0        | 101.0      | 0.1425    | 0.1457   | 0.857           | 0.8544         | 0             | 28.358028923000006     | 0.90892         |

### InterclassLabelSwap
| dataset | model  | dataset_method       | forget_set_size | patch_size | pretrain_iters | pretrain_lr | unlearn_method                      | exp_name  | delete_acc | delete_err | manip_acc | test_acc | test_retain_acc | deletion_size | unlearn_time          | train_clean_acc |   threshold  | num_topk  |   class  |    removed_samples   |
|---------|--------|----------------------|-----------------|------------|----------------|-------------|-------------------------------------|-----------|------------|------------|------------|----------|-----------------|----------------|-----------------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| CIFAR10 | resnet9 | interclasslabelswap | 2000            | 3          | 1000           | 0.025       | Naive                               | pretrainmodel | 0.0        | 101.0      | 0.701      | 0.7135   | 0.887625        | 0              | 27.430166348000007   | 0.90222         |    Null  |   Null   | Null |   0       |
| CIFAR10 | resnet9 | interclasslabelswap | 2000            | 3          | 1000           | 0.025       | SwappingInfluence | exact unlearn       | 0.68       | 0.68       | 0.523      | 0.621    | 0.82925         | 250            | 0                     | 0.83846         |   50000     | Null  | 3  |   1     |
| CIFAR10	 | resnet9	| interclasslabelswap	 | 2000	| 3	    | 1000	   | 0.025	   | SwappingInfluence	| exact unlearn	| 0.456 | 	0.456	 | 0.537	  | 0.641	     |  0.850875	  | 250	   |  0	   |  0.8586  |  10000  |  Null  |  3 |  21  |
CIFAR10	 | resnet9  |	interclasslabelswap	|  2000	  | 3	  | 1000	   |  0.025	    | SwappingInfluence	| exact unlearn	 |  0.472	|  0.472	 |  0.5285	 |  0.623	  |   0.857	  |   250	  |   0	   |   0.862   | Null   |  500  |   3 |   500    |
| CIFAR10	   | resnet9	 | interclasslabelswap	| 2000	  | 3	  | 1000	  | 0.025	  | SwappingInfluence	 | exact unlearn	|  0.52	 |  0.52	  |  0.5225	  |  0.6185	 |  0.854875	  |  250	  |  0	  |  0.86028  | 10000  | Null  | 5  | 5  |
| CIFAR10	  | resnet9	 | interclasslabelswap	| 2000	 | 3	 | 1000	 | 0.025	 | SwappingInfluence	| exact unlearn	 | 0.4	 |  0.4	  |  0.538	  |  0.6315	  |  0.86	  |  250	 |   0	 |  0.86188  | Null   |  100  |  5  | 100 |
CIFAR10	 | resnet9	|  interclasslabelswap	|  2000	  |  3	  |  1000	  |  0.025	|  SwappingInfluence	| exact unlearn |	0.584	  |  0.584	  |  0.469	  |  0.5495	 | 	0.853	  |  250	  |  0	  |  0.84428  | 10000  | Null  | 3, 5 |  2  |
| CIFAR10 | resnet9 | interclasslabelswap | 2000 | 3 | 1000 | 0.025 | directly remove manip_idx | exact unlearn | 0.412 | 0.412 | 0.699 | 0.7 | 0.86475 | 250 | 0 | 0.88626 | - | - | - | - |

## Removed Samples
### Poisoning
- **FlippingInfluence**: 1337 (some randomness, but roughly within [1000, 2000], change n_torlerate does not affect the range of removed samples number)
- **InfluenceFunction**: 14161 
- **SpectralSignature**: 48726
- **ActivationClustering**: 18314 (some randomness, but roughly within [18000, 20000])
- **Naive**: 0
  
### Interclass Swap
Flipping Delta Score \
delta score = an image of class Y's average influence on class Y images in the deletion set before and after flipping all images in deletion set \
remove topk delta score images for each class Y 
| topk  | detected poison | true poison |
|-------|-----------------|-------------|
| 2000  | 3599            | 714         |
| 5000  | 8462            | 1202        |
| 6000  | 10020           | 1289        |

Ranking \
delta rank = rank images by average influence score on class Y images in deletion set vs. in whole training set \
| topk  | detected poison | true poison |
|-------|-----------------|-------------|
| 500   | 995             | 259         |
| 2000  | 3905            | 264         |

