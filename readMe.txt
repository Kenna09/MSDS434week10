--Create AWS user and log in to AWS locally--

Create a user in AWS IAM, give it a name then click next. Select Attach policies directly: search and add these roles:
AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
AmazonECS_FullAccess
AmazonS3FullAccess

click next, user created. And then click into your user and click "Create access key", select use case: Command Line Interface (CLI)
click next, then save or download the key info.

Install aws cli so you can use AWS commands in your local terminal


in your local terminal(I used bash in VSC) to configure AWS:
aws configure

it will prompt you with these questions below, use the key info you got from the key you just created above. questions: 

AWS Access Key ID [None]:
AWS Secret Access Key [None]: 
Default region name [None]: us-west-2
Default output format [None]: json

(not a command) just my AWS info. account ID: 941377144306



--Create docker image and push to AWS--

build the docker image locally:
docker build -t sentiment-wk10 .

to test locally:
docker run -p 8080:8080 sentiment-wk10

example command to login to AWS locally:
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com

What I used as a command:
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 941377144306.dkr.ecr.us-west-2.amazonaws.com

create repo in AWS:
aws ecr create-repository --repository-name sentiment-analysis-wk10

tag your image:
docker tag <docker-image> <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/sentiment-analysis-wk10

Note: sentiment-analysis is the name of my local docker image and sentiment-wk10 is the name of AWS ECR repository
docker tag sentiment-wk10 941377144306.dkr.ecr.us-west-2.amazonaws.com/sentiment-analysis-wk10





docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/sentiment-wk10:latest

docker push 941377144306.dkr.ecr.us-west-2.amazonaws.com/sentiment-analysis-wk10



