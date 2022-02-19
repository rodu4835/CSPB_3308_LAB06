from flask import Flask, render_template, url_for, request
app = Flask(__name__)
from PIL import Image

routeNames = []
aboutInfo = [
        {
            'className': 'Software Development',
            'classNumber': '3308',
            'classSemester': 'Spring',
            'classYear': '2022',
            'studentName': 'Ronald Durham',
            'studentId': 'rodu4835'
        }]


@app.route('/')
@app.route('/home')
def Home():
    return render_template('home.html', routeNames= routeNames)

@app.route('/about')
def About():
    return render_template('about.html', aboutInfo= aboutInfo, routeNames= routeNames)

@app.route('/colors')
def Colors():
    return render_template('colors.html', routeNames= routeNames)

@app.route('/image', methods=['GET', 'POST'])
def Image():
    return render_template('image.html', routeNames= routeNames)


with app.test_request_context():
    routeNames.append('Home')
    routeNames.append('About')
    routeNames.append('Colors')
    routeNames.append('Image')


if __name__ == '__main__':
    app.run(debug=True)
