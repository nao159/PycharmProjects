from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, url
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def append_cafe_to_csv(file_name, elements):
    with open(file_name, "a+", newline='') as data:
        writer = csv.writer(data)
        writer.writerow(elements)

class CafeForm(FlaskForm):
    rating_array = [1, 2, 3, 4, 5]
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url_link = StringField('Location URL', validators=[url()])
    open_time = StringField('open time', validators=[DataRequired()])
    closing_time = StringField('closing time', validators=[DataRequired()])
    coffee_rating = SelectField('coffee rating', choices=rating_array)
    wifi_rating = SelectField('wifi rating', choices=rating_array)
    power_outlet_rating = SelectField('power rating', choices=rating_array)
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
#
#               COMPLETED
#

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("True")
            cafe_row = [form.cafe.data,
                        form.url_link.data,
                        form.open_time.data,
                        form.closing_time.data,
                        form.coffee_rating.data,
                        form.wifi_rating.data,
                        form.power_outlet_rating.data]
            append_cafe_to_csv('cafe-data.csv', cafe_row)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    #
    #               COMPLETED
    #
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        # next(csv_data) skips heading because it pass it behind
        next(csv_data)
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            print(row)
    print(list_of_rows)
    headings = ('Cafe', 'Link', 'Open time', 'Closing time', 'Coffee rating', 'Wifi rating', 'Power outlet rating')
    return render_template('cafes.html', headings=headings, cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
