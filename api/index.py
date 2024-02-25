from flask import Flask, redirect, url_for, render_template, request
from model import preprocess_img, predict_result
 
# Our Flask app object
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')

@app.route('/')
@app.route('/index')
def index():
    """Our default routes of '/' and '/index'

    Return: The content we want to display to a user
    """

    return render_template('index.html')

# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            return render_template("result.html", predictions=str(pred))
 
    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)


@app.route('/<path:path>')
def catch_all(path):
    """A special route that catches all other requests

    Note: Let this be your last route. Priority is defined
    by order, so placing this above other functions will
    cause catch_all() to override then.

    Return: A redirect to our index route
    """

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
    