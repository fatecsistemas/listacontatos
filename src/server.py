from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
serve = HTTPServer (("", 8096), CGIHTTPRequestHandler)
serve.serve_forever()