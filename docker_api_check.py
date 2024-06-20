import requests
import socket
import re
import logging
import nmap

docker_ports = [2375, 2376, 2377, 4343, 4244]

logging.basicConfig(filename='docker_api_check.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def is_port_open(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set a timeout to avoid hanging
        sock.connect((host, port))
        sock.close()
        return True
    except socket.timeout:
        logging.warning(f"Timeout connecting to {host}:{port}")
        return False
    except socket.error as e:
        logging.debug(f"Error connecting to {host}:{port}: {e}")
        return False

# Define the function to check if the Docker API is exposed
def is_docker_api_exposed(host):
    try:
        # Use nmap to scan the host for open ports
        nm = nmap.PortScanner()
        nm.scan(host, ','.join(map(str, docker_ports)))

        for port in docker_ports:
            if nm[host].has_tcp(port) and nm[host]['tcp'][port]['state'] == 'open':
                return True
        return False
    except nmap.nmap.PortScannerError as e:
        logging.error(f"Error scanning {host}: {e}")
        return False

def is_vulnerable(host):
    try:
        # Check if the host is reachable
        if not is_host_reachable(host):
            logging.warning(f"{host} is not reachable")
            return False

        if is_docker_api_exposed(host):
            return True
        return False
    except Exception as e:
        logging.error(f"Error checking vulnerability for {host}: {e}")
        return False

def is_host_reachable(host):
    try:
        # Ping the host to check if it's reachable
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

company = "example.com"

if is_vulnerable(company):
    logging.info(f"{company} is vulnerable to the attack that exploits exposed Docker APIs.")
else:
    logging.info(f"{company} is not vulnerable to the attack that exploits exposed Docker APIs.")
