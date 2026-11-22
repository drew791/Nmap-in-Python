from port_scanner import full_port_scan
from banner_grabber import *
from utils import *
import json, time, socket

TIMEOUT_GRABBER = 3
TIMEOUT_SCANNER = 0.8
MAX_THREADS = 100

def main(target):
    dict_ports = {}
    request_str = f'''GET / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\nAccept: */*\r\n\r\n'''
    HTTP_REQUEST = request_str.encode()

    lprint('info', f'Starting scan on target {target}.')

    ports = full_port_scan(server=target, max_threads=MAX_THREADS, timeout=TIMEOUT_SCANNER)
    
    for port in ports:
        headers = {}
        probe = 'passive'
        if port not in HTTP_PORTS + HTTPS_PORTS: 
            # passive ports: grabs the banner and related info without using a probe
            banner = banner_grabber(ip=target, port=port, probe=None, timeout=TIMEOUT_GRABBER)
            service, source = resolve_service(banner, port)

        else:
            if port in HTTP_PORTS:
                # ports which require a probe (an http message the port responds to with the banner)
                banner = banner_grabber(ip=target, port=port, probe=HTTP_REQUEST, timeout=TIMEOUT_GRABBER, use_ssl=False)
                headers = parse_headers(banner)
                service, source = resolve_service(banner, port)
                probe = 'http'

            else:
                # ports which require both a probe and ssl certificates (do NOT use ssl.CERT_NONE unless you're in a safe space to use this tool)
                banner = banner_grabber(ip=target, port=port, probe=HTTP_REQUEST, timeout=TIMEOUT_GRABBER, use_ssl=True)
                service, source = resolve_service(banner, port)
                probe = 'https'

        dict_ports[f'Port {port}'] = {
            'port': port, 
            'service': service,
            'service source': source,
            'banner headers': headers,
            'full banner': banner,
            'probe': probe,
            }
    with open('scan_result.json', 'w', encoding='utf-8') as f:
        json.dump(dict_ports, f, ensure_ascii=False, indent=4)
    lprint('info', 'Successfully dumped results into json file.')
    print(f'{len(ports)} ports found. All results have been collected in \"scan_result.json\"')
    return dict_ports



if __name__ == '__main__':
    lprint('info', 'Process initialized on \"main.py\".')
    try:
        TARGET = input('Enter host to scan: ')
        t1 = time.time()
        main(TARGET)
        t2 = time.time()
        lprint('info', f'Scan on {TARGET} successful! Process took {t2 - t1} seconds.\n')
    except KeyboardInterrupt: # to stop the script without causing an error
        lprint('info', 'CTRL + C pressed - process exited successfully.')
    except Exception as e:
        logger.exception(e)
        lprint('info', 'Process exited because an exception was encountered.\n')

# grazie claude