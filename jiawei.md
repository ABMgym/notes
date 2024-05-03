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
