from polyglot.detect import Detector
from polyglot.text import Text
from polyglot.downloader import downloader
import csv
import tweepy
from flask import Flask, request
import pyodbc

downloader.download("sentiment2.en")
downloader.download("sentiment2.yo")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=THA-MACHINE;'
                      'Database=SentiAna;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

app = Flask(__name__)


@app.route('/query-example')
def query_example():
    print('receiving incoming request...')
    value = request.args.get('language')
    return '''<h1> The language value is : {}<h1>'''.format(value)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''<h1> The language value is : {}<h1>
                  <h1> The frameworkvalue is : {}<h1>'''.format(language, framework)
    return '''<form method='POST'>
                Language: <input type="text" name="language"/><br/>
                Framework: <input type="text" name="framework"/><br/>
                <input type="submit" value="Submit"><br/>
                </form>'''


@app.route('/do-sentiment-analysis', methods=['POST'])
def do_sentiment_analysis():
    req_data = request.get_json()

    sentence = req_data['sentence']
    time = req_data['time']
    type_of_person = req_data['type_of_person']
    group_chat_name = req_data['group_chat_name']

    text = Text(sentence)

    sentiment = text.polarity

    cursor.execute('''
                INSERT INTO SentiAna.dbo.Sentiment_Analysis(Sentence, Sentiment, TypeOfPerson, GroupName)
                VALUES
                (?,?,?,?)
                ''', (sentence, sentiment, type_of_person, group_chat_name))
    conn.commit()

    return '''
            status_code:{},
            status:{},
            message:{}
            '''.format('200', 'successful', 'Analysis was successful')


if __name__ == '__main__':
    app.run(debug=True, port=6001)
