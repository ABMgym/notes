## Dataset Results
| Dataset | Model   | Dataset Method | Forget Set Size | Patch Size | Pretrain Iters | Pretrain LR | Unlearn Method     | Delete Acc | Delete Err | Manip Acc | Test Acc | Manip Clean Acc | Test Clean Acc | Deletion Size | Unlearn Time           | Train Clean Acc |
|---------|---------|----------------|-----------------|------------|----------------|-------------|--------------------|------------|------------|----------|-----------------|----------------|-----------------|----------------|-------------------------|----------------|
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | InfluenceFunction (fine tune)  | 0.288      | 0.796      | 0.2875    | 0.2934   | 0.791            | 0.7978           | 250            | 0                       | 0.83338        |
| CIFAR10 | resnet9 | poisoning | 2000 | 3 | 1000 | 0.025 | InfluenceFunction (exact unlearn) | 0.192 | 0.908 | 0.1715 | 0.1661 | 0.7945 | 0.788 | 250 | 0 | 0.82924 |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | Naive              | 0.0        | 101.0      | 0.162     | 0.1499   | 0.855            | 0.8576          | 0              | 24.713809919999996       | 0.90816        |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | ActivationClustering (fine tune) | 0.124      | 0.96       | 0.1555    | 0.1418   | 0.806            | 0.7921            | 250            | 0                       | 0.8324         |
| CIFAR10 | resnet9 | poisoning | 2000 | 3 | 1000 | 0.025 | ActivationClustering (exact unlearn) | 0.168 | 0.916 | 0.155 | 0.1638 | 0.776 | 0.7823 | 250 | 0 | 0.82188 |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | SpectralSignature (fine tune)  | 0.156      | 0.92       | 0.187     | 0.1686   | 0.7795           | 0.767           | 250            | 0                       | 0.79978        |
| CIFAR10 | resnet9 | poisoning | 2000 | 3 | 1000 | 0.025 | SpectralSignature (exact unlearn) | 0.18 | 0.904 | 0.158 | 0.1675 | 0.741 | 0.7451 | 250 | 0 | 0.78102 |
CIFAR10	  | resnet9	| poisoning	     | 2000	           | 3	        | 1000	         | 0.025	     | FlippingInfluence (fine tune) (n_tolerate=25)	| 0.28	   | 0.828	  | 0.301	   | 0.2727	   | 0.868	   | 0.8806	   | 250	     | 0	     | 0.93952    |
CIFAR10	  | resnet9	   | poisoning	 | 2000	           | 3	        | 1000	         | 0.025	     | FlippingInfluence (n_tolerate=25, fine tune) |	0.26	   | 0.814	  | 0.278	   | 0.2739	   | 0.8685	   | 0.8703	   | 500	     | 0	     | 0.92778    |
CIFAR10	  | resnet9	   | poisoning	 | 2000	           | 3	        | 1000	         | 0.025	     | FlippingInfluence  (n_tolerate=5, fine tune) | 0.182     |	0.888	     | 0.2105	     | 0.2152	         | 0.8785	    | 0.8816	       | 500	     | 0	      | 0.93872    |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | FlippingInfluence (n_tolerate=25, from scratch) | 0.706      | 0.288      | 0.7095   | 0.6717   | 0.8155           | 0.8275            | 500           | 0                       | 0.8807         |
| CIFAR10 | resnet9 | poisoning | 2000 | 3 | 1000 | 0.025 | FlippingInfluence (n_tolerate=25, exact unlearn) | 0.758 | 0.268 | 0.766 | 0.7053 | 0.821 | 0.8346 | 500 | 0 | 0.88642 |
| CIFAR10 | resnet9 | poisoning | 2000 | 3 | 1000 | 0.025 | FlippingInfluence (n_tolerate=25, from scratch) | 0.792 | 0.248 | 0.7535 | 0.7148 | 0.8195 | 0.8277 | 250 | 0 | 0.87954 |
| CIFAR10 | resnet9 | poisoning | 2000 | 3 | 1000 | 0.025 | FlippingInfluence (n_tolerate=25, exact unlearn) | 0.556 | 0.504 | 0.5895 | 0.5637 | 0.8185 | 0.8295 | 250 | 0 | 0.8819 |
| CIFAR10 | resnet9 | interclasslabelswap | 2000 | 3 | 1000 | 0.025 | FlippingInfluence (n_tolerate=25, exact unlearn) | 0.516 | 0.516 | 0.477 | 0.5245 | Null | Null  | 250 | 0 | 0.83006 |
| CIFAR10 | resnet9 | interclasslabelswap | 2000 | 3 | 1000 | 0.025 | Naive, pretrainmodel | 0.0 | 101.0 | 0.701 | 0.7135 | Null | Null  | 0 | 27.430166348000007 | 0.90222 |
CIFAR10	  | resnet9	| interclasslabelswap	| 2000 | 3 | 1000	 | 0.025	| SwappingInfluence	(Y=3, exact unlearn) | 0.0	| 0.0 |	0.449	| 0.4505	| Null | Null	| 250	 | 0	| 0.66724 |

## Removed Samples

### Poisoning
- **FlippingInfluence**: 1337 (some randomness, but roughly within [1000, 2000], change n_torlerate does not affect the range of removed samples number)
- **InfluenceFunction**: 14161 
- **SpectralSignature**: 48726
- **ActivationClustering**: 18314 (some randomness, but roughly within [18000, 20000])
- **Naive**: 0

### InterclassLabelSwap
| dataset | model  | dataset_method       | forget_set_size | patch_size | pretrain_iters | pretrain_lr | unlearn_method                      | exp_name  | delete_acc | delete_err | manip_acc | test_acc | test_retain_acc | deletion_size | unlearn_time          | train_clean_acc |
|---------|--------|----------------------|-----------------|------------|----------------|-------------|-------------------------------------|-----------|------------|------------|------------|----------|-----------------|----------------|-----------------------|-----------------|
| CIFAR10 | resnet9 | interclasslabelswap | 2000            | 3          | 1000           | 0.025       | Naive                               | pretrainmodel | 0.0        | 101.0      | 0.701      | 0.7135   | 0.887625        | 0              | 27.430166348000007   | 0.90222         |
| CIFAR10 | resnet9 | interclasslabelswap | 2000            | 3          | 1000           | 0.025       | SwappingInfluence (threshold=50000) | unlearn       | 0.68       | 0.68       | 0.523      | 0.621    | 0.82925         | 250            | 0                     | 0.83846         |


