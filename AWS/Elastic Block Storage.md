### Elastic Block Storage:

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
