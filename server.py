from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 6767

class GraveyardEngine(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def routeUrlGET(self, route):
        routes = {"index": self.index, "add": self.add}
        if route == "":
            route = "index"

        try:
            routes[route]()
        except:
            self.send_response(message="test",code=400)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("{'Invalid Route 404'}","utf-8"))

    def do_GET(self):
        route = self.path.split('/')[1]
        self.routeUrlGET(route)

    def index(self):
        self.send_response(message="test",code=200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{msg:'index'}","utf-8"))

    def add(self):
        pass

server = HTTPServer((HOST,PORT),GraveyardEngine)
print(f"Server running on port {PORT}")
server.serve_forever()
server.server_close()