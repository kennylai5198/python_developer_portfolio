from flask import Flask, render_template, url_for, request, redirect
import os, io, csv
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')

@app.route('/<string:page_name>/<string:reply>')
def reply_page(page_name, reply):
    return render_template(f'{page_name}.html', reply=reply)

def write_to_file(sub_data):
    with open("database.txt", "a") as database:
        email = sub_data['email']
        subject = sub_data['subject']
        message = sub_data['message']
        print(f'{email},{subject},{message}')
        database.write(f'\n{email},{subject},{message}')
        database.close()

def write_to_csv(sub_data):
    with open('database2.csv', newline='', mode='a') as database2:
        email = sub_data['email']
        subject = sub_data['subject']
        message = sub_data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        database2.close()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            email = data['email']
            write_to_csv(data)
            return redirect(f'/thankyou/{email}')
        except:
            return 'Error writing to database. Did not save to database.'
    else:
        return 'Something went wrong. Try again.'



# if __name__ == '__main__':
#     app.run(debug=True)


