import json
import threading
import time

from . import managers


class ApaimaneeGameMonitor(threading.Thread):
    def __init__(self, room):
        super().__init__()
        self._running = True
        self._sleep_time = 1
        self._room = room

    def stop(self):
        self._running = False

    def run(self):
        while self._running:
            for r in self._room.rooms:
                print("update r:", r)
            time.sleep(self._sleep_time)
            print('weak up')


class ApaimaneeController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

        self.user = managers.User(self.mqtt_client)
        self.room = managers.Room(self.mqtt_client)

        self.game_controller = ApaimaneeGameMonitor(self.room)
        self.game_controller.start()


    def hello(self, payload):
        print('login first:', payload)

    def status(self, payload):
        self.user = game_controller()

    def create_room(self, payload):
        print('new_create_room', payload)
