# Log-Analysis-and-Monitoring-script
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log Monitoring Script</title>
</head>
<body>

<h1>Log Monitoring Script</h1>

<p>This Python script continuously monitors a specified log file for new entries, performs basic log analysis, and provides summary reports. Below is an explanation of the flow of the code:</p>

<h2>1. Configuration and Setup</h2>

<p>The script begins by importing necessary modules: logging, time, random, signal, sys, and collections.defaultdict.</p>
<ul>
    <li>Logging is configured to store logs in a file named "my_logfile.log" in the current directory.</li>
    <li>The log level is set to DEBUG, and the log message format includes timestamp, log level, and message.</li>
</ul>

<h2>2. Logging Setup</h2>

<ul>
    <li>A logger named logger is created using the <code>__name__</code> attribute.</li>
    <li>Log message formats are defined for different log levels: INFO, DEBUG, and ERROR.</li>
    <li>A list of log levels to cycle through is defined.</li>
</ul>

<h2>3. Log Analysis Functions</h2>

<ul>
    <li><code>analyze_logs(log_file)</code>: This function reads the log file line by line and counts the occurrences of specific keywords or patterns (e.g., "ERROR", "WARNING").</li>
    <li><code>display_summary_report(keywords_count)</code>: This function displays a summary report based on the log analysis results, showing the count of occurrences for each keyword.</li>
</ul>

<h2>4. Signal Handling</h2>

<p>A signal handler function <code>signal_handler(sig, frame)</code> is defined to handle keyboard interrupt (Ctrl+C). It prints a message and exits the script gracefully.</p>

<h2>5. Main Loop</h2>

<p>The script enters a main loop that continuously logs messages, performs log analysis, and displays summary reports.</p>
<ul>
    <li>A random log level is selected from the defined log levels (INFO, DEBUG, ERROR).</li>
    <li>A log message is generated using the selected log level and logged using the logger.</li>
    <li>Log analysis is performed by calling the <code>analyze_logs()</code> function, which counts occurrences of specific keywords in the log file.</li>
    <li>The summary report is displayed using the <code>display_summary_report()</code> function, showing the count of occurrences for each keyword.</li>
    <li>The script sleeps for a short interval (1 second) before the next iteration.</li>
</ul>

<h2>6. Exception Handling</h2>

<p>The script includes exception handling to catch FileNotFoundError and other exceptions. If the log file is not found or an error occurs, an appropriate error message is printed, and the script exits gracefully.</p>

<h2>Dependencies</h2>

<p>This script requires Python 3.x to be installed.</p>

<h2>How to Use</h2>

<ol>
    <li><strong>Clone the Repository:</strong><br>
        <code>git clone &lt;repository_url&gt;</code></li>
    <li><strong>Navigate to the Script Directory:</strong><br>
        <code>cd log_monitoring_script</code></li>
    <li><strong>Run the Script:</strong><br>
        <code>python log_monitor.py</code><br>
        This will start the script, continuously monitoring the log file and displaying summary reports.</li>
    <li><strong>Interrupt the Script:</strong><br>
        To stop the script, press <kbd>Ctrl+C</kbd>. The script will handle the interrupt signal and exit gracefully.</li>
</ol>

<h2>Testing</h2>

<p>To test the script, follow these steps:</p>

<ol>
    <li>Ensure that the script file <code>log_monitor.py</code> is in the appropriate directory.</li>
    <li>Create a sample log file named <code>my_logfile.log</code> in the same directory as the script.</li>
    <li>Add some sample log entries to the log file manually or by running another process that generates log messages.</li>
    <li>Run the script using the instructions provided in the "How to Use" section.</li>
    <li>Verify that the script correctly monitors the log file, performs analysis, and displays summary reports as expected.</li>
</ol>

<p>This script provides a basic example of log monitoring and analysis, which can be extended or modified based on specific requirements.</p>

</body>
</html>
