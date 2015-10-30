import json

def get_payload(msg):
    return json.loads(msg.payload.decode('utf-8'))

def rpc_request(client, controller, msg):
    print("rpc request")
    payload = get_payload(msg)
    if payload['method'] == 'login':
        controller.user.login(payload)

    if payload['method'] == 'register':
        controller.user.register(payload)

def hello(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.hello(payload)

def status(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.status(payload)
