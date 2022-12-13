"""
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


@file server.py
@brief initiate and run a socket communication for a server that listen to client
request, once connected the server will send messages written into console to client(s)
and if the connection needed to be terminated to all connected client(s) one has to press
escape into the server console if connection(s) were not established

@author ramy ezzat
@contact ramy.ezzat@ericsson.com
@date 12/12/2022

"""

# import used libraries
import socket
import queue
import sys
import tty
import termios
import time
from threading import Event

# define hostname and port number other used variables
host = "server"
port = 1024
queue_max_size = 1024
message_queue = queue.Queue(maxsize=queue_max_size)
loop_condition = Event()
conn = None


def run_server():
    """
    @brief function that initiate and run server forever until bye word
    @param None
    @return None
    """
    try:
        loop_condition.set()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  # creates a new socket
            conn = None # defining conn
            orig_settings = termios.tcgetattr(sys.stdin) #terminal settings
            tty.setcbreak(sys.stdin) #tty terminal
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                     1)  # set the value of the given socket option
            server_socket.bind((host, port))  # bind the socket to address
            server_socket.listen(2)  # Enable a server to accept connections
            conn, addr = server_socket.accept()  # Accept a connection
            print("Connection from: " + str(addr))
            print("press escape to exit...")
            while loop_condition.is_set() or not message_queue.empty():
                x = sys.stdin.read(1)[0] #read character
                if x != chr(27): # check if input is escape
                    message_queue.put(x)
                    print(x, end="", flush=True)
                else:
                    loop_condition.clear()
                if not message_queue.empty():
                    conn.send(message_queue.get().encode("utf-8"))  # send data entered by user encoded into
                time.sleep(1 / 50)
            print("\nexiting")
        conn.close()  # mark the socket closed - double check besides with statement
    except KeyboardInterrupt as error:  # handling KeyboardInterruption error ctrl+c
        print("  Exiting  ")

    except BrokenPipeError as error:  # handling BrockenPipeError if client terminate
        print(error)
        print("seems that client exited")

    finally:
        if conn:
            conn.close()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) # restore terminal settings


if __name__ == "__main__":
    run_server()
