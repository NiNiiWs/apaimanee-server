import json

def get_payload(msg):
    return json.loads(msg.payload.decode('utf-8'))

def rpc_request(client, controller, msg):
    payload = get_payload(msg)

    print("rpc request :", payload)

    rpc_methods = dict(
            login=controller.user.login,
            register=controller.user.register,
            create_room=controller.room.create_room
            )

    call_name=payload.get('method', None)
    if call_name is None:
        print('"%s" not found in register rpc callback',
                payload.get('method', None))

    method = rpc_methods.get(call_name, None)
    print('get method', method)
    if method is not None:
        method(payload)


def hello(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.hello(payload)

def status(client, controller, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    controller.status(payload)
