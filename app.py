from flask import Flask, jsonify, request
from playwright.sync_api import Page, expect, sync_playwright

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/get-page-screenshot')
def get_page_screenshot():
    url = request.args.get('url')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        # wait for 5 seconds
        page.wait_for_timeout(5000)
        img = page.screenshot()
        browser.close()
    return '<img src="data:image/png;base64,' + img + '" />'

if __name__ == '__main__':
    app.run(debug=True)