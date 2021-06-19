from flask import Flask, render_template

app = Flask(__name__)

#豆瓣爬虫练习
@app.route('/0')
def hello_world1():
    return render_template('page1.html')
@app.route('/25')
def hello_world2():
    return render_template('page2.html')

#alice练习
@app.route('/alice')
def hello_world3():
    return render_template('alice.html')

if __name__ == '__main__':
    app.run(debug=True)
