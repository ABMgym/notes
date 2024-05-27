# Dataset Results

| Dataset | Model   | Dataset Method | Forget Set Size | Patch Size | Pretrain Iters | Pretrain LR | Unlearn Method     | Exp Name      | Train Iters | k   | Factor | kd_T | Gamma | Alpha | msteps | Delete Acc | Delete Err | Manip Acc | Test Acc | Manip Clean Acc | Test Clean Acc | Test Retain Acc | Deletion Size | Unlearn Time           | Train Clean Acc |
|---------|---------|----------------|-----------------|------------|----------------|-------------|--------------------|---------------|-------------|-----|--------|-------|-------|-------|--------|------------|------------|-----------|----------|-----------------|----------------|-----------------|----------------|-------------------------|----------------|
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | InfluenceFunction  | unlearn       | Null        | Null| Null   | Null  | Null  | Null  | Null   | 0.288      | 0.796      | 0.2875    | 0.2934   | 0.791            | 0.7978          | Null            | 250            | 0                       | 0.83338        |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | Naive              | pretrainmodel | Null        | Null| Null   | Null  | Null  | Null  | Null   | 0.0        | 101.0      | 0.162     | 0.1499   | 0.855            | 0.8576          | Null            | 0              | 24.713809919999996       | 0.90816        |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | FlippingInfluence  | unlearn       | Null        | Null| Null   | Null  | Null  | Null  | Null   | 0.164      | 0.928      | 0.142     | 0.144    | 0.877            | 0.8765          | Null            | 250            | 0                       | 0.93562        |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | ActivationClustering | unlearn     | Null        | Null| Null   | Null  | Null  | Null  | Null   | 0.124      | 0.96       | 0.1555    | 0.1418   | 0.806            | 0.7921          | Null            | 250            | 0                       | 0.8324         |
| CIFAR10 | resnet9 | poisoning      | 2000            | 3          | 1000           | 0.025       | SpectralSignature  | unlearn       | Null        | Null| Null   | Null  | Null  | Null  | Null   | 0.156      | 0.92       | 0.187     | 0.1686   | 0.7795           | 0.767           | Null            | 250            | 0                       | 0.79978        |

## Removed Samples

- **FlippingInfluence**: 1337 (some randomness, but roughly within [1000, 1500], change n_torlerate does not affect the range of removed samples number)
- **InfluenceFunction**: 14161 
- **SpectralSignature**: 48726
- **ActivationClustering**: 18314 (some randomness, but roughly within [18000, 20000])
- **Naive**: 0

