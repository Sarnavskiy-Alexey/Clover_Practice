# Information: https://clover.coex.tech/en/simple_offboard.html#gettelemetry

import rospy
from clover import srv
import os
import datetime

rospy.init_node('get_telemetry')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)

# Print drone's state

log_counter = 0
while os.path.exists(os.path.join(os.path.curdir, f'log_{log_counter}.log')):
    log_counter += 1

with open(f"log_{log_counter}.log", mode='wt') as f:
    f.write(f"Start time: {datetime.datetime.now()}\n\n")
    while True:
        f.write(f"{str(get_telemetry())}\n\n")
        rospy.sleep(1)
