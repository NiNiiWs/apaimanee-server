import json

def hello(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.hello(payload)

def status(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.status(payload)
