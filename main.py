from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Hello</h1>'


if(__name__ == '__main__'):
  app.run(debug=True)