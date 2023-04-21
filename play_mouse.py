import argparse
import json
import time
from pynput import mouse


mouse_events = []
mouse_controller = mouse.Controller()


def get_recording(file):
    with open(file, "r") as f:
        global mouse_events
        mouse_events = json.load(f)


def play_recording():
    print("Playing recording")
    for mouse_event in mouse_events:
        # print(f"Waiting {round(mouse_event[2], 2)} seconds before {mouse_event[1]} clicking at {mouse_event[0]}")
        time.sleep(mouse_event[2])
        mouse_controller.position = mouse_event[0]
        mouse_controller.click(getattr(mouse.Button, mouse_event[1]))


def main(file, repeat):
    get_recording(file)

    if repeat > 1:
        delay = float(input("Enter the delay (in minutes) between each repetition of the recorded mouse events: "))
        delay_in_sec = delay * 60
        for i in range(repeat):
            play_recording()
            print(f"Waiting {delay} minutes before repeating the recorded mouse events")
            time.sleep(delay_in_sec)
    else:
        play_recording()

    print("Done")


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-f", "--file",
                           help="The file containing the recording of mouse events",
                           default="mouse_events.txt")
    argParser.add_argument("-r", "--repeat",
                           help="Number of times to repeat the recorded mouse events (default: 100)",
                           default=100)

    args = argParser.parse_args()
    main(args.file, args.repeat)
