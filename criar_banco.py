from programa import database, app
from programa.models import Usuario,Materia

with app.app_context():
    database.create_all()