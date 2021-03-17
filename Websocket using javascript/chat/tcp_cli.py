import socket, sys

if len(sys.argv) != 3:
	print "Benutzung python %s <ip> <port>"%sys.argv[0]
	sys.exit(1)
try:
	port = int(sys.argv[2])
except:
	print "%s ist keine gueltige Portnummer"%sys.argv[2]
	sys.exit(1)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], port))
	s.send('Hello, world')
	data = s.recv(1024)
	print "empfangen: %s"%data
	s.close()
except:
	print "Verbindung abgelehnt"
	sys.exit(1)

