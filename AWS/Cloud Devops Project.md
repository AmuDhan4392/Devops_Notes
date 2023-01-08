### Project:

Create a sample webpage which keeps on changing as per the demands of the project. To demonstrate implementation of Devops using AWS services.
Establish a codedeploy and pipeline for continuous intergration, testing and deployment.

Pipeline should have the following features

    1. Developers Code (what programming language?)
    2. EC2 Instances (developer, testing, production)
    3. Source code management (git, s3 bucket)
    4. IAM roles and policies
    5. Codedeploy
    6. SNS
    7. CLoudwatch
    
Step1: Creating two instances one for development and other for production.
  
  ![image](https://user-images.githubusercontent.com/119385929/211187218-9f1aea51-0933-4ffa-b96c-9a5f9a7c5785.png)

Adding tags to instances while creating for both the instances which will be helpful in mapping for codedeploy and pipeline
 
  ![image](https://user-images.githubusercontent.com/119385929/211187332-9b4b91ac-eacd-4299-b0a4-291b0b56dd4c.png)

Step2: Installing Codedeploy agent on production sever. Below is aws documentation

https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-linux.html
https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource-kit-bucket-names

Check whether codedeploy agent service is runninng, if not start the service
      
      systemctl status codedeploy-agent
      systemctl start codedeploy-agent
      systemctl enable codedeploy-agent

Step3: Creating IAM user and give access control.

 ![image](https://user-images.githubusercontent.com/119385929/211188067-90070903-4adc-4a9d-a2ee-9020dd833fb2.png)

Attaching policies to that user

 ![image](https://user-images.githubusercontent.com/119385929/211188157-283deffc-1c59-4ecb-94b6-831d86b6427e.png)

#### Creating Roles: The purpose for creating a roles is to communicate between two services(within AWS). So in this project we are creating roles to communicate 
#### between EC2 - S3 bucket and S3 bucket - Codedeploy, which will be helpful in later stage of this project.

  ![image](https://user-images.githubusercontent.com/119385929/211188336-c4fadaa0-7ff2-4143-8622-fbfc4363396d.png)

Attach IAM role to both the instances (development and production)

      EC2 Dashboard -----> Actions ------> Security ---------> Modify IAM Role

  ![image](https://user-images.githubusercontent.com/119385929/211188433-7c44caaf-7ec3-4a09-b50a-bb07332ffa4a.png)

Step4: In developer machine, starting creating the application code with codedeploy appspec file

#### What is Appspec file?

The application specification file (AppSpec file) is a YAML or JSON formatted file used by CodeDeploy to manage a deployment. The AppSpec file for an
EC2/On-Premises deployment must be named appspec.yml or appspec.json
 
Below is the documentation for creating appspec file format

https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-example.html

Developers would have created their application using any of the programming language and will be pushing it to common source code management platform from where
devops engineer will start configuring the deployment procedures

![Developer 2](https://user-images.githubusercontent.com/119385929/211189246-ff299f67-f1e7-4577-b33c-992a2028e4cb.png)

![Developer1](https://user-images.githubusercontent.com/119385929/211189247-11bd9dc3-2557-450c-80df-c8ea4166e21b.png)


Codedeploy:

https://github.com/AmuDhan4392/Devops_Notes/blob/main/AWS/Code%20Deploy.md

Code Pipeline:

https://github.com/AmuDhan4392/Devops_Notes/blob/main/AWS/Code%20Pipeline.md
