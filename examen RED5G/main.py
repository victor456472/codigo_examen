from flask import Flask, render_template, request, url_for, redirect, flash
from bd import Users, engine, Base, session

app = Flask(__name__)

app.secret_key = 'my_secret_key'

@app.route('/')
def Index():
    data = session.query(Users).all()
    return render_template('index.html', users = data)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        fullname_r = request.form['fullname']
        email_r = request.form['email']
        password_r = request.form['password']
        address_r = request.form['address']
        phone_r = request.form['phone']
        born_date_r = request.form['born_date']

        new_user = Users(fullname=fullname_r, email=email_r, password=password_r, address=address_r , phone=phone_r , born_date=born_date_r)
        session.add(new_user)
        session.commit()
        flash('user added successfully')
        return redirect(url_for('Index'))

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login-test', methods=['POST'])
def login_test():
    if request.method == 'POST':
        email_r=request.form['email_written']
        password_r=request.form['password_written']
        
        users = session.query(Users).all()

        door=True

        for user in users:
            print (user.email)
            print (user.password)
            if ((user.email==email_r) & (user.password==password_r)):
                if door:
                    enter=True
                    door=False
                else:
                    pass 
            else:
                if door:
                    enter=False
                else:
                    pass
                   
        if enter:
            logged_user = session.query(Users).filter(Users.email==email_r).first()
            flash(f'welcome {logged_user.fullname}')
        else:
            flash("the user doesn't exist or the credentials are incorrect")
        
        return redirect(url_for('login')) 
        

if __name__ == "__main__":
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    app.run(port = 3000, debug = True)