from flask import Flask, jsonify, request
from playwright.sync_api import Page, expect, sync_playwright
import os
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/lookup')
def lookup():
    path = request.args.get('path')
    folders = os.listdir(path)
    return jsonify(folders)

@app.route('/get-page-screenshot')
def get_page_screenshot():
    url = request.args.get('url')
    args=[
        "--disable-gpu",
        "--single-process",
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch(slow_mo=50, args=args)
        page = browser.new_page()
        page.goto(url)
        print(page.title())
        # wait for 5 seconds
        page.wait_for_timeout(500)
        img = page.screenshot()
        browser.close()
    encoded_string = base64.b64encode(img).decode('utf-8')
    return '<img src="data:image/png;base64,' + encoded_string + '" />'

@app.route('/getallenv')
def get_all_env():
    envs = dict()
    for key in os.environ:
        envs[key] = str(os.environ[key])
    return jsonify(envs)

if __name__ == '__main__':
    app.run(debug=True)