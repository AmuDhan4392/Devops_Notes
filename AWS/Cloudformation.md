#### Cloudformation

  For AWS cloud development, the built-in choice for infrastructure as code is cloudformation
  
#### What is Infrastructure as Code (IaC)?

  IaC is the process for provisioning, configurating and managing cloud resources by writing a template file that is both human readable and machine consumable
  which is used to automate all the tasks end to end
  
  ![image](https://user-images.githubusercontent.com/119385929/205580649-7d3cc292-19e1-43a2-944e-6985e73d7bd6.png)

#### 3 Main Task Category:
  
   1. Infrastructure Provisioning (like creating new server's, loadbalancers, network confiuration etc..)
   2. Configuration of Provisioned Infrastructure (like installing the apps/db, managing those apps)
   3. Deployment of application (deploying app in already provisioned infrastructure)

  In the above steps, we can merge points 2 & 3 my writing a dockerfile. We can take the application and all the configuration & package it 
  together in a needed environment - so will have it as a image itself
  
#### IaC Tools:
  Tools which carry out the above mentioned tasks. Ansible, Chef, Puppet, Terraform, Cloudformation(Specific to AWS) tools available in market. 
  
 








