import firebase_admin
from firebase_admin import credentials, firestore, db, initialize_app, storage
from flask import Flask, redirect, url_for, render_template, request
import base64

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://biotopsamling-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference('/')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/arter')
def arter():
    alleArter = []
    getArter = ref.get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/art')
def art():
    norsk_navn = request.args.get('norsk_navn')
    alleArter = []
    getArter = ref.order_by_child('norsk_navn').equal_to(norsk_navn).get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('art.html', arter=alleArter)

@app.route('/stilksporesopper')
def stilksporesopper():
    alleArter = []
    getArter = ref.order_by_child('rekke').equal_to('Stilksporesopper').get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/bladmoser')
def bladmoser():
    alleArter = []
    getArter = ref.order_by_child('rekke').equal_to('Bladmoser').get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/karsporeplanter')
def karsporeplanter():
    alleArter = []
    getArter = ref.order_by_child('rekke').equal_to('Karsporeplanter').get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/nakenfrøinger')
def nakenfrøinger():
    alleArter = []
    getArter = ref.order_by_child('rekke').equal_to('Nakenfrøinger').get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/dekkfrøete_planter')
def dekkfrøete_planter():
    alleArter = []
    getArter = ref.order_by_child('rekke').equal_to('Dekkfrøete planter').get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/leddyr')
def leddyr():
    alleArter = []
    getArter = ref.order_by_child('rekke').equal_to('Leddyr').get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/ryggstrengdyr')
def ryggstrengdyr():
    alleArter = []
    getArter = ref.order_by_child('rekke').equal_to('Ryggstrengdyr').get()
    sorted_firebaseArter = sorted(getArter.items(), key=lambda x: (x[1]["rike"], x[1]["rekke"], x[1]["klasse"]))

    for i, Art_details in sorted_firebaseArter:
        Art = {
            "norsk_navn": Art_details.get("norsk_navn", ""),
            "latinsk_navn": Art_details.get("latinsk_navn", ""),
            "bilde": Art_details.get("bilde", ""),
            "rike": Art_details.get("rike", ""),
            "rekke": Art_details.get("rekke", ""),
            "klasse": Art_details.get("klasse", ""),
            "orden": Art_details.get("orden", ""),
            "familie": Art_details.get("familie", ""),
            "slekt": Art_details.get("slekt", ""),
            "dato": Art_details.get("dato", ""),
            "tekst": Art_details.get("tekst", "")
            }
        alleArter.append(Art)
    return render_template('arter.html', arter=alleArter)

@app.route('/nyart', methods=['GET', 'POST']) # admin siden
def nytur():
    if request.method == 'POST':
        try:
            bilde = request.files['bilde']
            bilde_data = bilde.read()
            bilde_base64 = base64.b64encode(bilde_data).decode('utf-8')#gjør bildet om til tekst
            
            norsk_navn = request.form["norsk_navn"]
            latinsk_navn = request.form["latinsk_navn"]
            rike = request.form["rike"]
            rekke = request.form["rekke"]
            klasse = request.form["klasse"]
            orden = request.form["orden"]
            familie = request.form["familie"]
            slekt = request.form["slekt"]
            dato = request.form["dato"]
            tekst = request.form["tekst"]

            ArtData = { # setter den inn i en variabel
                "bilde": bilde_base64,
                "norsk_navn":  norsk_navn,
                "latinsk_navnnavn": latinsk_navn,
                "rike": rike,
                "rekke": rekke,
                "klasse": klasse,
                "orden": orden,
                "familie": familie,
                "slekt": slekt,
                "dato": dato,
                "tekst": tekst
            }
            ref.push(ArtData) # pusher inn i databasen
            return redirect('/')
        except Exception as e:
            app.logger.error("Error, kan ikke lagre art: %s", e)
            return "Det oppstod en feil ved lagring av arten" #hvis det oppstår en feil
    elif request.method == 'GET':
        return render_template('nyart.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
