/*
Copyright (C) 2022 Ramy Ezzat - Ericsson Eesti AS

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


@file Program.cs
@brief initiate and run a client communication for client that request connection to server,
once connected this client will echo messages from the server console, and if the he connection
is closed from the server side this client will close as well

@author ramy ezzat
@contact ramy.ezzat@ericsson.com
@date 11/12/2022

*/

// including used namespces
using System;
using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Text;

namespace TcpEchoClient{
	public class TcpEchoServer{
		public static void Main(){
			// defining used variables
			const int port = 1024;
			const string SERVER_IP = "server";
			byte[] bytes_to_read;
			int bytes_read;
			string read_string = "";
			try{
				TcpClient client = new TcpClient(SERVER_IP, port); // client connections for TCP network services
				while(true){
					NetworkStream nwStream = client.GetStream(); // Returns the NetworkStream used to send and receive data
					//---read server text---
					bytes_to_read = new byte[client.ReceiveBufferSize]; // assign new byte to read with available buffer length
					bytes_read = nwStream.Read(bytes_to_read, 0, client.ReceiveBufferSize); // Reads data from the NetworkStream and stores it to a byte array.
					read_string = Encoding.ASCII.GetString(bytes_to_read, 0, bytes_read); // decode ASCII message
					if (read_string == ""){
						Console.WriteLine("connection terminated\n");
						break;
					}
					Console.Write(read_string);
					if (read_string == "bye"){
						Console.WriteLine("bye");
						Console.WriteLine("connection closed\n");
						break;
					}
				}
				client.Close();
			}
			catch (SocketException){ // handle socket exception
				Console.WriteLine("Server socket connection refused");
			} 
		}
	}
}
