import socket 
import threading 
 
HOST = "192.168.2.102"  # Standard loopback interface address (localhost) 
PORT = 4449        # Port to listen on (non-privileged ports are > 1023) 
 
def handle_client(conn, addr): 
  """Handles a client connection by receiving and responding to data.""" 
  print(f"Connected by {addr}") 
  while True: 
    try: 
      data = conn.recv(4096) 
      if not data: 
        break 
      print(f"Received from {addr}: {data.decode()}") 
      # Process data here (e.g., modify and send back) 
      response = input("Enter a response: ") 
      print("response",response)
      conn.sendall(response.encode()) 
    except ConnectionError: 
      print(f"Client {addr} disconnected") 
      break 
  conn.close() 
 
def main(): 
  """Sets up the server socket and listens for incoming connections.""" 
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((HOST, PORT)) 
    s.listen() 
    print(f"Server listening on {HOST}:{PORT}") 
    while True: 
      conn, addr = s.accept() 
      client_thread = threading.Thread(target=handle_client, args=(conn, addr)) 
      client_thread.start() 
 

 
main()