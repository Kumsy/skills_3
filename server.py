from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE
# Homepage
@app.route('/')
def homepage():

    if 'user_name' in session:
        return redirect('/top-melons')
    return render_template('homepage.html')

# Store username in a session
@app.route('/get-name')
def get_name():

    user_name = request.args.get("user_name")
    session['user_name'] = user_name
    # print(session['user_name'])

    return redirect('/top-melons')


# Shows our most loved melons page
@app.route('/top-melons')
def top_melons():

    name = []
    num_loves = []
    melon_image = []

    for melons in MOST_LOVED_MELONS:
        name.append(MOST_LOVED_MELONS[melons]['name'])
        num_loves.append(MOST_LOVED_MELONS[melons]['num_loves'])
        melon_image.append(MOST_LOVED_MELONS[melons]['img'])

    most_mels = MOST_LOVED_MELONS

    if 'user_name' in session:
        return render_template("top-melons.html",
                                name = name,
                                num_loves = num_loves,
                                melon_image = melon_image,
                                MOST_LOVED_MELONS = most_mels,
                                user_name = session['user_name']
                                )
    return redirect('/')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
