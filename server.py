from flask import Flask, render_template, request
import predict_7_stages as p7s
import predict_benign_normal_malignant as bnm
import predict_dense_fatty_glandular as dfg
import read_medical_record as rmd
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('login.html')

@app.route('/logged_in', methods=['POST'])
def login_in():
    username = request.form['username']
    password = request.form['password']
    if username=="admin" and password=="admin":
        return render_template('index.html', path = None)
    else:
        return render_template('login.html', msg="invalid")

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/graphs')
def show_graphs():
    return render_template('graph.html')


@app.route('/process', methods=['POST'])
def process():
    imgNo = request.form['name']
    print imgNo
    pType = os.popen('python predict_benign_normal_malignant.py '+imgNo).read().strip()
    pType = pType.split(',')
    prob = float(pType[1])
    pType[1] = str(int(float("{:.3}".format(prob*100))) -2 ) + "%"
    pBack = os.popen('python predict_dense_fatty_glandular.py '+imgNo).read().strip()
    pBack = pBack.split(',')
    prob = float(pBack[1])
    pBack[1] = "{:.3}%".format(prob*100)
    pAbnorm = os.popen('python predict_7_stages.py '+imgNo).read().strip()
    pAbnorm = pAbnorm.split(',')
    prob = float(pAbnorm[1])
    pAbnorm[1] = "{:.3}%".format(prob*100)

    medical_info = rmd.read_data(imgNo)
    return render_template('index.html', path = imgNo,
                            pType = pType[0], pType1 = pType[1],
                            pBack = pBack[0], pBack1 = pBack[1],
                            pAbnorm = pAbnorm[0],pAbnorm1 = pAbnorm[1],
                            name=medical_info[1], age=medical_info[2], sex=medical_info[3], medical_info=medical_info[4])

if __name__ == "__main__":
    p7s.load()
    bnm.load()
    dfg.load()
    app.run(host='0.0.0.0', port=8080, debug=True)