from flask import Flask, render_template
from pokeapi import pokecambio
import os

app = Flask(__name__)

@app.route('/')
def home():
    all_curr = ['USD', 'BOB', 'CAD', 'NZD', 'EUR', 'RUB', 'ARS', 'CLP', 'COP']
    pagina = []
    i = 0

    for i in all_curr:
        
        pagina.append(
        f'''
        <div>
        <p class="text-center text-4xl font-bold mt-10">{pokecambio.ExcToPkm_name(i)}</p>
        <img src="{pokecambio.ExcToPkm_img(i)}" alt="" style="width:10em">
        <p class="text-center text-2xl">{pokecambio.ExcToPkm_cambio(i)}</p>
        <p class="text-center text-2xl">{pokecambio.ExcToPkm_coins(i)}</p>
        </div>
        ''')



    return render_template('index.html', p1 = pagina[0], p2 = pagina[1], p3 = pagina[2], p4 = pagina[3], 
    p5 = pagina[4], p6 = pagina[5], p7 = pagina[6], p8 = pagina[7], p9 = pagina[8])

port = int(os.getenv('PORT', 5000))
app.run(host = '0.0.0.0', port = port)