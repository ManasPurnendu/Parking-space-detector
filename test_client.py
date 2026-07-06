import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected!")
    sio.emit('start_detection', namespace='/')

@sio.on('detection_result')
def on_message(data):
    print(f"Received detection_result: free_spaces={data['free_spaces']}")
    sio.disconnect()

sio.connect('http://localhost:5000')
sio.wait()
