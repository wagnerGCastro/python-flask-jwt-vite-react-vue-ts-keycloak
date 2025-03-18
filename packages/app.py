from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)


# Flask-Migrate
migrate = Migrate(app, db)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    def __repr__(self):
        return f"<Product {self.name}>"
      
      
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"
  
@app.route("/products")
def prd_index():
    my_list = []
  
    for p in Product.query.all():
      # my_list.append(p)
      my_list.append( f"</br> Produto = {p.name} ID = {p.id}. ")
      # print(p.name, p.id)
  
    my_string = ", ".join(my_list)
    
    # mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
  
    return my_string