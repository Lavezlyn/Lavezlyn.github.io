---
title: "A taste to slurm"
subtitle: How to train your model on a cluster?
categories:
  - Blog
tags:
  - slurm
  - machine learning
toc: true
toc_sticky: true
comments: true
---

What is slurm? **SLURM** (Simple Linux Utility for Resource Management) is an open-source job scheduler for Linux and Unix-like operating systems. It is widely used in high-performance computing (HPC) environments to manage and allocate resources such as CPU, memory, and storage to various jobs or tasks submitted by users. SLURM allows for efficient utilization of computational resources, ensuring that jobs are executed in a timely and orderly manner.

<!--more-->

Check [documentation](https://slurm.schedmd.com/documentation.html) for more info. 

Recently I am fine-tuning some transformer models on [Multi-NLI](https://huggingface.co/datasets/nyu-mll/multi_nli) dataset. :hugs: At first I was troubled by limited computational resources I could access. Then it dawned on me that I could take advantage of clusters provided for AI students, after all, an RTX-3090 might be a good rescue. :thinking:

However, beginners are often time clumsy when it comes to building conda environments, debugging on virtual machines, allocating resources and supervising training process. Things do get ugly! :dizzy_face:

Let's check out what I have learned. Hope this article can serve as a quick and convenient intro to hands-on training experience with slurm.

## Quick Start

### Connect to the cluster

``` bash
$ ssh -p <ID> username@xxx.xxx.xxx.xx
```

Enter specific username and IP.

### Allocate GPU

Once you are on, run this command to invoke slurm.
```bash
$ module load slurm
```
Below are some useful commands.
```bash
$ sinfo # check out available GPUs
$ sacctmgr show qos # see QoS
$ squeue # see currently running jobs
$ scancel <job_id> # cancel a job
```

You need to name arguments in order to allocate runtime resources, e.g.:
``` bash
$ srun --partition=IAI_SLURM_3090 --nodes 1 --gres=gpu:1 --cpus-per-task=10 --qos=debug --time 1:00:00 --comment="demo" --pty bash
```
QoS stands for **Quality of Service**, time limits the maximum runtime, comments declares job's name.
Other argument names are straight-forward.

### Submit jobs

You need a script that tells the terminal how to run you procedure. Let's call it ```run.sh```. Inside it we write

``` 
#! /bin/bash

#SBATCH --partition=IAI_SLURM_3090
#SBATCH --job-name=sbatch_example
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --qos=singlegpu
#SBATCH --cpus-per-task=10
#SBATCH --time 12:00:00
python train.py
```
Then run the following command.

``` bash
$ sbatch run.sh
```

Congrats! You are done! :blush:

### Takeaway

* Build your conda environment beforehand, make sure to install all dependencies.
* Debug on small subset of the dataset, ensure your codes are error-free before submission.
* Use tools such as WandB to log and plot training metrics, as well as monitor your progress conveniently.

## More to learn

* Files transfer, use ```scp``` or ```rsync```.
* Run jobs on multiple clusters.

## More Info

### Slurm

* https://researchcomputing.princeton.edu/support/knowledge-base/pytorch 
* http://faculty.bicmr.pku.edu.cn/~wenzw/pages/slurm.html
* https://docs.hpc.sjtu.edu.cn/index.html

### Pytorch with slurm 

* [Overview](https://pytorch.org/tutorials/beginner/ddp_series_intro.html)
* [Single-node-multiple-GPU DDP](https://pytorch.org/tutorials/beginner/ddp_series_multigpu.html)
* [Multiple nodes](https://pytorch.org/tutorials/intermediate/ddp_series_multinode.html)