# Docker_Notes

Docker is a platform / program - running, building, managing and deploying containers for application purpose.

What is Container?

An isolated environment for running an application which has its own library and dependencies

## Docker & Docker_Images Architecture

Docker images are build using "Layer Architecture"

## Docker_Command-line_Commands

This material contains commands for CentOS users. Below commands are for root users, if a non-root user wants to setup the docker repository use 'sudo' before.

Check whether docker already installed in your server using any one the commands:
      
      yum list docker
      rpm -qa | grep docker
      
 Uninstall the earlier versions of Docker/Docker-engine along with associated dependencies using the following commands:

      yum remove docker \
      docker-common\
      docker-selinux \
      docker-engine

Though YUM reports that the packages are not installed, the contents available in "/var/lib/docker/" are saved, including images, containers, volumes and networks.
 
## Setup Docker Repository

Install required packages. Utils provides the yum-config-manager utility:
      
      yum install utils 

Set up the stable repository by using the following command:

      yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo 

With everything set, we can finally move on to installing Docker on CentOS by running:
     
      yum install docker

The system should begin the installation. Once it finishes, it will notify us the installation is complete and which version of Docker is now running on our system.
Using yum repository to install docker by default it will install all its dependencies as well.


After, Docker package has been installed, start the daemon, check its status and enable it system-wide (starts the service at boot time) using the below commands:

      systemctl start docker && systemctl status docker && systemctl enable docker -l

Finally, run a container test image to verify if Docker works properly, by issuing the following command:

      docker run hello-world

This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits. See the sample output


![image](https://user-images.githubusercontent.com/119385929/205113856-5b3ab7fa-9743-4710-8ad3-9b81172b1481.png)


## Basic Docker Commands:

Checks the version of the docker
  
      # docker --version
      
For system-wide information on Docker

      # docker info
      
To get a list of all available Docker commands type docker on the console

      # docker
      
      # docker inspect
To list all the available Docker images on our server issue the following command

      # docker images
      
      # docker ps
      
      # docker ps -a
      
















