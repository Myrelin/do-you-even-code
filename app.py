from flask import Flask, render_template
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    open_sessions = data_manager.get_recent_sessions()

    return render_template('index.html', open_sessions=open_sessions)

#
# def main():
#     app.run(debug=True)

#
# if __name__ == '__main__':
#     main()
