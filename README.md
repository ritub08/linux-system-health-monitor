# Linux System Health Monitor

A Bash-based Linux system monitoring tool designed to collect system health information and generate timestamped reports.

## Project Overview

This project automates basic Linux system health monitoring using Bash scripting and native Linux utilities. It demonstrates practical skills in system administration, infrastructure monitoring, and security operations.

## Features

- CPU and system load monitoring
- RAM and memory utilization monitoring
- Disk space utilization monitoring
- Running process inspection
- Network connectivity checks
- Timestamped system health reports

## Technologies Used

- Bash Shell Scripting
- Linux (Ubuntu)
- VMware Workstation
- Git and GitHub

## Linux Commands Used

| Command | Purpose |
|---------|---------|
| uptime | Check system uptime and load |
| free | Monitor memory utilization |
| df | Monitor disk space |
| ps | Inspect running processes |
| ping | Check network connectivity |

## Project Structure

```text
linux-system-health-monitor/
├── system_monitor.sh
└── README.md
```

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/ritub08/linux-system-health-monitor.git
```

Navigate to the project directory:

```bash
cd linux-system-health-monitor
```

Grant execution permission:

```bash
chmod +x system_monitor.sh
```

Run the script:

```bash
./system_monitor.sh
```

## Cybersecurity Relevance

System health monitoring is an important component of security operations. Monitoring resource utilization, running processes, and network connectivity helps establish system baselines and supports the identification of unusual system behavior.

## Learning Outcomes

- Linux system administration
- Bash scripting and automation
- System resource monitoring
- Process and network inspection
- Automated report generation
- GitHub project documentation

## Future Enhancements

- Configurable resource utilization thresholds
- Automated alerts
- Scheduled monitoring using cron
- CSV and JSON report generation
- Integration with centralized monitoring tools

## Author

Developed by [ritub08](https://github.com/ritub08)

Cybersecurity | Linux | Security Operations | Automation
