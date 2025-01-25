from flask import Flask, render_template, redirect, url_for, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dbmodels import Car, CarImage, db
from flask_migrate import Migrate
import secrets
from flask_admin.form import SecureForm
from wtforms.validators import DataRequired

from flask_mail import Mail, Message

app = Flask(__name__) # Создаётся объект Flask, __name__ используется для определения корневого пути приложения.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./car.db" # Настраивает URI для базы данных, в данном случае база данных хранится в файле car.db
app.secret_key = secrets.token_hex(16) # Устанавливает секретный ключ для приложения, который используется Flask для безопасных сессий и защиты данных.
db.init_app(app) # Это связывает базу данных db и приложение app
migrate = Migrate(app, db)



# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # or another SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'egorsever07@gmail.com'
app.config['MAIL_PASSWORD'] = 'semenujik187'
app.config['MAIL_DEFAULT_SENDER'] = 'egorsever07@gmail.com'
mail = Mail(app)


admin = Admin(app, name='My Admin', template_mode='bootstrap3') # Создаёт объект Админ-Панели. name - Имя Админ-Панели. template_mode - задает тему для административной панели.
admin.add_view(ModelView(Car, db.session)) # Добавляет представление модели Car в административную панель.

class CarImageView(ModelView):
    form_base_class = SecureForm
    form_columns = ['car_id', 'image_url']
    form_args = {
        'car_id': {
            'validators': [DataRequired()]
        },
        'image_url': {
            'validators': [DataRequired()]
        }
    }

admin.add_view(CarImageView(CarImage, db.session))

@app.route('/send', methods=['POST'])
def send_email():
    first_name = request.form['first-name']
    second_name = request.form['second-name']
    phone_email = request.form['phone-email']
    
    msg = Message("New Contact Form Submission",
                  recipients=['recipient-email@example.com'])
    msg.body = f"Name: {first_name} {second_name}\nPhone or Email: {phone_email}"

    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
        print("Email sent successfully!")  # Debugging message
    except Exception as e:
        flash(f'Failed to send email. Error: {e}', 'danger')
        print(f'Failed to send email. Error: {e}')  # Debugging message

    return redirect(url_for('deal'))


@app.route('/')  # Декоратор, который определяет маршрут для корневого URL (/).
def home_redirect():
    return redirect(url_for('index'))

@app.route('/car/<int:product_id>')
def details(product_id):
    car = Car.query.get_or_404(product_id)
    images = CarImage.query.filter_by(car_id=car.id).all()
    return render_template('details.html', car=car, images=images)

@app.route('/index.html') # Декоратор для работы с index.html
def index():
    cars = Car.query.all() # Извлекает все записи из db
    return render_template('index.html', cars=cars) # Рендерит шаблон HTML, а также передаёт ему переменную cars

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/car/deal.html')
@app.route('/deal.html')
def deal():
    return render_template('deal.html')

if __name__ == '__main__':
    app.run(debug=True)