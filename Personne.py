class Personne():
    firstname: str
    lastname: str
    phone: str | None
    email: str | None

    def __init__(self, firstname, lastname, email, phone) -> None:
        print('Welcome {}'.format(firstname))
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone

    def afficher(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone": self.phone,
            "email": self.email
        }

class Menu():
  is_open: False

  def __init__(self) -> None:
    self.is_open = False

  def get_contacts(self) -> list[Personne]:
    data = {}
    with open('./carnet.json', 'r') as f:
      data = json.load(f)
      return data

  def register_contact(self, personne: Personne, filename='carnet.json'):
      with open(filename,'r+') as file:
          file_data = json.load(file)
          file_data["contacts"] = {}
          file_data["contacts"].append(personne.afficher())
          file.seek(0)
          json.dump(file_data, file, indent = 4)


  def creer_personne(self) -> None:
    firstname = str(input('Veuillez entrer un prenom: '))
    lastname = str(input('Veuillez entrer un nom: '))
    email = str(input('Veuillez entrer une adresse mail (optionnel): '))
    if email == '':
      email = None
    phone = str(input('Veuillez entrer votre numéro de téléphone (optionnel): '))
    if phone == '':
      phone = None
    new_personne = Personne(firstname, lastname, email, phone)
    self.register_contact(new_personne)

menu = Menu()
menu.creer_personne()
menu.get_contacts()