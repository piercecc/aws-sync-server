import subprocess


username = input("Enter the username to be created: ")


# Invoke the adduser command using subprocess


subprocess.run(["sudo", "adduser", username])