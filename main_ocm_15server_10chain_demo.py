# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:58:06 2019
Georgia State University
CSC8820
@author: Mart Panichvatana 
@author: Xiang Li (supplying the Cost Swtiching Calculation)

"""

import random
import math

def ext1(input):
    return (input[1:])

def m1(input):
    return float(input[1:])

def m2(input):
    return float(input[2:])

def madd(input, add):
    return (input[0]+str(float(input[1:])+float(add)))
    
def mdel(input, delete):
    return (input[0]+str(float(input[1:])-float(delete)))    
        
class subchain:
    
    # Subchain class 
    # phin: # of VNFs
    # phip: the amount of packets to process
    # ovs_type: kernel or DPDK
    # placement_function: g or d
    # packet_size: 100 or 1500
    
    def __init__(self, phin = 25, phip = 10000, ovs_type = 'kernel', placement_function = 'g', packet_size = 100):
        self.phin = phin
        self.phip = phip
        self.ovs_type = ovs_type
        self.placement_function = placement_function
        self.packet_size = packet_size
        self.get_constant()
        self.f = self.F()
        
 #       phip = 1000, ovs_type = 'kernel', placement_function = 'g', packet_size = 100)    
 #       if self.ovs_type == 'kernel' and self.placement_function == 'g' and self.packet_size == 100:
 #           self.alpha = 0.586
 #           self.beta = 0.858
 #           self.gamma = -1.789
            
    def get_constant(self):
        if self.ovs_type == 'kernel' and self.placement_function == 'g' and self.packet_size == 100:
            self.alpha = 0.586
            self.beta = 0.858
            self.gamma = -1.789
        elif self.ovs_type == 'kernel' and self.placement_function == 'g' and self.packet_size == 1500:
            self.alpha = 0.752
            self.beta = 0.979
            self.gamma = -3.856
        elif self.ovs_type == 'kernel' and self.placement_function == 'd' and self.packet_size == 100:
            self.alpha = 0.660
            self.beta = 0.243
            self.gamma = -2.661
        elif self.ovs_type == 'kernel' and self.placement_function == 'd' and self.packet_size == 1500:
            self.alpha = 1.009
            self.beta = 0.268
            self.gamma = -7.176
        elif self.ovs_type == 'DPDK' and self.placement_function == 'g' and self.packet_size == 100:
            self.alpha = 0.370
            self.beta = 0.467
            self.gamma = 1.543
        elif self.ovs_type == 'DPDK' and self.placement_function == 'g' and self.packet_size == 1500:
            self.alpha = 0.478
            self.beta = 0.578
            self.gamma = 0.194
        elif self.ovs_type == 'DPDK' and self.placement_function == 'd' and self.packet_size == 100:
            self.alpha = 0.217
            self.beta = 0.091
            self.gamma = 3.795
        elif self.ovs_type == 'DPDK' and self.placement_function == 'd' and self.packet_size == 1500:
            self.alpha = 0.157
            self.beta = 0.109
            self.gamma = 4.718
            
    def F(self):
        
        # Compute the cost of this subchain
        
        self.logc = self.alpha * math.log(self.phin) + self.beta * math.log(self.phip) + self.gamma
        return self.logc
    
    def concurrent_F(self,r):
        
        # compute the cost of this subchain concurrent r times
        
        self.logc = self.alpha * math.log(self.phin*r) + self.beta * math.log(self.phip) + self.gamma
        return self.logc
    
    def get_delta(self,r):
        
        # compute the switching cost delta
        
        self.concur_f = self.concurrent_F(r)
        self.delta = r * self.f - self.concur_f
        return self.delta
    

class multiple_subchain:
    
    # class of multiple subchains
    
    def __init__(self, subchain_list):
        self.r = len(subchain_list)
        self.subchain_list = subchain_list
        self.get_f_list()
        self.get_delta_list()
        
    def get_delta_list(self):
        self.delta_list = []
        for i in range(self.r):
            delta = self.subchain_list[i].get_delta(self.r)
            self.delta_list.append(delta)
            
    def get_f_list(self):
        self.f_list = []
        for i in range(self.r):
            f = self.subchain_list[i].f
            self.f_list.append(f)
            
    def get_cost(self):
        self.cost = sum(self.f_list)-(self.r-1)*sum(self.delta_list)/self.r
        return(self.cost)
        
        
        
        
class Server:
    """
    A Class to keep track of an instance of a Server.

    An instance has at least the following attributes.
    ========== ================================================================
    Attribute  Description
    ========== ================================================================
    server_location_id   Server Location by ID
    server_topology   Resource
    ========== ================================================================
    Example of Resource
        server_topology = [
                 ('s1', 'c10', 'u3','a7',),
                 ('s2', 'c10', 'u2','a8',),
                ]
    """

    
    server_topology = []

    def __init__(self, location, server_topology):
        self.server_location_id = location
        self.server_topology = server_topology

    def print_all_list(self):
        print ("") 
        print ("An instance of Server") 
        for a, b, c, d, e in self.server_topology :
            print ("Server=", ext1(a))
            print ("cpu_total=", ext1(b))            
            print ("cpu_used=", ext1(c))       
            print ("cpu_avail=", ext1(d))       
            print ("VNF length=", ext1(e))                             
    
    def __str__(self):
        return "An instance of Server : server_location_id=%s\n server_topology=%s\n" % \
                (self.server_location_id, self.server_topology)
       
class Service_Chain:
    """
    A Class to keep track of an instance of a Service_Chain.

    An instance has at least the following attributes.
    ========== ================================================================
    Attribute  Description
    ========== ================================================================
    service_chain_location_id   Service_Chain Location by ID
    service_chain_topology   Resource
    ========== ================================================================
    Example of Resource
            service_chain_topology = [
                     ('c1', 'v1', 'u3','o1',),
                     ('c1', 'v2', 'u2','o2',),
                     ('c2', 'v1', 'u5','o1',),
                     ('c2', 'v3', 'u4','o2',),
                     ('c2', 'v4', 'u2','o3',),
                    ]
    """

    
    service_chain_topology = []

    def __init__(self, location, service_chain_topology):
        self.service_chain_location_id = location
        self.service_chain_topology = service_chain_topology

    def print_all_list(self):
        print ("") 
        print ("An instance of Service Chain") 
        for a, b, c, d in self.service_chain_topology :
            print ("Service Chain ID=", ext1(a))
            print ("VNF ID          =", ext1(b))            
            print ("VNF required CPU=", ext1(c))       
            print ("VNF Flow order  =", ext1(d))       
            
    def __str__(self):
        return "An instance of Service_Chain : service_chain_location_id=%s\n service_chain_topology=%s\n" % \
                (self.service_chain_location_id, self.service_chain_topology)


class Partition_Chain:
    """
    A Class to keep track of an instance of a Partition_Chain.

    An instance has at least the following attributes.
    ========== ================================================================
    Attribute  Description
    ========== ================================================================
    partition_chain_location_id   Partition_Chain Location by ID
    partition_chain_topology   Resource
    ========== ================================================================
    Example of Resource
            partition_chain_topology = [
                     ('c1', 'b1', 'p1', 'v1', 'u3', 'o1',),
                     ('c1', 'b1', 'p2', 'v2', 'u2', 'o2',),
                     ('c1', 'b2', 'p1', 'v1', 'u3', 'o1',),
                     ('c1', 'b2', 'p1', 'v2', 'u2', 'o2',),
                     
                     ('c2', 'b1', 'p1', 'v1', 'u5', 'o1',),
                     ('c2', 'b1', 'p2', 'v3', 'u4', 'o2',),
                     ('c2', 'b1', 'p3', 'v4', 'u2', 'o3',),
                     ('c2', 'b2', 'p1', 'v1', 'u5', 'o1',),
                     ('c2', 'b2', 'p1', 'v3', 'u4', 'o2',),
                     ('c2', 'b2', 'p2', 'v4', 'u2', 'o3',),
                     ('c2', 'b3', 'p1', 'v1', 'u5', 'o1',),
                     ('c2', 'b3', 'p2', 'v3', 'u4', 'o2',),
                     ('c2', 'b3', 'p2', 'v4', 'u2', 'o3',),
                     ('c2', 'b4', 'p1', 'v1', 'u5', 'o1',),
                     ('c2', 'b4', 'p2', 'v3', 'u4', 'o2',),
                     ('c2', 'b4', 'p1', 'v4', 'u2', 'o3',),       
                     ('c2', 'b5', 'p1', 'v1', 'u5', 'o1',),
                     ('c2', 'b5', 'p1', 'v3', 'u4', 'o2',),
                     ('c2', 'b5', 'p1', 'v4', 'u2', 'o3',),             
                     
                     ]
    """

    
    partition_chain_topology = []

    def __init__(self, location, partition_chain_topology):
        self.partition_chain_location_id = location
        self.partition_chain_topology = partition_chain_topology

    def print_all_list(self):
        print ("") 
        print ("An instance of Partition Chain") 
        for a, b, c, d ,e , f in self.partition_chain_topology :
            print ("Service Chain ID=", ext1(a), \
                   " Bell ID        =", ext1(b), \
                   " Partition ID   =", ext1(c), \
                   " VNF ID         =", ext1(d), \
                   " VNF CPU        =", ext1(e), \
                   " VNF Flow       =", ext1(f))
 
    
    def __str__(self):
        return "An instance of partition_chain : partition_chain_location_id=%s\n partition_chain_topology=%s\n" % \
                (self.partition_chain_location_id, self.partition_chain_topology)
                
                
def load_topology(location):
    
    """
    server_topology
            (Data Structure list of tuples)
    =========== ===============================================================
    Attribute   Description
    =========== ===============================================================
    server_id   Server ID
    cpu_total   Total number of cpu
    cpu_used    Number of used cpu
    cpu_avail   Number of available cpu
    VNF_length  Number of VNF on server
    =========== ===============================================================
    """
    server_topology = [

#             ('s1', 'c20', 'u3','a10', 'l1' ),
#             ('s2', 'c20', 'u2','a10', 'l1' ),
            
             ('s1', 'c30', 'u0','a27', 'l1'),
             ('s2', 'c29', 'u0','a26', 'l1'),
             ('s3', 'c31', 'u0','a28', 'l1'),
             ('s4', 'c21', 'u0','a18', 'l1'),
             ('s5', 'c26', 'u0','a23', 'l1'),
             ('s6', 'c25', 'u0','a22', 'l1'),
             ('s7', 'c23', 'u0','a20', 'l1'),
             ('s8', 'c21', 'u0','a18', 'l1'),
             ('s9', 'c31', 'u0','a28', 'l1'),
             ('s10', 'c20', 'u0','a17','l1'),
             ('s11', 'c27', 'u0','a24', 'l1'),
             ('s12', 'c20', 'u0','a17', 'l1'),
             ('s13', 'c25', 'u0','a22', 'l1'),
             ('s14', 'c18', 'u0','a16', 'l1'),
             ('s15', 'c29', 'u0','a26', 'l1'),
             ]
    
    myServer = Server(location, server_topology)
#    server_topology = [
#             ('s1', 'c20', 'u3','a17', ),
#             ('s2', 'c20', 'u2','a18', ),
#            ]
#    myServer = Server(location, server_topology)
    
#       Anh's requirement
#        server_topology = [
#             ('s1', 'c30', 'u0','a27', 'l0'),
#             ('s2', 'c29', 'u0','a26', 'l0'),
#             ('s3', 'c31', 'u0','a28', 'l0'),
#             ('s4', 'c21', 'u0','a18', 'l0'),
#             ('s5', 'c26', 'u0','a23', 'l0'),
#             ('s6', 'c25', 'u0','a22', 'l0'),
#             ('s7', 'c23', 'u0','a20', 'l0'),
#             ('s8', 'c21', 'u0','a18', 'l0'),
#             ('s9', 'c31', 'u0','a28', 'l0'),
#             ('s10', 'c20', 'u0','a17','l0'),
#             ('s11', 'c27', 'u0','a24', 'l0'),
#             ('s12', 'c20', 'u0','a17', 'l0'),
#             ('s13', 'c25', 'u0','a22', 'l0'),
#             ('s14', 'c18', 'u0','a16', 'l0'),
#             ('s15', 'c29', 'u0','a26', 'l0'),
#             ]
#        

    """
    service_chain_topology
            (Data Structure list of tuples)
    =========== ===============================================================
    Attribute   Description
    =========== ===============================================================
    chain_id    Service Chain ID
    vnf_id      VNF ID
    vnf_cpu     VNF required CPU number
    vnf_flow_id VNF Flow order ID
    =========== ===============================================================
    """
    service_chain_topology = [
             ('c1', 'v11', 'u3','o1',),
             ('c1', 'v12', 'u3','o2',),
             ('c1', 'v13', 'u3','o3',),
             ('c1', 'v14', 'u3','o4',),
             
             ('c2', 'v21', 'u2','o1',),
             ('c2', 'v22', 'u3','o2',),
             ('c2', 'v23', 'u2','o3',),
             ('c2', 'v24', 'u2','o4',),
             
             ('c3', 'v31', 'u7','o1',),
             ('c3', 'v32', 'u7','o2',),
             ('c3', 'v33', 'u7','o3',),
             ('c3', 'v34', 'u7','o4',),
             
             ('c4', 'v41', 'u2','o1',),
             ('c4', 'v42', 'u2','o2',),
             ('c4', 'v43', 'u2','o3',),
             ('c4', 'v44', 'u2','o4',),
             
             ('c5', 'v51', 'u5','o1',),
             ('c5', 'v52', 'u5','o2',),
             ('c5', 'v53', 'u5','o3',),
             ('c5', 'v54', 'u5','o4',),
             
             ('c6', 'v61', 'u2','o1',),
             ('c6', 'v62', 'u2','o2',),
             ('c6', 'v63', 'u2','o3',),
             ('c6', 'v64', 'u2','o4',),
             
             ('c7', 'v71', 'u4','o1',),
             ('c7', 'v72', 'u4','o2',),
             ('c7', 'v73', 'u4','o3',),
             ('c7', 'v74', 'u4','o4',),
             
             ('c8', 'v81', 'u2','o1',),
             ('c8', 'v82', 'u2','o2',),
             ('c8', 'v83', 'u2','o3',),
             ('c8', 'v84', 'u2','o4',),
             
             ('c9', 'v91', 'u2','o1',),
             ('c9', 'v92', 'u2','o2',),
             ('c9', 'v93', 'u2','o3',),       
             ('c9', 'v94', 'u2','o4',),
             
             ('c10', 'v101', 'u7','o1',),
             ('c10', 'v102', 'u7','o2',),
             ('c10', 'v103', 'u7','o3',),    
             ('c10', 'v104', 'u7','o4',),              
            ]
    myService_Chain = Service_Chain(location, service_chain_topology)


#       For testing.
#             ('c1', 'v11', 'u1','o1',),
#             ('c1', 'v12', 'u2','o2',),
#             ('c1', 'v13', 'u3','o3',),
#             ('c1', 'v14', 'u3','o4',),
#             
#             ('c2', 'v21', 'u2','o1',),
#             ('c2', 'v22', 'u3','o2',),

    
    """
    partition_chain_topology
        (Data Structure list of tuples)
    =========== ===============================================================
    Attribute   Description
    =========== ===============================================================
    chain_id    Service Chain ID
    bell_id     Bell Number 
    partition_id    Partition ID  
    vnf_id      VNF ID
    vnf_cpu     VNF required CPU number
    vnf_flow_id VNF Flow order ID
    =========== ===============================================================
    Example: set 2 VNFs= [1, 2]
    [{1, 2}]
    [{2}, {1}]
    The Bell number is 2
    Example: set 3 VNFs= [1, 3, 4]
    [{1, 3, 4}]
    [{1, 4}, {3}]
    [{3, 4}, {1}]
    [{4}, {1, 3}]
    [{4}, {3}, {1}]
    The Bell number is 5
    """
    partition_chain_topology = [

#             ('c1', 'b1', 'p1', 'v11', 'u3','o1',),
#             ('c1', 'b1', 'p1', 'v12', 'u3','o2',),
#             ('c1', 'b1', 'p1', 'v13', 'u3','o3',),
#             ('c1', 'b1', 'p2', 'v14', 'u3','o4',),
#             ('c2', 'b1', 'p1', 'v21', 'u3','o1',),
#             ('c2', 'b1', 'p1', 'v22', 'u3','o2',),
#             ('c2', 'b1', 'p2', 'v23', 'u3','o3',),
#             ('c2', 'b1', 'p2', 'v24', 'u3','o4',),             
             
#            Anh's requirement
             ('c1', 'b1', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b1', 'p1', 'v12', 'u3','o2',),
             ('c1', 'b1', 'p1', 'v13', 'u3','o3',),
             ('c1', 'b1', 'p1', 'v14', 'u3','o4',),
 
             ('c1', 'b2', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b2', 'p2', 'v12', 'u3','o2',),
             ('c1', 'b2', 'p2', 'v13', 'u3','o3',),
             ('c1', 'b2', 'p2', 'v14', 'u3','o4',),

             ('c1', 'b3', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b3', 'p1', 'v12', 'u3','o2',),
             ('c1', 'b3', 'p2', 'v13', 'u3','o3',),
             ('c1', 'b3', 'p2', 'v14', 'u3','o4',),

             ('c1', 'b4', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b4', 'p2', 'v12', 'u3','o2',),
             ('c1', 'b4', 'p3', 'v13', 'u3','o3',),
             ('c1', 'b4', 'p3', 'v14', 'u3','o4',),
             
             ('c1', 'b5', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b5', 'p1', 'v12', 'u3','o2',),
             ('c1', 'b5', 'p1', 'v13', 'u3','o3',),
             ('c1', 'b5', 'p2', 'v14', 'u3','o4',),

             ('c1', 'b6', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b6', 'p2', 'v12', 'u3','o2',),
             ('c1', 'b6', 'p2', 'v13', 'u3','o3',),
             ('c1', 'b6', 'p3', 'v14', 'u3','o4',),

             ('c1', 'b7', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b7', 'p1', 'v12', 'u3','o2',),
             ('c1', 'b7', 'p3', 'v13', 'u3','o3',),
             ('c1', 'b7', 'p4', 'v14', 'u3','o4',),

             ('c1', 'b8', 'p1', 'v11', 'u3','o1',),
             ('c1', 'b8', 'p2', 'v12', 'u3','o2',),
             ('c1', 'b8', 'p3', 'v13', 'u3','o3',),
             ('c1', 'b8', 'p4', 'v14', 'u3','o4',),


             ('c2', 'b1', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b1', 'p1', 'v22', 'u6','o2',),
             ('c2', 'b1', 'p1', 'v23', 'u6','o3',),
             ('c2', 'b1', 'p1', 'v24', 'u6','o4',),
 
             ('c2', 'b2', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b2', 'p2', 'v22', 'u6','o2',),
             ('c2', 'b2', 'p2', 'v23', 'u6','o3',),
             ('c2', 'b2', 'p2', 'v24', 'u6','o4',),

             ('c2', 'b3', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b3', 'p1', 'v22', 'u6','o2',),
             ('c2', 'b3', 'p2', 'v23', 'u6','o3',),
             ('c2', 'b3', 'p2', 'v24', 'u6','o4',),

             ('c2', 'b4', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b4', 'p2', 'v22', 'u6','o2',),
             ('c2', 'b4', 'p3', 'v23', 'u6','o3',),
             ('c2', 'b4', 'p3', 'v24', 'u6','o4',),

             ('c2', 'b5', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b5', 'p1', 'v22', 'u6','o2',),
             ('c2', 'b5', 'p1', 'v23', 'u6','o3',),
             ('c2', 'b5', 'p2', 'v24', 'u6','o4',),

             ('c2', 'b6', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b6', 'p2', 'v22', 'u6','o2',),
             ('c2', 'b6', 'p2', 'v23', 'u6','o3',),
             ('c2', 'b6', 'p3', 'v24', 'u6','o4',),

             ('c2', 'b7', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b7', 'p1', 'v22', 'u6','o2',),
             ('c2', 'b7', 'p3', 'v23', 'u6','o3',),
             ('c2', 'b7', 'p4', 'v24', 'u6','o4',),

             ('c2', 'b8', 'p1', 'v21', 'u6','o1',),
             ('c2', 'b8', 'p2', 'v22', 'u6','o2',),
             ('c2', 'b8', 'p3', 'v23', 'u6','o3',),
             ('c2', 'b8', 'p4', 'v24', 'u6','o4',),


             ('c3', 'b1', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b1', 'p1', 'v32', 'u7','o2',),
             ('c3', 'b1', 'p1', 'v33', 'u7','o3',),
             ('c3', 'b1', 'p1', 'v34', 'u7','o4',),
 
             ('c3', 'b2', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b2', 'p2', 'v32', 'u7','o2',),
             ('c3', 'b2', 'p2', 'v33', 'u7','o3',),
             ('c3', 'b2', 'p2', 'v34', 'u7','o4',),

             ('c3', 'b3', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b3', 'p1', 'v32', 'u7','o2',),
             ('c3', 'b3', 'p2', 'v33', 'u7','o3',),
             ('c3', 'b3', 'p2', 'v34', 'u7','o4',),

             ('c3', 'b4', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b4', 'p2', 'v32', 'u7','o2',),
             ('c3', 'b4', 'p3', 'v33', 'u7','o3',),
             ('c3', 'b4', 'p3', 'v34', 'u7','o4',),

             ('c3', 'b5', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b5', 'p1', 'v32', 'u7','o2',),
             ('c3', 'b5', 'p1', 'v33', 'u7','o3',),
             ('c3', 'b5', 'p2', 'v34', 'u7','o4',),

             ('c3', 'b6', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b6', 'p2', 'v32', 'u7','o2',),
             ('c3', 'b6', 'p2', 'v33', 'u7','o3',),
             ('c3', 'b6', 'p3', 'v34', 'u7','o4',),

             ('c3', 'b7', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b7', 'p1', 'v32', 'u7','o2',),
             ('c3', 'b7', 'p3', 'v33', 'u7','o3',),
             ('c3', 'b7', 'p4', 'v34', 'u7','o4',),

             ('c3', 'b8', 'p1', 'v31', 'u7','o1',),
             ('c3', 'b8', 'p2', 'v32', 'u7','o2',),
             ('c3', 'b8', 'p3', 'v33', 'u7','o3',),
             ('c3', 'b8', 'p4', 'v34', 'u7','o4',),



             ('c4', 'b1', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b1', 'p1', 'v42', 'u6','o2',),
             ('c4', 'b1', 'p1', 'v43', 'u6','o3',),
             ('c4', 'b1', 'p1', 'v44', 'u6','o4',),
 
             ('c4', 'b2', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b2', 'p2', 'v42', 'u6','o2',),
             ('c4', 'b2', 'p2', 'v43', 'u6','o3',),
             ('c4', 'b2', 'p2', 'v44', 'u6','o4',),

             ('c4', 'b3', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b3', 'p1', 'v42', 'u6','o2',),
             ('c4', 'b3', 'p2', 'v43', 'u6','o3',),
             ('c4', 'b3', 'p2', 'v44', 'u6','o4',),

             ('c4', 'b4', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b4', 'p2', 'v42', 'u6','o2',),
             ('c4', 'b4', 'p3', 'v43', 'u6','o3',),
             ('c4', 'b4', 'p3', 'v44', 'u6','o4',),

             ('c4', 'b5', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b5', 'p1', 'v42', 'u6','o2',),
             ('c4', 'b5', 'p1', 'v43', 'u6','o3',),
             ('c4', 'b5', 'p2', 'v44', 'u6','o4',),

             ('c4', 'b6', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b6', 'p2', 'v42', 'u6','o2',),
             ('c4', 'b6', 'p2', 'v43', 'u6','o3',),
             ('c4', 'b6', 'p3', 'v44', 'u6','o4',),

             ('c4', 'b7', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b7', 'p1', 'v42', 'u6','o2',),
             ('c4', 'b7', 'p3', 'v43', 'u6','o3',),
             ('c4', 'b7', 'p4', 'v44', 'u6','o4',),

             ('c4', 'b8', 'p1', 'v41', 'u6','o1',),
             ('c4', 'b8', 'p2', 'v42', 'u6','o2',),
             ('c4', 'b8', 'p3', 'v43', 'u6','o3',),
             ('c4', 'b8', 'p4', 'v44', 'u6','o4',),
             

             ('c5', 'b1', 'p1', 'v51', 'u6','o1',),
             ('c5', 'b1', 'p1', 'v52', 'u6','o2',),
             ('c5', 'b1', 'p1', 'v53', 'u6','o3',),
             ('c5', 'b1', 'p1', 'v54', 'u6','o4',),
 
             ('c5', 'b2', 'p1', 'v51', 'u5','o1',),
             ('c5', 'b2', 'p2', 'v52', 'u5','o2',),
             ('c5', 'b2', 'p2', 'v53', 'u5','o3',),
             ('c5', 'b2', 'p2', 'v54', 'u5','o4',),

             ('c5', 'b3', 'p1', 'v51', 'u5','o1',),
             ('c5', 'b3', 'p1', 'v52', 'u5','o2',),
             ('c5', 'b3', 'p2', 'v53', 'u5','o3',),
             ('c5', 'b3', 'p2', 'v54', 'u5','o4',),

             ('c5', 'b4', 'p1', 'v51', 'u5','o1',),
             ('c5', 'b4', 'p2', 'v52', 'u5','o2',),
             ('c5', 'b4', 'p3', 'v53', 'u5','o3',),
             ('c5', 'b4', 'p3', 'v54', 'u5','o4',),

             ('c5', 'b5', 'p1', 'v51', 'u5','o1',),
             ('c5', 'b5', 'p1', 'v52', 'u5','o2',),
             ('c5', 'b5', 'p1', 'v53', 'u5','o3',),
             ('c5', 'b5', 'p2', 'v54', 'u5','o4',),

             ('c5', 'b6', 'p1', 'v51', 'u5','o1',),
             ('c5', 'b6', 'p2', 'v52', 'u5','o2',),
             ('c5', 'b6', 'p2', 'v53', 'u5','o3',),
             ('c5', 'b6', 'p3', 'v54', 'u5','o4',),

             ('c5', 'b7', 'p1', 'v51', 'u5','o1',),
             ('c5', 'b7', 'p1', 'v52', 'u5','o2',),
             ('c5', 'b7', 'p3', 'v53', 'u5','o3',),
             ('c5', 'b7', 'p4', 'v54', 'u5','o4',),

             ('c5', 'b8', 'p1', 'v51', 'u5','o1',),
             ('c5', 'b8', 'p2', 'v52', 'u5','o2',),
             ('c5', 'b8', 'p3', 'v53', 'u5','o3',),
             ('c5', 'b8', 'p4', 'v54', 'u5','o4',),



             ('c6', 'b1', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b1', 'p1', 'v62', 'u6','o2',),
             ('c6', 'b1', 'p1', 'v63', 'u6','o3',),
             ('c6', 'b1', 'p1', 'v64', 'u6','o4',),
 
             ('c6', 'b2', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b2', 'p2', 'v62', 'u6','o2',),
             ('c6', 'b2', 'p2', 'v63', 'u6','o3',),
             ('c6', 'b2', 'p2', 'v64', 'u6','o4',),

             ('c6', 'b3', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b3', 'p1', 'v62', 'u6','o2',),
             ('c6', 'b3', 'p2', 'v63', 'u6','o3',),
             ('c6', 'b3', 'p2', 'v64', 'u6','o4',),

             ('c6', 'b4', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b4', 'p2', 'v62', 'u6','o2',),
             ('c6', 'b4', 'p3', 'v63', 'u6','o3',),
             ('c6', 'b4', 'p3', 'v64', 'u6','o4',),

             ('c6', 'b5', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b5', 'p1', 'v62', 'u6','o2',),
             ('c6', 'b5', 'p1', 'v63', 'u6','o3',),
             ('c6', 'b5', 'p2', 'v64', 'u6','o4',),

             ('c6', 'b6', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b6', 'p2', 'v62', 'u6','o2',),
             ('c6', 'b6', 'p2', 'v63', 'u6','o3',),
             ('c6', 'b6', 'p3', 'v64', 'u6','o4',),

             ('c6', 'b7', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b7', 'p1', 'v62', 'u6','o2',),
             ('c6', 'b7', 'p3', 'v63', 'u6','o3',),
             ('c6', 'b7', 'p4', 'v64', 'u6','o4',),

             ('c6', 'b8', 'p1', 'v61', 'u6','o1',),
             ('c6', 'b8', 'p2', 'v62', 'u6','o2',),
             ('c6', 'b8', 'p3', 'v63', 'u6','o3',),
             ('c6', 'b8', 'p4', 'v64', 'u6','o4',),
             
             
 
             ('c7', 'b1', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b1', 'p1', 'v72', 'u4','o2',),
             ('c7', 'b1', 'p1', 'v73', 'u4','o3',),
             ('c7', 'b1', 'p1', 'v74', 'u4','o4',),
 
             ('c7', 'b2', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b2', 'p2', 'v72', 'u4','o2',),
             ('c7', 'b2', 'p2', 'v73', 'u4','o3',),
             ('c7', 'b2', 'p2', 'v74', 'u4','o4',),

             ('c7', 'b3', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b3', 'p1', 'v72', 'u4','o2',),
             ('c7', 'b3', 'p2', 'v73', 'u4','o3',),
             ('c7', 'b3', 'p2', 'v74', 'u4','o4',),

             ('c7', 'b4', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b4', 'p2', 'v72', 'u4','o2',),
             ('c7', 'b4', 'p3', 'v73', 'u4','o3',),
             ('c7', 'b4', 'p3', 'v74', 'u4','o4',),

             ('c7', 'b5', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b5', 'p1', 'v72', 'u4','o2',),
             ('c7', 'b5', 'p1', 'v73', 'u4','o3',),
             ('c7', 'b5', 'p2', 'v74', 'u4','o4',),

             ('c7', 'b6', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b6', 'p2', 'v72', 'u4','o2',),
             ('c7', 'b6', 'p2', 'v73', 'u4','o3',),
             ('c7', 'b6', 'p3', 'v74', 'u4','o4',),

             ('c7', 'b7', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b7', 'p1', 'v72', 'u4','o2',),
             ('c7', 'b7', 'p3', 'v73', 'u4','o3',),
             ('c7', 'b7', 'p4', 'v74', 'u4','o4',),

             ('c7', 'b8', 'p1', 'v71', 'u4','o1',),
             ('c7', 'b8', 'p2', 'v72', 'u4','o2',),
             ('c7', 'b8', 'p3', 'v73', 'u4','o3',),
             ('c7', 'b8', 'p4', 'v74', 'u4','o4',),    
             
             
 
             ('c8', 'b1', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b1', 'p1', 'v82', 'u6','o2',),
             ('c8', 'b1', 'p1', 'v83', 'u6','o3',),
             ('c8', 'b1', 'p1', 'v84', 'u6','o4',),
 
             ('c8', 'b2', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b2', 'p2', 'v82', 'u6','o2',),
             ('c8', 'b2', 'p2', 'v83', 'u6','o3',),
             ('c8', 'b2', 'p2', 'v84', 'u6','o4',),

             ('c8', 'b3', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b3', 'p1', 'v82', 'u6','o2',),
             ('c8', 'b3', 'p2', 'v83', 'u6','o3',),
             ('c8', 'b3', 'p2', 'v84', 'u6','o4',),

             ('c8', 'b4', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b4', 'p2', 'v82', 'u6','o2',),
             ('c8', 'b4', 'p3', 'v83', 'u6','o3',),
             ('c8', 'b4', 'p3', 'v84', 'u6','o4',),

             ('c8', 'b5', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b5', 'p1', 'v82', 'u6','o2',),
             ('c8', 'b5', 'p1', 'v83', 'u6','o3',),
             ('c8', 'b5', 'p2', 'v84', 'u6','o4',),

             ('c8', 'b6', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b6', 'p2', 'v82', 'u6','o2',),
             ('c8', 'b6', 'p2', 'v83', 'u6','o3',),
             ('c8', 'b6', 'p3', 'v84', 'u6','o4',),

             ('c8', 'b7', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b7', 'p1', 'v82', 'u6','o2',),
             ('c8', 'b7', 'p3', 'v83', 'u6','o3',),
             ('c8', 'b7', 'p4', 'v84', 'u6','o4',),

             ('c8', 'b8', 'p1', 'v81', 'u6','o1',),
             ('c8', 'b8', 'p2', 'v82', 'u6','o2',),
             ('c8', 'b8', 'p3', 'v83', 'u6','o3',),
             ('c8', 'b8', 'p4', 'v84', 'u6','o4',),    

 
             ('c9', 'b1', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b1', 'p1', 'v92', 'u2','o2',),
             ('c9', 'b1', 'p1', 'v93', 'u2','o3',),
             ('c9', 'b1', 'p1', 'v94', 'u2','o4',),
 
             ('c9', 'b2', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b2', 'p2', 'v92', 'u2','o2',),
             ('c9', 'b2', 'p2', 'v93', 'u2','o3',),
             ('c9', 'b2', 'p2', 'v94', 'u2','o4',),

             ('c9', 'b3', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b3', 'p1', 'v92', 'u2','o2',),
             ('c9', 'b3', 'p2', 'v93', 'u2','o3',),
             ('c9', 'b3', 'p2', 'v94', 'u2','o4',),

             ('c9', 'b4', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b4', 'p2', 'v92', 'u2','o2',),
             ('c9', 'b4', 'p3', 'v93', 'u2','o3',),
             ('c9', 'b4', 'p3', 'v94', 'u2','o4',),

             ('c9', 'b5', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b5', 'p1', 'v92', 'u2','o2',),
             ('c9', 'b5', 'p1', 'v93', 'u2','o3',),
             ('c9', 'b5', 'p2', 'v94', 'u2','o4',),

             ('c9', 'b6', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b6', 'p2', 'v92', 'u2','o2',),
             ('c9', 'b6', 'p2', 'v93', 'u2','o3',),
             ('c9', 'b6', 'p3', 'v94', 'u2','o4',),

             ('c9', 'b7', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b7', 'p1', 'v92', 'u2','o2',),
             ('c9', 'b7', 'p3', 'v93', 'u2','o3',),
             ('c9', 'b7', 'p4', 'v94', 'u2','o4',),

             ('c9', 'b8', 'p1', 'v91', 'u2','o1',),
             ('c9', 'b8', 'p2', 'v92', 'u2','o2',),
             ('c9', 'b8', 'p3', 'v93', 'u2','o3',),
             ('c9', 'b8', 'p4', 'v94', 'u2','o4',),    


 
             ('c10', 'b1', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b1', 'p1', 'v102', 'u7','o2',),
             ('c10', 'b1', 'p1', 'v103', 'u7','o3',),
             ('c10', 'b1', 'p1', 'v104', 'u7','o4',),
 
             ('c10', 'b2', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b2', 'p2', 'v102', 'u7','o2',),
             ('c10', 'b2', 'p2', 'v103', 'u7','o3',),
             ('c10', 'b2', 'p2', 'v104', 'u7','o4',),

             ('c10', 'b3', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b3', 'p1', 'v102', 'u7','o2',),
             ('c10', 'b3', 'p2', 'v103', 'u7','o3',),
             ('c10', 'b3', 'p2', 'v104', 'u7','o4',),

             ('c10', 'b4', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b4', 'p2', 'v102', 'u7','o2',),
             ('c10', 'b4', 'p3', 'v103', 'u7','o3',),
             ('c10', 'b4', 'p3', 'v104', 'u7','o4',),

             ('c10', 'b5', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b5', 'p1', 'v102', 'u7','o2',),
             ('c10', 'b5', 'p1', 'v103', 'u7','o3',),
             ('c10', 'b5', 'p2', 'v104', 'u7','o4',),

             ('c10', 'b6', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b6', 'p2', 'v102', 'u7','o2',),
             ('c10', 'b6', 'p2', 'v103', 'u7','o3',),
             ('c10', 'b6', 'p3', 'v104', 'u7','o4',),

             ('c10', 'b7', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b7', 'p1', 'v102', 'u7','o2',),
             ('c10', 'b7', 'p3', 'v103', 'u7','o3',),
             ('c10', 'b7', 'p4', 'v104', 'u7','o4',),

             ('c10', 'b8', 'p1', 'v101', 'u7','o1',),
             ('c10', 'b8', 'p2', 'v102', 'u7','o2',),
             ('c10', 'b8', 'p3', 'v103', 'u7','o3',),
             ('c10', 'b8', 'p4', 'v104', 'u7','o4',),   
             
             
                    
             ]

    myPartition_Chain = Partition_Chain(location, partition_chain_topology)

    return (myServer, myService_Chain, myPartition_Chain)



class cost_of_virtual_switching():
    """
    cost_of_virtual_switching
    To calculate the placement CPU cost between one subchain and one server
    Based on the IEEE INFOCOM 2018 -Apr 2018 Page 3-5
    Optimizing NFV Chian Deployment Through Minimizing the Cost of Virtual Switching
    """

    def __init__(self, chain, bell, partition, vnf, usedcpu, order, \
                                          server, cpu_total, cpu_used, cpu_available):
        self.chain = chain
        self.bell = bell
        self.partition = partition
        self.vnf = vnf
        self.usedcpu = usedcpu
        self.order = order
        self.server = server
        self.cpu_total = cpu_total
        self.cpu_used = cpu_used
        self.cpu_available = cpu_available
        
#    def cost_of_virtual_switching_calculator(self,chain, bell, partition, vnf, \
#                    usedcpu, order, server, cpu_total, cpu_used, cpu_available):
#        return (random.uniform(0, 1))
        

    def cost_of_virtual_switching_calculator(self,chain, bell, partition, vnf, \
                    usedcpu, order, server, cpu_total, cpu_used, cpu_available, \
                    vnf_length, myVNFLengthinPartition, myVNFListTotalCPUinPartition ):

        """
        To use switch cost function;
            it is required to have lenght of VNF in server to be >0. 
            If it gets 0, "ValueError: math domain error" will be errer.
        """

        
#        """
#        Example of placement_function = 'g'
#        """
#        a = subchain(phin = float(vnf_length[1:]), phip = 1000, ovs_type = 'kernel', \
#                     placement_function = 'g', packet_size = 100)
#        b = subchain(phin = float(myVNFLengthinPartition), phip = 1000, ovs_type = 'kernel', \
#                     placement_function = 'g', packet_size = 100)

        """
        Example of placement_function = 'd'
        """
        a = subchain(phin = float(vnf_length[1:]), phip = 1000, ovs_type = 'kernel', \
                     placement_function ='d', packet_size = 100)
        b = subchain(phin = float(myVNFLengthinPartition), phip = 1000, ovs_type = 'kernel', \
                     placement_function = 'd', packet_size = 100)

        """ 
         To change the negative value
        """
        c = multiple_subchain([a,b])
        
#        mycost = round(c.get_cost(),2)        
#        if (mycost < 0 ):
#                mycost = 0
#        return (round(mycost,2))


        return (round(c.get_cost(),2))


#        s=round((random.uniform(0, 1)),2)
#        return ( s )
        """
        For Testing with random number    
        return (random.uniform(0, 1))
        """ 
    


        
    def __str__(self):
        return  (random.uniform(0, 1))

    
    

class optimal_cost_placement():
    """
    optimal_cost_placement
    To calculate the minimum CPU cost for all chains.
    
    Goes over all partitions of service chain, grouping subsets of VNFs. 
    For each partition in set, use the switching cost model to find 
    the cost placement on each server. Then find an optimal placement of 
    this partition by finding the maximal matching between sub-chains 
    and servers.
    
    
    Based on the IEEE INFOCOM 2018 -Apr 2018 Page 3-5
    Optimizing NFV Chian Deployment Through Minimizing the Cost of Virtual Switching


    service_chain_placement
        (Data Structure list of tuples)
    =========== ===============================================================
    Attribute   Description
    =========== ===============================================================
    chain_id    Service Chain ID
    bell_id     Bell Number 
    partition_id    Partition ID  
    vnf_id      VNF ID
    vnf_cpu     VNF required CPU number
    vnf_flow_id VNF Flow order ID
    server_id   Server ID
    cpu_total   Total number of cpu
    cpu_used    Number of used cpu
    cpu_avail   Number of available cpu    
    server_vnf_len      Number of VNF length in server
    partition_vnf_len   Number of VNF length in partition
    Total Required CPU  Number of required CPU in prtition
    Switch Cost         Number of Switch Cost
    =========== ===============================================================
    
    
    Example of the resulf of OCP.
    service_chain_placement = [
             ('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's1', 'c20', 'u4','a14','l4','l5','t5','cv4.0',),
             ('c1', 'b1', 'p1', 'v2', 'u2', 'o2', 's2', 'c20', 'u4','a16','l4','l5','t5','cv4.0',),           
  
             ('c2', 'b4', 'p2', 'v1', 'u5', 'o1', 's1', 'c20', 'u11','a9','l7','l3','t6','cv5.0'),
             ('c2', 'b4', 'p2', 'v3', 'u4', 'o2', 's2', 'c20', 'u8','a12','l7','l3','t6','cv5.0'),
             ('c2', 'b4', 'p2', 'v4', 'u2', 'o3', 's1', 'c20', 'u13','a7','l7','l3','t6','cv5.0'),  
             
             ]
    
    server_placement
        (Data Structure list of tuples)    
    =========== ===============================================================
    Attribute   Description
    =========== ===============================================================
    server_id   Server ID
    cpu_total   Total number of cpu
    cpu_used    Number of used cpu
    cpu_avail   Number of available cpu
    VNF_length  Number of VNF on server
    =========== ===============================================================
    
    This is the resulted server_topology.
    server_topology = [
             ('s1', 'c30', 'u11','a9','l7',),
             ('s2', 'c30', 'u8','a12','l7',),
            ]

    This service_chain_topology remains no change.
        service_chain_topology = [
             ('c1', 'v1', 'u3','o1',),
             ('c1', 'v2', 'u2','o2',),
             ('c2', 'v1', 'u5','o1',),
             ('c2', 'v3', 'u4','o2',),
             ('c2', 'v4', 'u2','o3',),
            ]

    """
    service_chain_placement = []
    service_chain_server_result = []    
    myServer = []
    myService_Chain = []     
    myPartition_Chain = []
    service_chan_all =[]


    """
    #    To Test the cost_of_virtual_switching function
    #    for i in range(1, 11): 
    #        print (i , "  =  ", cost_of_virtual_switching())
    """

    
    
    def __init__(self, location, myServer, myService_Chain, myPartition_Chain):
        self.service_chain_placement_location_id = location
        self.myServer = myServer
        self.myService_Chain = myService_Chain        
        self.myPartition_Chain = myPartition_Chain
        self.perform_placement()
        self.service_chain_placement
        self.service_chain_server_result = myServer



    def print_all_list():
        print ("") 
        print ("An instance of Result placement :") 
        for a, b, c, d ,e , f, g, h, i, j in optimal_cost_placement.service_chain_placement  :
            print ("Service Chain ID=", a, \
                   " Bell ID=", b, \
                   " Partition ID=", c, \
                   " VNF ID=", d, \
                   " VNF CPU=", e, \
                   " VNF Flow=", f, \
                   " Server=", g,  \
                   " cpu_total=", h, \
                   " cpu_used=", i, \
                   " cpu_avail=", j)

                 

    # Placement Proecedure
    def perform_placement(self):
        """
        Perform_Placement is function to find place on Serer for each VNF
        Methodology OPTIMIZED OPERATIONAL COST PLACEMENT 
        Goes over all partitions of service chain, grouping subsets of VNFs. 
        For each partition in set, use the switching cost model to find 
        the cost placement on each server. Then find an optimal placement of 
        this partition by finding the maximal matching between sub-chains and servers.
        
        Given:
            - List of tuple : Server 
            - List of tuple : Service Chain with VNF
            - List of tuple : Partition of VNF in Service Chain
        Output:
            - List of tuple : VNF with Server
        
        Conditions:
            - Chain list is in pririty order from low to hight.
            - Chain list has not allowed the two same priority.
            - Chain list could have same VNF in multip times, but only different name
              For example; v1 ==> v1.1, v1.2
            - Server Resource has to be avalable for worst case scenario.
        """


        def ext1(input):
            return (input[1:])

        def m1(input):
            return float(input[1:])

        def m2(input):
            return float(input[2:])
        
        def madd(input, add):
            return (input[0]+str(float(input[1:])+float(add)))
            
        def mdel(input, delete):
            return (input[0]+str(float(input[1:])-float(delete)))      
        
        def UpdateServerResourceCV(vnf_list, server_list, b_first_vnf, cv_at_server):
            """
            Function for upgrading myServer list.
            Input : the VNF list and current Server list on VNF level
            Output : The udpated of both lists
            
            For Example:
            Input :
                VNF list= ('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's2', 'c20', 'u2', 'a18', 
                           'l1', 'l2, 't5', 'cv0.123456789))
                Server list = [
                                 ('s1', 'c20', 'u3','a17', 'l1'),
                                 ('s2', 'c20', 'u2','a18', 'l1'),
                              ]
            server_topology
                    (Data Structure list of tuples)
            =========== ===============================================================
            Attribute   Description
            =========== ===============================================================
            server_id   Server ID
            cpu_total   Total number of cpu
            cpu_used    Number of used cpu
            cpu_avail   Number of available cpu
            VNF_length  Number of VNF on server
            =========== ===============================================================

            service_chain_placement
                (Data Structure list of tuples)
            =========== ===============================================================
            Attribute   Description
            =========== ===============================================================
            chain_id    Service Chain ID
            bell_id     Bell Number 
            partition_id    Partition ID  
            vnf_id      VNF ID
            vnf_cpu     VNF required CPU number
            vnf_flow_id VNF Flow order ID
            server_id   Server ID
            cpu_total   Total number of cpu
            cpu_used    Number of used cpu
            cpu_avail   Number of available cpu    
            server_vnf_len      Number of VNF length in server
            partition_vnf_len   Number of VNF length in partition
            Total Required CPU  Number of required CPU in prtition
            Switch Cost         Number of Switch Cost
            =========== ===============================================================

            """

                

            
#             Update VNF list
            lst = list(vnf_list)
            """
            Used = the total Switching cost  + the total required CPU
            """
            used = float(m1(lst[12])) + float(m2(lst[13]))
#            print(used)
            
            lst[9] = mdel(lst[9],(used)) #Availalbe CPU
            lst[8] = madd(lst[8],(used)) #Used CPU
            lst[10] = madd(lst[10],m1(lst[11])) #Used CPU            
            vnf_list = (tuple(lst))
            # Update Server List
            new_server_list = []
#            lst[6]  # Server ID
#            print (lst[6])
            
            if (b_first_vnf) :
                for s in server_list :
                    if s[0] == lst[6] :
#                        print ('yes', lst[6])
                        s_lst = list(s)
                        if ( used > m1(s_lst[3]) ):
                            cv_at_server = 9999
                        else :
                            s_lst[3] = mdel(s_lst[3],(used))  #Availalbe CPU
                            s_lst[2] = madd(s_lst[2],(used))  #Used CPU
                            s_lst[4] = madd(s_lst[4],m1(lst[11])) #length of VNF                                
                            s = (tuple(s_lst))
#                    else :    
#                       print ('no')
                    new_server_list.append(s)
#                print(new_server_list)
                new_server_list= sorted(set(new_server_list))
            else:
                new_server_list= sorted(set(server_list))
            
#            cv_at_server = 9999
            
            return (vnf_list, new_server_list, cv_at_server)

        def UpdateServerResource(vnf_list, server_list):
            """
            Function for upgrading myServer list.
            Input : the VNF list and current Server list on VNF level
            Output : The udpated of both lists
            
            For Example:
            Input :
                VNF list= ('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's2', 'c20', 'u2', 'a18','l1')
                Server list = [
                                 ('s1', 'c20', 'u3','a17', 'l1'),
                                 ('s2', 'c20', 'u2','a18', 'l1'),
                              ]
            """
            # Update VNF list
            lst = list(vnf_list)
            used = lst[4]
#            print(used)
            lst[9] = mdel(lst[9],m1(used))
            lst[8] = madd(lst[8],m1(used))
            vnf_list = (tuple(lst))
            # Update Server List
            new_server_list = []
#            lst[6]  # Server ID
#            print (lst[6])
            for s in server_list :
                if s[0] == lst[6] :
#                    print ('yes', lst[6])
                    s_lst = list(s)
                    s_lst[3] = mdel(s_lst[3],m1(used))
                    s_lst[2] = madd(s_lst[2],m1(used))
                    s = (tuple(s_lst))
#                else :    
#                    print ('no')
                new_server_list.append(s)
#            print(new_server_list)
            new_server_list= sorted(set(new_server_list))
            return (vnf_list, new_server_list)


        def custom_sort(t):
            return t[1]  # Sort by Available CPU
        """        
        # End of def
        """

        # Sort the Partition_Chain_Topology

        # Placement Proecedure
    
        myPartition_Chain.partition_chain_topology = \
                sorted(myPartition_Chain.partition_chain_topology)
#        print ('Sorted ====', myPartition_Chain.partition_chain_topology)
        
            
        """            
        # Find list of given Chain.
        # Find list of given Bell, Partion, VNF of Chain.
        """
        myChainList = []
        myChainListAll = []
        for chain in myPartition_Chain.partition_chain_topology:
            myChainList.append(chain[0])
            myChainListAll.append(chain)              
        myChainList= sorted(set(myChainList))
#        print ('MyChianList=', myChainList)
    
        """
        # Start running fron Chain #1
        """
        myChainServer = self.myServer.server_topology            
        myChainRun = myChainList[0]      
        for c in range (len(myChainList)):
            myChainRun = myChainList[c]
            print ('===============myChainRun=', myChainRun)
            
            """
            # Find list of given Bell of this current Chain.
            # Find list of given Partition and VNF of Bell.            
            """
            myBellList = []
            myBellListAll = []
            for bell in myChainListAll:
                if bell[0] == myChainRun :
                    myBellList.append(bell[1])
                    myBellListAll.append(bell)                    
            myBellList= sorted(set(myBellList))
#            print ('MyBellList=', myBellList)
            
            """
            # Start from 1st Bell                    
            """
#            print(myChainServer)
            myBellServer = myChainServer           
            myBellRun = myBellList[0]
            min_cv_at_bell = 1000
            cv_at_bell = 0            
            service_chain_placement_bell = []
            for b in range (len(myBellList)):
                    myBellRun = myBellList[b]
                    print ('===============myBellRun=', myBellRun)
#                    print ('myBellServer=',myBellServer)
                    """
                    # Find list of given Partition of this current Bell.
                    # Find list of given VNF of Partition.
                    """
                    myPartionList = []
                    myPartionListAll = []
                    for partition in myBellListAll:
                        if ((partition[0] == myChainRun) and \
                            (partition[1] == myBellRun))  :
                            myPartionList.append(partition[2])
                            myPartionListAll.append(partition)
                    myPartionList= sorted(set(myPartionList))
                    myPartionListAll= sorted(set(myPartionListAll))
#                    print ('MyPartionList=', myPartionList)
#                    print ('myPartionListAll=', myPartionListAll)
    
                    """
                    # Start from 1st Partition           
                    """               
                    myPartitionServer = myBellServer
                    myPartitionRun = myPartionList[0]
                    min_cv_at_partition = 1000
                    cv_at_bell = 0  
                    cv_at_partition = 0                  
                    service_chain_placement_partition = []
                    myVNFListTotalCPUinPartition = 0.00
                    myVNFLength = 0
                    myVNFLengthinPartition = 0
                    for p in range (len(myPartionList)):
                            myPartitionRun = myPartionList[p]
                            print ('myPartitionRun=', myPartitionRun)
    
                            """
                            # Find list of given VNF of this current Partition.
                            """
                            myVNFList = []
                            myVNFListAll = []
                            myVNFListTotalCPUinPartition = 0.00
                            for vnf in myPartionListAll:
                                if ((vnf[0] == myChainRun) and \
                                    (vnf[1] == myBellRun) and \
                                    (vnf[2] == myPartitionRun))  :
                                    myVNFList.append(vnf[3])
                                    myVNFListAll.append(vnf)
                                    myVNFLengthinPartition = int(myVNFLengthinPartition + 1)
#                                    print ('+++++++++++++myVNFLengthinPartition=', myVNFLengthinPartition)
                                    myVNFListTotalCPUinPartition = myVNFListTotalCPUinPartition + float(ext1(vnf[4]))
                                    
                            myVNFList= sorted(set(myVNFList))                            
                            myVNFListAll= sorted(set(myVNFListAll))
#                            print ('myVNFList=', myVNFList)
#                            print ('myVNFListAll=', myVNFListAll)
                            
                            """
                            # Start from 1st VNF
                            """

                            myPartitionServer.sort(key=custom_sort)                        
                            myVNFServer = myPartitionServer
                            myVNFRun = myVNFList[0]
                            
                            """
                            # Calulate the OPS cost switching of 
                            # each Partition on each server. 
                            # By running all VNFs on that Partition.
                            """

                            cv_at_vnf = 0
                            service_chain_placement_vnf = []
                            b_first_vnf = True
                            cv_at_server = 0
                            myVNFServer_2nd = []
                            match_at_server = False                            
                            for v in range (len(myVNFList)):
                                    myVNFRun = myVNFList[v]
                                    print ('myVNFRun=', myVNFRun)
                                                                  
                                    """
                                    # Search the required CPU 
                                    """
                                    service_chain_placement_vnf_server = ()
                                    min_cv_at_server = 1000
#                                    cv_at_server = 0
                                    for cpu in myVNFListAll:
                                        if ((cpu[0] == myChainRun) and \
                                            (cpu[1] == myBellRun) and \
                                            (cpu[2] == myPartitionRun) and \
                                            (cpu[3] == myVNFRun))  :
                                            
#                                            print('==VNF==', cpu)
                                            
                                            """
                                            # Search cost on each Server   
                                            # for 1st VNF in Partitiion
                                            """
#                                            print('if (b_first_vnf == True)')
                                            if (b_first_vnf == True) :   
#                                                print('(b_first_vnf == True)')      
                                                

                                                for s in  myVNFServer  : 
                                                        cv_at_server = \
                                                cost_of_virtual_switching.cost_of_virtual_switching_calculator( \
                                                self, myChainRun, myBellRun, myPartitionRun, myVNFRun, \
                                                cpu[4], cpu[5], s[0], s[1], s[2], s[3], s[4], myVNFLengthinPartition,\
                                                myVNFListTotalCPUinPartition )
#                                                        print('cv_at_server=',cv_at_server)
        #                                                if ((cv_at_server+myVNFListTotalCPUinPartition) < min_cv_at_server ):
                                                        if ((cv_at_server) < min_cv_at_server ):
                                                            
                                                            match_at_server = True                                                            
                                                            print('==============cv_at_server < min_cv_at_server')
                                                            print('min_cv_at_server=',min_cv_at_server)
#                                                            print('(cv_at_server+myVNFListTotalCPUinPartition)=',(cv_at_server+myVNFListTotalCPUinPartition) )
#                                                            min_cv_at_server = (cv_at_server+myVNFListTotalCPUinPartition)                                                         
                                                            min_cv_at_server = (cv_at_server)                                                         
                                                            print('min_cv_at_server=',min_cv_at_server)
                                                            service_chain_placement_vnf_server = (myChainRun, myBellRun, \
                                                                    myPartitionRun, myVNFRun, cpu[4], cpu[5], s[0], s[1], \
                                                                    s[2], s[3], s[4], ('l'+str(myVNFLengthinPartition)), ('t'+str(myVNFListTotalCPUinPartition)), \
                                                                    ('cv'+str(cv_at_server)))
                                                            myVNFServer_2nd = s
                                                            myVNFServer_2nd = (*myVNFServer_2nd, ('cv'+str(cv_at_server)))
#                                                            print('myVNFServer_2nd.append(s)')
#                                                            print('myVNFServer_2nd=',myVNFServer_2nd)
#                                                            print('service_chain_placement_vnf_server=',service_chain_placement_vnf_server)
                                                            
#                                            """
#                                            # Search cost on each Server       
#                                            # for Not 1st VNF in Partitiion
#                                            """
                                            else:
                                                service_chain_placement_vnf_server = (myChainRun, myBellRun, \
                                                                    myPartitionRun, myVNFRun, cpu[4], cpu[5], myVNFServer_2nd[0], myVNFServer_2nd[1], \
                                                                    myVNFServer_2nd[2], myVNFServer_2nd[3], myVNFServer_2nd[4], \
                                                                    ('l'+str(myVNFLengthinPartition)), ('t'+str(myVNFListTotalCPUinPartition)), \
                                                                     myVNFServer_2nd[5])                                              
#                                                print('service_chain_placement_vnf_server=',service_chain_placement_vnf_server)
#                                                self.service_chan_all.append(service_chain_placement_vnf_server)
                                            """ 
                                            # After Exit Server Loop ==> Only lowest cv_at_server in list                                                    
                                            """
    
                                    """
                                    # Bottom of VNF Loop ==> Adding cv_at_server to VNF
                                    """
#                                    cv_at_vnf = cv_at_vnf + cv_at_server
#                                    cv_at_vnf =  cv_at_server


                                    
                                    """
                                    # Update Server Resource based on the allocated CPU
                                    """
#                                    print ('Update Server Resource based on the allocated CPU')
#                                    print ('BEFORE==myVNFServer=',myVNFServer)
#                                    print ('BEFORE==service_chain_placement_vnf_server=', service_chain_placement_vnf_server)
                                    service_chain_placement_vnf_server, myVNFServer, cv_at_server = \
                                        UpdateServerResourceCV(service_chain_placement_vnf_server, \
                                                               myVNFServer,b_first_vnf, cv_at_server)
#                                        UpdateServerResource(service_chain_placement_vnf_server, myVNFServer)
                                    if (cv_at_server == 9999) :
#                                                print ('cv_at_server == 9999')
                                                service_chain_placement_vnf_server = (myChainRun, myBellRun, \
                                                        myPartitionRun, myVNFRun, service_chain_placement_vnf_server[4], \
                                                        service_chain_placement_vnf_server[5], 's', 'c', \
                                                        'u', 'a', 'l', ('l'+str(myVNFLengthinPartition)), ('t'+str(myVNFListTotalCPUinPartition)), \
                                                        ('cv'+str(cv_at_server)))
                                                service_chain_placement_vnf.append(service_chain_placement_vnf_server)
                                                self.service_chan_all.append(service_chain_placement_vnf_server)
                                    else:
                                        self.service_chan_all.append(service_chain_placement_vnf_server)
#                                        print('AFTER==myVNFServer=',myVNFServer)
                                        service_chain_placement_vnf.append(service_chain_placement_vnf_server)
                                        b_first_vnf = False
#                                        print ('b_first_vnf = False')
                                    # This is required for breaking the loop.
                                    cv_at_vnf =  cv_at_server
                                    
                            """
                            # Bottom of Partition Loop ==> Adding cv_at_vnf to Partition
                            """
                            cv_at_partition = cv_at_partition + cv_at_vnf     
#                            print ('cv_at_partition=', cv_at_partition)
                            
                            service_chain_placement_partition.append(service_chain_placement_vnf)

                            myPartitionServer = myVNFServer
#                            print ('myPartitionServer=', myPartitionServer)
                            """
                            # Reset myVNFLengthinPartition to 0
                            """                       
                            myVNFLengthinPartition = 0
                            match_at_server = False                            
                    """
                    # After Exit Partition Loop ==> Adding cv_at_vnf to Partition
                    """
#                    print ('min_cv_at_partition =',  min_cv_at_partition)                    
                    """
                    # Bottom of Bell Loop    
                    """
                    cv_at_bell = cv_at_bell + cv_at_partition    
                    print('Bottom of Bell Loop: cv_at_bell=', cv_at_bell)
                    print('cv_at_bell =', cv_at_bell, '   min_cv_at_bell=',min_cv_at_bell )
                    if (cv_at_bell < min_cv_at_bell): 
                        service_chain_placement_bell = []                                               
                        min_cv_at_bell = cv_at_bell
                        service_chain_placement_bell.append(service_chain_placement_partition)  # adding cv_at_bell
                        myBellServerMin = myPartitionServer    
#                        print ('myBellServerMin=', myBellServerMin)
#                        print ('service_chain_placement_bell=',service_chain_placement_bell)
#                        print ('BBBBB')             
                    elif ( cv_at_bell == 9999):
                        myBellServerMin = myBellServer
                        service_chain_placement_bell.append(service_chain_placement_partition)  # adding cv_at_bell                        
            """
            # After Exit Bell Loop    
            """
#            print ('min_cv_at_bell =',  min_cv_at_bell)               
            
            """
            # Bottom of Chain Loop    
            """
            self.service_chain_placement.append(service_chain_placement_bell)  # adding cv_at_bell
            service_chain_result = []
            def list_all(obj):
                if not isinstance(obj, list):
                    return [obj]
                else:
                    return [item for sublist in obj for item in list_all(sublist)]
           
            service_chain_result = (list_all(self.service_chain_placement))   
#            print('service_chain_result=',service_chain_result)
            
            myChainServer = myBellServerMin
            service_chain_server_result = myChainServer

        """
        Print the placement result on screen
        """
        print ("") 
        print ("Print the placement result on screen") 
        print ("") 
        print ("The result of Service Chain on Servers.")         
        for a, b, c, d ,e , f, g, h, i, j, k, l, m, n in service_chain_result :
            print ("Service Chain ID=", ext1(a), \
                   " Bell ID=", ext1(b), \
                   " Partition ID=", ext1(c), \
                   " VNF ID=", ext1(d), \
                   " VNF CPU=", ext1(e), \
                   " VNF Flow=", ext1(f), \
                   " Server=", ext1(g),  \
                   " cpu_total=", ext1(h), \
                   " cpu_used=", ext1(i), \
                   " cpu_avail=", ext1(j), \
                   " VNF Length on Server=", ext1(k), \
                   " VNF Length on Partition=", ext1(l), \
                   " Total Required CPU=", ext1(m), \
                   " Switching Cost", m2(n))

            
#        print ('service_chain_result ==== ', service_chain_result)       
        print ("") 
        print ("The result of Server allocation.") 
        for a, b, c, d , e in service_chain_server_result :
            print ("Server       =", ext1(a))
            print ("cpu_total    =", ext1(b))            
            print ("cpu_used     =", ext1(c))       
            print ("cpu_available=", ext1(d))  
            print ("VNF Length   =", ext1(e))  

#        print ("") 
#        print ("Print the placement result on screen") 
#        print ("") 
#        print ("The result of Service Chain on Servers.")         
#        for a, b, c, d ,e , f, g, h, i, j, k, l, m, n in service_chain_result :
#            print ("Service Chain ID=", a, \
#                   " Bell ID=", b, \
#                   " Partition ID=", c, \
#                   " VNF ID=", d, \
#                   " VNF CPU=", e, \
#                   " VNF Flow=", f, \
#                   " Server=", g,  \
#                   " cpu_total=", h, \
#                   " cpu_used=", i, \
#                   " cpu_avail=", j, \
#                   " VNF Length on Server=", k, \
#                   " VNF Length on Partition=", l, \
#                   " Total Required CPU=", m, \
#                   " Switching Cost", n)
#
#            
##        print ('service_chain_result ==== ', service_chain_result)       
#        print ("") 
#        print ("The result of Server allocation.") 
#        for a, b, c, d , e in service_chain_server_result :
#            print ("Server       =", a)
#            print ("cpu_total    =", b)            
#            print ("cpu_used     =", c)       
#            print ("cpu_available=", d)  
#            print ("VNF Length   =", e)  
# End of class optimal_cost_placement(object):
    
if __name__ == '__main__':

    location1 = 'Site1'
    
    """    
    Load all Server, Service Chain, and Partition into memory.
    """
    myServer, myService_Chain, myPartition_Chain = load_topology(location1)
    

    """    
    Print all Server, Service Chain, and Partition from memory.
    """
#    myServer.print_all_list()
#    print (myService_Chain)
#    myService_Chain.print_all_list()
#    print (myPartition_Chain)
#    myPartition_Chain.print_all_list()    
    
    
    """    
    To calculate the minimum cost placment of all service chains.
    Print the result of placement    
    
    """
    myService_Chain_Placement = optimal_cost_placement \
        (location1, myServer, myService_Chain, myPartition_Chain)
    
    
        
    """    
    Print the result of placement
    """
    print ("")     
    print ("Summary View.")     
#    print (optimal_cost_placement.service_chain_placement)
    def list_all(obj):
        if not isinstance(obj, list):
            return [obj]
        else:
            return [item for sublist in obj for item in list_all(sublist)]
   
    optimal_cost_placement.service_chain_placement = (list_all(optimal_cost_placement.service_chain_placement))   
    for s in optimal_cost_placement.service_chain_placement:
            print (s)    
    print ("") 

#    print (optimal_cost_placement.service_chan_all)    
#    for s in optimal_cost_placement.service_chan_all:
#            print (s)
