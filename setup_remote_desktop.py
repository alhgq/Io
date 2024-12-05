import os

def configure_remote_desktop():
    print("Configuring Google Remote Desktop...")
    auth_code = input("Please enter the SSH code from Google: ")
    print("Setting up remote desktop with default PIN: 123456")
    setup_command = f"chrome-remote-desktop --start --pin=123456 --auth-token={auth_code}"
    os.system(setup_command)

if __name__ == "__main__":
    configure_remote_desktop()
