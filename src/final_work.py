# Information: https://clover.coex.tech/programming

import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

# 1 meter UP
# TO 1,0,1
# TO 1,1,1
# TO 0,1,1
# TO 0,0,0

print('Take off and hover 1 m above the ground')
# navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)
navigate(x=0, y=0, z=1, frame_id='map', auto_arm=True)

# Wait for 5 seconds
rospy.sleep(5)

print('Fly to 1,0,1')
# navigate(x=1, y=0, z=0, frame_id='body')
navigate(x=1, y=0, z=1, frame_id='map')

# Wait for 5 seconds
rospy.sleep(5)

print('Fly to 1,1,1')
# navigate(x=0, y=1, z=0, frame_id='body')
navigate(x=1, y=1, z=1, frame_id='map')

# Wait for 5 seconds
rospy.sleep(5)

print('Fly to 0,1,1')
# navigate(x=-1, y=0, z=0, frame_id='body')
navigate(x=0, y=1, z=1, frame_id='map')

# Wait for 5 seconds
rospy.sleep(5)

print('Fly to 0,0,1')
# navigate(x=0, y=-1, z=0, frame_id='body')
navigate(x=0, y=0, z=1, frame_id='map')

# Wait for 5 seconds
rospy.sleep(5)

print('Perform landing')
land()
