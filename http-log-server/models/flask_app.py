import json
import time
from multiprocessing import Process, Value

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from service.data_source_writer_service import DataSourceWriterService
from service.text_line_service import TextLineService

from models.statistics import Statistics

load_dotenv()


class ProcessDataPayloadAnswer(object):
    def perform(self, request_data):
        if len(request_data) <= 0 or request_data is None:
            return jsonify({"status": 200})

        loaded_data = json.loads(request_data)
        endpoint = loaded_data.get("endpoint", "/")

        if endpoint == "/line":
            if len(request_data) == 0:
                return jsonify({"status": 404})
            loaded_data = json.loads(request_data)
            payload = loaded_data.get("payload", {})
            return self._when_line(payload.get("number", -1))
        elif endpoint == "/db":
            if len(request_data) == 0:
                return jsonify({"status": 404})
            loaded_data = json.loads(request_data)
            payload = loaded_data.get("payload", {})
            return self._when_batch(payload.get("batch", []))
        elif endpoint == "/":
            return jsonify({"status": 200})

        return jsonify({"status": 404})

    def _when_line(self, line_number):
        if line_number == None:
            return jsonify({"status": 404})

        response = TextLineService().perform(line_number)

        Statistics().perform()

        return jsonify(response)

    def _when_batch(self, batch):
        if len(batch) == 0:
            return jsonify({"status": 404})

        response = DataSourceWriterService().perform(batch)

        Statistics().perform()

        return jsonify(response)


class FlaskApp(object):
    app = Flask(__name__)

    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

    def perform(self):
        self.app.run(host=self.kwargs["address"],
                     port=self.kwargs["port"], debug=True)

    @app.route('/', methods=['POST'])
    def _base_url_as_post():
        return ProcessDataPayloadAnswer().perform(request.data)

    @app.route('/', methods=['GET'])
    def _base_url_as_get():
        return ProcessDataPayloadAnswer().perform(request.data)

    @app.route('/pulse', methods=['POST'])
    def _pulse_as_post():
        print(request.data)
        return jsonify({'status': 200})

    @app.route('/pulse', methods=['GET'])
    def _pulse_as_get():
        print(request.data)
        return jsonify({'status': 200})

    @app.route('/line/<int:number>', methods=['GET'])
    def _text_line(number):
        response = TextLineService().perform(number)
        return jsonify(response)

    @app.route('/db', methods=['POST'])
    def _send_data_to_file():
        print(request.data)
        if len(request.data) == 0:
            return jsonify({"status": 404})
        db_new_inserts = json.loads(request.data)["batch"]
        response = DataSourceWriterService().perform(db_new_inserts)
        return jsonify(response)
