from flask import Flask, jsonify

app = Flask(__name__)

# Your final JSON
final_result_json = {
    "6": "A",
    "12": "A",
    "41": "A",
    "LE-6": "A"
}

@app.route("/")
def return_json():
    return jsonify(final_result_json)

if __name__ == "__main__":
    app.run(debug=True)
