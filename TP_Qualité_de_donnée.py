import pandas as pd
import random
from datetime import datetime, timedelta

num_lines = 10

names = ['Samba', 'Oumou', 'Awa', 'Mansour', 'Cylia']
first_names = ['Thiam', 'Diop', 'Sy', 'Faye', 'Niang']
addresses = ['rue de la Paix', 'avenue des Champs', 'boulevard de la République']
cantons = ['Sénégal', 'Maroc', 'Algérie', 'Cameroun', 'France']
insurances = ['Zurich', 'Generali', 'AXA', 'Allianz', 'TSC']

def generate_random_date(start_year=1950, end_year=2000):
    start_date = datetime(year=start_year, month=1, day=1)
    end_date = datetime(year=end_year, month=12, day=31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date

def standardize_canton(canton):
    canton_mapping = {
        'Sénégal': 'SN',
        'France': 'FR',
        'Cameroun': 'CM',
        'Maroc': 'MA',
        'Algérie': 'DZ'
    }
    return canton_mapping.get(canton, canton)

data = []

for _ in range(num_lines):
    birth_date = generate_random_date()
    assured_since_date = birth_date + timedelta(days=random.randint(18 * 365, 40 * 365))
    permis_id = random.randint(100000, 999999)
    nom = random.choice(names)
    prenom = random.choice(first_names)
    adresse = f"{random.randint(1, 100)} {random.choice(addresses)}"
    canton = standardize_canton(random.choice(cantons))
    assurance = random.choice(insurances)

    data.append({
        'Permis ID': permis_id,
        'Nom': nom,
        'Prénom': prenom,
        'Date naiss.': birth_date.strftime('%d/%m/%Y'),
        'Adresse': adresse,
        'Canton': canton,
        'Assurance': assurance,
        'Assuré depuis': assured_since_date.strftime('%d/%m/%Y')
    })

df = pd.DataFrame(data)
df = df.drop_duplicates(subset=['Permis ID'])
output_filename = '/Users/mac/documents/assurance_data.xlsx'  # Ajustez le chemin selon votre système et vos préférences
df.to_excel(output_filename, index=False)
