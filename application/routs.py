
from . import app
from.views import main_view, check_jwt_view



from application import views
app.add_url_rule('/', view_func= check_jwt_view, methods=['GET'])
app.add_url_rule('/main', view_func= main_view, methods= ['GET'])
app.add_url_rule('/events/form', view_func= views.event_form_view, methods=['GET'])
app.add_url_rule('/events/form/submit', view_func= views.event_submit_view, methods=['POST'])
app.add_url_rule('/events', view_func=views.events_view, methods=['GET'])
app.add_url_rule('/registration/form', view_func= views.registration_form_view, methods=['GET'])
app.add_url_rule('/registration/submit', view_func= views.registration_submit_view, methods= ['POST'])
app.add_url_rule('/login/form', view_func= views.login_form_view, methods= ['GET'])
app.add_url_rule('/login/form/submit', view_func=views.login_form_submit_view, methods = ['POST'])
# app.add_url_rule('/upload_files', view_func= views.upload_files_view, methods=['GET'])
# app.add_url_rule('/user/)




