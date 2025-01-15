import firebase_admin
from firebase_admin import credentials, db, firestore, initialize_app, storage
from flask import Flask, redirect, url_for, render_template, request

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://biotopsamling-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference('/')

db = firestore.client()

collection_ref = db.collection('/')
query = collection_ref.where('rekke', '==', 'Stilksporesopper')
results = query.stream()
for doc in results:
    print(f'{doc.id} => {doc.to_dict()}')

arter = [
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Risker er skivesopper, de er spesiell fordi de produserer melkesaft som kan ha forskjellige farger som oransje, gul eller fiolett, men som oftest så er de hvit. Når melkesaften utsettes for luft så endrer den ofte farge. Det finnes mer enn 70 arter i Norge, og flere av de danner sopprot med spesifikke trær."},
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Korsedderkoppen er 7 til 20 mm lang og hunnen er vesentlig større enn hannen. Den har fem hvite flekker på bakkroppen som former et kors, hvorav navnet korsedderkopp. En korsedderkopp legger hundrevis av egg på høsten, og ungene overvintrer to ganger før de er kjønnsmodne."},
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Korsedderkoppen er 7 til 20 mm lang og hunnen er vesentlig større enn hannen. Den har fem hvite flekker på bakkroppen som former et kors, hvorav navnet korsedderkopp. En korsedderkopp legger hundrevis av egg på høsten, og ungene overvintrer to ganger før de er kjønnsmodne."},
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Korsedderkoppen er 7 til 20 mm lang og hunnen er vesentlig større enn hannen. Den har fem hvite flekker på bakkroppen som former et kors, hvorav navnet korsedderkopp. En korsedderkopp legger hundrevis av egg på høsten, og ungene overvintrer to ganger før de er kjønnsmodne."},
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Korsedderkoppen er 7 til 20 mm lang og hunnen er vesentlig større enn hannen. Den har fem hvite flekker på bakkroppen som former et kors, hvorav navnet korsedderkopp. En korsedderkopp legger hundrevis av egg på høsten, og ungene overvintrer to ganger før de er kjønnsmodne."},
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Korsedderkoppen er 7 til 20 mm lang og hunnen er vesentlig større enn hannen. Den har fem hvite flekker på bakkroppen som former et kors, hvorav navnet korsedderkopp. En korsedderkopp legger hundrevis av egg på høsten, og ungene overvintrer to ganger før de er kjønnsmodne."},
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Korsedderkoppen er 7 til 20 mm lang og hunnen er vesentlig større enn hannen. Den har fem hvite flekker på bakkroppen som former et kors, hvorav navnet korsedderkopp. En korsedderkopp legger hundrevis av egg på høsten, og ungene overvintrer to ganger før de er kjønnsmodne."},
    {"norsk_navn": "Korsedderkopp", "latinsk_navn": "Araneus diadematus", "bilde": "bilde", "rike": "Dyreriket", "rekke": "Leddyr", "klasse": "Edderkoppdyr", "orden": "Edderkopper", "familie": "Hjulspinnere", "slekt": "Araneus", "dato": "07.09.2024", "tekst": "Korsedderkoppen er 7 til 20 mm lang og hunnen er vesentlig større enn hannen. Den har fem hvite flekker på bakkroppen som former et kors, hvorav navnet korsedderkopp. En korsedderkopp legger hundrevis av egg på høsten, og ungene overvintrer to ganger før de er kjønnsmodne."},
]

#for art in arter:
#    ref.push(art)

#print("Artene er lagt til.")

#db.reference().delete()