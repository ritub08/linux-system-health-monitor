
# Failed Login Attempt Detector

## Project Overview

The Failed Login Attempt Detector is a Python-based cybersecurity project designed to analyze Linux authentication logs and identify repeated failed SSH login attempts.

The project demonstrates basic security log analysis, authentication monitoring, event filtering, and brute-force detection concepts.

## Objectives

- Analyze Linux authentication logs.
- Identify failed SSH login attempts.
- Extract usernames and source IP addresses.
- Count failed login attempts.
- Identify IP addresses exceeding a predefined threshold.
- Generate security alerts and reports.

## Technologies Used

- Python 3
- Ubuntu Linux
- Regular Expressions
- Linux Authentication Logs
- Git and GitHub

## Project Structure

```text
failed-login-attempt-detector/
│
├── logs/
│   ├── sample_auth.log
│   └── .gitignore excludes real_auth.log
│
├── src/
│   └── detector.py
│
├── reports/
│   └── .gitkeep
│
├── .gitignore
└── README.md
```

## Detection Logic

1. Read authentication log entries.
2. Identify failed password events.
3. Extract usernames and source IP addresses.
4. Count failed attempts for each IP.
5. Compare the count against a predefined threshold.
6. Generate an alert when the threshold is reached.

## Detection Threshold

The current detection threshold is 5 failed login attempts from the same IP address.

## Sample Detection Result

| Source IP | Failed Attempts | Result |
|---|---:|---|
| 192.168.1.105 | 5 | High Alert |
| 10.0.0.25 | 2 | No Alert |
| 172.16.0.50 | 2 | No Alert |

## How to Run

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate into the project:

```bash
cd failed-login-attempt-detector
```

Run the detector:

```bash
python3 src/detector.py
```

## Learning Outcomes

- Linux authentication log analysis
- SSH authentication monitoring
- Python log parsing
- Regular expression usage
- Brute-force detection fundamentals
- Security alert generation

## Future Improvements

- Real-time authentication log monitoring
- Time-window-based brute-force detection
- Improved detection of invalid usernames
- Timestamp-based event analysis
- Enhanced security reporting

## Disclaimer

This project is developed for educational purposes in a controlled local lab environment.

Only synthetic sample logs are included in this repository. Real system authentication logs are excluded to protect sensitive information.
