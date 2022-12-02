## Basic Linux Commands

    hostname
   
 It gives us the IP or domain name of the user. To change the existing hostname use the follwing command
 
    hostnamectl set-hostname # (as per organization)

Kindly note hostname should not be modified in an working environment. It will be set by naming convention as per the organization
Usually it will be like which location, datacenter the server is mapped and the domain name.

To display kernel and its version

    uname  or  uname -r
    
Command to display present / current working directory

    pwd
    
To change from one directory to another we can either use absolute or exact path.

    cd # command used to change the directory path
   
    /home/user  # assume it is present working directory
    
    cd dockerfile   # which is a absolute path where docker folder is already available in user directory
    
    cd /var/lib/docker # which is a exact path where changing from one location to another location
    
To return to root directory from any location

    cd /
 
Going one step back from any location to another

    cd ..
    
### Creating and removing a directory

    mkdir  # Will create directory in same location

    mkdir / # Will create directory in root location

    mkdir -p # for creating a nested directory (p) stands for parent directory

    rmdir # removes directory

    rm -rf # remove recurrivesly forcefully removes nested directory as well as files

    clear  # to clear the terminal
    
To check what are the contents available in a directory (long listing)
    
    ls
    
To see hidden files in a directory
   
    ls -la
To see in reverse order with date&time, file permission types, user and group user
    
    ls -lrt 

To create and write a text, script, yml, py or any other files using text editor commands 

    touch file.txt
    touch autobot.sh
    touch fetch.yml
    touch script.py

Touch command used to create a empty file and ". " anything after dot will create that exentsion file

    vi file.txt
    vi autobot.sh
    vi fetch.yml
    vi script.py
    
#### To start editing press "i", in order to delete any existing lines in the file before editing press "dd"
#### Press ESC for saving the file ":wq"
#### ":wq!" - forcefully saves the files
#### ":q" - closes the files without saving


To write, append and viewing the content in the files

    cat  # used to see content of a particular file / what is inside

    cat > # can be used writing a content in file and also will be overridden the content inside the file if exist

    cat >>  # to append content's inside the file

    head  # used to view lines in the top of the  file
		head -n 10

    tail  # used to view bottom lines of the file
    
    
Copying, Pasting, Renaming, Moving files/directory: For all these arguments we need to give source and destination

    cp - used for copying the files

    cp -r - used for copying a directory

    mv - used for moving/renaming the files/directory

To get help about a command

    man - mannuals about each command

To know past commands used in a terminal

    history

To know the current process running on the system with process ID

    ps -aux 
    ps

To kill any kind of process

	  kill -9 PID

To install package from YUM package manager, because of using yum it will also install the dependencies by default.
    
    yum clean all # Removing all cache's enabled at YUM repositories  
  
    yum install {package_name} 
  
    yum install {package_name} -version # Install specific version of a package
  
    yum remove {package_name} /  # this will also remove the dependencies
        update {package_name} / 
        upgrade {package_name} 
        
    rpm -e  # will uninstall only the specified package but not their dependencies 

### How to check the installed package from which repo it is installed?

When a package conflict issues appears this will helps us to know from which repository/repo the package has been installed inorder to troubleshoot that package.

	yum info package-name
	
  yumdb info package-name # gives us package information from which repository installed

	yum list installed | more | wc -l(tells total no packages) # gives only the installed packages from which repository

	yum repolist  # gives the list of repositories which are enabled

	yum repolist all  # gives repositories which are enabled as well as disabled

	yum list all / available | less | more  # will list all the packages

	yumdb search from_repo repoid-name  # search where a package is available in particular repo, also shows only the packages that are installed. 

	yum-config-manager --enable repository <repository name>
  
	yum-config-manager --disable repository <repository name>


### Creating a User:

useradd, adduser -  username

Changing password's for user's - 

    passwd username {should have sudo access}

userdel, deluser - deleting a user

    chmod - used for chanding dir/file permission types
    chown - changing File/Dir Ownership

To know the file permission types:

	  r - read  4
	  w - write 2
	  x - execute 1
	  - - Nothing 

    0 - Nothing
    1 - Only execute
    2 - only write
    3 - only execute and write
    4 - only read
    5 - read and execute
    6 - read and write
    7 - read, write and execute



