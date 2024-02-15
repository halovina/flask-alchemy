from . import pubsub_blueprint
from .. import dbredis
from flask import request, Response, render_template
import time

@pubsub_blueprint.route('/pubsub/post-message', methods=['POST'])
def post_publish_message():
    message = request.form['message']
    channel_name = "chat-message-test"
    dbredis.publish(channel=channel_name, message=message)
    return Response(status=204)

@pubsub_blueprint.route('/pubsub/get-event-stream', methods=['GET'])
def get_event_stream():
    def stream():
        pubsub = dbredis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe('chat-message-test')
        for message in pubsub.listen():
            # data = message['data']
            time.sleep(0.5)
            yield "data: {}\n\n".format(message['data'])
            
    return Response(stream(), mimetype='text/event-stream')
            

@pubsub_blueprint.route('/pubsub/homepage', methods=['GET'])
def pubsub_sample_page():
    return render_template('messages.html')