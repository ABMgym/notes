# Dataset Results
| Dataset | Model   | Dataset Method | Forget Set Size | Patch Size | Pretrain Iters | Pretrain LR | Unlearn Method     | Delete Acc | Delete Err | Manip Acc | Test Acc | Manip Clean Acc | Test Clean Acc | Deletion Size | Unlearn Time           | Train Clean Acc |
|---------|---------|----------------|-----------------|------------|----------------|-------------|--------------------|------------|------------|----------|-----------------|----------------|-----------------|----------------|-------------------------|----------------|
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | InfluenceFunction  | 0.288      | 0.796      | 0.2875    | 0.2934   | 0.791            | 0.7978           | 0            | 0                       | 0.83338        |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | Naive              | 0.0        | 101.0      | 0.162     | 0.1499   | 0.855            | 0.8576          | 0              | 24.713809919999996       | 0.90816        |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | ActivationClustering | 0.124      | 0.96       | 0.1555    | 0.1418   | 0.806            | 0.7921            | 0            | 0                       | 0.8324         |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | SpectralSignature  | 0.156      | 0.92       | 0.187     | 0.1686   | 0.7795           | 0.767           | 0            | 0                       | 0.79978        |
CIFAR10	  | resnet9	| poisoning	     | 2000	           | 3	        | 1000	         | 0.025	     | FlippingInfluence (n_tolerate=25)	| 0.28	   | 0.828	  | 0.301	   | 0.2727	   | 0.868	   | 0.8806	   | 250	     | 0	     | 0.93952    |
CIFAR10	  | resnet9	   | poisoning	 | 2000	           | 3	        | 1000	         | 0.025	     | FlippingInfluence (n_tolerate=25) |	0.26	   | 0.814	  | 0.278	   | 0.2739	   | 0.8685	   | 0.8703	   | 500	     | 0	     | 0.92778    |
CIFAR10	  | resnet9	   | poisoning	 | 2000	           | 3	        | 1000	         | 0.025	     | FlippingInfluence | 0.182     |	0.888	     | 0.2105	     | 0.2152	         | 0.8785	    | 0.8816	       | 500	     | 0	      | 0.93872    |

## Removed Samples

- **FlippingInfluence**: 1337 (some randomness, but roughly within [1000, 2000], change n_torlerate does not affect the range of removed samples number)
- **InfluenceFunction**: 14161 
- **SpectralSignature**: 48726
- **ActivationClustering**: 18314 (some randomness, but roughly within [18000, 20000])
- **Naive**: 0
