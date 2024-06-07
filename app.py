from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route("/sum", methods=["POST"])
def sum():
    data = request.get_json()
    a = data.get('num_a')
    b = data.get('num_b')
    result = a + b   
    return jsonify({"sum": result}), 200

@app.route("/about")
def about_us():
    return "This is the about us page"



if __name__ == "__main__":
    app.run(debug = True)


