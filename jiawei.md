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
| Metric            | Naive              | SpectralSignature | InfluenceFunction (threshold: -10.0) | InfluenceFunction (threshold: 0.0) | ActivationClustering |
|-------------------|--------------------|-------------------|----------------------|-------------------|----------------------|
| dataset           | CIFAR10            | CIFAR10           | CIFAR10              | CIFAR10           | CIFAR10              |
| model             | resnet9            | resnet9           | resnet9              | resnet9           | resnet9              |
| dataset_method    | poisoning          | poisoning         | poisoning            | poisoning         | poisoning            |
| forget_set_size   | 500                | 500               | 500                  | 500               | 500                  |
| patch_size        | 3                  | 3                 | 3                    | 3                 | 3                    |
| pretrain_iters    | 1000               | 1000              | 1000                 | 1000              | 1000                 |
| pretrain_lr       | 0.025              | 0.025             | 0.025                | 0.025             | 0.025                |
| unlearn_method    | Naive              | SpectralSignature | InfluenceFunction-10 | InfluenceFunction | ActivationClustering |
| exp_name          | pretrainmodel      | unlearn           | unlearn              | unlearn           | unlearn              |
| train_iters       | Null               | Null              | Null                 | Null              | Null                 |
| k                 | Null               | Null              | Null                 | Null              | Null                 |
| factor            | Null               | Null              | Null                 | Null              | Null                 |
| kd_T              | Null               | Null              | Null                 | Null              | Null                 |
| gamma             | Null               | Null              | Null                 | Null              | Null                 |
| alpha             | Null               | Null              | Null                 | Null              | Null                 |
| msteps            | Null               | Null              | Null                 | Null              | Null                 |
| delete_acc        | 0.0                | 0.592             | 0.352                | 0.404             | 0.2                  |
| delete_err        | 101.0              | 0.444             | 0.732                | 0.66              | 0.88                 |
| manip_acc         | 0.192              | 0.592             | 0.358                | 0.412             | 0.228                |
| test_acc          | 0.1969             | 0.5665            | 0.3302               | 0.3917            | 0.2136               |
| manip_clean_acc   | 0.836              | 0.796             | 0.81                 | 0.812             | 0.754                |
| test_clean_acc    | 0.857              | 0.7969            | 0.8044               | 0.8023            | 0.762                |
| test_retain_acc   | Null               | Null              | Null                 | Null              | Null                 |
| deletion_size     | 0                  | 500               | 250                  | 250               | 250                  |
| unlearn_time      | 23.9510807         | 0                 | 0                    | 0                 | 0                    |
| train_clean_acc   | 0.91274            | 0.84192           | 0.83422              | 0.83382           | 0.81254              |

## April 14
Implement a Influence method based on Influence function threshold in the benchmark.
