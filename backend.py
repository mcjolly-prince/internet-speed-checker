from flask import Flask, render_template, jsonify
import speedtest
from ping3 import ping

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("front.html")

@app.route("/test")
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Mbps
        latency = ping('google.com') * 1000  # ms

        return jsonify({
            "download": round(download_speed, 2),
            "ping": round(latency, 2)
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
