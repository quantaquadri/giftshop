from flask import Flask,render_template
app = Flask(__name__)
 

@app.route("/gifts")
def abdul():
 	return render_template('gift_list.html')

@app.route("/cart")
def cart():
 	return render_template('cart.html')
 
if __name__ == "__main__":
    app.run(debug = True)