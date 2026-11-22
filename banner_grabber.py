import socket, ssl, re
from utils import logger, PATTERNS

def banner_grabber(ip, port, probe, use_ssl=False, timeout=5):
    def recv_all(sock, stop=b'\r\n\r\n', max_bytes=65536):
        """Reads from socket until: connections stops, \'stop\' appears,
        connection times out or \'max bytes\' limit is exceeded. Returns all received bytes."""
        data = bytearray()
        while len(data) < max_bytes:
            try:
                chunk = sock.recv(4096)
            except (socket.timeout, TimeoutError):
                break               
            if not chunk:           
                break
            data += chunk
            if stop in data:        
                break
        return bytes(data)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if use_ssl == True:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE # Not proctected - NEVER use ssl.CERT_NONE if you're not using this tool on Metasploitable or trusted sources
                with context.wrap_socket(sock, server_hostname=ip) as ssock:
                    ssock.settimeout(timeout)
                    ssock.connect((ip, port))
                    ssock.send(probe)
                    raw = recv_all(ssock)
                    text = raw.decode(encoding='latin-1', errors='ignore')
            else:
                sock.settimeout(timeout)
                sock.connect((ip, port))
                if probe is not None:
                    sock.send(probe)
                    raw = recv_all(sock)
                    text = raw.decode(encoding='latin-1', errors='ignore')
                else:
                    raw = recv_all(sock, stop=b'\n')
                    text = raw.decode(encoding='latin-1', errors='ignore')
        if text is None or len(text) < 1:
            return None
        else:
            return text
    except (socket.timeout, TimeoutError) as e:
        logger.info(f'{ip}:{port} - {e}')
    except ConnectionRefusedError as e:
        logger.info(f'{ip}:{port} - {e}')
    except OSError as e:
        logger.exception(e)
    except TypeError as e:
        logger.exception(e)

def detect_service(text: str, patterns=PATTERNS):
    if not text:
        return None

    for name, pattern in patterns.items():
        service = re.search(pattern, text, flags=re.I)
        if service is not None:
            return name
    return None

def parse_headers(text):
    headers = {}
    if not text:
        return headers
    for line in text.splitlines():
        m = re.match(r'^([\w-]+):\s*(.+)$', line)
        if m:
            headers[m.group(1).lower()] = m.group(2).strip()
    return headers

def resolve_service(banner, port, patterns=PATTERNS):
    service = detect_service(banner, patterns)
    if service:
        return service, 'banner'
    try:
        return socket.getservbyport(port, 'tcp'), 'port'
    except OSError:
        return 'unknown', 'none'
    