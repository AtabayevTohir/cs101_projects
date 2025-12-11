def analyze_logs(log_entries):
    result = {}
    for details in log_entries:
        ip_address,status_code = details.split(' - ')
        status_code = status_code.strip()
        if status_code == "404" or status_code == "500" :
            if not ip_address in result:
                result[ip_address]=0
            result[ip_address] +=1
    return result   

def flag_suspicious_ips(error_dict):
    for ip_address, error_count in error_dict.items():
        if error_count >= 3:
            print(f"SECURITY ALERT: {ip_address} has {error_count} errors.")

log_entries = [
    "192.168.1.1 - 200",
    "10.0.0.5 - 404",
    "192.168.1.1 - 200",
    "10.0.0.5 - 500",
    "172.16.0.1 - 404",
    "10.0.0.5 - 404",
    "192.168.1.1 - 500",
    "10.0.0.5 - 404"
]

errors = analyze_logs(log_entries)

print("Error Counts:")
for ip_address, error_count in errors.items():
    print(ip_address + ": " + str(error_count))

print("--------------------")

flag_suspicious_ips(errors)