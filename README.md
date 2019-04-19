# csc8820-vnf-placement
csc8820-vnf-placement

Introduction

Virtual Network Function (VNF) chain is a chain of different network functions (NF). Each network function is an application level service such as Firewall, Intrusion Detection System, Encoder, etc, .... Data packets may flow through these services in an established order. A specific order of these network functions/services is called a service chain. Virtualization technique allows the service chain to be deployed into the cloud in a flexible way that can satisfy different objectives such as minimizing deployment cost, or maximizing the service performance.




Run main.py

runfile('C:/data/an/project/main.py', wdir='C:/data/an/project')
An instance of Server : server_location_id=Site_1
 server_topology=[('s1', 'c10', 'u3', 'a7'), ('s2', 'c10', 'u2', 'a8')]

An instance of Server
Server= s1
cpu_total= c10
cpu_used= u3
cpu_avail= a7
Server= s2
cpu_total= c10
cpu_used= u2
cpu_avail= a8
An instance of Service_Chain : service_chain_location_id=Site_1
 service_chain_topology=[('c1', 'v1', 'u3', 'o1'), ('c1', 'v2', 'u2', 'o2'), ('c2', 'v1', 'u5', 'o1'), ('c2', 'v3', 'u4', 'o2'), ('c2', 'v4', 'u2', 'o3')]

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
An instance of partition_chain : partition_chain_location_id=Site_1
 partition_chain_topology=[('c1', 'b1', 'p1', 'v1', 'u3', 'o1'), ('c1', 'b1', 'p2', 'v2', 'u2', 'o2'), ('c1', 'b2', 'p1', 'v1', 'u3', 'o1'), ('c1', 'b2', 'p1', 'v2', 'u2', 'o2'), ('c2', 'b1', 'p1', 'v1', 'u5', 'o1'), ('c2', 'b1', 'p2', 'v3', 'u4', 'o2'), ('c2', 'b1', 'p3', 'v4', 'u2', 'o3'), ('c2', 'b2', 'p1', 'v1', 'u5', 'o1'), ('c2', 'b2', 'p1', 'v3', 'u4', 'o2'), ('c2', 'b2', 'p2', 'v4', 'u2', 'o3'), ('c2', 'b3', 'p1', 'v1', 'u5', 'o1'), ('c2', 'b3', 'p2', 'v3', 'u4', 'o2'), ('c2', 'b3', 'p2', 'v4', 'u2', 'o3'), ('c2', 'b4', 'p1', 'v1', 'u5', 'o1'), ('c2', 'b4', 'p2', 'v3', 'u4', 'o2'), ('c2', 'b4', 'p1', 'v4', 'u2', 'o3'), ('c2', 'b5', 'p1', 'v1', 'u5', 'o1'), ('c2', 'b5', 'p1', 'v3', 'u4', 'o2'), ('c2', 'b5', 'p1', 'v4', 'u2', 'o3')]

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
