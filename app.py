from flask import Flask, render_template,url_for #import flask class

app = Flask(__name__) #class instance so that flask 
#knows where to look for resources such as templates and static files.

posts = [
    {
        'author': 'Thomas',
        'title': 'About Me',
        'content': 'I am blabla welcome to my blog',
        'date_posted': 'Oct 18 2022'},
    {
        'author': 'Nalu',
        'title': 'Lion King',
        'content': 'Lion King now in studios',
        'date_posted': 'Oct 18 2022'
    }
]

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/") #specify url to trigger func to display content
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug = True)