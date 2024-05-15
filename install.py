import os

utils = ['figlet', 'gnome-tweaks', 'tmux', 'git', 'vim-gtk', 'curl', 'pandoc', 'weasyprint', 'ssh', 'neofetch',
         'python3-venv', 'python3', 'python3-pip', 'youtube-dl', 'build-essential', 'cmake', 'gnome-sushi']
media = ['obs-studio', 'ffmpeg', 'vlc', 'v4l-utils', 'youtube-dl', 'gimp']
vidioEditing = ['kdenlive', 'blender']
snaps = ['code']
photo = ['darktable', 'openshot']
other = ['inkscape', 'scribus']
themes = ['materia-gtk-theme', 'numix-gtk-theme', 'numix-icon-theme',
          'numix-icon-theme-circle', 'papirus-icon-theme', 'faenza-icon-theme']
programming = ['dotnet-sdk-8.0','code']

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


def install_gaming():
    # Install wine staging
    os.system('sudo dpkg --add-architecture i386')
    os.system(
        'wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -')
    os.system(
        "sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'")
    os.system('sudo apt update')
    os.system('sudo apt install --install-recommends winehq-staging -y')

    # install game mode
    os.system('sudo apt install gamemode -y')
    # install steam
    os.system('sudo apt install steam -y')
    # install lutris
    os.system('sudo add-apt-repository ppa:lutris-team/lutris')
    os.system('sudo apt-get update')
    os.system('sudo apt install lutris -y')


if __name__ == "__main__":
    update()
    install_programs(utils)
    install_programs(media)
    # install_programs(vidioEditing)
    # install_programs(photo)
    # install_programs(other)
    install_programs(themes)
    # install_snaps(snaps)
    # install_gaming()
    install_programs(programming)
