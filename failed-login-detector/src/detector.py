import re
from pathlib import Path
from collections import Counter

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Input log file
LOG_FILE = BASE_DIR / "logs" / "sample_auth.log"

# Output report
REPORT_FILE = BASE_DIR / "reports" / "security_report.txt"

# Detection threshold 
THRESHOLD = 5


def analyze_logs():

    failed_attempts = Counter()
    usernames = {}

    print("\n====================================")
    print("       FAILED LOGIN DETECTOR")
    print("====================================")

    if not LOG_FILE.exists():
        print("Error: Authentication log file not found.")
        return

    with open(LOG_FILE, "r") as file:

        for line in file:

            if "Failed password" in line:

                match = re.search(
                    r"Failed password for (?:invalid user )?(\S+) from ([\d.]+)",
                    line
                )

                if match:
                    username = match.group(1)
                    ip_address = match.group(2)

                    failed_attempts[ip_address] += 1

                    usernames.setdefault(ip_address, set()).add(username)

    print("\n[+] LOG ANALYSIS COMPLETED")

    print("\nFailed Login Summary:")

    for ip, count in failed_attempts.items():

        print(f"IP Address: {ip} | Failed Attempts: {count}")

    alerts = []

    print("\n====================================")
    print("           SECURITY ALERTS")
    print("====================================")

    for ip, count in failed_attempts.items():

        if count >= THRESHOLD:

            alert = (
                f"ALERT: Suspicious login activity detected!\n"
                f"Source IP: {ip}\n"
                f"Failed Attempts: {count}\n"
                f"Target Usernames: {', '.join(sorted(usernames[ip]))}\n"
                f"Severity: HIGH\n"
            )

            alerts.append(alert)
            print(alert)

    if not alerts:
        print("No suspicious login activity detected.")

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(REPORT_FILE, "w") as report:

        report.write("FAILED LOGIN DETECTION REPORT\n")
        report.write("================================\n\n")

        for ip, count in failed_attempts.items():
            report.write(
                f"IP: {ip} | Failed Attempts: {count}\n"
            )

        report.write("\nSECURITY ALERTS\n")
        report.write("================\n\n")

        if alerts:
            report.writelines(alerts)
        else:
            report.write("No suspicious activity detected.\n")

    print("\n[+] Report saved successfully!")
    print(f"[+] Report location: {REPORT_FILE}")


if __name__ == "__main__":
    analyze_logs()

