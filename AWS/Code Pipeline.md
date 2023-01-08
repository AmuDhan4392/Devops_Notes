### Code Pipeline

Step1: Search for code pipeline from AWS console and create pipeline

![image](https://user-images.githubusercontent.com/119385929/211191057-0bb36752-ae84-4607-b95a-99f21ffc3fee.png)

Step2: Add the source location

![image](https://user-images.githubusercontent.com/119385929/211191124-42a80f14-71aa-439b-9194-0c5f4dcc01d7.png)

Step3: Skip the build stage and in deploy stage provide the application name and deployment group

 ![image](https://user-images.githubusercontent.com/119385929/211191320-c8bf7174-fc99-449b-85b1-6ba55b9ae387.png)

Review and create the pipeline. Once created whenever the developers push the new version of code to S3 bucket it automatically deploys the application
  
  ![image](https://user-images.githubusercontent.com/119385929/211191405-97fbee6f-4715-4704-af33-04ce9d99ea47.png)

  ![image](https://user-images.githubusercontent.com/119385929/211191438-988f1dec-9072-4d13-bd89-b1e9c74fca6e.png)

In oder, to notify any failure in the pipeline

  ![image](https://user-images.githubusercontent.com/119385929/211191472-0d2e2879-00b6-4d2d-9ede-f6e20d85b497.png)

Before this create a SNS topic, refer below

  https://github.com/AmuDhan4392/Devops_Notes/blob/main/AWS/Cloudwatch.md

  ![image](https://user-images.githubusercontent.com/119385929/211191519-6127b850-734f-4e01-a0b9-6c95fa490ed8.png)
  
  ![image](https://user-images.githubusercontent.com/119385929/211191592-a4fef378-75be-4e23-922e-d19dfecee667.png)



