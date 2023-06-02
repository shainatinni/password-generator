from flask import Flask, render_template
import random
import string

papp = Flask(__name__)

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@papp.route('/')
def home():
    password = generate_password()
    return render_template('index.html', password=password)

if __name__ == '__main__':
    papp.run()
