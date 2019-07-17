from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def homepage():

    url = "https://github.com/coltonfischer/gitpod-redirect"

    if request.referrer and host(request.referrer) == "github.com":
        url = "https://gitpod.io/#" + request.referrer

    return redirect(url)

def host(url):
    
    spltAr = url.split("://")
    i = (0,1)[len(spltAr)>1]
    return spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

