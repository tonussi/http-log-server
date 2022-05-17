import json
from logging.config import dictConfig

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from service.data_source_writer_service import DataSourceWriterService
from service.health_check_service import HealthCheckService
from service.text_line_service import TextLineService
from service.replica_writer_service import ReplicaWriterService

from model.primary_backup import PrimaryBackup
from model.throughput_logger import ThroughputLogger

load_dotenv()
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

class FlaskApp():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def base_url():
        """Base url to test API. Here its possible to directly check the health of the backups"""
        response = HealthCheckService().perform()

        print(jsonify(response))
        return jsonify(response)

    @app.route('/line', methods=['GET'])
    def text_line():
        """Base url to test API. Here its possible to directly check the health of the backups"""
        line_number = request.args.get('number')
        response = TextLineService().perform(line_number)
        print(jsonify(response))

        ThroughputLogger().perform()
        return jsonify(response)

    @app.route('/db', methods=['POST'])
    def send_data_to_file():
        """URL for registering data."""
        db_new_inserts = json.loads(request.data)["batch"]
        response = DataSourceWriterService().perform(db_new_inserts)

        print(jsonify(response))
        return jsonify(response)

    @app.route('/rep', methods=['POST'])
    def send_data_to_replica():
        """URL for registering data."""
        db_new_inserts = json.loads(request.data).get("batch", [])
        which_replica = json.loads(request.data).get("which_replica", None)

        response = {}

        if which_replica:
            response = ReplicaWriterService(
                which_replica).perform(db_new_inserts)
        else:
            response = DataSourceWriterService().perform(db_new_inserts)

        print(jsonify(response))
        return jsonify(response)

    @app.route('/pb', methods=['POST'])
    def start_primary_backup():
        """URL for registering data."""
        response = PrimaryBackup().perform()

        print(jsonify(response))
        return jsonify(response)
