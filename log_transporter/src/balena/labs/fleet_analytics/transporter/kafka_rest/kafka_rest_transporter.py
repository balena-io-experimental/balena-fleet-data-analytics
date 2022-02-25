import requests
#from balena.labs.fleet_analytics.transporter import message_transporter
import uuid
import json

class KafkaTopicTransporter():
    """
    Message sending using kafka rest proxy endpoint
    """

    REQUEST_HEADERS = {"content-Type": "application/vnd.kafka.json.v2+json",
                       "accept": "application/vnd.kafka.v2+json, application/vnd.kafka+json, application/json"}

    def __init__(self, entpoint_url):
        # probably had to check if the
        self.endpoint_url = entpoint_url

    def send_message(self, msg):
        """
        Sends message to kafka rest proxy endpoint
        :return:
            dict {
                "status": status of the returned response
                "messge": message of the response
                "response": full response (http)
            }
        """
        records = { "records" :[
            {
                "key": str(uuid.uuid1()),
                "value": msg
            }
        ] }

        print(records)
        print(type(records))
        res = requests.post(self.endpoint_url, json = records, headers=self.REQUEST_HEADERS)
        print(res)
        print(res.reason)
        return {
            "message": res.reason,
            "status": res.status_code,
            "response": res.json()
        }

    def close():
        pass

    def connect():
        pass
