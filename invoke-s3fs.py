import subprocess

def call_s3fs(command):
    try:
        # Run the s3fs command
        result = subprocess.run(['s3fs'] + command.split(), check=True, capture_output=True, text=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr)

if __name__ == "__main__":
    # Prompt for ACCESS_KEY and SECRET_KEY
    s3_access_key = input("Paste your ACCESS_KEY to the desired S3 Bucket :")
    s3_secret_key = input("Paste your SECRET_KEY to the desired S3 Bucket :")
    # Add ACCESS_KEY and SECRET_KEY to secrets file
    try: 
    # Command to 
    s3_command = "s3fs"
    s3_secrets_command = "echo" & s3_access_key & ":" & s3_secret_key & "> ~/.passwd-s3fs"
    call_
    call_s3fs(s3_command)