# csc8820-vnf-placement
csc8820-vnf-placement

Introduction

Virtual Network Function (VNF) chain is a chain of different network functions (NF). Each network function is an application level service such as Firewall, Intrusion Detection System, Encoder, etc, .... Data packets may flow through these services in an established order. A specific order of these network functions/services is called a service chain. Virtualization technique allows the service chain to be deployed into the cloud in a flexible way that can satisfy different objectives such as minimizing deployment cost, or maximizing the service performance.


Given: 
a) Set of physical servers K
b) Sequence of service chains ɸ



Goal: Minimized the switching CPU cost.
Per each service chain in the sequence, find partition of chain called sub-chain
Allocate each sub-chain on server in a way to minimized the total switch cost.


Methodology
OPTIMIZED OPERATIONAL COST PLACEMENT
Goes over all partitions of service chain, grouping subsets of VNFs. For each partition in set, use the switching cost model to find the cost placement on each server. Then find an optimal placement of this partition by finding the maximal matching between sub-chains and servers.



Run 
$python3 main.py
