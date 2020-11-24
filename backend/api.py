from flask import Flask
from flask import request
from flask import jsonify
from service.health_check_service import HealthCheckService
from model.primary_backup import PrimaryBackup
from service.db_writer_service import DbWriterService

app = Flask(__name__)


@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API. Here its possible to directly check the health of the backups"""

    response = HealthCheckService().perform()

    return jsonify(response)


@app.route('/db', methods=['POST'])
def send_data_to_file():
    """URL for registering data."""
    db_new_inserts = request.data["inserts"]

    response = DbWriterService().perform(db_new_inserts)

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
