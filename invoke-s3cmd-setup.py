import subprocess

def call_s3cmd(command):
    try:
        # Run the s3cmd command
        result = subprocess.run(['s3cmd'] + command.split(), check=True, capture_output=True, text=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr)

if __name__ == "__main__":
    # Example command to list buckets
    s3_command = "s3cmd --configure"
    call_s3cmd(s3_command)