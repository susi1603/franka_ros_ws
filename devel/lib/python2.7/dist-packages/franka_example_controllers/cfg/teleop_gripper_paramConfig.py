## *********************************************************
##
## File autogenerated for the franka_example_controllers package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'GRIPPERPARAMETER', 'lower': 'gripperparameter', 'srcline': 124, 'name': 'GripperParameter', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::GRIPPERPARAMETER', 'field': 'DEFAULT::gripperparameter', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 12, 'description': 'Grasping force to be applied on an object. [N]', 'max': 60.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/franka_ros_ws/src/franka_ros/franka_example_controllers/cfg/teleop_gripper_param.cfg', 'name': 'grasp_force', 'edit_method': '', 'default': 40.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 15, 'description': 'Speed of the follower gripper when opening [m/s]', 'max': 0.4, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/airocs/franka_ros_ws/src/franka_ros/franka_example_controllers/cfg/teleop_gripper_param.cfg', 'name': 'move_speed', 'edit_method': '', 'default': 0.3, 'level': 0, 'min': 0.01, 'type': 'double'}], 'type': 'apply', 'id': 1}], 'parameters': [], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

