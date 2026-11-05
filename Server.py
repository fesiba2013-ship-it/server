  import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class FakeGhostbustersServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Responder de forma simple a peticiones web genéricas
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Servidor de Ghostbusters Activo en la Nube")

    def do_POST(self):
        # Aquí es donde la carpeta gateway enviará los archivos .proto
        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream")
        self.end_headers()
        
        # Por ahora, devolvemos una respuesta vacía para pruebas iniciales
        self.wfile.write(b"")
        print(f"Petición recibida en: {self.path}")

def run():
    # Render y los servicios en la nube asignan un puerto dinámico usando variables de entorno
    port = int(os.environ.get("PORT", 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, FakeGhostbustersServer)
    print(f"Arrancando servidor falso en el puerto {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
