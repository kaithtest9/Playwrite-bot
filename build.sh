apt-get update && \
    apt-get install -y sudo libevent-dev
pip install playwright && \
    playwright install --with-deps
playwright install-deps
pip install flask gunicorn