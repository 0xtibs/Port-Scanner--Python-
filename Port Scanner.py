import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Liver")
print(ascii_banner)

#defining our target
if len(sys.argv) == 2:
    #translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of argument")

#show progress and commands
print("+" * 100)
Print("Authorized only for educational purposes!")
print("Scan in progress for target: " + target)
print("Scan started at: " + str(datetime.now()))
print("=" * 100)
print("Press 'Q' at anytime to exit the script. Happy Hunting :)" )

try:
    #scanning target ports 1 to 65,535
    for port in range(1,40):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #returns error indicator
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Please Stop Interacting with the Script")
except socket.gaierror:
    print("\n Host name Invalid")
    sys.exit()
except socket.error:
    print("\n Server not responding")
    sys.exit()
