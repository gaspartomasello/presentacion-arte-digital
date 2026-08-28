#!/usr/bin/env python3
"""
Servidor para jugar a Casa Sim en la red del aula (no necesita internet).

Uso:
    python3 servidor-lan.py            # puerto 8080
    python3 servidor-lan.py 3000       # otro puerto

Dejalo abierto en la compu del docente y pasale a los alumnos la dirección
que imprime en pantalla. Se corta con Ctrl+C.
"""
import http.server
import os
import socket
import socketserver
import sys

PUERTO = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
CARPETA = os.path.dirname(os.path.abspath(__file__))


def direcciones_lan():
    """Devuelve las IP de esta máquina en la red local."""
    encontradas = set()
    try:                                     # la IP con la que salimos a la red
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.168.1.1", 80))
        encontradas.add(s.getsockname()[0])
        s.close()
    except OSError:
        pass
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            encontradas.add(info[4][0])
    except OSError:
        pass
    return sorted(ip for ip in encontradas if not ip.startswith("127."))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=CARPETA, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass                                  # sin ruido en la consola


class Servidor(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    ips = direcciones_lan()
    print()
    print("  🏠  CASA SIM — servidor del aula")
    print("  " + "-" * 46)
    if ips:
        print("  Los alumnos entran a:")
        for ip in ips:
            print(f"      http://{ip}:{PUERTO}/")
    else:
        print("  No pude detectar la IP de red. Fijate la IP de esta máquina")
        print(f"  y pasala como  http://LA-IP:{PUERTO}/")
    print(f"\n  En esta misma compu:  http://localhost:{PUERTO}/")
    print("\n  Cortar con Ctrl+C")
    print("  " + "-" * 46 + "\n")
    try:
        with Servidor(("0.0.0.0", PUERTO), Handler) as srv:
            srv.serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor cerrado.\n")
    except OSError as e:
        print(f"\n  No pude abrir el puerto {PUERTO}: {e}")
        print(f"  Probá con otro, por ejemplo:  python3 servidor-lan.py 8081\n")
