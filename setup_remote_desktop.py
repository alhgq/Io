
import os

def install_xfce4_and_dependencies():
    print("Installing XFCE4 and required packages...")
    os.system("sudo apt update && sudo apt install -y xfce4 xfce4-goodies")

def install_google_remote_desktop():
    print("Installing Google Remote Desktop...")
    os.system("wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb")
    os.system("sudo dpkg -i chrome-remote-desktop_current_amd64.deb || sudo apt -f install -y")

def configure_remote_desktop():
    print("Configuring Google Remote Desktop...")
    auth_url_command = "chrome-remote-desktop --setup --user"
    os.system(auth_url_command)

    auth_code = input("Please enter the SSH code from Google: ")
    print("Setting up remote desktop with default PIN: 123456")
    setup_command = f"chrome-remote-desktop --start --pin=123456 --auth-token={auth_code}"
    os.system(setup_command)

if __name__ == "__main__":
    install_xfce4_and_dependencies()
    install_google_remote_desktop()
    configure_remote_desktop()
