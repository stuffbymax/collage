import socket

def dns_check(hostname="www.google.com"):
    try:
        host_ip = socket.gethostbyname(hostname)
        print(f"DNS lookup succeeded. IP address of {hostname} is {host_ip}.")
        return True
    except socket.gaierror:
        print("DNS lookup failed.")
        return False

# Example usage
dns_check()
