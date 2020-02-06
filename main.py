"""
    1704423 Leon Whelan's Ank Vector Project
"""

import anki_vector
from anki_vector.util import degrees


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:

        # Connect vector to cube
        docking = None
        print("Connecting to cube...")
        robot.behavior.say_text("Connecting to cube")
        robot.world.connect_cube()

        # Init Cube docking procedure
        if robot.world.connected_light_cube:
            print("Cube docking procedure activate...")
            robot.behavior.say_text("Initiating cube docking procedure")
            dock_response = robot.behavior.dock_with_cube(robot.world.connected_light_cube, num_retries=1)
            if dock_response:
                docking = dock_response.result

            # Disconnect from cube when done
            robot.world.disconnect_cube()

    # Check if the docking procedure succeeded
    if docking:
        if docking.code != anki_vector.messaging.protocol.ActionResult.ACTION_RESULT_SUCCESS:
            robot.behavior.say_text("Cube docking procedure failed")
            print("Cube docking failed with code {0} ({1})".format(str(docking).rstrip('\n\r'), docking.code))
        else:
            robot.behavior.say_text("Cube docking procedure failed")
            print("Cube docking failed.")


if __name__ == '__main__':
    main()
