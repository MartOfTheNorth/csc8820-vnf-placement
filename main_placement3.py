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
        print ("") 
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
        print ("") 
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
        print ("") 
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
        
    def cost_of_virtual_switching_calculator(self,chain, bell, partition, vnf, \
                    usedcpu, order, server, cpu_total, cpu_used, cpu_available):
        return (random.uniform(0, 1))
        
        
    def __str__(self):
        return  (random.uniform(0, 1))
    
    

class optimal_cost_placement(object):
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
    =========== ===============================================================
    
    
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
    
    
    
#    service_chain_placement = [
#         ('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's1', 'c20', 'u6','a14',),
#         ('c1', 'b1', 'p2', 'v2', 'u2', 'o2', 's2', 'c20', 'u4','a16',),           
#  
#         ('c2', 'b4', 'p1', 'v1', 'u5', 'o1', 's1', 'c20', 'u11','a9',),
#         ('c2', 'b4', 'p2', 'v3', 'u4', 'o2', 's2', 'c20', 'u8','a12',),
#         ('c2', 'b4', 'p1', 'v4', 'u2', 'o3', 's1', 'c20', 'u13','a7',),   
#         
#         ]
    myServer = []
    myService_Chain = []     
    myPartition_Chain = []

    """
    # To Test the cost_of_virtual_switching function
    """
#    for i in range(1, 11): 
#        print (i , "  =  ", cost_of_virtual_switching())
    
    
    def __init__(self, location, myServer, myService_Chain, myPartition_Chain):
        self.service_chain_placement_location_id = location
        self.myServer = myServer
        self.myService_Chain = myService_Chain        
        self.myPartition_Chain = myPartition_Chain
        self.perform_placement()



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
        
        Condition:
            - Chain list is in pririty order from low to hight.
            - Chain list has not allowed the two same priority.
        """
#        print (myPartition_Chain)
#        print (type(myPartition_Chain))

        def m1(input):
            return int(input[1:])
        
        def madd(input, add):
            return int(int(input[1:])+int(add))
            
        def mdel(input, delete):
            return int(int(input[1:])-int(delete))   

        
        # Sort the Partition_Chain_Topology
#        print ('Before ====', myPartition_Chain.partition_chain_topology)
        myPartition_Chain.partition_chain_topology = \
            sorted(myPartition_Chain.partition_chain_topology)
#        print ('Sorted ====', myPartition_Chain.partition_chain_topology)

            
        # Find list of given Chain.
        # Find list of given Bell, Partion, VNF of Chain.
        myChainList = []
        myChainListAll = []
        for chain in myPartition_Chain.partition_chain_topology:
            myChainList.append(chain[0])
            myChainListAll.append(chain)              
        myChainList= sorted(set(myChainList))
        print ('MyChianList=', myChainList)

        # Start running fron Chain #1
        myChainRun = myChainList[0]
        for c in range (len(myChainList)):
            myChainRun = myChainList[c]
            print ('myChainRun=', myChainRun)
            
            # Find list of given Bell of this current Chain.
            # Find list of given Partition and VNF of Bell.            
            myBellList = []
            myBellListAll = []
            for bell in myChainListAll:
                if bell[0] == myChainRun :
                    myBellList.append(bell[1])
                    myBellListAll.append(bell)                    
            myBellList= sorted(set(myBellList))
            print ('MyBellList=', myBellList)
            
            myBellRun = myBellList[0]
            for b in range (len(myBellList)):
                    myBellRun = myBellList[b]
                    print ('myBellRun=', myBellRun)
                    
                    # Find list of given Partition of this current Bell.
                    # Find list of given VNF of Partition.
                    myPartionList = []
                    myPartionListAll = []
                    for partition in myBellListAll:
                        if ((partition[0] == myChainRun) and \
                            (partition[1] == myBellRun))  :
                            myPartionList.append(partition[2])
                            myPartionListAll.append(partition)
                    myPartionList= sorted(set(myPartionList))
                    myPartionListAll= sorted(set(myPartionListAll))
                    print ('MyPartionList=', myPartionList)
                    print ('myPartionListAll=', myPartionListAll)
                    
                    myPartionRun = myPartionList[0]
                    min_cv_partion = 1000
                    cv_at_partion = 0
                    service_chain_placement_partition = []
                    for p in range (len(myPartionList)):
                            myPartionRun = myPartionList[p]
                            print ('MyPartionRun=', myPartionRun)

                            # Find list of given VNF of this current Partition.
                            myVNFList = []
                            myVNFListAll = []
                            for vnf in myPartionListAll:
                                if ((vnf[0] == myChainRun) and \
                                    (vnf[1] == myBellRun) and \
                                    (vnf[2] == myPartionRun))  :
                                    myVNFList.append(vnf[3])
                                    myVNFListAll.append(vnf)
                            myVNFList= sorted(set(myVNFList))
                            myVNFListAll= sorted(set(myVNFListAll))
                            print ('myVNFList=', myVNFList)
                            print ('myVNFListAll=', myVNFListAll)
                            
                            # Start from 1st VNF
                            myVNFRun = myVNFList[0]
                            # Calulate the OPS cost switching of 
                            # each VNV on each server.
                            min_cv_vnf = 1
                            service_chain_placement_vnf = []
                            for v in range (len(myVNFList)):
                                    myVNFRun = myVNFList[v]
                                    print ('myVNFRun=', myVNFRun)
                                                                  

                                    myVNFonServerList = []
                                    for place in myVNFListAll:
                                        if ((place[0] == myChainRun) and \
                                            (place[1] == myBellRun) and \
                                            (place[2] == myPartionRun) and \
                                            (place[3] == myVNFRun)) :
                                                
                                             #Server   
                                             for s in Service_Chain.service_chain_topology :                    
                                                cv = \
                                        cost_of_virtual_switching.cost_of_virtual_switching_calculator( \
                                        self, myChainRun, myBellRun, myPartionRun, myVNFRun, \
                                        place[4], s[0], s[1], s[2], s[3] )
                                    
                                                if (cv < min_cv_vnf ):
                                                    min_cv_vnf = cv
                                                    service_chain_placement_vnf.append = place
                                                    cv_at_partion = cv_on_partion + cv
                                                    print (service_chain_placement_vnf)
                            #End of VNF Loop                             
                            if (cv_at_partion < min_cv_partion):
                                 min_cv_partion = cv_at_partion
                                
#         service_chain_placement = [
#             ('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's1', 'c20', 'u6','a14',),                                       
                                            



                        
#            for chain, bell in myPartition_Chain.partition_chain_topology:
#                if chain = 
#                myChainList.append(chain[0])
#            myChainList= sorted(set(myChainList))
#            print ('MyChianList=', myChainList)
            
#            for chain, bell, partition, vnf, usedcpu, order in myPartition_Chain.partition_chain_topology:
#                if myChainRun  == chain :
#                    #Define min= minimum CPU cost for this partition. Start with the highest whcih is 1.
#                    min = 1.0             
#                    # Define placement_temp as list
#                    placement_temp = []   
#                    print (chain, bell, partition)
#                    for  server, cpu_total, cpu_used, cpu_available in myServer.server_topology:
#                        print ("==Partition==", chain, bell, partition, vnf, usedcpu, order, \
#                               "==Server==", server, cpu_total, cpu_used, cpu_available  )
#                        
#                        cv = cost_of_virtual_switching.cost_of_virtual_switching_calculator(
#                                self, chain, bell, partition, vnf, usedcpu, order, \
#                                server, cpu_total, cpu_used, cpu_available )
#    #                    cv =0.9
#    #                    print (type(cv), ' cv = ', cv )
#                        if (cv < min ):
#                            min = cv
#                            placement_temp = (chain, bell, partition, vnf, usedcpu, order, \
#                                                  server, cpu_total, cpu_used, cpu_available )
#                            print ('cv < min : cv=', cv, ' min=', min )
                            
    #                        print (m1(placement_temp[0]))
    #                        print (madd(placement_temp[0], m1(placement_temp[1])))
    #                        print (mdel(placement_temp[0], m1(placement_temp[1])))
#                    if (float(cv) <= float(min) ):
#                        self.service_chain_placement.append(placement_temp )
#                        print ('placement_temp', placement_temp)
    #                    print (self.m1(placement_temp[0]))
    #                    print ('service_chain_placement', self.service_chain_placement)

                
        #End For loop of each chain




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
    print ("Site = " , location1)
#    print (myServer)
#    myServer.print_all_list()
##    print (myService_Chain)
#    myService_Chain.print_all_list()
##    print (myPartition_Chain)
#    myPartition_Chain.print_all_list()    
    
    
    """    
    To calculate the minimum cost placment of all service chains.
    """
#    service_chain_placement = optimal_cost_placement(location1, myServer, myService_Chain, myPartition_Chain)
    optimal_cost_placement(location1, myServer, myService_Chain, myPartition_Chain)
    
    
#    optimal_cost_placement.perform_placement()
##    print (service_chain_placement)
##    service_chain_placement.print_all_list()    
#    service_chain_placement.perform_placement()
    
        
    """    
    Print the result of placement
    """
#    print (service_chain_placement)
#    service_chain_placement.print_all_list()    
#    optimal_cost_placement.print_all_list()