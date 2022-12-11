<#
MIT License

Copyright (c) 2022 Ramy Ezzat - Ericsson Eesti AS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
#>

#docker pulls latest server image ramyezzateric/server_socket
write-host "downloading server_socket:latest"
docker pull ramyezzateric/server_socket:latest

#docker pulls latest client image ramyezzateric/client_socket
write-host "`ndownloading client_socket:latest"
docker pull ramyezzateric/client_socket:latest

#docker a network "server_client_net" to bridge the two containers to be created
write-host "`ncreating network bridge server_client_net"
docker network create --driver bridge server_client_net

#docker inspect the network
write-host "`ninspecting network bridge server_client_net before connections"
docker network inspect server_client_net

#docker creates a container from image ramyezzateric/server_socket, name it "server" on the network
#bridge "server_client_net" (in this sense no need define IP as it can vary in different machines)
write-host "`nrunning container server_socket"
docker run -dit --name server --network server_client_net ramyezzateric/server_socket:latest bash

#docker creates a container from image ramyezzateric/client_socet, name it "client" on the network
#bridge "server_client_net" (in this sense no need define IP as it can vary in different machines)
write-host "`nrunning container client_socket"
docker run -dit --name client --network server_client_net ramyezzateric/client_socket:latest bash

#docker inspect the network
write-host "`ninspecting network bridge server_client_net after connections"
docker network inspect server_client_net

Write-Host "`nPress any key to exit shell..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
