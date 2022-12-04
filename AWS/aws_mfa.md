
### AWS - Amazon Web Service

#### Why we go to cloud?

  1. Cloud is a serveless concept
  2. Depending on the load we can either increase or decrease our servers
  3. These server's can be used temporarily depending on the requirement of our projects, so that cost is reduced
  4. Time saving and not required manpower for implementation
  5. Cloud is running on rental basis, so server's are available for rental without any ownership


#### Categories of Cloud Computing:

  1. SaaS - Software as a Service
  2. Paas - Platform as a Service
  3. IaaS - Infrastructure as a Service

#### Types of CLoud:

  1. Private Cloud
  2. Public Cloud
  3. Hybrid Cloud (Combination of 1 & 2)

AWS comes under public cloud and it uses Infrastructure as a Service (IaaS)

#### AWS Regions and Availability Zones:

  Here countries are assigned as regions, ex: India, Japan, Singapore, Australia etc..
  Datacenters are known as availability zones that are present/available in that particular region.
  
Always select nearby location/regions (or) as per client requirement where they are going to host their app/db/web server's.

#### Login using Multi-Factor Authentication (MFA):

Logging into AWS can be done in different ways either using paswword or through MFA.

  How to setup MFA?
  
  #### 1.Search for IAM - Identity Access Management
  
  ![image](https://user-images.githubusercontent.com/119385929/205498999-21a6eac4-cd44-4f07-9572-34a68ee8eab9.png)

  
  #### 2. In IAM Dashboard - Add MFA
  
  ![image](https://user-images.githubusercontent.com/119385929/205499342-2fdbd92e-fe43-41af-b074-b479f88135a5.png)

  
  #### 3. Click on Activate MFA
    
  ![image](https://user-images.githubusercontent.com/119385929/205499412-8a07177b-542b-4af7-ba91-d25658054294.png)


  #### 4. In MFA Manage device provide the name and choose virtual MFA and click continue
  

  ![image](https://user-images.githubusercontent.com/119385929/205499446-aaba08dc-243c-4f32-b74e-706ff1266a94.png)

  #### 5. Virtual MFA - Scan QR code from any authenticator app from our phone and type the two consecutive MFA codes where Assign MFA check boxes highlighted

  ![1](https://user-images.githubusercontent.com/119385929/205499702-b2b9e2bd-7500-4603-8775-606dda441d17.png)
 
  ![4](https://user-images.githubusercontent.com/119385929/205499723-2747c568-5cb2-4f68-8ea3-016c2e4306b0.png)
  
   #### 6. Finally, logout and login to our AWS account where MFA has been enabled successfully. Type the code which is chosen on the authenticator app.
  
  ![5](https://user-images.githubusercontent.com/119385929/205499724-5de38456-cec5-4525-8070-921898230dfe.png)
