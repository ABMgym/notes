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
Collect results of 2 baselines: ActivationClustering and SpectralSignature.
| Attribute         | SpectralSignature                        | ActivationClustering                    |
|-------------------|------------------------------------------|------------------------                   |
| **Dataset**           | CIFAR10                                  | CIFAR10                                  |
| **Model**             | resnet9                                  | resnet9                                  |
| **Dataset Method**    | poisoning                                | poisoning                                |
| **Forget Set Size**   | 500                                      | 500                                      |
| **Patch Size**        | 3                                        | 3                                        |
| **Pretrain Iters**    | 1000                                     | 1000                                     |
| **Pretrain LR**       | 0.025                                    | 0.025                                    |
| **Unlearn Method**    | Naive                                    | Naive                                    |
| **Exp Name**          | pretrainmodel                            | pretrainmodel                            |
| **Train Iters**       | Null                                     | Null                                     |
| **k**                 | Null                                     | Null                                     |
| **Factor**            | Null                                     | Null                                     |
| **kd_T**              | Null                                     | Null                                     |
| **Gamma**             | Null                                     | Null                                     |
| **Alpha**             | Null                                     | Null                                     |
| **msteps**            | Null                                     | Null                                     |
| **Delete Acc**        | 0.0                                      | 0.0                                      |
| **Delete Err**        | 101.0                                    | 101.0                                    |
| **Manip Acc**         | 0.192                                    | 0.196                                    |
| **Test Acc**          | 0.1969                                   | 0.2134                                   |
| **Manip Clean Acc**   | 0.836                                    | 0.858                                    |
| **Test Clean Acc**    | 0.857                                    | 0.8547                                   |
| **Test Retain Acc**   | Null                                     | Null                                     |
| **Deletion Size**     | 0                                        | 0                                        |
| **Unlearn Time**      | 24.40451660300000                        | 52.83270964700000                        |
| **Train Clean Acc**   | 0.91274                                  | 0.90858                                
