from website import create_app, threading
from website.models import background

app = create_app()
# set debug mode
@app.before_first_request
def start_background_task():
    thread = threading.Thread(target=background)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    app.run()


