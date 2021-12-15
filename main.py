# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from http.server import HTTPServer
import time
from ourServer import MyServer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hostName = "localhost"
    serverPort = 8080

    webServer = HTTPServer((hostName, serverPort), MyServer)
    time1 = time.time()
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    time2 = time.time()
    print(f'\nServer stopped. Total runtime was {time2-time1:.2f} seconds')

