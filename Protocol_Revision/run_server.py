import sys
from SERVER import Server

if __name__ == "__main__":
  # Check if the user provided all of the 
  # arguments. The script name counts
  # as one of the elements, so we need at 
  # least three, not fewer.
  if len(sys.argv) < 2:
    print ("Usage: ")
    print (" python server.py <host> <port>")
    print (" e.g. python server.py localhost 8888")
    print
    sys.exit()
  host = sys.argv[1]
  port = int(sys.argv[2])
  sock = Server(host, port)
  sock.start_server()
  print("Running server on host [{0}] and port [{1}]".format(host, port))
  RUNNING = True
  COUNTER = 0
  while RUNNING:
    try:
      message, conn = sock.get_message()
      if sock.checksum(message):
        print("MESSAGE: [{0}]".format(message))
        result, msg = sock.handle_message(message)
      else:
        result, msg = ("ERROR","Data failed to transfer.")
        print ("Result: {0}\nMessage: {1}\n".format(result, msg))
      if sock.ALA_service(COUNTER):
        result = "ERROR"
        msg = "Too many attemps.\nNubmer Attempted: {0}\nPlease try again in one hour.\nThank you,\nServer.".format(COUNTER + 1)
        RUNNING = False
      elif result == "ERROR":
        CSmsg = "{0}: {1}".format(result, msg)
        new_msg = sock.md5(CSmsg)
        conn.sendall(bytes("{2} {0}: {1}\0".format(result,msg,new_msg)))
        COUNTER += 1
      else:
        CSmsg = "{0}: {1}".format(result, msg)
        new_msg = sock.md5(CSmsg)
        conn.sendall(bytes("{2} {0}: {1}\0".format(result,msg,new_msg)))
        COUNTER = 0
    else:
      print("'else' reached.")
      RUNNING = False
    conn.close()
  sock.stop_server(sock)
