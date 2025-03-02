source /opt/ros/humble/setup.bash
echo "ROS2 is Turn On."
vncserver
vncserver :1 -rfbport 6000
export DISPLAY=:1