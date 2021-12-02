from werkzeug.utils import redirect
from consumApa import app
from flask import render_template, request
import consumApa
from consumApa.models import ApaRece
from consumApa import db

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