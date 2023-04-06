# Python-Basics

The term "distributed" is used to specify whether to run the program on a single machine with multiple graphics cards. The terminal command only supports Ubuntu. "CUDA_VISIBLE_DEVICES" is used to specify the graphics card on Ubuntu.

On Windows systems, DP mode is used by default, which calls all graphics cards and does not support DDP.

DP mode:

Set "distributed = False"
Enter "CUDA_VISIBLE_DEVICES=0,1 python train.py" in the terminal
DDP mode:

Set "distributed = True"
Enter "CUDA_VISIBLE_DEVICES=0,1 python -m torch.distributed.launch --nproc_per_node=2 train.py" in the terminal.
