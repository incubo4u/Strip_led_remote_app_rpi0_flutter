import fcntl
import simplejson
from http.server import BaseHTTPRequestHandler, HTTPServer
import os, sys ,time

host_name = 'xxx.xxx.xxx.xxx'  #Raspberry Pi IP address
host_port = 8000


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length).decode("utf-8") 
        test_data = dict(simplejson.loads(post_data))
        #print(test_data)

        if test_data['lightState'] == 'on':
            os.system('sudo pkill -f led_off.py')
            os.system('sudo python3 /Path/to/led_on.py &')  #Path to led_on.py file
        if test_data['lightState'] == 'off':
            os.system('sudo pkill -f led_on.py')
            os.system('sudo python3 /Path/to/led_off.py &')  #Path to led_off.py file
        if test_data['lightState'] == '0':
            os.system('sudo shutdown -h now')


if __name__ == '__main__':

    f = open('lock', 'w')
    try:
        fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except:
        sys.stderr.write('[%s] Script already running.\n' % time.strftime('%c'))
        sys.exit(-1)

    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
