#/bin/bash!

clear

echo 'Installing useful software for your course ... '
echo
echo
echo -n 'Installing Figlet ... '
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq figlet < /dev/null > /dev/null
echo 'Complete!'
echo
echo -n 'Installing Open Broadcaster Software (OBS) ... '
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq ffmpeg obs-studio < /dev/null > /dev/null
echo 'Complete!'
echo
echo -n 'Installing Chromium ... '
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq chromium-browser < /dev/null > /dev/null
echo 'Complete!'
echo
echo -n 'Installing Video 4 Linux Utilities (to control webcams) ... '
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq v4l-utils < /dev/null > /dev/null
echo 'Complete!'
echo
echo -n 'Installing Openshot Video Editor ... '
sudo DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:openshot.developers/ppa > /dev/null 2>&1
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq openshot-qt < /dev/null > /dev/null
echo 'Complete!'
echo
echo -n 'Installing GNU Image Manipulation Software (GIMP) ... '
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq gimp < /dev/null > /dev/null
echo 'Complete!'
echo
echo -n 'Installing Inkscape ... '
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq inkscape < /dev/null > /dev/null
echo 'Complete!'
echo
echo -n 'Installing Youtube downloader ... '
sudo DEBIAN_FRONTEND=noninteractive apt-get install -qq youtube-dl < /dev/null > /dev/null
echo 'Complete!'
echo
clear
PURPLE="\e[35m"
printf "${PURPLE}"
figlet -f standard 'All Applications are now installed'
