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
             ('s1', 'c20', 'u3','a17',),
             ('s2', 'c20', 'u2','a18',),
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
#             
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
    service_chain_server_result = []    
    myServer = []
    myService_Chain = []     
    myPartition_Chain = []


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


        

        def m1(input):
            return int(input[1:])
        
        def madd(input, add):
            return (input[0]+str(int(input[1:])+int(add)))
            
        def mdel(input, delete):
            return (input[0]+str(int(input[1:])-int(delete)))      
        
        def UpdateServerResource(vnf_list, server_list):
            """
            Function for upgrading myServer list.
            Input : the VNF list and current Server list on VNF level
            Output : The udpated of both lists
            
            For Example:
            Input :
                VNF list= ('c1', 'b1', 'p1', 'v1', 'u3', 'o1', 's2', 'c20', 'u2', 'a18')
                Server list = [
                                 ('s1', 'c20', 'u3','a17',),
                                 ('s2', 'c20', 'u2','a18',),
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
#            print ('===============myChainRun=', myChainRun)
            
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
            myBellServer = myChainServer           
            myBellRun = myBellList[0]
            min_cv_at_bell = 1000
            cv_at_bell = 0            
            service_chain_placement_bell = []
            for b in range (len(myBellList)):
                    myBellRun = myBellList[b]
#                    print ('===============myBellRun=', myBellRun)
                    
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
                    myPartionRun = myPartionList[0]
#                    min_cv_at_partition = 1000
                    cv_at_bell = 0  
                    cv_at_partition = 0                  
                    service_chain_placement_partition = []
                    for p in range (len(myPartionList)):
                            myPartionRun = myPartionList[p]
#                            print ('MyPartionRun=', myPartionRun)
    
                            """
                            # Find list of given VNF of this current Partition.
                            """
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
#                            print ('myVNFList=', myVNFList)
#                            print ('myVNFListAll=', myVNFListAll)
                            
                            """
                            # Start from 1st VNF
                            """
                            myVNFServer = myPartitionServer
                            myVNFRun = myVNFList[0]
                            
                            """
                            # Calulate the OPS cost switching of 
                            # each VNV on each server.
                            """
#                            min_cv_at_vnf = 1
                            cv_at_vnf = 0
                            service_chain_placement_vnf = []
                            for v in range (len(myVNFList)):
                                    myVNFRun = myVNFList[v]
#                                    print ('myVNFRun=', myVNFRun)
                                                                  
                                    """
                                    # Search the required CPU 
                                    """
                                    service_chain_placement_vnf_server = ()
                                    min_cv_at_server = 1
                                    cv_at_server = 0
                                    for cpu in myVNFListAll:
                                        if ((cpu[0] == myChainRun) and \
                                            (cpu[1] == myBellRun) and \
                                            (cpu[2] == myPartionRun) and \
                                            (cpu[3] == myVNFRun)) :
                                            
#                                             print('==VNF==')
                                            """
                                            # Search cost on each Server   
                                             for s in  self.myServer.server_topology   :     
                                            """
                                            for s in  myVNFServer  : 
                                                cv_at_server = \
                                        cost_of_virtual_switching.cost_of_virtual_switching_calculator( \
                                        self, myChainRun, myBellRun, myPartionRun, myVNFRun, \
                                        cpu[4], cpu[5], s[0], s[1], s[2], s[3] )
                                                

                                                if (cv_at_server < min_cv_at_server ):
                                                    min_cv_at_server = cv_at_server
                                                    service_chain_placement_vnf_server = (myChainRun, myBellRun, \
                                                            myPartionRun, myVNFRun, cpu[4], cpu[5], s[0], s[1], s[2], s[3] )

                                            """
                                             # Search cost on each Server   
                                             # After Exit Server Loop ==> Only lowest cv_at_server in list                                                    
                                            """

    
                                    """
                                    # Bottom of VNF Loop ==> Adding cv_at_server to VNF
                                    """
                                    cv_at_vnf = cv_at_vnf + cv_at_server

                                    
                                    """
                                    # Update Server Resource based on the allocated CPU
                                    """
                                    service_chain_placement_vnf_server, myVNFServer = \
                                        UpdateServerResource(service_chain_placement_vnf_server, myVNFServer)
     

                                    service_chain_placement_vnf.append(service_chain_placement_vnf_server)

                                    
                            """
                            # Bottom of Partition Loop ==> Adding cv_at_vnf to Partition
                            """
                            cv_at_partition = cv_at_partition + cv_at_vnf     

                            
                            service_chain_placement_partition.append(service_chain_placement_vnf)

                            myPartitionServer = myVNFServer

                    """
                    # After Exit Partition Loop ==> Adding cv_at_vnf to Partition
                    """
#                    print ('min_cv_at_partition =',  min_cv_at_partition)                    
                    """
                    # Bottom of Bell Loop    
                    """
                    cv_at_bell = cv_at_bell + cv_at_partition    

                    if (cv_at_bell < min_cv_at_bell): 
                        service_chain_placement_bell = []                                               
                        min_cv_at_bell = cv_at_bell
                        service_chain_placement_bell.append(service_chain_placement_partition)  # adding cv_at_bell
                        myBellServerMin = myPartitionServer    
#                        print ('BBBBB')                     
            """
            # After Exit Bell Loop    
            """
#            print ('min_cv_at_bell =',  min_cv_at_bell)               
            
            """
            # Bottom of Chain Loop    
            """
            self.service_chain_placement.append(service_chain_placement_bell)  # adding cv_at_bell
            service_chain_result = []
            service_chain_result = []
            def list_all(obj):
                if not isinstance(obj, list):
                    return [obj]
                else:
                    return [item for sublist in obj for item in list_all(sublist)]
           
            service_chain_result = (list_all(self.service_chain_placement))   
            
            myChainServer = myBellServerMin
            service_chain_server_result = myChainServer

        """
        Print the placement result on screen
        """
        print ("") 
        print ("Print the placement result on screen") 
        print ("") 
        print ("The result of Service Chain on Servers.")         
        for a, b, c, d ,e , f, g, h, i, j in service_chain_result :
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
#        print ('service_chain_result ==== ', service_chain_result)       
        print ("") 
        print ("The result of Server acclocation.") 
        for a, b, c, d in service_chain_server_result :
            print ("Server       =", a)
            print ("cpu_total    =", b)            
            print ("cpu_used     =", c)       
            print ("cpu_available=", d)  


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
    myServer.print_all_list()
#    print (myService_Chain)
    myService_Chain.print_all_list()
#    print (myPartition_Chain)
    myPartition_Chain.print_all_list()    
    
    
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
    print (optimal_cost_placement.service_chain_placement)
    print ("") 

       