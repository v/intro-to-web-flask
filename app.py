from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'first_name' in request.args:
        name = request.args['first_name']
        lunch = request.args['lunch']

        # this gets run anytime submits an order.

        with open('orders.txt', 'a') as handle:
            handle.write(name + '|'+ lunch + "\n")
            handle.close()

        return render_template('thanks.html', name=name, lunch=lunch)
    return render_template('lunch.html')

@app.route('/orders')
def orders():

    #list in python.
    orders_list = []

    with open('orders.txt', 'r') as handle:
        for line in handle.readlines():
            name, lunch = line.strip().split('|')

            orders_list.append((name, lunch))

    return render_template('orders.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
