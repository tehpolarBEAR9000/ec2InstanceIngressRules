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
        #outputDATA = [['i-0f2af9db526ba74d2', 'sg-03eef53ce84a11079', 1433, 1433, '172.31.0.162/32'], ['i-0f2af9db526ba74d2', 'sg-097dc024170b8fc8a', 8080, 8080, '192.168.1.14/32'], ['i-0f2af9db526ba74d2', 'sg-0495a5fbd9afe4d76', 1433, 1433, '10.10.0.12/32']]
        headers = ['instanceID','securityGroupID','FromPort','ToPort','CidrIP']
        with open('secGroupsPerInstance.csv', 'w', newline='') as fileOBJ:
            outputToCSV = csv.writer(fileOBJ)
            outputToCSV.writerow(headers)
            outputToCSV.writerows(self.joinedDATAStore)
            #outputToCSV.writerows(outputDATA)
            fileOBJ.close()
    def outputToJSON(self):
        #outputDATA = [['i-0f2af9db526ba74d2', 'sg-03eef53ce84a11079', 1433, 1433, '172.31.0.162/32'], ['i-0f2af9db526ba74d2', 'sg-097dc024170b8fc8a', 8080, 8080, '192.168.1.14/32'], ['i-0f2af9db526ba74d2', 'sg-0495a5fbd9afe4d76', 1433, 1433, '10.10.0.12/32']]
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
    #ingressListings = [ {'FromPort': 1433, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '172.21.15.12/32', 'Description': 'Reporting'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 1433, 'UserIdGroupPairs': []}, {'FromPort': 3389, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': '192.168.10.23/23', 'Description': 'AWS'}, {'CidrIp': '10.10.23.12/32', 'Description': 'Office'}], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 3389, 'UserIdGroupPairs': []}]
    for IPRule in securityGroup:
        for egressRule in IPRule['IpRanges']:
            return [(IPRule['FromPort'],IPRule['ToPort'],IPRule['CidrIp'])]

logDriver = storageDriver()
listInstances(ec2,logDriver)
logDriver.joinDataStorage()
logDriver.outputToCSV()
logDriver.outputToJSON()
