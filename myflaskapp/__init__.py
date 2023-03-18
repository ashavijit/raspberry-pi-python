from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def get_ip():
    ip=request.remote_addr
    return f"Your IP is {ip}"

def run():
    app.run()