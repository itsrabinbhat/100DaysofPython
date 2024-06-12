import socket
import time

import prompt_toolkit.formatted_text
import pyfiglet

# Creating a banner
banner = pyfiglet.figlet_format('PORT SCANNER')
print(banner)


# defining a scanner function
def scanner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ip, port))
        print(f"[!] Port {port} is open.")
    except:
        None


def main():
    start_time = time.time()
    ip_addr = input(f"[~] Enter ip address: ")
    port = input(f"[~] Enter port range separated by dash(-): ")
    port_range = port.split('-')

    # scanning each port
    for port in range(int(port_range[0]), int(port_range[1])):
        print(f'[~] Scanning port {port}')
        scanner(ip_addr, port)

    end_time = time.time()
    print(f"Scanned {port_range[1]} ports in {end_time - start_time} seconds.")


if __name__ == '__main__':
    main()
