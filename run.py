import json
from flask import Flask, render_template

app = Flask(__name__)

        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pictures')
def pictures():
        return {'nb_ppl' : nb_ppl, 
                'nb_man' : nb_man, 
                'nb_women' : nb_women, 
                'average_age_man' : average_age_man, 
                'average_age_women' : average_age_women, 
                'average_age' : average_age, 
                'ages_man' : ages_man, 
                'ages_women' : ages_women, 
                'ages' : ages,
                'emotions' : emotions}

if __name__ == "__main__":
    
    nb_man = 0
    nb_women = 0
    nb_ppl = 0
    ages_man = []
    ages_women = []
    emotions = []
    #Indiquer tous les fichiers json utilisés
    #Attention, peut demander le chemin absolu en fonction des machines [r"pathcomplet"]
    name_files = ["picture1.json", "picture2.json", "picture3.json", 'picture4.json']

    for i in range(len(name_files)):
        file = open(name_files[i])
        data = json.load(file)

        for face in data['response']['faces']:
            if face['gender'] == 'male':
                nb_man += 1
                ages_man.append(int(face['age']))
                emotions.append(face['emotions'])
            else:
                nb_women += 1
                ages_women.append(int(face['age']))
                emotions.append(face['emotions'])

        nb_ppl += data['response']['face_count']

    average_age_man = sum(ages_man) / nb_man
    average_age_women = sum(ages_women) / nb_women
    average_age = (average_age_man + average_age_women) / 2
    ages = ages_women + ages_man

    app.run(debug=True)