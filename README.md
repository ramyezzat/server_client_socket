## 1 - server_client_socket
Socket server client containers

## 2 - System definition 
The system contains two docker containers. 
A server that is running a python socket program, and a client that is running a .NET based client program.
The server can have up to two connection of clients.  

## 3 - Minimum requirements
- Bash or cmd/PowerShell
- Docker/Moby

## 4 - steps
    a- on windows
        1- run install.ps1
        2- run run_server.ps1
        3- run run_client.ps1 (another Powershell terminal)
    b- on linux
        1- run install.sh
        2- run run_server.sh
        3- run run_client.sh (another bash terminal)

## 5 - Installation
- upon running the installation app "install.ps1" the following steps takes place
    please note that installation takes around one minute to complete
  - docker pulls latest server image ramyezzateric/server_socket
  - docker pulls latest client image ramyezzateric/client_socket
  - docker a network "server_client_net" to bridge the two containers to be created
  - docker creates a container from image ramyezzateric/server_socet, name it "server" on the network bridge "server_client_net" (in this sense no need define IP as it can vary in different machines)
  - docker creates a container from image ramyezzateric/client_socet, name it "client" on the network bridge "server_client_net" (in this sense no need define IP as it can vary in different machines)
## 6 - Run process
After installation run the server and client in either way
  ### 6.1 - run both run_server.ps1 and run_client.ps1
  - on server container, run the following command 
    - $python3 /home/server.py
  - on client container, run the following commands
    - $cd /home/client_socket_cs/App/
    - $dotnet run
  ### 6.2 - run two entities of bash or cmd or Powershell and run:
  - on server side, start server container
    - $docker start server
    - $docker exec -it server bash 
    - inside server container, run the following command 
      - $python3 /home/server.py
  - on client side, start client container
    - $docker start client
    - $docker exec -it client bash
    - inside client container, run the following commands
      - $cd /home/client_socket_cs/App/
      - $dotnet run
- Write a message into server side and watch the client side echo
- To exit the programs write "bye" into the server and both programs will exit