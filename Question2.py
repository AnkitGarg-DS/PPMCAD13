# Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. 
# Write a Python program to monitor the health of the CPU. Few pointers to be noted:
# ●       The program should continuously monitor the CPU usage of the local machine.
# ●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
# ●       The program should run indefinitely until interrupted.
# ●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

# Hint:
# ●       The psutil library in Python can be used to retrieve system information, including CPU usage. 
#         You can install it using pip install psutil.
# ●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

# Expected Output:
# Monitoring CPU usage...
# Alert! CPU usage exceeds threshold: 85%
# Alert! CPU usage exceeds threshold: 90%
# ... (continues until interrupted)

import psutil
import time

def monitor_cpu(threshold: float = 10.0):
    print("Monitoring CPU usage...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)  # Sleep for a second before checking again
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()
