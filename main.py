from flask import Flask, jsonify, request, render_template
from markupsafe import Markup
import requests
import json

app = Flask('app')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    res = requests.get(
        "https://www.google.com/complete/search",
        params={
            "q": query,
            "cp": len(query),
            "client": "psy-ab",
            "xssi": "t",
            "gs_ri": "gws-wiz",
            "hl": "en",
            "authuser": 0,
            "psi": "UaP3X5P4OJG5ggeD27aoCw.1610064722698",
            "dpr": "1.3513514995574951"
        },
        headers={
            "user-agent": "Mozilla/5.0 (X11; CrOS x86_64 13505.73.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.109 Safari/537.36"
        }
    )
    body = json.loads(
        res.text.splitlines()[1]
    )
    results = []
    for item in body[0]:
        result_text = item[3]["zh"] if len(item) > 3 else Markup(item[0]).striptags()
        result_subtext = item[3]["zi"] if len(item) > 3 else ''

        results.append({
            "result": result_text,
            "subtext": result_subtext
        })
    return jsonify(results)


app.run(host='0.0.0.0', port=8080)