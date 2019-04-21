# csc8820-vnf-placement
csc8820-vnf-placement

Introduction


Virtual Network Function (VNF) chain is a chain of different network functions (NF). Each network function is an application level service such as Firewall, Intrusion Detection System, Encoder, etc, .... Data packets may flow through these services in an established order. A specific order of these network functions/services is called a service chain. Virtualization technique allows the service chain to be deployed into the cloud in a flexible way that can satisfy different objectives such as minimizing deployment cost, or maximizing the service performance.


Given: 

a) Set of physical servers K
b) Sequence of service chains ɸ



Goal: 

Minimized the switching CPU cost.
Per each service chain in the sequence, find partition of chain called sub-chain
Allocate each sub-chain on server in a way to minimized the total switch cost.


Methodology

OPTIMIZED OPERATIONAL COST PLACEMENT
Goes over all partitions of service chain, grouping subsets of VNFs. For each partition in set, use the switching cost model to find the cost placement on each server. Then find an optimal placement of this partition by finding the maximal matching between sub-chains and servers.



Run 

$python3  main_ocm_placement.py



Example:

An instance of Server
Server= s1
cpu_total= c20
cpu_used= u3
cpu_avail= a17
Server= s2
cpu_total= c20
cpu_used= u2
cpu_avail= a18

An instance of Service Chain
Service Chain ID= c1
VNF ID          = v1
VNF required CPU= u3
VNF Flow order  = o1
Service Chain ID= c1
VNF ID          = v2
VNF required CPU= u2
VNF Flow order  = o2
Service Chain ID= c2
VNF ID          = v1
VNF required CPU= u5
VNF Flow order  = o1
Service Chain ID= c2
VNF ID          = v3
VNF required CPU= u4
VNF Flow order  = o2
Service Chain ID= c2
VNF ID          = v4
VNF required CPU= u2
VNF Flow order  = o3

An instance of Partition Chain
Service Chain ID= c1  Bell ID= b1  Partition ID= p1  VNF ID= v1  VNF CPU= u3  VNF Flow= o1
Service Chain ID= c1  Bell ID= b1  Partition ID= p2  VNF ID= v2  VNF CPU= u2  VNF Flow= o2
Service Chain ID= c1  Bell ID= b2  Partition ID= p1  VNF ID= v1  VNF CPU= u3  VNF Flow= o1
Service Chain ID= c1  Bell ID= b2  Partition ID= p1  VNF ID= v2  VNF CPU= u2  VNF Flow= o2
Service Chain ID= c2  Bell ID= b1  Partition ID= p1  VNF ID= v1  VNF CPU= u5  VNF Flow= o1
Service Chain ID= c2  Bell ID= b1  Partition ID= p2  VNF ID= v3  VNF CPU= u4  VNF Flow= o2
Service Chain ID= c2  Bell ID= b1  Partition ID= p3  VNF ID= v4  VNF CPU= u2  VNF Flow= o3
Service Chain ID= c2  Bell ID= b2  Partition ID= p1  VNF ID= v1  VNF CPU= u5  VNF Flow= o1
Service Chain ID= c2  Bell ID= b2  Partition ID= p1  VNF ID= v3  VNF CPU= u4  VNF Flow= o2
Service Chain ID= c2  Bell ID= b2  Partition ID= p2  VNF ID= v4  VNF CPU= u2  VNF Flow= o3
Service Chain ID= c2  Bell ID= b3  Partition ID= p1  VNF ID= v1  VNF CPU= u5  VNF Flow= o1
Service Chain ID= c2  Bell ID= b3  Partition ID= p2  VNF ID= v3  VNF CPU= u4  VNF Flow= o2
Service Chain ID= c2  Bell ID= b3  Partition ID= p2  VNF ID= v4  VNF CPU= u2  VNF Flow= o3
Service Chain ID= c2  Bell ID= b4  Partition ID= p1  VNF ID= v1  VNF CPU= u5  VNF Flow= o1
Service Chain ID= c2  Bell ID= b4  Partition ID= p2  VNF ID= v3  VNF CPU= u4  VNF Flow= o2
Service Chain ID= c2  Bell ID= b4  Partition ID= p1  VNF ID= v4  VNF CPU= u2  VNF Flow= o3
Service Chain ID= c2  Bell ID= b5  Partition ID= p1  VNF ID= v1  VNF CPU= u5  VNF Flow= o1
Service Chain ID= c2  Bell ID= b5  Partition ID= p1  VNF ID= v3  VNF CPU= u4  VNF Flow= o2
Service Chain ID= c2  Bell ID= b5  Partition ID= p1  VNF ID= v4  VNF CPU= u2  VNF Flow= o3

Print the placement result on screen

The result of Service Chain on Servers.
Service Chain ID= c1  Bell ID= b1  Partition ID= p1  VNF ID= v1  VNF CPU= u3  VNF Flow= o1  Server= s2  cpu_total= c20  cpu_used= u5  cpu_avail= a15
Service Chain ID= c1  Bell ID= b1  Partition ID= p2  VNF ID= v2  VNF CPU= u2  VNF Flow= o2  Server= s2  cpu_total= c20  cpu_used= u7  cpu_avail= a13
Service Chain ID= c2  Bell ID= b1  Partition ID= p1  VNF ID= v1  VNF CPU= u5  VNF Flow= o1  Server= s1  cpu_total= c20  cpu_used= u8  cpu_avail= a12
Service Chain ID= c2  Bell ID= b1  Partition ID= p2  VNF ID= v3  VNF CPU= u4  VNF Flow= o2  Server= s1  cpu_total= c20  cpu_used= u12  cpu_avail= a8
Service Chain ID= c2  Bell ID= b1  Partition ID= p3  VNF ID= v4  VNF CPU= u2  VNF Flow= o3  Server= s2  cpu_total= c20  cpu_used= u9  cpu_avail= a11

The result of Server acclocation.
Server       = s1
cpu_total    = c20
cpu_used     = u12
cpu_available= a8
Server       = s2
cpu_total    = c20
cpu_used     = u9
cpu_available= a11

Summary View.
[[[[('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's2', 'c20', 'u5', 'a15')], [('c1', 'b1', 'p2', 'v2', 'u2', 'o2', 's2', 'c20', 'u7', 'a13')]]], [[[('c2', 'b1', 'p1', 'v1', 'u5', 'o1', 's1', 'c20', 'u8', 'a12')], [('c2', 'b1', 'p2', 'v3', 'u4', 'o2', 's1', 'c20', 'u12', 'a8')], [('c2', 'b1', 'p3', 'v4', 'u2', 'o3', 's2', 'c20', 'u9', 'a11')]]]]
[]
