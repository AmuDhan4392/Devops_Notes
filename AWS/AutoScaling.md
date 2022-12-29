### Auto Scaling:

In order to create a auto scaling we need to have an AMI image, Load balancer, launch configurations.

We can create a AMI image either from running or stopped instances were our application/webserver has been hosted. Provide the image name and save it which can be viewed from right side of the dashboard(AMI)

![AMI Image](https://user-images.githubusercontent.com/119385929/209920839-a7b27657-c8c2-4eef-bb8c-ad04bd8682c8.png)

#### Elastic Load Balancer:

Create a classic ELB which is available in bottom.

![CEBL1](https://user-images.githubusercontent.com/119385929/209920691-b711b53f-a9da-4ae2-9b41-f73e9a94de39.png)

Select the existing security group 

![CEBL2](https://user-images.githubusercontent.com/119385929/209920700-87f6c2d1-547b-4c28-864e-d0810d9b9e96.png)

Configuring health check: Used to check the status of the server's/instances for every interval time to know whether it is in up state or not.

![CEBL3](https://user-images.githubusercontent.com/119385929/209920707-42b2d7dd-892c-4dae-8db5-22af33daf454.png)

No need to add any EC2 instances in load balancer's as it creates while doing for auto scaling

![CEBL4](https://user-images.githubusercontent.com/119385929/209920718-64a21eb5-5cd3-4045-aa5c-f27684e8fea5.png)

Add key and value in tag tabs 

![CEBL5](https://user-images.githubusercontent.com/119385929/209920738-1a431d69-46d4-4d62-9059-2797cff67ec4.png)

Finally review and create a LB

![CEBL7](https://user-images.githubusercontent.com/119385929/209920749-15947fda-4998-4ba4-8794-e637f9d6bfae.png)

#### Launch Configuration to be created using AMI image. LC cannot be edited after creation it can be copied and used as template.

LC is available in right side of the dashboard and click create. Provide the name and select for amazon machine image

![LC1](https://user-images.githubusercontent.com/119385929/209921797-571064ac-e2ae-47e2-b62c-065e9c1471b1.png)

Choose instance type, free tier

![LC2](https://user-images.githubusercontent.com/119385929/209922163-b0d29c7a-ee0d-4e32-b038-0dbfd595ac56.png)


The storage volumes are created based on the base image we uploaded if needed we can add additional space.

Select the existing security group which we provided in load balancer as well

![LC3](https://user-images.githubusercontent.com/119385929/209922173-2f5f44f0-1d09-4a36-bcee-9418b1fc0aae.png)

Choose the key pair while creating the instances

![LC4](https://user-images.githubusercontent.com/119385929/209922317-e47a63ea-eba3-475f-a0e9-b2c5a77f3116.png)

Then create launch configuration

![LC5](https://user-images.githubusercontent.com/119385929/209922470-3f6de7bf-cd2d-4c5d-b29a-e824ec3c092c.png)

#### Auto Scaling:

The purpose of using autoscaling is to scali-in or scale-out the website/application traffic during peak and non-peak hours/days

Scale -in Reducing instances

Scale -out Adding instances

aka Fleet Management

Auto Scaling used for only front end application.

Go to auto scaling group in the AWS dashboard and click on create. Provide AGS name and switch to launch configuration & select it from drop-down

![ags1](https://user-images.githubusercontent.com/119385929/209923429-1d29101b-5c91-4e03-b2a5-e47badb674e1.png)

Click next and then add network options like VPC and availability zones. Keep in mind choosing availability zones should be based on our target users/customers 
who is going to access our applications.

![AGS2](https://user-images.githubusercontent.com/119385929/209924106-3f006558-d465-41dc-9619-3928de9a2056.png)

We have already created load balancer so know attaching and configuring the health check up. Since we have created classic LB we are enabling CBL or else enable 
target LB groups.

![AGS3](https://user-images.githubusercontent.com/119385929/209924116-2268ca00-11e9-433a-801a-988c9ab4587f.png)

Configuring the group size and policies. Desired capacity, Minimum capcity (scale-in), Maximum capacity (scale-out) when auto scaling is launched if the desired capacity
is 2, then 2 instances will be launched. Depends upon the instances utilization auto scaling triggers the next instances with same application configuration.

![AGS4](https://user-images.githubusercontent.com/119385929/209925334-342064d2-1f32-46ff-b085-98e01c52aecd.png)

![AGS5](https://user-images.githubusercontent.com/119385929/209925342-270c9e88-72e8-4512-b747-82570996782d.png)

Autoscaling as well as two new instances created.

![AGS6](https://user-images.githubusercontent.com/119385929/209925608-68e068cf-fa1b-4384-994b-c5321e78a597.png)

![AGS7](https://user-images.githubusercontent.com/119385929/209925617-d84bc906-3707-46b2-9c12-2307682fdfdd.png)

