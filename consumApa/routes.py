from datetime import datetime
#from werkzeug.utils import redirect
#cd import cs50
import sqlite3
#from cs50 import SQL

#from consumApa import app
from flask import render_template, request, Flask, g, redirect
#import consumApa
#from consumApa.models import ApaRece
#from consumApa import db
app = Flask(__name__)
#db = cs50.SQL("sqlite:///consumApa.db")

"""
@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        index_buc = request.form['indexBuc']
        index_baie = request.form['indexBaie']
        index_wc = request.form['indexWC']
        inreg_noua = ApaRece(indexBuc=index_buc, indexBaie=index_baie, indexWCServiciu=index_wc)
        db.session.add(inreg_noua)
        db.session.commit()
        return redirect('/')
    else:
        total_inreg = ApaRece.query.order_by(ApaRece.dataConsum).all()
        return render_template('home.html', inreg=total_inreg)
"""

def connect_db():
    sql = sqlite3.connect('consumApa/consumApa.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    #Check if DB is there
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

@app.route("/")
def home():
    db = get_db()
    cursor = db.execute('SELECT * FROM ApaRece')
    result = cursor.fetchall()
    return render_template("home.html", inreg=result)

@app.route("/adauga", methods=["POST"])
def adauga():
    indexBuc = request.form.get("indexBuc")
    indexBaie = request.form.get("indexBaie")
    indexWC = request.form.get("indexWC")
    #data = datetime.utcnow
    data = datetime.now()
    format_data = data.strftime('%d.%m.%Y %H:%M')

    db=get_db()
    cursor = db.execute("INSERT INTO ApaRece (indexBuc, indexBaie, indexWC, dataConsum) VALUES(?, ?, ?, ?)", (indexBuc, indexBaie, indexWC, format_data))
    
    db.commit()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)