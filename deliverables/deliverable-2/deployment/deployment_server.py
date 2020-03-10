from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import parse_qs

from io import BytesIO
import os


'''
Please set the following conrtants before using this deployment server
'''
repo_name = "team-project-9-princess-margaret-cancer-centre"
repo_url = "git@github.com:csc301-winter-2020/team-project-9-princess-margaret-cancer-centre.git"
release_branch = "master"
deployment_script = "./deploy.sh"
deployment_password="YourDeployPassword1234"
port_to_listen=8081


def log(msg):
    print(msg)

def deploy():
    ret = -1
    if not os.path.exists(repo_name):
        ret = os.system("git clone " + repo_url)
        log("GitCloneReturn:" + str(ret))
    else:
        ret = 0
    if int(ret) == 0:
        ret = os.system("git -C \"" + repo_name +"\" pull origin " + release_branch)
        log("PullBranch:" + str(ret))
    if int(ret) == 0:
        ret = os.system(deployment_script)
        log("Deployment:" + str(ret))



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b'Deployment Password:<form action="." method="POST"><input type="password" name="pwd" value=""><input type="submit" value="Submit"></form> ')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        fields = parse_qs(body)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        if str(fields[b"pwd"][0], "utf-8") == deployment_password:
            deploy()
            response.write(b'Deployment Dispatched')
        else:
            response.write(b'Invalid Deployment. ')
            response.write(b'Received: ')
            response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('', port_to_listen), SimpleHTTPRequestHandler)
httpd.serve_forever()

