apt-get update && \
    apt-get install -y libevent
pip install playwright && \
    playwright install --with-deps
pip install flask gunicorn