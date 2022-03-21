import boto3 
import csv,json

# storage class
class storageDriver():
    def __init__(self):
        self.instanceStorage = []
        self.ACLStorage = []
        self.joinedDATAStore = []
    def instanceDataStorage(self, updateStorageData: list) -> list:
        self.instanceStorage.append(updateStorageData)
        return self.instanceStorage
    def ACLDataStorage(self, updateACLData: list) -> list:
        self.ACLStorage.append(updateACLData)
        return self.ACLStorage
    def joinDataStorage(self):
        dataStore = zip(self.instanceStorage,self.ACLStorage)
        for set in dataStore:
            if set[1] != None:
                self.joinedDATAStore.append(set[0]+list(set[1][0]))
    def outputToCSV(self):
        #outputDATA = [['i-0f2af9db526ba74d2', 'sg-03eef53ce84a11079', 1433, 1433, '172.31.0.162/32'], ['i-0f2af9db526ba74d2', 'sg-097dc024170b8fc8a', 8080, 8080, '50.208.147.49/32'], ['i-0f2af9db526ba74d2', 'sg-0495a5fbd9afe4d76', 1433, 1433, '3.138.211.184/32'], ['i-0f2af9db526ba74d2', 'sg-028227f34657d2ced', 80, 80, '172.31.28.55/32'], ['i-0f2af9db526ba74d2', 'sg-09afa408219e441d7', 80, 80, '3.137.182.93/32'], ['i-0f2af9db526ba74d2', 'sg-09383f7b4c062692e', 1433, 1433, '34.211.164.21/32'], ['i-0f2af9db526ba74d2', 'sg-000cabe2444a0c797', 1433, 1433, '172.31.28.55/32'], ['i-0f2af9db526ba74d2', 'sg-0765b8d169d781366', 1433, 1433, '172.31.16.0/20'], ['i-0f2af9db526ba74d2', 'sg-0bd7b485eb9f42a77', 1433, 1433, '18.224.134.61/32'], ['i-0bc3f754bfd670387', 'sg-0a9fbeabb7533b525', 22, 22, '50.208.147.49/32'], ['i-09aec994905f631b6', 'sg-0495a5fbd9afe4d76', 1433, 1433, '3.138.211.184/32'], ['i-09aec994905f631b6', 'sg-0228b9f1d1e9dd5ec', 1433, 1433, '199.168.209.50/32'], ['i-09aec994905f631b6', 'sg-08a1378d78bca0fee', 1433, 1433, '172.31.0.162/32'], ['i-09aec994905f631b6', 'sg-0ffae324aa82645a3', 1433, 1433, '169.254.192.220/30'], ['i-09aec994905f631b6', 'sg-025c051c56ddc14af', 80, 80, '172.31.5.71/32'], ['i-09aec994905f631b6', 'sg-0765b8d169d781366', 1433, 1433, '172.31.16.0/20'], ['i-0ecb60e0fb64003a8', 'sg-0228b9f1d1e9dd5ec', 1433, 1433, '199.168.209.50/32'], ['i-0ecb60e0fb64003a8', 'sg-0ffae324aa82645a3', 1433, 1433, '169.254.192.220/30'], ['i-0ecb60e0fb64003a8', 'sg-08efb1980198149cb', 445, 445, '172.31.0.162/32'], ['i-0ecb60e0fb64003a8', 'sg-025c051c56ddc14af', 80, 80, '172.31.5.71/32'], ['i-0ecb60e0fb64003a8', 'sg-0765b8d169d781366', 1433, 1433, '172.31.16.0/20'], ['i-0a96dbc89ecab7a7f', 'sg-085f9fc172072210e', 1433, 1433, '73.114.208.138/32'], ['i-0a96dbc89ecab7a7f', 'sg-0d90b2348c2e8bba8', 445, 445, '172.31.17.75/32'], ['i-0a96dbc89ecab7a7f', 'sg-0e22459086bb51cdc', 3389, 3389, '50.208.147.49/32'], ['i-04f60541d9574c08b', 'sg-0c682655437ff353c', 22, 22, '172.31.0.162/32'], ['i-04f60541d9574c08b', 'sg-085f9fc172072210e', 1433, 1433, '73.114.208.138/32'], ['i-04f60541d9574c08b', 'sg-0d90b2348c2e8bba8', 445, 445, '172.31.17.75/32'], ['i-04f60541d9574c08b', 'sg-0e22459086bb51cdc', 3389, 3389, '50.208.147.49/32'], ['i-0650524ec48e1c282', 'sg-03eef53ce84a11079', 1433, 1433, '172.31.0.162/32'], ['i-0650524ec48e1c282', 'sg-0c682655437ff353c', 22, 22, '172.31.0.162/32'], ['i-0650524ec48e1c282', 'sg-0a2be036096b6a57c', 445, 445, '172.31.28.55/32'], ['i-0650524ec48e1c282', 'sg-07c4d63eca52e36c6', 1433, 1433, '50.208.147.49/32'], ['i-0650524ec48e1c282', 'sg-08efb1980198149cb', 445, 445, '172.31.0.162/32'], ['i-0650524ec48e1c282', 'sg-0e22459086bb51cdc', 3389, 3389, '50.208.147.49/32'], ['i-0f22eb96a91ceb307', 'sg-0c682655437ff353c', 22, 22, '172.31.0.162/32'], ['i-0f22eb96a91ceb307', 'sg-08efb1980198149cb', 445, 445, '172.31.0.162/32'], ['i-0f22eb96a91ceb307', 'sg-0c0afda9f1d5fface', 3389, 3389, '172.31.0.162/32'], ['i-0f22eb96a91ceb307', 'sg-0bc8ea5f4fd6682de', 5985, 5985, '172.31.5.71/32'], ['i-0eec8a9371384d530', 'sg-090dfb5c08a4db15b', 22, 22, '50.208.147.49/32'], ['i-0bd345e877c67419f', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-0bd345e877c67419f', 'sg-083743025ba1721de', 30608, 30608, '172.31.28.55/32'], ['i-0d84b5dfcbe2cecf6', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-032df07706434e602', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-07a4bc4a204c56cc8', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-07a4bc4a204c56cc8', 'sg-083743025ba1721de', 30608, 30608, '172.31.28.55/32'], ['i-01e95e412f26ac7f2', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-09f5fe5104c7023c4', 'sg-02065ddda1dfeb5eb', 22, 22, '3.15.100.195/32'], ['i-09b4829829185012b', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-0ea81d11d1eea6c0b', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-09622c4a4248bacd2', 'sg-0896224c1e8c5fbd5', -1, -1, '192.168.9.0/24'], ['i-09622c4a4248bacd2', 'sg-0f41727aee10c0643', 22, 22, '192.168.9.0/24'], ['i-02f20118c49830f54', 'sg-0896224c1e8c5fbd5', -1, -1, '192.168.9.0/24'], ['i-02f20118c49830f54', 'sg-0f41727aee10c0643', 22, 22, '192.168.9.0/24'], ['i-000ad213d3bb16503', 'sg-02065ddda1dfeb5eb', 22, 22, '3.15.100.195/32'], ['i-0705344aad1f9971c', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-038bee3ba5a7bed40', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-05fd0af6abd28c1f3', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32']]
        headers = ['instanceID','securityGroupID','FromPort','ToPort','CidrIP']
        with open('secGroupsPerInstance.csv', 'w', newline='') as fileOBJ:
            outputToCSV = csv.writer(fileOBJ)
            outputToCSV.writerow(headers)
            outputToCSV.writerows(self.joinedDATAStore)
            #outputToCSV.writerows(outputDATA)
            fileOBJ.close()
    def outputToJSON(self):
        #outputDATA = [['i-0f2af9db526ba74d2', 'sg-03eef53ce84a11079', 1433, 1433, '172.31.0.162/32'], ['i-0f2af9db526ba74d2', 'sg-097dc024170b8fc8a', 8080, 8080, '50.208.147.49/32'], ['i-0f2af9db526ba74d2', 'sg-0495a5fbd9afe4d76', 1433, 1433, '3.138.211.184/32'], ['i-0f2af9db526ba74d2', 'sg-028227f34657d2ced', 80, 80, '172.31.28.55/32'], ['i-0f2af9db526ba74d2', 'sg-09afa408219e441d7', 80, 80, '3.137.182.93/32'], ['i-0f2af9db526ba74d2', 'sg-09383f7b4c062692e', 1433, 1433, '34.211.164.21/32'], ['i-0f2af9db526ba74d2', 'sg-000cabe2444a0c797', 1433, 1433, '172.31.28.55/32'], ['i-0f2af9db526ba74d2', 'sg-0765b8d169d781366', 1433, 1433, '172.31.16.0/20'], ['i-0f2af9db526ba74d2', 'sg-0bd7b485eb9f42a77', 1433, 1433, '18.224.134.61/32'], ['i-0bc3f754bfd670387', 'sg-0a9fbeabb7533b525', 22, 22, '50.208.147.49/32'], ['i-09aec994905f631b6', 'sg-0495a5fbd9afe4d76', 1433, 1433, '3.138.211.184/32'], ['i-09aec994905f631b6', 'sg-0228b9f1d1e9dd5ec', 1433, 1433, '199.168.209.50/32'], ['i-09aec994905f631b6', 'sg-08a1378d78bca0fee', 1433, 1433, '172.31.0.162/32'], ['i-09aec994905f631b6', 'sg-0ffae324aa82645a3', 1433, 1433, '169.254.192.220/30'], ['i-09aec994905f631b6', 'sg-025c051c56ddc14af', 80, 80, '172.31.5.71/32'], ['i-09aec994905f631b6', 'sg-0765b8d169d781366', 1433, 1433, '172.31.16.0/20'], ['i-0ecb60e0fb64003a8', 'sg-0228b9f1d1e9dd5ec', 1433, 1433, '199.168.209.50/32'], ['i-0ecb60e0fb64003a8', 'sg-0ffae324aa82645a3', 1433, 1433, '169.254.192.220/30'], ['i-0ecb60e0fb64003a8', 'sg-08efb1980198149cb', 445, 445, '172.31.0.162/32'], ['i-0ecb60e0fb64003a8', 'sg-025c051c56ddc14af', 80, 80, '172.31.5.71/32'], ['i-0ecb60e0fb64003a8', 'sg-0765b8d169d781366', 1433, 1433, '172.31.16.0/20'], ['i-0a96dbc89ecab7a7f', 'sg-085f9fc172072210e', 1433, 1433, '73.114.208.138/32'], ['i-0a96dbc89ecab7a7f', 'sg-0d90b2348c2e8bba8', 445, 445, '172.31.17.75/32'], ['i-0a96dbc89ecab7a7f', 'sg-0e22459086bb51cdc', 3389, 3389, '50.208.147.49/32'], ['i-04f60541d9574c08b', 'sg-0c682655437ff353c', 22, 22, '172.31.0.162/32'], ['i-04f60541d9574c08b', 'sg-085f9fc172072210e', 1433, 1433, '73.114.208.138/32'], ['i-04f60541d9574c08b', 'sg-0d90b2348c2e8bba8', 445, 445, '172.31.17.75/32'], ['i-04f60541d9574c08b', 'sg-0e22459086bb51cdc', 3389, 3389, '50.208.147.49/32'], ['i-0650524ec48e1c282', 'sg-03eef53ce84a11079', 1433, 1433, '172.31.0.162/32'], ['i-0650524ec48e1c282', 'sg-0c682655437ff353c', 22, 22, '172.31.0.162/32'], ['i-0650524ec48e1c282', 'sg-0a2be036096b6a57c', 445, 445, '172.31.28.55/32'], ['i-0650524ec48e1c282', 'sg-07c4d63eca52e36c6', 1433, 1433, '50.208.147.49/32'], ['i-0650524ec48e1c282', 'sg-08efb1980198149cb', 445, 445, '172.31.0.162/32'], ['i-0650524ec48e1c282', 'sg-0e22459086bb51cdc', 3389, 3389, '50.208.147.49/32'], ['i-0f22eb96a91ceb307', 'sg-0c682655437ff353c', 22, 22, '172.31.0.162/32'], ['i-0f22eb96a91ceb307', 'sg-08efb1980198149cb', 445, 445, '172.31.0.162/32'], ['i-0f22eb96a91ceb307', 'sg-0c0afda9f1d5fface', 3389, 3389, '172.31.0.162/32'], ['i-0f22eb96a91ceb307', 'sg-0bc8ea5f4fd6682de', 5985, 5985, '172.31.5.71/32'], ['i-0eec8a9371384d530', 'sg-090dfb5c08a4db15b', 22, 22, '50.208.147.49/32'], ['i-0bd345e877c67419f', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-0bd345e877c67419f', 'sg-083743025ba1721de', 30608, 30608, '172.31.28.55/32'], ['i-0d84b5dfcbe2cecf6', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-032df07706434e602', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-07a4bc4a204c56cc8', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-07a4bc4a204c56cc8', 'sg-083743025ba1721de', 30608, 30608, '172.31.28.55/32'], ['i-01e95e412f26ac7f2', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-09f5fe5104c7023c4', 'sg-02065ddda1dfeb5eb', 22, 22, '3.15.100.195/32'], ['i-09b4829829185012b', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32'], ['i-0ea81d11d1eea6c0b', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-09622c4a4248bacd2', 'sg-0896224c1e8c5fbd5', -1, -1, '192.168.9.0/24'], ['i-09622c4a4248bacd2', 'sg-0f41727aee10c0643', 22, 22, '192.168.9.0/24'], ['i-02f20118c49830f54', 'sg-0896224c1e8c5fbd5', -1, -1, '192.168.9.0/24'], ['i-02f20118c49830f54', 'sg-0f41727aee10c0643', 22, 22, '192.168.9.0/24'], ['i-000ad213d3bb16503', 'sg-02065ddda1dfeb5eb', 22, 22, '3.15.100.195/32'], ['i-0705344aad1f9971c', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-038bee3ba5a7bed40', 'sg-0540c549e49598e02', 443, 443, '172.31.28.55/32'], ['i-05fd0af6abd28c1f3', 'sg-08464ddf1409820ff', 443, 443, '172.31.28.55/32']]
        dictionary = {}
        for i in range(len(self.joinDataStorage)):
            dictionary[i] = {"instanceID":self.joinDataStorage[i][0],"securityGroupID":self.joinDataStorage[i][1],"FromPort":self.joinDataStorage[i][2],"ToPort":self.joinDataStorage[i][3],"CidrIP":self.joinDataStorage[i][4]}
        with open("test.json","w") as outfile:
            outfile.write(json.dumps(dictionary))
            outfile.close()

ec2 = boto3.resource('ec2')
def listInstances(ec2,logDriver):
    instances = ec2.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    "running"
                ]
            }
        ],
        MaxResults = 100
    )
    for instance in instances:
        for group in instance.security_groups:
            logDriver.instanceDataStorage([instance.id,group['GroupId']])
            logDriver.ACLDataStorage(listSecurityGroupACLS(ec2.SecurityGroup(group['GroupId']).ip_permissions))     
def listSecurityGroupACLS(securityGroup):
    #ingressListings = [{'FromPort': 1433, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '34.211.164.21/32', 'Description': 'Payix Reporting'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 1433, 'UserIdGroupPairs': []}, {'FromPort': 3389, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '18.205.40.159/32', 'Description': 'Payix AWS'}, {'CidrIp': '71.78.90.154/32', 'Description': 'Payix Office'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 3389, 'UserIdGroupPairs': []}, {'FromPort': 443, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '18.205.4.100/32', 'Description': 'TWF - Payix Silo'}, {'CidrIp': '18.205.40.159/32', 'Description': 'Payix AWS'}, {'CidrIp': '18.233.238.147/32', 'Description': 'Rt138 Payix Silo'}, {'CidrIp': '23.21.50.212/32', 'Description': 'IVY - Payix Silo'}, {'CidrIp': '3.225.211.57/32', 'Description': 'UBCC - Payix Silo'}, {'CidrIp': '3.227.204.217/32', 'Description': 'Macho - Payix Silo'}, {'CidrIp': '3.232.161.67/32', 'Description': 'RUF - Payix Silo'}, {'CidrIp': '3.91.114.90/32', 'Description': 'Rt66 - Payix Silo'}, {'CidrIp': '34.233.181.8/32', 'Description': 'Payix - 10262021'}, {'CidrIp': '34.236.4.152/32', 'Description': 'MCE - Payix Silo'}, {'CidrIp': '35.169.194.97/32', 'Description': 'AWF - Payix Silo'}, {'CidrIp': '52.1.38.204/32', 'Description': 'Husky Payix Silo'}, {'CidrIp': '52.202.51.89/32', 'Description': 'AWF - Payix Silo'}, {'CidrIp': '52.205.97.104/32', 'Description': 'UBCC - Payix Silo'}, {'CidrIp': '52.21.33.58/32', 'Description': 'IHF - Payix Silo'}, {'CidrIp': '52.45.216.75/32', 'Description': 'Powersports'}, {'CidrIp': '54.144.168.251/32', 'Description': 'ORF - Payix Silo'}, {'CidrIp': '54.144.170.200/32', 'Description': 'SVF - Payix Silo'}, {'CidrIp': '54.160.41.86/32', 'Description': 'Husky Payix Silo'}, {'CidrIp': '54.161.165.128/32', 'Description': 'Payix - 10262021'}, {'CidrIp': '54.211.142.113/32', 'Description': 'PSL - Payix Silo'}, {'CidrIp': '54.242.6.30/32', 'Description': 'Trinity - Payix Silo'}, {'CidrIp': '54.85.140.252/32', 'Description': 'FFC - Payix Silo'}, {'CidrIp': '75.101.171.108/32', 'Description': 'UBCC - Payix Silo'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 443, 'UserIdGroupPairs': []}]
    for IPRule in securityGroup:
        for egressRule in IPRule['IpRanges']:
            return [(IPRule['FromPort'],IPRule['ToPort'],IPRule['CidrIp'])]

logDriver = storageDriver()
listInstances(ec2,logDriver)
logDriver.joinDataStorage()
logDriver.outputToCSV()
logDriver.outputToJSON()