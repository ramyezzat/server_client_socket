## 1 - server_client_socket
Socket server client containers

## 2 - System definition 
The system contains two docker containers. A server that is running a python socket program, and a client 
that is running a .NET based client program. The server can have up to two connection of clients.

## 3 - Minimum requirements
- Bash or cmd/PowerShell
- Docker/Moby

## 4 - Brief steps
    a- on windows
        1- run windows_os/install.ps1
        2- run windows_os/run_server.ps1
        3- run windows_os/run_client.ps1 (another Powershell terminal)
        4- on server run $python3 /home/server.py
        5- on client run $cd /home/client_socket_cs/App/
        6- on client run $dotnet run
    b- on linux (chomd u+x <file_name>.sh to make file executable)
        1- run linux_os/install.sh
        2- run linux_os/run_server.sh
        3- run linux_os/run_client.sh (another bash terminal)
        4- on server run $python3 /home/server.py
        5- on client run $cd /home/client_socket_cs/App/
        6- on client run $dotnet run

## 5 - Installation
upon running the installation app "install.ps1" or "install.sh" the following steps takes place
        ** please note that installation takes around one-three minutes to complete
  - docker pulls latest server image ramyezzateric/server_socket
    - https://hub.docker.com/repository/docker/ramyezzateric/server_socket
  - docker pulls latest client image ramyezzateric/client_socket
    - https://hub.docker.com/repository/docker/ramyezzateric/client_socket
  - docker a network "server_client_net" to bridge the two containers to be created
  - docker creates a container from image ramyezzateric/server_socket, name it "server" on the network bridge "server_client_net" (in this sense no need define IP as it can vary in different machines)
  - docker creates a container from image ramyezzateric/client_socket, name it "client" on the network bridge "server_client_net" (in this sense no need define IP as it can vary in different machines)
## 6 - Run process
After installation run the server and client in either way described in 6.1 or 6.2
### 6.1 using run scripts
runt using pre-written script for PowerShell and bash
#### 6.1.1 - Windows
- go to windows_os
- right click run_server.ps1 and select Run with PowerShell 
  - on server container, run the following command
    - $python3 /home/server.py
- right click run_client.ps1 and select Run with PowerShell
  - on client container, run the following commands
    - $cd /home/client_socket_cs/App/
    - $dotnet run
#### 6.1.2 - Linux
- open a terminal in repository directory
- run $chmod u+x /linux_os/run_server.sh
- run $chmod u+x /linux_os/run_client.sh
- open two terminals and run $./linux_os/run_server.sh and $./linux_os/run_client.sh respectively
  - on server container, run the following command
    - $python3 /home/server.py
  - on client container, run the following commands
    - $cd /home/client_socket_cs/App/
    - $dotnet run
### 6.2 - using commands
run two entities of bash or cmd or Powershell and run:
  - run in terminal $docker start server and $docker start client and then open another terminal 
  - on server side, start server container
    - $docker exec -it server bash or $docker attach server
    - inside server container, run the following command 
      - $python3 /home/server.py
  - on client side, start client container
    - $docker exec -it client bash or $docker attach client
    - inside client container, run the following commands
      - $cd /home/client_socket_cs/App/
      - $dotnet run
## 7 - Result
- Write a message onto the server side, press enter and watch the client side echoes the message
- To exit the programs press escape key into the server and both programs will exit