"""Util functions for this project"""

import os

def get_robot_world_file(basefilename):
    """Get a robot world file"""
    return open(os.path.join(os.environ.get("ROBOT_WORLDS_DIR",'testworlds/'),basefilename))