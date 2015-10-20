import json

def rpc_request(client, controller, msg):
    print("rpc request")
    payload = json.loads(msg.payload.decode('utf-8'))
    if payload['method'] == 'login':
        controller.login(payload)

def hello(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.hello(payload)

def status(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.status(payload)
