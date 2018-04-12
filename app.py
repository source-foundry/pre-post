from flask import Flask
from flask import render_template
app = Flask(__name__)

VALID_SIZES = [8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 30, 36, 48, 60, 72, 90]
RENDER_SIZES = [8, 9, 10, 11, 12, 13, 14, 16, 20, 24, 30, 36]

@app.route('/')
def hello_world():
    return 'Use the URL format: http://localhost:5000/[woff|woff2]/(variant)/(size)'

@app.route('/woff/')
def woff():
    render_sizes = RENDER_SIZES
    extension = "woff"
    variant = "regular"
    return render_template('specimen.html', sizes=render_sizes, extension=extension, variant=variant)

@app.route('/woff/<user_variant>/')
def woff_variant(user_variant):
    render_sizes = RENDER_SIZES
    extension = "woff"
    variant = user_variant
    return render_template('specimen.html', sizes=render_sizes, extension=extension, variant=variant)

@app.route('/woff/<user_variant>/<int:user_fontsize>/')
def woff_fontsize(user_variant, user_fontsize):
    render_sizes = [user_fontsize]
    extension = "woff"
    variant = user_variant
    return render_template('specimen.html', sizes=render_sizes, extension=extension, variant=variant)




@app.route('/woff2/')
def woff2():
    render_sizes = RENDER_SIZES
    extension = "woff2"
    variant = "regular"
    return render_template('specimen.html', sizes=render_sizes, extension=extension, variant=variant)

@app.route('/woff2/<user_variant>/')
def woff2_variant(user_variant):
    render_sizes = RENDER_SIZES
    extension = "woff2"
    variant = user_variant
    return render_template('specimen.html', sizes=render_sizes, extension=extension, variant=variant)

@app.route('/woff2/<user_variant>/<int:user_fontsize>/')
def woff2_fontsize(user_variant, user_fontsize):
    render_sizes = [user_fontsize]
    extension = "woff2"
    variant = user_variant
    return render_template('specimen.html', sizes=render_sizes, extension=extension, variant=variant)
