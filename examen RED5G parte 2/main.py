from flask import Flask, render_template, request, url_for, redirect, flash
from bd import Products, engine, Base, session

app = Flask(__name__)

app.secret_key = 'my_secret_key'

@app.route('/')
def Index():
    data = session.query(Products).all()
    return render_template('index.html', products = data)

@app.route('/add_product', methods=['POST'])
def add_user():
    if request.method == 'POST':
        tittle_r = request.form['tittle']
        description_r = request.form['description']
        value_r = request.form['value']
        quantity_r = request.form['quantity']

        new_product = Products(tittle=tittle_r, description=description_r, value=float(value_r), quantity=int(quantity_r))
        session.add(new_product)
        session.commit()
        flash('product added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_contact(id):
    frame=session.query(Products).filter(Products.id==id)
    for element in frame:
        product_data = element
    return render_template('edit-product.html', selected_product=product_data)

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        session.query(Products).filter(Products.id == id).update(
            {
                Products.tittle:request.form['tittle_edit'],
                Products.description:request.form['description_edit'],
                Products.value:float(request.form['value_edit']),
                Products.quantity:int(request.form['quantity_edit'])
            }
        )
        session.commit()
        flash('product updated successfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    session.query(Products).filter(Products.id==id).delete()
    session.commit()
    flash('product deleted successfully')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    app.run(port = 3000, debug = True)