#### Elastic Block Storage:

EBS allows us to create storage volumes to running/stopped EC2 instances. One attached, we can create file system on that volumes and use them for our purpose

Step1: Create volume from the left side (EBS) of the dashboard

![image](https://user-images.githubusercontent.com/119385929/210324680-dba9635b-8e95-43fb-b823-76ba0a77a34c.png)

Step2: Provide volume type (general/IOPS) and availability zone, remember the EBS will be attached to EC2 instances so choose the same availability zone

![image](https://user-images.githubusercontent.com/119385929/210325087-664be413-1258-4117-98fe-d7ff2c70a5b9.png)

Step 3: Volume has been created and it is ready to use which can be seen from volume state.
From attached instances tab, in which location it has been mounted in EC2 instances

![image](https://user-images.githubusercontent.com/119385929/210325307-493de645-4e07-43ab-986f-0e46556942ea.png)

Step 4: Adding EBS to EC2 instnaces and then configurating it. Either new instances can be created n added / add it to existing instance as well

![image](https://user-images.githubusercontent.com/119385929/210326184-f72dfe8b-a082-4a0e-8197-db272b99382b.png)

Attachig volume to EC2 instances

![image](https://user-images.githubusercontent.com/119385929/210326305-2de504f3-d90a-44e7-87ef-e64b783f31aa.png)

Step 5: Now Log into the instances to see it is available. Create a file system and mount point for uninterpreted usuage of the volume.

![image](https://user-images.githubusercontent.com/119385929/210326919-33a03b63-5eab-43a9-b8c0-beb0313e9cd3.png)
![image](https://user-images.githubusercontent.com/119385929/210327846-05914c21-98ac-4dea-ba9c-5f4910223c6f.png)
![image](https://user-images.githubusercontent.com/119385929/210327909-3892f4b7-edae-430d-9148-efc5cdf596b1.png)

To mount permently, registry the mount point in "/etc/fstab" while booting it will load all the available file system.

#### CloudWatch:

Cloudwatch is a inbuild monitoring tools available in AWS.Uses alarms, logs and event data to take automated actions and reduce time to resolution.
Step1: Create SNS (Simple Notification Service)

![image](https://user-images.githubusercontent.com/119385929/210336089-a634e110-2b50-4cdd-b4c0-2c9b40a74c3d.png)

Step2: Create subscription, provide the email address in Endpoint dialog box

![image](https://user-images.githubusercontent.com/119385929/210336578-d4f4228e-1f22-4cf0-a81c-47c6a3905ef4.png)

Select the subscription and click on request confirmation, a email will be sent. Copy the confirmation url and save it in SNS.

![image](https://user-images.githubusercontent.com/119385929/210337369-9e33b4b6-a942-44f7-8484-39faf98f7718.png)

Step3: Go to cloudwatch dashboard and then create alarm for EC2 Low CPU utilization where it automatically triggers a mail and also stop/terminate 
the instances when the usuage is very low  

      Select Metric ----> EC2 ------> Pre-Instance Metric ------> CPU Utilization

![image](https://user-images.githubusercontent.com/119385929/210338052-5be7e2b0-4a32-4528-aff5-24bcb4fe7af9.png)

Select the instance id and time period

![image](https://user-images.githubusercontent.com/119385929/210338293-b9b9cf88-f3c1-4119-8fce-85d3370c3c39.png)

Specify the conditions

![image](https://user-images.githubusercontent.com/119385929/210338377-b9df75d1-557c-4403-85bf-a7650b7b555c.png)

Select the subsciption in notification dialog box

![image](https://user-images.githubusercontent.com/119385929/210338748-f195cc9b-c350-468f-8f33-ee171d38716e.png)

What should EC2 instances do when the alarm is triggered.

![image](https://user-images.githubusercontent.com/119385929/210338873-a296a1c9-f76b-43dd-acb2-686f82d0eda1.png)

![image](https://user-images.githubusercontent.com/119385929/210339161-63c8e7cd-8ee5-4f3a-9c85-d79d9f10eaef.png)
![image](https://user-images.githubusercontent.com/119385929/210339195-285653c3-7277-47ae-a5bb-a94f59065a51.png)

Running instance with Low CPU utilization has been stopped 
![image](https://user-images.githubusercontent.com/119385929/210339334-8422c8bb-f1de-4f2a-a308-2ac24f2c85ff.png)



