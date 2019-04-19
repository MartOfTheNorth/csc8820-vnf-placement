# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:58:06 2019
Georgia State University
CSC8820
@author: Mart Panichvatana

"""

import random




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
        print ("An instance of Server") 
        for a, b, c, d in self.server_topology :
            print ("Server=", a)
            print ("cpu_total=", b)            
            print ("cpu_used=", c)       
            print ("cpu_avail=", d)       
                        
    def __iter__(self):
        return self

    def __next__(self):
        return self
    
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
        print ("An instance of Service Chain") 
        for a, b, c, d in self.service_chain_topology :
            print ("Service Chain ID=", a)
            print ("VNF ID          =", b)            
            print ("VNF required CPU=", c)       
            print ("VNF Flow order  =", d)       
            
#    def __iter__(self):
#        if self.i < len(self.l):
#            self.i = self.i + 1
#            return self.l[self.i-1]
#        else:
#            raise StopIteration

#    def __next__(self):
#        return self    
    
    def __next__(self):   
        if self.i < len(self.l):
            self.i = self.i + 1
            return self.l[self.i-1]
        else:
            raise StopIteration
            
            
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
        print ("An instance of Partition Chain") 
        for a, b, c, d ,e , f in self.partition_chain_topology :
            print ("Service Chain ID=", a, \
                   " Bell ID=", b, \
                   " Partition ID=", c, \
                   " VNF ID=", d, \
                   " VNF CPU=", e, \
                   " VNF Flow=", f)

    def __iter__(self):
        return self

    def __next__(self):
        return self
    
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
    =========== ===============================================================
    """
    server_topology = [
             ('s1', 'c10', 'u3','a7',),
             ('s2', 'c10', 'u2','a8',),
            ]
    myServer = Server(location, server_topology)


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
             ('c1', 'v1', 'u3','o1',),
             ('c1', 'v2', 'u2','o2',),
             ('c2', 'v1', 'u5','o1',),
             ('c2', 'v3', 'u4','o2',),
             ('c2', 'v4', 'u2','o3',),
            ]
    myService_Chain = Service_Chain(location, service_chain_topology)

    
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

    myPartition_Chain = Partition_Chain(location, partition_chain_topology)


    return (myServer, myService_Chain, myPartition_Chain)

class cost_of_virtual_switching():
    """
    cost_of_virtual_switching
    To calculate the placement CPU cost between one subchain and one server
    Based on the IEEE INFOCOM 2018 -Apr 2018 Page 3-5
    Optimizing NFV Chian Deployment Through Minimizing the Cost of Virtual Switching
    """

    def __str__(self):
        return  random.uniform(0, 1)
    
    

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

    Example of the resulf of OCP.
    service_chain_placement = [
             ('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's1', 'c20', 'u6','a14',),
             ('c1', 'b1', 'p2', 'v2', 'u2', 'o2', 's2', 'c20', 'u4','a16',),           
  
             ('c2', 'b4', 'p1', 'v1', 'u5', 'o1', 's1', 'c20', 'u11','a9',),
             ('c2', 'b4', 'p2', 'v3', 'u4', 'o2', 's2', 'c20', 'u8','a12',),
             ('c2', 'b4', 'p1', 'v4', 'u2', 'o3', 's1', 'c20', 'u13','a7',),   
             
             ]
    
    This is the updated server_topology.
    server_topology = [
             ('s1', 'c20', 'u11','a9',),
             ('s2', 'c20', 'u8','a12',),
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
    myServer = []
    myService_Chain = []     
    myPartition_Chain = []
# To Test the cost_of_virtual_switching function
    for i in range(1, 11): 
        print (i , "  =  ", cost_of_virtual_switching())
    
#    for chain, bell, partition, vnf, usedcpu, order in localPartition_Chain:
#            for  server, cpu_total, cpu_used, cpu_available in myServer:
#                print ("==Partition==", chain, bell, partition, vnf, usedcpu, order, "==Server==", server, cpu_total, cpu_used, cpu_available  )

    def __init__(self, location, myServer, myService_Chain, myPartition_Chain):
        self.service_chain_placement_location_id = location
        self.myServer = myServer
        self.myService_Chain = myService_Chain        
        self.myPartition_Chain = myPartition_Chain

#        length = len(self.myServer) 
#        for i in range(length): 
#            print(self.myServer[i]) 
#            print ("==Server==", key )

#        self.perform_placement        

#        print (self.myServer)
#        print (self.myService_Chain)
#        print (self.myPartition_Chain)
        
    def __str__(self):        
        for chain in self.myPartition_Chain:
                print (chain[0])
                
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        return self

            
    def perform_placement(self):
        for chain, bell, partition, vnf, usedcpu, order in self.myPartition_Chain:
                for  server, cpu_total, cpu_used, cpu_available in self.myServer:
                    print ("==Partition==", chain, bell, partition, vnf, usedcpu, order, "==Server==", server, cpu_total, cpu_used, cpu_available  )

#    def perform_placement(self):
#        print ("==Server==", self.myServer.[0] )
        
#        for chain in self.myPartition_Chain:
#        for  key in self.myServer:
#            print ("==Server==", key )


        
    def __str__(self):
        return "The result of partition_chain on each server : Location_id=%s\n service_chain_placement=%s\n" % \
                (self.service_chain_placement_location_id, self.service_chain_placement)        


    
if __name__ == '__main__':

    location1 = 'Site1'
    
    """    
    Load all Server, Service Chain, and Partition into memory.
    """
    myServer, myService_Chain, myPartition_Chain = load_topology(location1)
    

    """    
    Print all Server, Service Chain, and Partition from memory.
    """
#    print ("Site = " , location1)
#    print (myServer)
    myServer.print_all_list()
#    print (myService_Chain)
    myService_Chain.print_all_list()
#    print (myPartition_Chain)
    myPartition_Chain.print_all_list()    
    
    
    """    
    To calculate the minimum cost placment of all service chains.
    """
    service_chain_placement = optimal_cost_placement(location1, myServer, myService_Chain, myPartition_Chain)
#    print (service_chain_placement)
#    service_chain_placement.perform_placement()