cmake_minimum_required(VERSION 2.8.3)
project(cob_moveit_interface)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

install(PROGRAMS scripts/load_scene_example.py scripts/move_group_example.py scripts/reactive_planning_example.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts
)

