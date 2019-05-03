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

$python3  project_gls_placement.py
$python3  project_ocm_placement.py



Example:

runfile('C:/project_gls_placement.py')
==GREEDY_LONGEST_SUBCHAIN==
SERVER_ASCENDING=TRUE  (123)
SWITCHING_COST_PLACEMENT_FUNCTION=DISTRIBUTED METHOD
===============myChainRun= c1
===============myChainRun= c10
===============myChainRun= c2
===============myChainRun= c3
===============myChainRun= c4
===============myChainRun= c5
===============myChainRun= c6
===============myChainRun= c7
===============myChainRun= c8
===============myChainRun= c9

The result of Server allocation.
Server       = s1 cpu_total    = c30 cpu_used     = u25.03 cpu_available= a1.9699999999999989 VNF Length   = l4.0
Server       = s10 cpu_total    = c20 cpu_used     = u7.59 cpu_available= a9.41 VNF Length   = l1.0
Server       = s11 cpu_total    = c27 cpu_used     = u0 cpu_available= a24 VNF Length   = l0
Server       = s12 cpu_total    = c20 cpu_used     = u7.59 cpu_available= a9.41 VNF Length   = l1.0
Server       = s13 cpu_total    = c25 cpu_used     = u21.91 cpu_available= a0.08999999999999986 VNF Length   = l3.0
Server       = s14 cpu_total    = c18 cpu_used     = u13.03 cpu_available= a1.9700000000000006 VNF Length   = l4.0
Server       = s15 cpu_total    = c29 cpu_used     = u25.03 cpu_available= a0.9699999999999989 VNF Length   = l4.0
Server       = s2 cpu_total    = c29 cpu_used     = u25.03 cpu_available= a0.9699999999999989 VNF Length   = l4.0
Server       = s3 cpu_total    = c31 cpu_used     = u25.03 cpu_available= a2.969999999999999 VNF Length   = l4.0
Server       = s4 cpu_total    = c21 cpu_used     = u17.03 cpu_available= a0.9699999999999989 VNF Length   = l4.0
Server       = s5 cpu_total    = c26 cpu_used     = u0 cpu_available= a24 VNF Length   = l0
Server       = s6 cpu_total    = c25 cpu_used     = u21.91 cpu_available= a0.08999999999999986 VNF Length   = l3.0
Server       = s7 cpu_total    = c23 cpu_used     = u0 cpu_available= a20 VNF Length   = l0
Server       = s8 cpu_total    = c21 cpu_used     = u9.03 cpu_available= a8.97 VNF Length   = l4.0
Server       = s9 cpu_total    = c31 cpu_used     = u25.03 cpu_available= a2.969999999999999 VNF Length   = l4.0

myChainCost= [('c1', '1.03'), ('c10', '1.5'), ('c2', '1.03'), ('c3', '1.5'), ('c4', '1.03'), ('c5', '1.03'), ('c6', '1.03'), ('c7', '1.03'), ('c8', '1.03'), ('c9', '1.03')]

Summary View.
('c1', 'b1', 'p1', 'v11', 'u3', 'o1', 's14', 'c18', 'u13.03', 'a1.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c1', 'b1', 'p1', 'v12', 'u3', 'o2', 's14', 'c18', 'u13.03', 'a1.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c1', 'b1', 'p1', 'v13', 'u3', 'o3', 's14', 'c18', 'u13.03', 'a1.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c1', 'b1', 'p1', 'v14', 'u3', 'o4', 's14', 'c18', 'u13.03', 'a1.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c10', 'b2', 'p1', 'v101', 'u7', 'o1', 's10', 'c20', 'u7.59', 'a9.41', 'l1.0', 'l1', 't7.0', 'cv0.59')
('c10', 'b2', 'p2', 'v102', 'u7', 'o2', 's13', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c10', 'b2', 'p2', 'v103', 'u7', 'o3', 's13', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c10', 'b2', 'p2', 'v104', 'u7', 'o4', 's13', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c2', 'b1', 'p1', 'v21', 'u6', 'o1', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c2', 'b1', 'p1', 'v22', 'u6', 'o2', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c2', 'b1', 'p1', 'v23', 'u6', 'o3', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c2', 'b1', 'p1', 'v24', 'u6', 'o4', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c3', 'b2', 'p1', 'v31', 'u7', 'o1', 's12', 'c20', 'u7.59', 'a9.41', 'l1.0', 'l1', 't7.0', 'cv0.59')
('c3', 'b2', 'p2', 'v32', 'u7', 'o2', 's6', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c3', 'b2', 'p2', 'v33', 'u7', 'o3', 's6', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c3', 'b2', 'p2', 'v34', 'u7', 'o4', 's6', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c4', 'b1', 'p1', 'v41', 'u6', 'o1', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c4', 'b1', 'p1', 'v42', 'u6', 'o2', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c4', 'b1', 'p1', 'v43', 'u6', 'o3', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c4', 'b1', 'p1', 'v44', 'u6', 'o4', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v51', 'u6', 'o1', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v52', 'u6', 'o2', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v53', 'u6', 'o3', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v54', 'u6', 'o4', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v61', 'u6', 'o1', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v62', 'u6', 'o2', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v63', 'u6', 'o3', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v64', 'u6', 'o4', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c7', 'b1', 'p1', 'v71', 'u4', 'o1', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c7', 'b1', 'p1', 'v72', 'u4', 'o2', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c7', 'b1', 'p1', 'v73', 'u4', 'o3', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c7', 'b1', 'p1', 'v74', 'u4', 'o4', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c8', 'b1', 'p1', 'v81', 'u6', 'o1', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c8', 'b1', 'p1', 'v82', 'u6', 'o2', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c8', 'b1', 'p1', 'v83', 'u6', 'o3', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c8', 'b1', 'p1', 'v84', 'u6', 'o4', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c9', 'b1', 'p1', 'v91', 'u2', 'o1', 's8', 'c21', 'u9.03', 'a8.97', 'l4.0', 'l4', 't8.0', 'cv1.03')
('c9', 'b1', 'p1', 'v92', 'u2', 'o2', 's8', 'c21', 'u9.03', 'a8.97', 'l4.0', 'l4', 't8.0', 'cv1.03')
('c9', 'b1', 'p1', 'v93', 'u2', 'o3', 's8', 'c21', 'u9.03', 'a8.97', 'l4.0', 'l4', 't8.0', 'cv1.03')
('c9', 'b1', 'p1', 'v94', 'u2', 'o4', 's8', 'c21', 'u9.03', 'a8.97', 'l4.0', 'l4', 't8.0', 'cv1.03')


runfile('C:/project_ocm_placement.py')
==OPERATIONAL SWITCHING COST MINIMIZATION==
SWITCHING_COST_PLACEMENT_FUNCTION=DISTRIBUTED METHOD
===============myChainRun= c1
===============myChainRun= c10
===============myChainRun= c2
===============myChainRun= c3
===============myChainRun= c4
===============myChainRun= c5
===============myChainRun= c6
===============myChainRun= c7
===============myChainRun= c8
===============myChainRun= c9

The result of Server allocation.
Server       = s1 cpu_total    = c30 cpu_used     = u25.03 cpu_available= a1.9699999999999989 VNF Length   = l4.0
Server       = s10 cpu_total    = c20 cpu_used     = u15.18 cpu_available= a1.8200000000000003 VNF Length   = l2.0
Server       = s11 cpu_total    = c27 cpu_used     = u0 cpu_available= a24 VNF Length   = l0
Server       = s12 cpu_total    = c20 cpu_used     = u9.03 cpu_available= a7.970000000000001 VNF Length   = l4.0
Server       = s13 cpu_total    = c25 cpu_used     = u21.91 cpu_available= a0.08999999999999986 VNF Length   = l3.0
Server       = s14 cpu_total    = c18 cpu_used     = u13.03 cpu_available= a2.9700000000000006 VNF Length   = l4.0
Server       = s15 cpu_total    = c29 cpu_used     = u25.03 cpu_available= a0.9699999999999989 VNF Length   = l4.0
Server       = s2 cpu_total    = c29 cpu_used     = u25.03 cpu_available= a0.9699999999999989 VNF Length   = l4.0
Server       = s3 cpu_total    = c31 cpu_used     = u25.03 cpu_available= a2.969999999999999 VNF Length   = l4.0
Server       = s4 cpu_total    = c21 cpu_used     = u17.03 cpu_available= a0.9699999999999989 VNF Length   = l4.0
Server       = s5 cpu_total    = c26 cpu_used     = u0 cpu_available= a23 VNF Length   = l0
Server       = s6 cpu_total    = c25 cpu_used     = u21.91 cpu_available= a0.08999999999999986 VNF Length   = l3.0
Server       = s7 cpu_total    = c23 cpu_used     = u0 cpu_available= a20 VNF Length   = l0
Server       = s8 cpu_total    = c21 cpu_used     = u0 cpu_available= a18 VNF Length   = l0
Server       = s9 cpu_total    = c31 cpu_used     = u25.03 cpu_available= a2.969999999999999 VNF Length   = l4.0

myChainCost= [('c1', '1.03'), ('c10', '1.5'), ('c2', '1.03'), ('c3', '1.5'), ('c4', '1.03'), ('c5', '1.03'), ('c6', '1.03'), ('c7', '1.03'), ('c8', '1.03'), ('c9', '1.48')]

Summary View.
('c1', 'b1', 'p1', 'v11', 'u3', 'o1', 's14', 'c18', 'u13.03', 'a2.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c1', 'b1', 'p1', 'v12', 'u3', 'o2', 's14', 'c18', 'u13.03', 'a2.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c1', 'b1', 'p1', 'v13', 'u3', 'o3', 's14', 'c18', 'u13.03', 'a2.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c1', 'b1', 'p1', 'v14', 'u3', 'o4', 's14', 'c18', 'u13.03', 'a2.9700000000000006', 'l4.0', 'l4', 't12.0', 'cv1.03')
('c10', 'b2', 'p1', 'v101', 'u7', 'o1', 's10', 'c20', 'u7.59', 'a9.41', 'l1.0', 'l1', 't7.0', 'cv0.59')
('c10', 'b2', 'p2', 'v102', 'u7', 'o2', 's13', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c10', 'b2', 'p2', 'v103', 'u7', 'o3', 's13', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c10', 'b2', 'p2', 'v104', 'u7', 'o4', 's13', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c2', 'b1', 'p1', 'v21', 'u6', 'o1', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c2', 'b1', 'p1', 'v22', 'u6', 'o2', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c2', 'b1', 'p1', 'v23', 'u6', 'o3', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c2', 'b1', 'p1', 'v24', 'u6', 'o4', 's15', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c3', 'b2', 'p1', 'v31', 'u7', 'o1', 's10', 'c20', 'u15.18', 'a1.8200000000000003', 'l2.0', 'l1', 't7.0', 'cv0.59')
('c3', 'b2', 'p2', 'v32', 'u7', 'o2', 's6', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c3', 'b2', 'p2', 'v33', 'u7', 'o3', 's6', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c3', 'b2', 'p2', 'v34', 'u7', 'o4', 's6', 'c25', 'u21.91', 'a0.08999999999999986', 'l3.0', 'l3', 't21.0', 'cv0.91')
('c4', 'b1', 'p1', 'v41', 'u6', 'o1', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c4', 'b1', 'p1', 'v42', 'u6', 'o2', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c4', 'b1', 'p1', 'v43', 'u6', 'o3', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c4', 'b1', 'p1', 'v44', 'u6', 'o4', 's2', 'c29', 'u25.03', 'a0.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v51', 'u6', 'o1', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v52', 'u6', 'o2', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v53', 'u6', 'o3', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c5', 'b1', 'p1', 'v54', 'u6', 'o4', 's1', 'c30', 'u25.03', 'a1.9699999999999989', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v61', 'u6', 'o1', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v62', 'u6', 'o2', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v63', 'u6', 'o3', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c6', 'b1', 'p1', 'v64', 'u6', 'o4', 's3', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c7', 'b1', 'p1', 'v71', 'u4', 'o1', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c7', 'b1', 'p1', 'v72', 'u4', 'o2', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c7', 'b1', 'p1', 'v73', 'u4', 'o3', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c7', 'b1', 'p1', 'v74', 'u4', 'o4', 's4', 'c21', 'u17.03', 'a0.9699999999999989', 'l4.0', 'l4', 't16.0', 'cv1.03')
('c8', 'b1', 'p1', 'v81', 'u6', 'o1', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c8', 'b1', 'p1', 'v82', 'u6', 'o2', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c8', 'b1', 'p1', 'v83', 'u6', 'o3', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c8', 'b1', 'p1', 'v84', 'u6', 'o4', 's9', 'c31', 'u25.03', 'a2.969999999999999', 'l4.0', 'l4', 't24.0', 'cv1.03')
('c9', 'b1', 'p1', 'v91', 'u2', 'o1', 's12', 'c20', 'u9.03', 'a7.970000000000001', 'l4.0', 'l4', 't8.0', 'cv1.03')
('c9', 'b1', 'p1', 'v92', 'u2', 'o2', 's12', 'c20', 'u9.03', 'a7.970000000000001', 'l4.0', 'l4', 't8.0', 'cv1.03')
('c9', 'b1', 'p1', 'v93', 'u2', 'o3', 's12', 'c20', 'u9.03', 'a7.970000000000001', 'l4.0', 'l4', 't8.0', 'cv1.03')
('c9', 'b1', 'p1', 'v94', 'u2', 'o4', 's12', 'c20', 'u9.03', 'a7.970000000000001', 'l4.0', 'l4', 't8.0', 'cv1.03')
