import sys
import time
import signal
from Focuser import Focuser
from RpiCamera import Camera

def start_work(signum, frame):
	camera = Camera()
	focuser = Focuser(1)

	camera.start_preview()

	focuser.reset(Focuser.OPT_MOTOR_X)
	focuser.reset(Focuser.OPT_MOTOR_Y)
	focuser.reset(Focuser.OPT_FOCUS)
	focuser.reset(Focuser.OPT_ZOOM)

	t_start = time.perf_counter()

	for ypos in range(0, 180):
		focuser.set(Focuser.OPT_MOTOR_Y, ypos)
	for xpos in range(0, 180):
		focuser.set(Focuser.OPT_MOTOR_X, xpos)

	for zoom in range(0, 15000, 1000):
		focuser.set(Focuser.OPT_ZOOM, zoom)
	for focus in range(0, 15000, 1000):
		focuser.set(Focuser.OPT_FOCUS, focus)

	t_end = time.perf_counter()

	print("start=", t_start, "end=", t_end, "time=", t_end - t_start, file=sys.stderr)

	camera.stop_preview()
	camera.close()
	sys.exit("Workload exiting...")

signal.signal(signal.SIGUSR1, start_work)
signal.pause()
