# DarkRobot - Robo Quadrupede controlado por ROS

03-12-2022 - instalando o ROS Noetic no raspberry pi3

- wget -c https://raw.githubusercontent.com/qboticslabs/ros_install_noetic/master/ros_install_noetic.sh && chmod +x ./ros_install_noetic.sh && ./ros_install_noetic.sh
- escolher a opção 3, instalando apenas o ROS base no raspberry pi, no pc de auxilio instalar a opção 1
- sudo apt update && sudo apt install build-essential

# Alterando o tamanho do swap para 2gb para melhorar a perfomance
- sudo apt install dphys-swapfile 
- sudo dphys-swapfile swapoff
- sudo nano /etc/dphys-swapfile
- alterar o campo CONF_SWAPFACTOR=2 e descomentar
- sudo dphys-swapfile setup
- sudo dphys-swapfile swapon
