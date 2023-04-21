from pynput import mouse
import time
import json


last_click_time = None
start_recording_time = None
mouse_events = []


def main():
    print("Press and hold any mouse button for 2 seconds to start recording mouse events")

    def start_recording(x, y, button, pressed):
        global last_click_time
        click_event_time = time.time()
        if pressed:
            last_click_time = click_event_time
        elif not pressed and last_click_time and click_event_time - last_click_time > 2:
            global start_recording_time
            start_recording_time = click_event_time
            print("Starting to record mouse")
            return False

    with mouse.Listener(on_click=start_recording) as listener:
        listener.join()

    print("Press and hold any mouse button for 2 seconds to stop recording mouse events")

    mouse_controller = mouse.Controller()

    def capture(x, y, button, pressed):
        global mouse_events
        click_event_time = time.time()
        if pressed:
            mouse_events.append((mouse_controller.position, button, click_event_time))
        elif not pressed and click_event_time - mouse_events[-1][2] > 2:
            print("Stopped recording mouse")
            return False

    with mouse.Listener(on_click=capture) as listener:
        listener.join()

    global start_recording_time, mouse_events
    rel_mouse_events = []
    prev_event_time = start_recording_time
    for mouse_event in mouse_events:
        rel_mouse_events.append((mouse_event[0], mouse_event[1].name, mouse_event[2] - prev_event_time))
        prev_event_time = mouse_event[2]

    with open("mouse_events.txt", "w") as f:
        json.dump(rel_mouse_events, f)


if __name__ == "__main__":
    main()
