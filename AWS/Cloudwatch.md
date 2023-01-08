### CloudWatch:

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

