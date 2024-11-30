

aws configure

AWS Access Key ID [None]:
AWS Secret Access Key [None]: 
Default region name [None]: us-west-2
Default output format [None]: json

(not a command) account ID: 941377144306

docker build -t sentiment-wk9 .

to test locally:
docker run -p 8080:8080 sentiment-wk9

aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 941377144306.dkr.ecr.us-west-2.amazonaws.com




aws ecr create-repository --repository-name sentiment-analysis-wk10



docker tag <docker-image> <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/sentiment-analysis-wk9

Note: sentiment-analysis is the name of my local docker image and sentiment-wk8 is the name of AWS ECR repository
docker tag sentiment-wk9 941377144306.dkr.ecr.us-west-2.amazonaws.com/sentiment-analysis-wk10





docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/sentiment-wk8:latest

docker push 941377144306.dkr.ecr.us-west-2.amazonaws.com/sentiment-analysis-wk10



