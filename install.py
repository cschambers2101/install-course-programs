import os
from pathlib import Path
import shutil
from datetime import datetime
import requests
import zipfile
import subprocess

i3 = ['i3', 'sddm', 'xfce4-terminal', 'thunar']
utils = ['btop', 'figlet', 'tmux', 'git', 'vim', 'curl', 'pandoc', 'weasyprint', 'ssh',
         'python3-venv', 'python3', 'python3-pip', 'build-essential', 'cmake', 'picom', 'nitrogen', 'feh', 'lxappearance', 'terminator']
media = ['obs-studio', 'ffmpeg', 'vlc', 'v4l-utils', 'gimp']
vidioEditing = ['kdenlive', 'blender']
snaps = ['code']
photo = ['darktable', 'openshot']
other = ['inkscape', 'scribus']
themes = ['materia-gtk-theme', 'numix-gtk-theme', 'numix-icon-theme',
          'numix-icon-theme-circle', 'papirus-icon-theme', 'faenza-icon-theme']
programming = ['python3-venv', 'python3', 'python3-pip', 'build-essential', 'cmake']

def update():
    os.system('sudo apt update')
    os.system('sudo apt upgrade -y')
    os.system('sudo apt autoremove -y')
    os.system('sudo apt install --fix-missing -y')


def install_programs(programs):
    for prog in programs:
        os.system(f'sudo apt install {prog} -y')


def install_snaps(snaps):
    for snap in snaps:
        os.system(f'sudo snap install --classic {snap}')

def createDirectory(path):
    """
    Creates a directory if it doesn't already exist.
    """
    dir_path = Path(path).expanduser()
    if not dir_path.is_dir():
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")
    else:
        print(f"Directory already exists: {dir_path}")


def copyConfigFile(file, copy_to, file_name_to_copy_to):
    """
    Copies a configuration file to a target directory, creating a backup if the file already exists.
    """
    target_path = Path(copy_to).expanduser() / file_name_to_copy_to
    source_path = Path(file).expanduser()

    # Ensure the target directory exists
    target_path.parent.mkdir(parents=True, exist_ok=True)

    if target_path.is_file():
        # Create a timestamped backup
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_path = target_path.with_suffix(f".old.{timestamp}")
        shutil.copy2(target_path, backup_path)
        print(f"Backup created: {backup_path}")

    # Copy the file
    shutil.copy2(source_path, target_path)
    print(f"Copied {source_path} to {target_path}")


def setupConfigFiles():
    """
    Sets up configuration files by creating required directories and copying default configs.
    """
    # Create required folders
    createDirectory("~/src")
    createDirectory("~/.config/i3")
    createDirectory("~/.config/picom")
    createDirectory("~/.config/tmux")

    # Copy sample picom config
    copyConfigFile('/usr/share/doc/picom/examples/picom.sample.conf', '~/.config/picom', 'picom.conf')
    # Copy modified picom config
    copyConfigFile('./picom.conf', '~/.config/picom', 'picom.conf')

    # Copy i3 config
    copyConfigFile('./i3config', '~/.config/i3', 'config')

    # Copy i3 status config
    copyConfigFile('./i3status.conf', '~/.config/i3', 'i3status.conf')


def downloadFile(url, save_to):
    """
    Downloads a file from the given URL and saves it to the specified location.

    Args:
        url (str): The URL of the file to download.
        save_to (str): The local path where the file should be saved.
    """
    save_path = Path(save_to).expanduser()
    save_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP issues

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded successfully: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")


def downloadFontandInstall(font_url):
    """
    Downloads the Nerd Font, extracts it to the fonts directory, and updates the font cache.
    """
    # Define the URL and target paths
    # font_url = "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/UbuntuMono.zip"
    download_path = "~/Downloads/UbuntuMono.zip"
    fonts_dir = "~/.local/share/fonts"

    # Step 1: Download the font zip file
    print("Downloading Font...")
    downloadFile(font_url, download_path)
    print(f"Downloaded Font to: {download_path}")

    # Step 2: Extract the zip file to the fonts directory
    download_path = Path(download_path).expanduser()
    fonts_dir = Path(fonts_dir).expanduser()
    fonts_dir.mkdir(parents=True, exist_ok=True)  # Ensure the fonts directory exists

    try:
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(fonts_dir)
        print(f"Extracted fonts to: {fonts_dir}")
    except zipfile.BadZipFile:
        print("Failed to extract the zip file. The file may be corrupted.")
        return

    # Step 3: Update the font cache
    try:
        subprocess.run(['fc-cache', '-f', '-v'], check=True)
        print("Font cache updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update font cache: {e}")

if __name__ == "__main__":
    update()
    install_programs(utils)
    install_programs(i3)
    install_programs(programming)
    install_programs(themes)
    setupConfigFiles()
    downloadFontandInstall("https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/UbuntuMono.zip")
    downloadFontandInstall("https://use.fontawesome.com/releases/v6.7.2/fontawesome-free-6.7.2-desktop.zip?_gl=1*9i1osb*_ga*MTgwMzQzNDg0Ny4xNzQ0MDI1NzMy*_ga_BPMS41FJD2*MTc0NDAyODIwOC4yLjEuMTc0NDAyODIxMi41Ni4wLjA.")
    # install_programs(media)
    # install_programs(other)
    # install_programs(vidioEditing)
    # install_programs(photo)
    # install_programs(other)
    # install_snaps(snaps)
    # install_gaming()
