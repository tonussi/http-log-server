import json
import logging

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from service.data_source_writer_service import DataSourceWriterService
from service.text_line_service import TextLineService

from models.statistics import Statistics

load_dotenv()


class FlaskApp(object):
    app = Flask(__name__)

    def __init__(self, **kwargs) -> None:
        self.address = kwargs["address"]
        self.port = kwargs["port"]
        self.tcp_onoff = kwargs["tcp_onoff"]
        self.node_id = kwargs["node_id"]
        logging.info(kwargs)

    def perform(self):
        logging.info(f"Starting {__name__}")
        self.app.run(host=self.address, port=self.port, debug=True)

    @app.route('/', methods=['GET'])
    def _base_url():
        """Base url to test API. Here its possible to directly check the health of the backups"""
        print(request)
        # response = HealthCheckService().perform()
        return "Ok"

    @app.route('/line', methods=['POST'])
    def _text_line():
        """Base url to test API. Here its possible to directly check the health of the backups"""
        print(request)
        line_number = json.loads(request.data)["number"]
        response = TextLineService().perform(line_number)
        Statistics().perform()
        return jsonify(response)

    @app.route('/db', methods=['POST'])
    def _send_data_to_file():
        """URL for registering data."""
        print(request)
        db_new_inserts = json.loads(request.data)["batch"]
        response = DataSourceWriterService().perform(db_new_inserts)
        Statistics().perform()
        return jsonify(response)

    # @app.route('/hashicorp-raft/join', methods=['POST'])
    # def _join():
    #     print(json.loads(request.data))
    #     return bytes('{"number":-1}', "utf-8")

    # @app.route('/hashicorp-raft/join', methods=['POST'])
    # def _join():
    #     print(json.loads(request.data))
    #     return bytes('{"batch":[{"operation":"INSERT","name":"luquas","city":"floripa"}]}', "utf-8")
