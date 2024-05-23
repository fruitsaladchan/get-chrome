import os
import requests
import subprocess

def download_file(url, dest):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check if the request was successful
    with open(dest, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    print(f"Downloaded {dest}")

def install_file(file_path):
    try:
        subprocess.run([file_path, '/silent', '/install'], check=True)
        print(f"Installed {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {file_path}: {e}")

def main():
    # URLs for the Google Chrome and Adobe Reader installers
    chrome_url = "https://dl.google.com/chrome/install/latest/chrome_installer.exe"
    adobe_url = "https://ardownload2.adobe.com/pub/adobe/reader/win/AcrobatDC/2200320043/AcroRdrDC2200320043_en_US.exe"

    # Destination paths for the installers
    chrome_installer_path = "chrome_installer.exe"
    adobe_installer_path = "adobe_reader_installer.exe"

    # Download the installers
    download_file(chrome_url, chrome_installer_path)
    download_file(adobe_url, adobe_installer_path)

    # Install the downloaded files
    install_file(chrome_installer_path)
    install_file(adobe_installer_path)

    # Cleanup downloaded installer files
    os.remove(chrome_installer_path)
    os.remove(adobe_installer_path)

if __name__ == "__main__":
    main()
