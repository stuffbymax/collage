import requests
import socket

def comprehensive_connectivity_check():
    results = {}

    # 1. HTTP Request Test
    try:
         # You can replace with any website
        url = "http://www.google.com" 
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            results["HTTP Test"] = "Internet connection is working (HTTP request succeeded)."
        else:
            results["HTTP Test"] = "Failed to reach the site (HTTP request did not return 200 status)."
    except requests.ConnectionError:
        results["HTTP Test"] = "No internet connection (HTTP request failed)."
    
    # 2. DNS Lookup Test
    hostname = "www.google.com"
    try:
        host_ip = socket.gethostbyname(hostname)
        results["DNS Test"] = f"DNS lookup succeeded. IP address of {hostname} is {host_ip}."
    except socket.gaierror:
        results["DNS Test"] = "DNS lookup failed."

    # Print all results
    for test, result in results.items():
        print(f"{test}: {result}")

    return results

# Example usage
comprehensive_connectivity_check()
