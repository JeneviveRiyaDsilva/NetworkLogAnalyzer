# Project 2: Network Log Analyzer with Success & Failed Visualization

import matplotlib.pyplot as plt

# Step 1: Read the log file
log_file = "sample_logs.txt"

logs = []
with open(log_file, "r") as file:
    for line in file:
        logs.append(line.strip())

# Step 2: Count failed and successful logins per IP
failed_logins = {}
success_logins = {}

for log in logs:
    ip_index = log.find("IP: ") + 4
    ip_address = log[ip_index:]
    
    if "Login: FAILED" in log:
        failed_logins[ip_address] = failed_logins.get(ip_address, 0) + 1
    elif "Login: SUCCESS" in log:
        success_logins[ip_address] = success_logins.get(ip_address, 0) + 1

# Step 3: Detect suspicious IPs (more than 2 failed attempts)
suspicious_ips = [ip for ip, count in failed_logins.items() if count > 2]

# Step 4: Print results
print("=== Failed Login Attempts ===")
for ip, count in failed_logins.items():
    print(f"{ip}: {count} failed attempts")

print("\n=== Suspicious IPs ===")
if suspicious_ips:
    for ip in suspicious_ips:
        print(ip)
else:
    print("No suspicious activity detected.")

# Step 5: Visualization
all_ips = list(set(list(failed_logins.keys()) + list(success_logins.keys())))
failed_counts = [failed_logins.get(ip, 0) for ip in all_ips]
success_counts = [success_logins.get(ip, 0) for ip in all_ips]

x = range(len(all_ips))
plt.figure(figsize=(10,6))
plt.bar(x, success_counts, color='green', label='SUCCESS')
plt.bar(x, failed_counts, color='red', bottom=success_counts, label='FAILED')

plt.xticks(x, all_ips)
plt.xlabel("IP Address")
plt.ylabel("Number of Attempts")
plt.title("Login Attempts per IP (Success vs Failed)")
plt.legend()
plt.show()
