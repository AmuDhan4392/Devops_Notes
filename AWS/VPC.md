#### What is a public & private cloud?

  A public cloud is shared cloud infrastructure. Multiple customers of the cloud vendor access that same infrastructure, although their data is not shared Public.
  Cloud service providers include AWS, Google Cloud Platform, and Microsoft Azure, among others.

  A private cloud, however, is single-tenant. A private cloud is a cloud service that is exclusively offered to one organization. 

#### What is VPC?

  A virtual private cloud (VPC) is a secure, isolated private cloud hosted/contained within a public cloud. 
  VPC customers can run code, store data, host websites, and do anything else they could do in an ordinary private cloud,
  but the private cloud is hosted remotely by a public cloud provider.
  It is logically isolated from other virtual networks in the AWS Cloud. 
  We can specify an IP address range for the VPC, add subnets, add gateways, create permanet IP and associate security groups. 

#### Why VPC is used?

  VPC enables us to build a virtual network in AWS cloud - no VPNs, hardware, or physical datacenters required. We can define our own network space, 
  and control how our network and EC2 resources inside our network are exposed to the Internet.

#### VPC Architecture:

  ![image](https://user-images.githubusercontent.com/119385929/206411870-68dd691f-df6c-4b5f-bdeb-bf96dcc79634.png)


#### IP addressing

  IP addresses enable resources in our VPC to communicate with each other, and with resources over the internet. 
  "Classless Inter-Domain Routing (CIDR)" notation is a way of representing an IP address and its network mask. 
  The format of these addresses is as follows:

  An individual IPv4 address is 32 bits, with 4 groups of up to 3 decimal digits. For example, 10.0.1.0, 72.152.152.100, 192.155.133.78 etc...

  An IPv4 CIDR block has four groups of up to three decimal digits, 0-255, followed by a slash and a number from 0 to 32. 
  For example, 10.0.0.0/16.
  https://dnsmadeeasy.com/support/subnet (refer for subnet mask)
  
  While creating a VPC, we assign it to a IPv4 CIDR block (a range of private IPv4 addresses)

#### Subnet

  A subnet is a range of IP addresses in your VPC.
  We can connect a subnet to the internet and route traffic to and from subnets using route tables.

#### Route table

  A route table contains a set of rules, called routes, that are used to determine where network traffic from our VPC is directed. 
  Each route in a route table specifies the subnet where we want the traffic to go (the destination) and the gateway, network interface, or connection through which to send the traffic (the target).

#### Internet Gateway

  An internet gateway is a component that allows communication between our VPC and the internet. It supports IPv4 and IPv6 traffic. 

  An internet gateway enables resources such as EC2 instances to connect to the internet if the resource has a public IPv4 address or an IPv6 address. 
  Similarly, resources on the internet can initiate a connection to our resources through subnet using the public IPv4 address or IPv6 address. 
  For example, an internet gateway enables us to connect to an EC2 instance in AWS using our local computer (putty). In simple terms, Internet Gateway allows instances with public IPs to access the internet.

#### NAT Gateway (Network Address Translation)

  A NAT gateway used to connect between one or more public and private servers. Assume if a Web server (public) hosted through AWS services wants to collect 
  data from the DB sever which is hosted in private server (which has no internet service) requires NAT gateway enabled.
  
  When we receive traffic from internet, an IPV4 address gets replaced with the NAT’s device address. 
  Once the response is obtained, it has to be sent to the instance, and in this case, the NAT device translates the address back to the IPV4 
  and it is given to the IPV4 address.
  
#### Elastic IP

  An Elastic IP address is a static(permanent), public IPv4 address designed for our cloud computing. We can associate an Elastic IP address with any instance or 
  network interface through our VPC account.

#### Security Group

  A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. 
  For example, a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.

  When we create a VPC, it comes with a default security group. we can also create additional security groups for each VPC.
  
  For each security group, add rules that control the traffic based on protocols and port numbers. 
  There are separate sets of rules for inbound and outbound traffic.


