from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/check-action', methods=['GET'])
def check_action():
    # You can implement your logic here to decide whether to send "yes" or "no"
    # For simplicity, we will randomly send "yes" or "no"
    import random
    action = random.choice(['yes', 'no'])
    return jsonify({'action': action})

if __name__ == '__main__':
    app.run(debug=True)
