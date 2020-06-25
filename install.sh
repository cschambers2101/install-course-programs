#/bin/bash!

clear

# function install_utils {
#     echo -n 'Installing Figlet ... '
#     sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq figlet < /dev/null > /dev/null
#     echo 'Complete!'
#     echo
#     
#     echo -n 'Installing Gnome Tweaks ... '
#     sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq gnome-tweaks < /dev/null > /dev/null
#     echo 'Complete!'
#     echo
# 
#     echo -n 'Installing ssh, tmux, git and vim ... '
#     sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq ssh tmux git vim < /dev/null > /dev/null
#     echo 'Complete!'
#     echo
# }

function install_media_programs {
    
    echo -n 'Installing blender ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq blender < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing ffmpeg ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq ffmpeg < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing vlc ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq vlc < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing kdenlive ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq kdenlive < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing obs-studio ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq obs-studio < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing Video 4 Linux Utilities (to control webcams) ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq v4l-utils < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing Youtube downloader ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq youtube-dl < /dev/null > /dev/null
    echo 'Complete!'
    echo
}

function install_software_development {
    
    echo -n 'Installing vscode ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq code < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing development essentials ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq vim tmux git pandoc weasyprint < /dev/null > /dev/null
    echo 'Complete!'
    echo

#     echo -n 'Installing nodejs 12.x ... '
#     sudo DEBIAN_FRONTEND=noninteractive curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh < /dev/null > /dev/null
#     sudo DEBIAN_FRONTEND=noninteractive sudo bash nodesource_setup.sh < /dev/null > /dev/null
#     echo -n 'Installed '
#     node --version
#     echo -n 'Installed: '
#     npm --version
#     echo 'Complete!'
#     echo
}

function install_photography_software {

    echo -n 'Installing Gimp (Photoshop replacement) ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq gimp < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing Darktable (Lightroom replacement) ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq darktable < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing Openshot (iPhoto replacement) ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq openshot < /dev/null > /dev/null
    echo 'Complete!'
    echo
}

function install_other_useful_software {

    echo -n 'Installing Inkscape ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq inkscape < /dev/null > /dev/null
    echo 'Complete!'
    echo

    echo -n 'Installing Scribus ... '
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq scribus < /dev/null > /dev/null
    echo 'Complete!'
    echo
}

function install_all_software {
    install_media_programs
    install_software_development
    install_photography_software
    install_other_useful_software
}

function menu {
    while true
    do
        echo 'Install programs'
        echo
        echo 'Select which software you want to install:'
        echo
        echo
        OPTIONS="media development photography useful all quit"
        select opt in $OPTIONS; do
            if [ "$opt" = "quit" ]; then
                all_done
                echo 'Quitting software installation'
                exit
            elif [ "$opt" = "media" ]; then
                echo 'Digital Media Software'
                install_media_programs
            elif [ "$opt" = "development" ]; then
                echo 'Software Design and Development Software'
                install_software_development 
            elif [ "$opt" = "photography" ]; then
                echo 'Photography Software'
                install_photography_software
            elif [ "$opt" = "useful" ]; then
                echo 'Other useful software'
                install_other_useful_software
            elif [ "$opt" = "all" ]; then
                echo 'All software'
                install_all_software
            else
                echo 'error: use a number corresponding to the word'
            fi
        done
    done
}

function all_done {
    echo
    clear
    PURPLE="\e[35m"
    printf "${PURPLE}"
    figlet -f standard 'All Applications are now installed'
}

menu

