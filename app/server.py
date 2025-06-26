import http.server, socketserver, threading, time, os

PORT = 5000
Handler = http.server.SimpleHTTPRequestHandler

def run_server():
    original_cwd = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except Exception as e:
        print(f"Error en el servidor: {e}")
    finally:
        os.chdir(original_cwd)

server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Servidor detenido manualmente")