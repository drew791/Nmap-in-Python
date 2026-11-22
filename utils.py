import logging

logger = logging.getLogger('Pyware')
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def lprint(level, message):
    """Funzione per stampare nel terminale e nel file di log contemporaneamente"""
    print(message, flush=True)

    log_method = getattr(logger, level, None)
    if not callable(log_method):
        raise ValueError(f"Unknown log level: {level}")

    log_method(message)

PATTERNS = {
    'ssh': r'^SSH-',
    'ftp': r'^220[- ].*FTP',
    'smtp': r'^220[- ].*SMTP',
    'http': r'^HTTP/\d',
    'pop3': r'^\+OK',
    'imap': r'^\* OK',
    'mysql': r'^.\x00\x00\x00\x0a\d+\.\d+\.\d+',  
    'redis': r'^(-ERR|\+PONG|\$\d+|-\w+)',        
    'rdp': r'^\x03\x00\x00\x13\x0e\xd0',          
    'telnet': r'^\xff[\xfb-\xfe]',                
    'vnc': r'^RFB \d{3}\.\d{3}',                  
    'irc': r'NOTICE\s+(AUTH|\*)',
}

HTTP_PORTS = [80, 8080, 8180, 8000, 8008, 8888, 3000, 5000]
HTTPS_PORTS = [443, 8443]