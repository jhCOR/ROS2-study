ros2 service call /turtle1/teleport_absolute turtlesim/TeleportAbsolute "{x: 10.0, y: 5.0, theta: 0.5}"
ros2 service call /spawn turtlesim/Spawn "{x: 50.0, y: 5.0, theta: -0.5, name: 'turtle2'}"
ros2 service call /reset std_srvs/srv/Empty "{}"

