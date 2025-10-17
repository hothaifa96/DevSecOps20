## Part 1: Bridge Network
 
* Create a custom bridge network named "my-network"
* Run two nginx containers on this custom bridge network, naming them web1 and web2
    - what is the ip for web1 
    - what is the ip for wev2 
    - **can we have them in one command ?**

* Test connectivity between the containers by pinging web2 from web1

* Try to curl the nginx service running on web2 from web1 on port 80

* Try to access the nginx service from your host machine using localhost (it should fail without port mapping)

* Remove one container and recreate it with port mapping, then try accessing from your host again

# WEB Application


* we have a website to run on docker with 3 parts :
    - frontend 
    - backend
    - data base
* draw the docker network isolation best practices diagram