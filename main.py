from flask import Flask, render_template
import subprocess

app = Flask(__name__)

#hell = print("hello")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/start_music', methods=['POST'])
def my_form_post():
    subprocess.call("./startmusic.sh")
    a = "Turned on"
    return render_template("index.html",output=a)

@app.route('/stop_music', methods=['POST'])
def stop_my_music():
    subprocess.call("./stopmusic.sh")
    b = "Turned off"
    return render_template("index.html",output=b)


if __name__ == "__main__":
   #app.run(debug=True)
   app.run(host='0.0.0.0', port=5000)