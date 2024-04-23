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

def analyze_logs(log_file):
    keywords_count = defaultdict(int)
    latest_log = ""
    with open(log_file, 'r') as file:
        for line in file:
            
            for keyword in ["ERROR", "WARNING"]:
                if keyword in line:
                    keywords_count[keyword] += 1
            
            latest_log = line.strip()
    return keywords_count, latest_log


def display_summary_report(keywords_count, last_execution_time, total_counts, latest_log):
    print("\n=== Latest Log ===")
    print(latest_log)
    print("\n=== Summary Report ===")
    print(f"Last Execution Time: {last_execution_time}")
    for keyword, count in keywords_count.items():
        total_counts[keyword] += count  
        print(f"{keyword}: {total_counts[keyword]} (new: {count})")


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
        logger.log(log_level, log_message)
        keywords_count, latest_log = analyze_logs('my_logfile.log')
        
        display_summary_report(keywords_count, last_execution_time, total_counts, latest_log)
        last_execution_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        time.sleep(1)

except FileNotFoundError:
    print("Log file not found.")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(5)
