"""
    Module contains code for abstracting message sending to the backend store.

"""
from abc import ABC, abstractmethod
from balena.labs.fleet_analytics.transporter.message_transporter import LogsTransporter


class LogsTransporter(ABC):
    """
        Placeholder abstract class with connection, message sending, and closing connection
    """

    @abstractmethod
    def connect(**kwargs):
        """
        Connects to backend message datastore if connection needs to be established prior to communication

        :return:
            may return any sort of connection object
        """
        pass

    @abstractmethod
    def send_message(msg, **kwargs):
        """
        Sends messages in json format
        :param kwargs:
        :parm msg: -- message in json format
        :return: custom status
        """
        pass

    @abstractmethod
    def close():
        """
        Closes a connection to source if necessary
        :return:
        """