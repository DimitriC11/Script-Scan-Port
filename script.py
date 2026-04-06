#!/usr/bin/env python3
import socket
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
from datetime import datetime

def scan_port(target, port, timeout=0.8):
    """Scan un port et retourne (port, statut)"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target, port))
            return port, result == 0
    except:
        return port, False

def port_scanner(target, start_port=1, end_port=1024, threads=150):
    print(f"\n{'='*60}")
    print(f"Scan de {target} | Ports {start_port}-{end_port}")
    print(f"Début : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    open_ports = []
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
                service = socket.getservbyport(port) if port < 1025 else "unknown"
                print(f"[+] Port {port:<5} OUVERT → {service}")

    print(f"\nScan terminé ! Ports ouverts trouvés : {len(open_ports)}")
    if open_ports:
        print("Ports ouverts :", sorted(open_ports))
    else:
        print("Aucun port ouvert trouvé dans la plage spécifiée.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Entrez l'adresse IP ou le nom d'hôte à scanner : ").strip()

    # Vous pouvez modifier ces valeurs selon vos besoins
    port_scanner(target, start_port=1, end_port=2000, threads=200)