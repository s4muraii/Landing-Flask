from flask import Flask, render_template, request, redirect
import csv
import os 
app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'
app.config
if not os.path.exists('products.csv'):
    with open('products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Produto', 'Preco', 'Estoque'])
if not os.path.exists('users.csv'):
    with open('users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Nome', 'Senha'])

@app.route('/')
def home():
    return redirect('/login')

@app.route('/list', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product = request.form['product']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        with open('products.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([product, price, stock])
        return redirect('/list')
    with open('products.csv', 'r') as f:
        products = [row for row in csv.reader(f)]
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.csv', 'r') as f:
            users = [row for row in csv.reader(f)]
        for user in users:
            if user[0] == username and user[1] == password:
                return redirect('/list')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
        return redirect('/login')
    
if __name__ == '__main__':
    app.run(debug=True)