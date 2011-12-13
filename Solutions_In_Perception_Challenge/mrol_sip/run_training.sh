#!/bin/bash 

# Change the 

export ROS_PACKAGE_PATH=$PWD/kinect_tools:$ROS_PACKAGE_PATH
export ROS_PACKAGE_PATH=$PWD/kinect_template:$ROS_PACKAGE_PATH
export ROS_PACKAGE_PATH=$PWD/mrol_sip:$ROS_PACKAGE_PATH

export PYTHONPATH=$PWD/mrol_sip/src:$PYTHONPATH
#export PYTHONPATH=~/repo/team_franklin/mrol_sip/src/rosutils_mrol:$PYTHONPATH
#export PYTHONPATH=~/repo/perception_repo/teamFranklin:$PYTHONPATH
export PYTHONPATH=$PWD/mrol_sip:$PYTHONPATH
export PYTHONPATH=$PWD/kinect_tools:$PYTHONPATH


#TOTAL_COUNT = 35
#START_COUNT = 0

rosrun mrol_sip trainer.py -B ~/tod_stub_dev/tod_stub/bin/obj16.bag --fiducial fiducial.yaml -C config.yaml --image image --camera_info camera_info --points points2 --team_name TeamFranklin --run_number 0 --object_id example




#until [ $START_COUNT -gt $TOTAL_COUNT ]; do
#        echo Object: $START_COUNT
#        let START_COUNT=START_COUNT+1
#done 
