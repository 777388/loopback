from flask import Flask, request

app = Flask(__name__)

# Handle all other requests on both ports
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handle_all(path):
    headers = dict(request.headers)
    data = request.get_data()
    response = {
        'headers': headers,
        'data': data.decode()
    }
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
