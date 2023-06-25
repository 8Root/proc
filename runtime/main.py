import os
import argparse
from datetime import datetime

def strip_vstart_prefix(input_string):
    # Remove the 'vstart://' prefix from the input string
    prefix = "vstart://"
    suffix = "/"

    if input_string.startswith(prefix):
        input_string = input_string[len(prefix):]

    if input_string.endswith(suffix):
        input_string = input_string[:-len(suffix)]

    return input_string

def main():
    # Check if the config argument is provided
    if args.config:
        # Define the config file path
        parsed_cfgname = strip_vstart_prefix(args.config)
        pre_config_file = parsed_cfgname + ".cfg"
        config_file = f"C:\\Proc\\runtime\\cfgs\\{pre_config_file}"
        logs_directory = os.path.join("C:\\Proc\\runtime\\logs\\")

        # Print the current working directory and config file path
        print(os.getcwd())
        print(config_file)

        if os.path.isfile(config_file):
            # Change the current working directory to 'cfgs'
            os.chdir(os.path.join("C:\\Proc\\runtime\\", "cfgs"))

            # Create 'logs' directory if it doesn't exist
            os.makedirs(logs_directory, exist_ok=True)

            # Read and execute each line in the config file as a command
            with open(config_file, mode='r') as cfgfile:
                for line in cfgfile:
                    command = line.strip()
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    log_file = os.path.join(logs_directory, f"{timestamp}.txt")  # Use timestamp as the log file name
                    output = os.popen(command).read().strip()  # Execute the command and capture the output
                    log_content = f"{command}: {output}"

                    with open(log_file, mode='w') as logfile:
                        logfile.write(log_content)

                    print(f"Command '{command}' executed. Log saved in '{log_file}'")

        else:
            print(f"Configuration file '{pre_config_file}' at '{config_file}' not found.")
    else:
        print("Please specify a configuration file using the '-c' or '--config' argument.")



# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Specify the configuration file")
args = parser.parse_args()

main()
