### Codedeploy

Creating Codedeploy application using aws cli commands (by IAM user)

  ![image](https://user-images.githubusercontent.com/119385929/211189306-f7ee7b09-3715-4704-a3a0-5f48233cd5a7.png)
  
  ![image](https://user-images.githubusercontent.com/119385929/211188763-fb5cc247-afa0-4878-9985-96dbb6864df7.png)

Create a S3 bucket and push all the developers code into bucket for deployment purpose

![image](https://user-images.githubusercontent.com/119385929/211189402-393d3f7f-6196-4edf-9644-5c311bf1ec49.png)

![image](https://user-images.githubusercontent.com/119385929/211189440-c56dfde3-930c-45ee-87ef-be324bc9115b.png)

Creating Codedeployment group

  ![image](https://user-images.githubusercontent.com/119385929/211188842-5f46646d-1014-4b42-9639-15f8aa2ab2bd.png)

Attaching the role created for S3 and codedeploy

  ![image](https://user-images.githubusercontent.com/119385929/211188896-e726bdd6-6bd2-4996-8363-cd6add9bc069.png)

Selecting in which environment the deployment to be conducted. Since we already created production instances with tagging will be mentioned that in this

  ![image](https://user-images.githubusercontent.com/119385929/211188951-2fce8a39-6231-495d-b8a8-8d219649ef14.png)

Already we have configured the codedeploy agent in production machine, if not enable this option

  ![image](https://user-images.githubusercontent.com/119385929/211189064-882bd118-c98a-453d-8b07-78efedc20885.png)

Create codedeploy group

  ![image](https://user-images.githubusercontent.com/119385929/211188799-d65cd4b2-f95c-4fc3-b518-346086cf86b2.png)

