# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#
import json


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def from_json_data(data):
        choix = [i[0] for i in data["choix"]]
        data_bonne_reponse = [i[0] for i in data["choix"] if i[1]]
        if len(data_bonne_reponse) != 1:
            return None
        q = Question(data["titre"], choix, data_bonne_reponse[0] )
        return q

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        print(self.choix[reponse_int-1])
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions, categorie, titre, difficulte):
        self.questions = questions
        self.categorie = categorie
        self.titre = titre
        self.difficulte = difficulte

    def from_json_data(data):
        questionnaire_data_questions = data["questions"]
        questions = [Question.from_json_data(i) for i in questionnaire_data_questions]
        return Questionnaire(questions, data["categorie"], data["titre"], data["difficulte"])
    def lancer(self):
        score = 0
        print("------")
        print("QUESTIONNAIRE : " + self.titre)
        print("  Catégorie : " + self.categorie)
        print("  Difficulte : " + self.difficulte)
        print("  Nombre de question : " + str(len(self.questions)))
        print("------")
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


filename = 'cinema_starwars_confirme.json' #input("Veuillez saisir le nom du fichier a utiliser:")

try:
 file = open(filename)
 file_data = file.read()
 file.close()
except:
    print("erreur de ficher")
else:
    questionnaire_data = json.loads(file_data)
    Questionnaire.from_json_data(questionnaire_data).lancer()

'''
    for item in questionnaire_data['questions']:
        for i in item['choix']:
            if i[1]:
                bonne_reponse = i[0]
        Questionnaire(
            (
                Question(item['titre'], item['choix'], bonne_reponse),
                Question(item['titre'], item['choix'], bonne_reponse)
            )
        ).lancer()
'''



