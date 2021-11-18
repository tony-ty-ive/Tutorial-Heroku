from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000/
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/hello')  # http://127.0.0.1:5000/
def hello2():  # put application's code here
    return '<h2>Hello2</h2>'

@app.route('/product/<name>')
def get_product(name):  # put application's code here
    # return "The product is " + str(name) + " " + __name__
    return render_template('user.html', productName = name)

if __name__ == '__main__':  # remove this 'if' when run by 'flask run'
    app.run(port=80, debug=True)
# default port is 5000
# with Debug Mode = False. When you update some code, you need to restart the server for the changes to come upon the web page.
# https://www.jetbrains.com/help/pycharm/run-debug-configuration-flask-server.html#1
# Run/Debug Configuration: Flask Server

# https://stackoverflow.com/questions/57219368/flask-is-running-in-different-port
# It's because your project is a Flask Project.Pycharm will take over some settings

# In Pycharm run configuration setting :
# Additional Options : --host=127.0.0.1 --port=80

# File | Settings | Languages & Frameworks | Flask > Flask Inegration checkbox
# checkbox is default selected for Flask Project