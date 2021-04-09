from flask import Flask, render_template, redirect, make_response, request, session
from flask_restful import abort
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # user = User()
    # user.name = "Пользователь 1"
    # user.about = "биография пользователя 1"
    # user.email = "email@email.ru"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit(
    app.run(host="127.0.0.1", port=8080)

@app.route("/reg")
def main_page():
    db_sess = db_session.create_session()
    teamleads = {}
    job_new = db_sess.query(Jobs)
    for user in db_sess.query(User).filter():
        teamleads[user.id] = user.name + " " + user.surname
    return render_template('jobs.html', job=job_new, tm=teamleads)


if __name__ == '__main__':
    main()