from flask import Flask, request
import sett

app = Flask(__name__)

@app.route('/bienvenido', methods=["GET"])
def bienvenido():
    return "Hola mundo desde flask"


@app.route('/webhook', methods=["GET"])
def verificar_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.chanllenge')

        if token == sett.token and challenge != None:
            return challenge
        else:
            return 'Token incorrect', 403

    except Exception as e:
        print(f"Error: {e}")


@app.route('/webhook', methods=['POST'])
def recibir_mensaje():
    try:
        body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['message'][0]
        number = message['from']
        text = message['text']


    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    app.run(debug=True)