
#### Ansible Ad-hoc coomand syntax:

ansible -i inv [inventory file] all [mention all server's in inventory or specific server's] -m [module] -a {module commands}

    Examples:
    ansible -i inv -m copy -a "src=/home/user/invv dest=/home/ansible/" all 
    ansible -i inv -m file -a "dest=/home/ansible/invv state=absent" all
    ansible -i inv -m service -a "name=firewalld state=started" all

#### Ansible Playbook: Executes the playbook task by task

Example 1:

![image](https://user-images.githubusercontent.com/119385929/209458267-93f3f2d7-57e3-4256-a200-f49d60c5335b.png)


Example 2:

![image](https://user-images.githubusercontent.com/119385929/209458276-6f630fff-864b-444f-b679-4a8804676e08.png)


After writing the playbook, first to chek the writen playbook is in correct format using syntax check and then execute it

      ansible-playbook -i inv < filename.yml > --syntax-check
      ansible-playbook -i inv < filename.yml >

##### Handlers: Playbook

Handlers are used whenever changes are made in the machine. It will only run when it is notified.

![image](https://user-images.githubusercontent.com/119385929/209458008-e4fbb8d2-3014-42aa-a48d-c1840a3b1856.png)

#### Variables: Playbook

There are different types system defined variable and user defined variables. Where we can store a set parameter in playbook or in external file and 
use those whenever is required while writing the playbooks.

Example 1:

![image](https://user-images.githubusercontent.com/119385929/209458025-ee916d30-ae52-4e90-9f95-8a3712b92896.png)


Example 2:

![image](https://user-images.githubusercontent.com/119385929/209458133-203a4b33-608f-4423-8abb-15ea4f1eb6f9.png)


------------------------------------------------------------

Using -vvv (verbose) to understand what is actually happening while running the playbook    

      ansible-playbook -i inv < filename.yml > -vvv

The below command is used, if the executed playbook runs for longer duration by using this command we come to know in which stage is got stuck

      ps -ef | grep ansible

#### Ansible Output:

RED: Failure

YELLOW: Success with changes

GREEN: Success with no changes

![ansible 1](https://user-images.githubusercontent.com/119385929/209457910-436e8451-c03e-4cb3-b201-06185a3d348c.png)



