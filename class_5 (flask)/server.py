import os
from flask import Flask, render_template_string, request

from datetime import datetime

app = Flask("This is my first app")

@app.route("/")
def say_me_hello():
    """Rendering with context variables"""
    date = datetime.utcnow().strftime("%A %B %d")
    html = """
        <html>
            <h1>Hello. It's {{date}}!</h1>
        </html>
    """
    return render_template_string(html, date=date)


#@app.route("/search/<searchterms>")
#def search(searchterms):
#    #_str = "Your search begins here"
#    html = """
#        <html>
#            <h1>You have searched for {{searchterms}}!</h1>
#        </html>
#    """
#    return render_template_string(html, searchterms=searchterms)


@app.route("/search")
def search():
    #_str = "Your search begins here"
    searchword = request.args.get('q','')
    html = """
        <html>
            <h1>You have searched for {{searchword}}!</h1>
            <h3>[DEBUG] Request info:</h3>
            <ul>
                <li>IP Address: {{ip_addr}}</li>
                <li>HTTP Method: {{method}}</li>
                <li>Path: {{path}}</li>
            </ul>
        </html>
    """
    return render_template_string(
        html, searchword=searchword, method=request.method, path=request.path, ip_addr = request.remote_addr)


if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)