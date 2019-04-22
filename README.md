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

$python3  main_vnf_placement.py



Example:

An instance of Server
Server= s1
cpu_total= c20
cpu_used= u3
cpu_avail= a17
VNF length= l1
Server= s2
cpu_total= c20
cpu_used= u2
cpu_avail= a18
VNF length= l1

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
Service Chain ID= c1  Bell ID= b2  Partition ID= p1  VNF ID= v1  VNF CPU= u3  VNF Flow= o1  Server= s1  cpu_total= c20  cpu_used= u12.544038277174801  cpu_avail= a7.455961722825199  VNF Length on Server= l1  VNF Length on Partition= l1  Total Required CPU= t5.0  Switching Cost cv4.544038277174801
Service Chain ID= c1  Bell ID= b2  Partition ID= p1  VNF ID= v2  VNF CPU= u2  VNF Flow= o2  Server= s1  cpu_total= c20  cpu_used= u12.544038277174801  cpu_avail= a7.455961722825199  VNF Length on Server= l1  VNF Length on Partition= l1  Total Required CPU= t5.0  Switching Cost cv4.544038277174801
Service Chain ID= c2  Bell ID= b5  Partition ID= p1  VNF ID= v1  VNF CPU= u5  VNF Flow= o1  Server= s1  cpu_total= c20  cpu_used= u28.088076554349602  cpu_avail= a-8.088076554349602  VNF Length on Server= l1  VNF Length on Partition= l1  Total Required CPU= t11.0  Switching Cost cv4.544038277174801
Service Chain ID= c2  Bell ID= b5  Partition ID= p1  VNF ID= v3  VNF CPU= u4  VNF Flow= o2  Server= s1  cpu_total= c20  cpu_used= u28.088076554349602  cpu_avail= a-8.088076554349602  VNF Length on Server= l1  VNF Length on Partition= l1  Total Required CPU= t11.0  Switching Cost cv4.544038277174801
Service Chain ID= c2  Bell ID= b5  Partition ID= p1  VNF ID= v4  VNF CPU= u2  VNF Flow= o3  Server= s1  cpu_total= c20  cpu_used= u28.088076554349602  cpu_avail= a-8.088076554349602  VNF Length on Server= l1  VNF Length on Partition= l1  Total Required CPU= t11.0  Switching Cost cv4.544038277174801

The result of Server allocation.
Server       = s1
cpu_total    = c20
cpu_used     = u28.088076554349602
cpu_available= a-8.088076554349602
VNF Length   = l1
Server       = s2
cpu_total    = c20
cpu_used     = u2
cpu_available= a18
VNF Length   = l1

Summary View.
[[[[('c1', 'b2', 'p1', 'v1', 'u3', 'o1', 's1', 'c20', 'u12.544038277174801', 'a7.455961722825199', 'l1', 'l1', 't5.0', 'cv4.544038277174801'), 
('c1', 'b2', 'p1', 'v2', 'u2', 'o2', 's1', 'c20', 'u12.544038277174801', 'a7.455961722825199', 'l1', 'l1', 't5.0', 'cv4.544038277174801')]]], [[[
('c2', 'b5', 'p1', 'v1', 'u5', 'o1', 's1', 'c20', 'u28.088076554349602', 'a-8.088076554349602', 'l1', 'l1', 't11.0', 'cv4.544038277174801'), 
('c2', 'b5', 'p1', 'v3', 'u4', 'o2', 's1', 'c20', 'u28.088076554349602', 'a-8.088076554349602', 'l1', 'l1', 't11.0', 'cv4.544038277174801'), 
('c2', 'b5', 'p1', 'v4', 'u2', 'o3', 's1', 'c20', 'u28.088076554349602', 'a-8.088076554349602', 'l1', 'l1', 't11.0', 'cv4.544038277174801')]]]]
