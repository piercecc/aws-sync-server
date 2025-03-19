import os

def grant_sudo_access():
    # Prompt for the username
    username = input("Enter the username to grant sudo access: ")

    # Check if the user exists
    try:
        # This will raise an error if the user does not exist
        os.system(f"id -u {username}")
    except Exception as e:
        print(f"User {username} does not exist.")
        return

    # Add the user to the sudo group
    try:
        os.system(f"usermod -aG sudo {username}")
        print(f"User {username} has been granted sudo access.")
    except Exception as e:
        print(f"Failed to grant sudo access to {username}. Error: {e}")

if __name__ == "__main__":
    grant_sudo_access()