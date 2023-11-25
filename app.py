import flask
from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['DEBUG']=True

# Pesan default Puja Kerang Ajaib
pesan_default = [
    "Memukuli SpongeBob di Rumah Nanas",
    "Memukuli Patrick di Rumah Batu",
    "Mengajak Sandy pergi Piknik",
    "Memakan Plankton di dapur Krusty Krab",
    "Menjaga Garry di Rumah Nanas",
    "Mengajak Larry Berenang",
    "Pergi ke ulang tahun Tuan Crab",
    "Main musik dengan Squidward di Rumahnya",
    "Memasak Krabby Patty di Krusty Krab",
    "Membasmi kejahatan bersama Bernekle Man & Bernekle Boy"
]

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/selamatdatang', methods=['POST'])
def selamat_datang():
    if 'nama' in request.form:
        nama = request.form['nama']
        pesan = f"Selamat datang {nama}, Puja Kerang Ajaib"
        pesan_acak = random.choice(pesan_default)
        perintah = f"Perintah : {pesan_acak}"
        return render_template('pesanform.html', pesan=pesan, perintah=perintah)
    else:
        return "Error: Parameter 'nama' tidak ditemukan dalam POST request"

if __name__ == '__main__':
    app.run(debug=True)