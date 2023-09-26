from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld=LaunchDescription()

    ts=Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtle_sim'
    )

    drive_ts=Node(
        package='turtlesim_multi',
        executable='single_drive',
        name='tbsim_driver'
    )

    ld.add_action(ts)
    ld.add_action(drive_ts)

    return ld