import re

def validate_ip(ip):
    # pola ipv4
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    # pola ipv6
    ipv6_pattern = r'^[\da-fA-F]{1,4}(:[\da-fA-F]{1,4}){7}$'

    # cek apakah ip sesuai dengan pola ipv4
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        # cek apakah setiap bagian ip dalam range 0-255
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"

    # cek apakah ip sesuai dengan pola ipv6
    if re.match(ipv6_pattern, ip):
        return "IPv6"
    
    # jika tidak sesuai dengan pola ipv4 atau ipv6 maka return "Bukan IP Address"
    return "Bukan IP Address"

N = int(input())
results = [validate_ip(input().strip()) for _ in range(N)]

print("\n".join(results))
