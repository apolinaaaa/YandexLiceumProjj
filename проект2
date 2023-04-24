from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session
from data.notes import Notes
from data.user import User
from forms.user import RegisterForm, LoginForm
from forms.notes import CreateNote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Invalid email or password",
                               form=form)
    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def index():
    session = db_session.create_session()
    notes = session.query(Notes).all()
    return render_template('index.html', notes=notes)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_required
@app.route('/addnote', methods=['GET', 'POST'])
def add_note():
    form = CreateNote()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if not db_sess.query(User).get(form.team_leader.data):
            return render_template('addnote.html', title='New Note',
                                   form=form,
                                   message="Invalid team leader")
        new_note = Notes(
            team_leader=form.team_leader.data,
            note=form.note.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(new_note)
        db_sess.commit()
        return redirect('/')
    return render_template('addnote.html', title='New Note', form=form)


def main():
    db_session.global_init('db/mars.db')
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
