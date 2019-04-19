# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:58:06 2019
Georgia State University
CSC8820
@author: Mart Panichvatana

"""
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
    
    def __str__(self):
        return "An instance of partition_chain : partition_chain_location_id=%s\n partition_chain_topology=%s\n" % \
                (self.partition_chain_location_id, self.partition_chain_topology)
                
                
def load_topology():
    
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
    myServer = Server('Site_1', server_topology)
    print (myServer)
    myServer.print_all_list()

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
    myService_Chain = Service_Chain('Site_1', service_chain_topology)
    print (myService_Chain)
    myService_Chain.print_all_list()
    
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

    myPartition_Chain = Partition_Chain('Site_1', partition_chain_topology)
    print (myPartition_Chain)
    myPartition_Chain.print_all_list()


def optimal_cost_placement():
    """
    optimal_cost_placement


    """
    
    
if __name__ == '__main__':
    """    
    Load all Server, Service Chain, and Partition into memory.
    """
    load_topology()

    """    
    To calculate the minimum cost placment of all service chains.
    """
    optimal_cost_placement()
