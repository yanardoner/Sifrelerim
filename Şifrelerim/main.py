# İçe aktar
from flask import Flask, render_template,request, redirect
# Veri tabanı kitaplığını bağlama
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma

class Card(db.Model):
    # Sütun oluşturma
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Başlık
    title = db.Column(db.String(100), nullable=False)
    # Metin
    text = db.Column(db.Text, nullable=False)

    # Nesnenin ve kimliğin çıktısı
    def __repr__(self):
        return f'<Card {self.id}>'
    
#Ödev #2. Kullanıcı tablosunu oluşturun
class User(db.Model):
    email = db.Column(db.String(30), nullable = False)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(20), nullable = False)


# İçerik sayfasını çalıştırma
@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''

    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']

        # Ödev #4. yetkilendirmeyi uygulamak
        users_db = User.query.all()

        for user in users_db:
            if form_login == user.email and form_password == user.password:
                return redirect('/index')

        # Eğer döngüden hiçbir kullanıcıyla eşleşme bulunamazsa
        error = 'Incorrect login or password'

    return render_template('login.html', error=error)
            
@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login = request.form['email']
        password = request.form['password']
        
        #Ödev #3 Kullanıcı verilerinin veri tabanına kaydedilmesini sağlayın
        user = User(email=login, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect('/')
    else:    
        return render_template('registration.html')

# İçerik sayfasını çalıştırma
@app.route('/index')
def index():
    # Veri tabanı girişlerini görüntüleme
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Kayıt sayfasını çalıştırma
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)
    return render_template('card.html', card=card)

@app.route('/Delete_card/<int:id>', methods=["POST"])
def Delete_card(id):
    if request.method == "POST":
        card_to_delete = Card.query.get(id)
        if card_to_delete:
            db.session.delete(card_to_delete)
            db.session.commit()
        return redirect('/index')
    else:
        return render_template('card.html', card=card)

# Giriş oluşturma sayfasını çalıştırma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Giriş formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        text =  request.form['text']

        # Veri tabanına gönderilecek bir nesne oluşturma
        card = Card(title=title, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

if __name__ == "__main__":
    app.run(debug=True)