import logging
import os
import sys
from flask import Flask, request, jsonify
import yaml
#from balena.labs.fleet_analytics.transporter.kafka_rest.kafka_rest_transporter import KafkaTopicTransporter

app = Flask(__name__)

@app.route("/kafka-rest", methods=['POST'])
def sendToKafkaProxy():
    """
    Sends a message to kafka proxy transformer
    :return:
    """
    message = request.get_json()
    print(message)
    logger.info("sending to kafka rest %s".format(message))
    response = kafka_rest_transporter.send_message (message)
    return jsonify(response)

if __name__ == '__main__':

    logger = logging.getLogger(__name__)

    with open(sys.argv[1], "r") as fh:
        # probably needs some sort of smarter paameter parsing to be able to use some kind of reflection
        params = yaml.safe_load(fh)
        kafka_rest = params.get('kafka_rest', None)
        if kafka_rest:
            kafka_rest_url = kafka_rest['proxy_url']
            import balena.labs.fleet_analytics.transporter.kafka_rest.kafka_rest_transporter as k
            kafka_rest_transporter = k.KafkaTopicTransporter(kafka_rest_url)
        app.run(host='0.0.0.0', debug=True, port=5000)