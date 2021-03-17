import socket,sys,time

if len(sys.argv) != 2:
	print "Benutzung: python %s <port>"%sys.argv[0]
	sys.exit(1)
try:
	port = int(sys.argv[1])
except:
	print "%s ist keine gueltige Portnummer"%sys.argv[1]
	sys.exit(1)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("", port))
	s.listen(1)
	while 1:
		conn, addr = s.accept()
		print "Verbindung von Host: %s, port %d"%(addr[0], addr[1])
		data = conn.recv(1024)
#		if not data: break
		print "empfangen: %s"%data
		time.sleep(10)
		conn.send("+++ " + data + " +++")
		conn.close()
	s.close()
except:
	print "Server error"
	sys.exit(1)

