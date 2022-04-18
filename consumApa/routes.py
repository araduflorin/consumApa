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
    cursor = db.execute("SELECT * FROM ApaRece UNION SELECT * FROM ApaCalda")
    cursorConsum = db.execute("SELECT id, indexBuc, indexBaie, indexWC, dataConsum, tipApa, indexBuc-lag(indexBuc,1) OVER (ORDER BY id) + indexBaie-lag(indexBaie,1) OVER (ORDER BY id) + indexWC-lag(indexWC,1) OVER (ORDER BY id) AS consum FROM ApaRece "+
     "UNION SELECT id, indexBuc, indexBaie, indexWC, dataConsum, tipApa, indexBuc-lag(indexBuc,1) OVER (ORDER BY id) + indexBaie-lag(indexBaie,1) OVER (ORDER BY id) + indexWC-lag(indexWC,1) OVER (ORDER BY id) AS consum FROM ApaCalda ")
     
    result = cursor.fetchall()    
    resultConsum = cursorConsum.fetchall()
    return render_template("home.html", inreg=result, consumA=resultConsum)

@app.route("/adaugaRece", methods=['GET','POST'])
def adaugaRece():
    if request.method == "POST":
        indexBuc = request.form['indexBuc']
        indexBaie = request.form["indexBaie"]
        indexWC = request.form["indexWC"]
        #data = datetime.utcnow
        data = datetime.now()
        format_data = data.strftime('%d.%m.%Y %H:%M')
        tipApa = "rece"
        db=get_db()
        cursor = db.execute("INSERT INTO ApaRece (indexBuc, indexBaie, indexWC, dataConsum, tipApa) VALUES(?, ?, ?, ?, ?)", (indexBuc, indexBaie, indexWC, format_data, tipApa))
        
        db.commit()
        return redirect('/')

@app.route("/adaugaCalda", methods=['GET','POST'])
def adaugaCalda():
    if request.method == "POST":
        indexBuc = request.form['indexBuc']
        indexBaie = request.form["indexBaie"]
        indexWC = request.form["indexWC"]
        #data = datetime.utcnow
        data = datetime.now()
        format_data = data.strftime('%d.%m.%Y %H:%M')
        tipApa = "calda"
        db=get_db()
        cursor = db.execute("INSERT INTO ApaCalda (indexBuc, indexBaie, indexWC, dataConsum, tipApa) VALUES(?, ?, ?, ?, ?)", (indexBuc, indexBaie, indexWC, format_data, tipApa))
        
        db.commit()
        return redirect('/')

@app.route("/modifica", methods=['GET','POST'])
def modifica():
    if request.method == "POST":
        db = get_db()
        cursor = db.execute('SELECT * FROM ApaRece')
        result = cursor.fetchall()
        id_data = request.form.get("id")
        print("ID-ul: ", id_data)
        indexBuc = request.form["indexBuc"]
        indexBaie = request.form["indexBaie"]
        indexWC = request.form["indexWC"]
        #data = datetime.utcnow
        data = datetime.now()
        format_data = data.strftime('%d.%m.%Y %H:%M')

        db=get_db()
        
        cursor = db.execute("""UPDATE ApaRece SET indexBuc=?, indexBaie=?, indexWC=?, dataConsum=? WHERE id=?;""", (indexBuc, indexBaie, indexWC, format_data, id_data))
        
        db.commit()
        return redirect("/")

if __name__=='__main__':
    app.run(debug=True, port=5002)