from flask import Flask, request, jsonify
# from user import deployment

app = Flask(__name__)

@app.route("/hi/<month>", methods=["GET"])
def demo(month):
    try:
        print(month)
        result =" deployment(month=month)"
        return f"<h1>hi <p>{month}</p></h1>", 200
    except Exception as e:
        # Log the error message if needed
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
