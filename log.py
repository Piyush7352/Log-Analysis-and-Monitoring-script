import logging
import time
import random
import signal
import sys
from collections import defaultdict

logging.basicConfig(filename='my_logfile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

# Function to generate random HTTP status codes
def generate_http_status():
    return random.choice([200, 404, 500, 503])

def analyze_logs(log_file):
    status_code_counts = defaultdict(int)
    latest_log = ""
    with open(log_file, 'r') as file:
        for line in file:
            if "HTTP Status:" in line:
                status_code = int(line.split("HTTP Status: ")[1].strip())
                status_code_counts[status_code] += 1
            latest_log = line.strip()
    return status_code_counts, latest_log

def display_summary_report(status_code_counts, last_execution_time, total_counts, latest_log):
    print("\n=== Latest Log ===")
    print(latest_log)
    print("\n=== Summary Report ===")
    print(f"Last Execution Time: {last_execution_time}")
    for status_code, count in status_code_counts.items():
        total_counts[status_code] += count  
        print(f"HTTP Status {status_code}: {total_counts[status_code]} (new: {count})")

def signal_handler(sig, frame):
    print("\nLogging interrupted. Exiting.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    last_execution_time = None
    total_counts = defaultdict(int)  
    while True:
        log_level = random.choice(log_levels)
        log_message = formats[log_level]
        http_status = generate_http_status() # Generate random HTTP status code
        logger.log(log_level, f"{log_message} - HTTP Status: {http_status}") # Log HTTP status along with the message
        status_code_counts, latest_log = analyze_logs('my_logfile.log')
        display_summary_report(status_code_counts, last_execution_time, total_counts, latest_log)
        last_execution_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        time.sleep(1)
except FileNotFoundError:
    print("Log file not found.")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(5)
