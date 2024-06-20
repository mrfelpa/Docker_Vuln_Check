# Configuration
- The script checks a predefined set of ports commonly used by the Docker API, listed in the docker_ports variable.
- The script uses the logging module to log information, warnings, and errors in a file called ***docker_api_check.log.*** The default log level is INFO.

# Use
- Clone the repository.
- Edit the ***company variable*** in the script for the domain you want to verify.
  
- Run the script:
  
            python docker_api_check.py
  
- The scan result will be logged in the ***docker_api_check.log file.***.
- The script will tell you whether the host is vulnerable or not.

# Remarks

- The script checks only a predefined set of Docker API ports, it is possible that the API is accessible on other ports not contemplated.
- The script does not attempt to connect directly to the Docker API, verification is done only by opening ports.

# Contributing

- Feel free to submit pull requests with improvements and fixes to the script.
