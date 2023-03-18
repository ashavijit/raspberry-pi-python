from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def get_ip():
    ip=request.remote_addr
    return f"Your IP is {ip}"

if __name__=='__main__':
    app.run(debug=True)