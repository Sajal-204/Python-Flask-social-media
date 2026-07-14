from flask import Flask, render_template, url_for, flash, redirect
from form import Sign_up, Login
app=Flask(__name__)
app.config["SECRET_KEY"] = "s67868ajal"
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    form=Sign_up()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data} !", "success")
        return redirect(url_for("home"))
    return render_template("signup.html",title="Sign up ", form = form )

@app.route("/login",methods=["GET","POST"])
def login():
    form=Login()
    if form.validate_on_submit():
        if form.password.data=="password" and form.email.data =="sajal@gmail.com":
            flash(f"Logged in as {form.email.data} !",'success')
            return redirect(url_for("home"))
        else:
            flash(f"Login failed. Please try again !",'danger')
    return render_template("login.html",title="Login",form=form)


if __name__ == "__main__":
    app.run(debug=True)
