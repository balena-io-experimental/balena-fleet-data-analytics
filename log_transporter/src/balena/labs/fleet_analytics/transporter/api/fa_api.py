import logging
import os
import sys
from flask import Flask, request, jsonify, redirect, url_for
import yaml
#from balena.labs.fleet_analytics.transporter.kafka_rest.kafka_rest_transporter import KafkaTopicTransporter

app = Flask(__name__)

@app.route("/kafka-rest", methods=['POST'])
def sendToKafkaRest():
    """

    :return:
    """
    message = request.get_json(force=True, silent=True, cache=False)
    logger.info("sending to kafka rest %s".format(message))
    return send_kafka_rest(message)


def send_kafka_rest(message):
    """
    Sends a message to kafka proxy transformer
    :return:
    """
    response = kafka_rest_transporter.send_message(message)
    return jsonify(response)


@app.route("/", methods=['POST'])
def processRequest():
    """
    redirects to specified endpoint
    :return:
    """
    message = request.get_json(force=True, silent=True, cache=False)
    if sink_type == "kafka_rest":
        return send_kafka_rest(message)

if __name__ == '__main__':

    logger = logging.getLogger(__name__)
    # this probably needs to be somehow abstracted so that it can take any value
    # POST requests cannot be reddirected 
    sink_type = os.getenv('BALENA_FLEET_SINK_TYPE', '')
    kafka_rest_url = os.getenv('BALENA_FLEET_ANALYTICS_KAFKA_URL', '')
    transporter_port = os.getenv('BALENA_FLEET_ANALYTICS_PORT', 5000)
    if kafka_rest_url:
        import balena.labs.fleet_analytics.transporter.kafka_rest.kafka_rest_transporter as k
        kafka_rest_transporter = k.KafkaTopicTransporter(kafka_rest_url)
    app.run(host='0.0.0.0', debug=True, port=transporter_port)