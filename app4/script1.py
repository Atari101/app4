from flask import Flask, render_template

app=Flask(__name__)
"""this is how to make a homepage
    to make a home and about page do render_template above
    and then change def home and def about like example below
    also make a templates folder to hold about and home files
"""
@app.route('/')
def home():
    return render_template("home.html")
"""this is how to make a about page dont forget to add slashes in localhost:/about/"""
@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
