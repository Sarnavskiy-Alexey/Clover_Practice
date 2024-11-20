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

# clover must fly by square with 5 meter side and print the telemetry before landing

print('Take off and hover 1 m above the ground')
navigate(x=0, y=0, z=1, frame_id='map', auto_arm=True)

# Wait for 5 seconds
rospy.sleep(5)

print('Fly to 5,0,1')
navigate(x=5, y=0, z=1, frame_id='map')

# Wait for 20 seconds
rospy.sleep(20)

print('Fly to 5,5,1')
navigate(x=5, y=5, z=1, frame_id='map')

# Wait for 20 seconds
rospy.sleep(20)

print('Fly to 0,5,1')
navigate(x=0, y=5, z=1, frame_id='map')

# Wait for 20 seconds
rospy.sleep(20)

print('Fly to 0,0,1')
navigate(x=0, y=0, z=1, frame_id='map')

# Wait for 20 seconds
rospy.sleep(20)

# print telemetry
print(get_telemetry())

print('Perform landing')
land()
