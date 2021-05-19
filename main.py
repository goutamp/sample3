import logging

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():

    """Return a friendly HTTP hello greeting."""

<<<<<<< HEAD
    return 'Hello Istiosha_added_1.0.4'
=======
<<<<<<< HEAD
    return 'Hello Istiosha_'
=======
    return 'Hello Istio_master_push_patch'
>>>>>>> a2642468e888504bc31d94a2d60e32ecc89c371f
>>>>>>> 038949c54bc1cdcd3b94f8b6cbf3a567df1a8b46


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
