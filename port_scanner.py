import socket, concurrent.futures
from utils import logger

def full_port_scan(server, max_threads=100, timeout=0.8):
    def port_scanner(port, server=server, timeout=timeout):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout) 
                is_open = sock.connect_ex((server, port)) == 0
                return port, is_open
        except KeyboardInterrupt:
            return port, False
        except socket.gaierror as e:
            logger.exception(e)
            return port, False
        except socket.error:
            logger.exception(e)
            return port, False
    try:
        ports = range(1, 1025)
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            open_ports = [port for port, is_open in executor.map(port_scanner, ports) if is_open]
        if len(open_ports) > 0:
            return open_ports
        else:
            return []
    except Exception as e:
        logger.exception(e)
        return []