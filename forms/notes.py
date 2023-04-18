from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from data import db_session
from data.user import User


class CreateNote(FlaskForm):
    team_leader = SelectField('Team Leader', choices=[], validators=[DataRequired()])
    note = StringField('Note', validators=[DataRequired()])
    work_size = IntegerField('Work Size')
    collaborators = StringField('Collaborators')
    is_finished = BooleanField('Is Finished')
    submit = SubmitField('Add Note')

    def __init__(self, *args, **kwargs):
        super(CreateNote, self).__init__(*args, **kwargs)
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        arr = [(user.id, user.fio) for user in users]
        self.team_leader.choices = arr
