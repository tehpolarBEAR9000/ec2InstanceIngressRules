Overview
- Lists all EC2 instances with 'status=on' label  
- Gets all ingress rules for each instance  
- Output available in both CSV and JSON format   

Components
- Python script    
- BOTO3 Library  
- AWS APIs  
  : ec2.instances  
  : ec2.SecurityGroup    
- Dockerfile      

Output
- CSV or JSON file  
- List of all IP Ingress rules for each EC2 instance  
- Container image  
