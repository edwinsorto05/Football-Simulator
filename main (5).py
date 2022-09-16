
#import modules: random, time, and os
import random
import time
import os

#text colors and background colors
redc = "\033[0;91m"
yellowc = "\033[0;93m"
green = "\033[0;92m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
white = "\033[0;97m"
blue_back = "\033[0;44m"
grey_back = "\033[0;40m"

#class function
#https://towardsdatascience.com/enhance-your-python-project-code-with-classes-5a19d0e9f841
#Team() gives the ratings for each team selected
class Team:
  def __init__(self, name, score, goaldif, goals, attack, defense, luck, speed, stamina, player):
    self.name = name
    self.score = score
    self.goaldif = goaldif
    self.goals = goals
    self.attack = attack
    self.defense = defense
    self.luck = luck
    self.speed = speed
    
    self.stamina = stamina
    self.red = False
    self.player = player

#welcomes user and presents menu with leagues to select from
while True:
  print(blue_back + "Welcome to Football Simulator! ⚽")
  print(blue + "Press ENTER to continue:")
  input()
  print(blue + "\n Select a league: (select a number)")
  print(yellowc + "  1. Premier League (England)")
  print(yellowc + "  2. Serie A (Italy)")
  print(yellowc + "  3. LaLiga (Spain)")
  print(yellowc + "  4. Bundesliga (Germany)")
  print(yellowc + "  5. Ligue 1 (France)")
  print(yellowc + "  6. MLS (USA)")
  print(yellowc + "  7. UCL Finals (Europe)")
  print(yellowc + "  8. Custom match")
  #takes input from user
  league = input("> " + white)
  #clears menu and will go to whichever league the user selects
  os.system("clear")

  #user selects premier league
  if league == "1" or league == "Premier League":
    print(magenta + "Choose your matchup: (select a number)")
    print(green + "  1. Manchester United vs. Manchester City")
    print(green + "  2. Tottenham vs. Arsenal")
    print(green + "  3. Chelsea vs. Liverpool")
    premierleague = input("> ")
    print(white + "")
    #user selects a matchup from the premier league
    if premierleague == '1' or premierleague == 'Manchester United vs. Manchester City':
      #Manchester United stats and lineup
      team1 = Team('Manchester United', 0, 0, 0, 85, 85, 85, 85, 85, ['David de Gea', 'Alex Telles', 'Harry Maguire', 'Raphaël Varane', 'Diego Dalot', 'Casemiro', 'Fred', 'Jadon Sancho', 'Bruno Fernandes', 'Marcus Rashford', 'Cristiano Ronaldo'])
      #Manchester City stats and lineup
      team2 = Team('Manchester City', 0, 0, 0, 88, 88, 88, 88, 88, ['Ederson', 'Sergio Gómez', 'Rúben Dias', 'John Stones', 'João Cancelo', 'Bernardo Silva', 'Rodri', 'Kevin De Bruyne', 'Phil Foden', 'Erling Haaland', 'Riyad Mahrez'])
      break
    elif premierleague == '2' or premierleague == 'Tottenham vs. Arsenal':
      #Tottenham stats and lineup
      team1 = Team('Tottenham', 0, 0, 0, 84, 84, 84, 84, 84, ['Hugo Lloris', 'Ben Davies', 'Eric Dier', 'Cristian Romero', 'Ivan Perišić', 'Pierre-Emile Højbjerg', 'Rodrigo Bentancur', 'Emerson', 'Heung-min Son', 'Dejan Kulusevski', 'Harry Kane'])
      #Arsenal stats and lineup
      team2 = Team('Arsenal', 0, 0, 0, 85, 85, 85, 85, 85, ['Aaron Ramsdale', 'Oleksandr Zinchenko', 'Gabriel', 'William Saliba', 'Ben White', 'Granit Xhaka', 'Thomas Partey', 'Gabriel Martinelli', 'Martin Ødegaard', 'Bukayo Saka', 'Gabriel Jesus'])
      break
    elif premierleague == '3'or premierleague == 'Chelsea vs. Liverpool':
      #Chelsea stats and lineup
      team1 = Team('Chelsea', 0, 0, 0, 87, 87, 87, 87, 87, ['Edouard Mendy', 'Marc Cucurella', 'Thiago Silva', 'César Azpilicueta', 'Raheem Sterling', 'Mateo Kovačić', 'Jorginho', "N'Golo Kanté", 'Mason Mount', 'Christian Pulisic', 'Kai Havertz'])
      #Liverpool stats and lineup
      team2 = Team('Liverpool', 0, 0, 0, 88, 88, 88, 88, 88, ['Alisson', 'Andy Robertson', 'Virgil van Dijk', 'Joel Matip', 'Trent Alexander-Arnold', 'Thiago Alcântara', 'Fabinho', "Jordan Henderson", 'Luis Díaz', 'Diogo Jota', 'Mohamed Salah'])
      break
    else:
      #if user inputs anything other than '1', '2', or '3', the screen is cleared and user can return to menu
      os.system("clear")

  #user selects serie a
  elif league == "2" or league == "Serie A":
    print(magenta + "Choose your matchup: (select a number)")
    print(green + "  1. Inter Milan vs. AC Milan")
    print(green + "  2. Juventus vs. Roma")
    print(green + "  3. Napoli vs. Juventus")
    seriea = input("> ")
    print(white + "")
    #user selects a matchup from the premier league
    if seriea == '1'or seriea == 'Inter Milan vs. AC Milan':
      #Inter Milan stats and lineup
      team1 = Team('Inter Milan', 0, 0, 0, 87, 87, 87, 87, 87, ['Samir Handanovič', 'Alessandro Bastoni', 'Milan Škriniar', "Danilo D'Ambrosio", 'Ivan Perišić', 'Arturo Vidal', 'Hakan Çalhanoğlu', "Nicolò Barella", 'Denzel Dumfries', 'Lautaro Martínez', 'Edin Džeko'])
      #AC Milan stats and lineup
      team2 = Team('AC Milan', 0, 0, 0, 86, 86, 86, 86, 86, ['Mike Maignan', 'Theo Hernández', 'Fikayo Tomori', "Pierre Kalulu", 'Davide Calabria', 'Franck Kessié', 'Ismaël Bennacer', 'Rafael Leão', 'Brahim Díaz', 'Junior Messias', 'Olivier Giroud'])
      break
    elif seriea == '2' or seriea == 'Juventus vs. Roma':
      #Juventus stats and lineup
      team1 = Team('Juventus', 0, 0, 0, 86, 86, 86, 86, 86, ['Wojciech Szczęsny', 'Daniele Rugani', 'Matthijs de Ligt', 'Danilo', 'Mattia De Sciglio', 'Adrien Rabiot', 'Arthur', 'Manuel Locatelli', 'Juan Cuadrado', 'Paulo Dybala', 'Dušan Vlahović'])
      #Roma stats and lineup
      team2 = Team('Roma', 0, 0, 0, 84, 84, 84, 84, 84, ['Rui Patrício', 'Robert Ibáñez', 'Chris Smalling', 'Gianluca Mancini', 'Nicola Zalewski', 'Sérgio Oliveira', 'Bryan Cristante', 'Rick Karsdorp', 'Henrikh Mkhitaryan', 'Lorenzo Pellegrini', 'Tammy Abraham'])
      break
    elif seriea == '3' or seriea == 'Napoli vs. Juventus':
      #Napoli stats and lineup
      team1 = Team('Napoli', 0, 0, 0, 84, 84, 84, 84, 84, ['David Ospina', 'Mário Rui', 'Kalidou Koulibaly', 'Amir Rrahmani', 'Giovanni Di Lorenzo', 'Stanislav Lobotka', 'Fabián Ruiz', 'Lorenzo Insigne', 'Piotr Zieliński', 'Matteo Politano', 'Victor Osimhen'])
      #Juventus stats and lineup
      team2 = Team('Juventus', 0, 0, 0, 86, 86, 86, 86, 86, ['Wojciech Szczęsny', 'Daniele Rugani', 'Matthijs de Ligt', 'Danilo', 'Mattia De Sciglio', 'Adrien Rabiot', 'Weston McKennie', 'Manuel Locatelli', 'Juan Cuadrado', 'Paulo Dybala', 'Dušan Vlahović'])
      break
    else:
      #if user inputs anything other than '1', '2', or '3', the screen is cleared and user can return to menu
      os.system("clear")

  #user selects laliga
  elif league == "3" or league == "LaLiga":
    print(magenta + "Choose your matchup: (select a number)")
    print(green + "  1. Real Madrid vs. Barcelona")
    print(green + "  2. Atlético Madrid vs Real Madrid")
    print(green + "  3. Barcelona vs. Atlético Madrid")
    laliga = input("> ")
    print(white + "")
    #user selects a matchup from laliga
    if laliga == '1' or laliga == 'Real Madrid vs. Barcelona':
      #Real Madrid stats and lineup
      team1 = Team('Real Madrid', 0, 0, 0, 89, 89, 89, 89, 89, ['Thibaut Courtois', 'Ferland Mendy', 'David Alaba', 'Éder Militão', 'Dani Carvajal', 'Federico Valverde', 'Aurélien Tchouaméni', 'Luka Modrić', 'Vini Jr.', 'Karim Benzema', 'Rodrygo'])
      #Barcelona stats and lineup
      team2 = Team('Barcelona', 0, 0, 0, 88, 88, 88, 88, 88, ['Marc-André ter Stegen', 'Jordi Alba', 'Eric García', 'Ronald Araújo', 'Jules Koundé', 'Pedri', 'Sergio Busquets', 'Frenkie de Jong', 'Raphinha', 'Robert Lewandowski', 'Ousmane Dembélé'])
      break
    elif laliga == '2' or laliga == 'Atlético Madrid vs Real Madrid':
      #Atlético Madrid stats and lineup
      team1 = Team('Atlético Madrid', 0, 0, 0, 87, 87, 87, 87, 87, ['Jan Oblak', 'Reinildo Mandava', 'José María Giménez', 'Stefan Savić', 'Renan Lodi', 'Thomas Lemar', 'Koke', 'Rodrigo De Paul', 'Marcos Llorente', 'João Félix', 'Antoine Griezmann'])
      #Real Madrid stats and lineup
      team2 = Team('Real Madrid', 0, 0, 0, 89, 89, 89, 89, 89, ['Thibaut Courtois', 'Ferland Mendy', 'David Alaba', 'Éder Militão', 'Dani Carvajal', 'Toni Kroos', 'Aurélien Tchouaméni', 'Luka Modrić', 'Vini Jr.', 'Karim Benzema', 'Marco Asensio'])
      break
    elif laliga == '3' or laliga == 'Barcelona vs. Atlético Madrid':
      #Barcelona stats and lineup
      team1 = Team('Barcelona', 0, 0, 0, 88, 88, 88, 88, 88, ['Marc-André ter Stegen', 'Jordi Alba', 'Ronald Araújo', 'Gerard Piqué', 'Dani Alves', 'Pedri', 'Sergio Busquets', 'Frenkie de Jong', 'Gavi', 'Ferran Torres', 'Adama Traoré'])
      #Atlético Madrid stats and lineup
      team2 = Team('Atlético Madrid', 0, 0, 0, 87, 87, 87, 87, 87, ['Jan Oblak', 'Mario Hermoso', 'José María Giménez', 'Stefan Savić', 'Šime Vrsaljko', 'Thomas Lemar', 'Koke', 'Rodrigo De Paul', 'João Félix', 'Luis Suárez', 'Yannick Carrasco'])
      break
    else:
      #if user inputs anything other than '1', '2', or '3', the screen is cleared and user can return to menu
      os.system("clear")

  #user selects bundesliga
  elif league == "4" or league == "Bundesliga":
    print(magenta + "Choose your matchup: (select a number)")
    print(green + " 1. Bayern Munich vs. Borussia Dortmund")
    print(green + " 2. Borussia Dortmund vs. RB Leipzig")
    print(green + " 3. RB Leipzig vs. Bayern Munich")
    bundesliga = input("> ")
    print(white + "")
    #user selects a matchup from bundesliga
    if bundesliga == '1' or bundesliga == 'Bayern Munich vs. Borussia Dortmund':
      #Bayern Munich stats and lineup
      team1 = Team('Bayern Munich', 0, 0, 0, 90, 90, 90, 90, 90, ['Manuel Neuer', 'Lucas Hernandez', 'Niklas Süle', 'Benjamin Pavard', 'Leon Goretzka', 'Joshua Kimmich', 'Kingsley Coman', 'Leroy Sané', 'Thomas Müller', 'Serge Gnabry', 'Sadio Mané'])
      #Borussia Dortmund stats and lineup
      team2 = Team('Borussia Dortmund', 0, 0, 0, 87, 87, 87, 87, 87, ['Gregor Kobel', 'Raphaël Guerreiro', 'Manuel Akanji', 'Emre Can', 'Felix Passlack', 'Axel Witsel', 'Thorgan Hazard', 'Jude Bellingham', 'Giovanni Reyna', 'Marius Wolf', 'Erling Haaland'])
      break
    elif bundesliga == '2' or bundesliga == 'Borussia Dortmund vs. RB Leipzig':
      #Borussia Dortmund stats and lineup
      team1 = Team('Borussia Dortmund', 0, 0, 0, 87, 87, 87, 87, 87, ['Gregor Kobel', 'Raphaël Guerreiro', 'Manuel Akanji', 'Emre Can', 'Felix Passlack', 'Axel Witsel', 'Thorgan Hazard', 'Jude Bellingham', 'Giovanni Reyna', 'Marius Wolf', 'Erling Haaland'])
      #RB Leipzig stats and lineup
      team2 = Team('RB Leipzig', 0, 0, 0, 87, 87, 87, 87, 87, ['Péter Gulácsi', 'Joško Gvardiol', 'Willi Orbán', 'Mohamed Simakan', 'Angeliño', 'Kevin Kampl', 'Dominik Szoboszlai', 'Benjamin Henrichs', 'Dani Olmo', 'André Silva', 'Christopher Nkunku'])
      break
    elif bundesliga == '3' or bundesliga == 'RB Leipzig vs. Bayern Munich':
      #RB Leipzig stats and lineup
      team1 = Team('RB Leipzig', 0, 0, 0, 87, 87, 87, 87, 87, ['Péter Gulácsi', 'Joško Gvardiol', 'Willi Orbán', 'Mohamed Simakan', 'Angeliño', 'Kevin Kampl', 'Konrad Laimer', 'Dominik Szoboszlai', 'Dani Olmo', 'André Silva', 'Christopher Nkunku'])
      #Bayern Munich stats and lineup
      team2 = Team('Bayern Munich', 0, 0, 0, 90, 90, 90, 90, 90, ['Manuel Neuer', 'Lucas Hernandez', 'Dayot Upamecano', 'Benjamin Pavard', 'Jamal Musiala', 'Joshua Kimmich', 'Kingsley Coman', 'Leroy Sané', 'Thomas Müller', 'Serge Gnabry', 'Robert Lewandowski'])
      break
    else:
      #if user inputs anything other than '1', '2', or '3', the screen is cleared and user can return to menu
      os.system("clear")

  #user selects ligue 1
  elif league == "5" or league == "Ligue 1":
    print(magenta + "Choose your matchup: (select a number)")
    print(green + "  1. PSG vs. Lyon")
    print(green + "  2. Marseille vs. PSG")
    print(green + "  3. Lyon vs. Monaco")
    ligue1 = input("> ")
    print(white + "")
    #user selects a matchup from ligue 1
    if ligue1 == '1' or ligue1 == 'PSG vs. Lyon':
      #PSG stats and lineup
      team1 = Team('PSG', 0, 0, 0, 87, 87, 87, 87, 87, ['Keylor Navas', 'Nuno Mendes', 'Presnel Kimpembe', 'Marquinhos', 'Achraf Hakimi', 'Marco Verratti', 'Danilo Pereira', 'Leandro Paredes', 'Kylian Mbappé', 'Neymar', 'Lionel Messi'])
      #Lyon stats and lineup
      team2 = Team('Lyon', 0, 0, 0, 83, 83, 83, 83, 83, ['Anthony Lopes', 'Emerson', 'Castello Lukeba', 'Thiago Mendes', 'Léo Dubois', 'Tanguy Ndombele', 'Maxence Caqueret', 'Karl Toko Ekambi', 'Lucas Paquetá', 'Romain Faivre', 'Moussa Dembélé'])
      break
    elif ligue1 == '2' or ligue1 == 'Marseille vs. PSG':
      #Marseille stats and lineup
      team1 = Team('Marseille', 0, 0, 0, 82, 82, 82, 82, 82, ['Steve Mandanda', 'Luan Peres', 'Duje Ćaleta-Car', 'William Saliba', 'Pol Lirola', 'Pape Gueye', 'Valentin Rongier', 'Amine Harit', 'Mattéo Guendouzi', 'Cengiz Ünder', 'Cédric Bakambu'])
      #PSG stats and lineup
      team2 = Team('PSG', 0, 0, 0, 87, 87, 87, 87, 87, ['Keylor Navas', 'Nuno Mendes', 'Presnel Kimpembe', 'Marquinhos', 'Achraf Hakimi', 'Marco Verratti', 'Idrissa Gueye', 'Leandro Paredes', 'Kylian Mbappé', 'Neymar', 'Lionel Messi'])
      break
    elif ligue1 == '3' or ligue1 == 'Lyon vs. Monaco':
      #Lyon stats and lineup
      team1 = Team('Lyon', 0, 0, 0, 83, 83, 83, 83, 83, ['Anthony Lopes', 'Emerson', 'Castello Lukeba', 'Thiago Mendes', 'Léo Dubois', 'Tanguy Ndombele', 'Maxence Caqueret', 'Karl Toko Ekambi', 'Lucas Paquetá', 'Romain Faivre', 'Moussa Dembélé'])
      #AS Monaco stats and lineup
      team2 = Team('Monaco', 0, 0, 0, 83, 83, 83, 83, 83, ['Alexander Nübel', 'Caio Henrique', 'Benoît Badiashile', 'Axel Disasi', 'Ruben Aguilar', 'Aurélien Tchouaméni', 'Aleksandr Golovin', 'Jean Lucas', 'Youssouf Fofana', 'Gelson Martins', 'Wissam Ben Yedder'])
      break
    else:
      #if user inputs anything other than '1', '2', or '3', the screen is cleared and user can return to menu
      os.system("clear")

  #user selects MLS
  elif league == "6" or league == "MLS":
    print(magenta + "Choose your matchup: (select a number)")
    print(green + "  1. New England Revolution vs. New York Red Bulls")
    print(green + "  2. LAFC vs. LA Galaxy")
    print(green + "  3. CF Montréal vs. Toronto FC")
    mls = input("> ")
    print(white + "")
    #user selects a matchup from the MLS
    if mls == '1' or mls == 'New England Revolution vs. New York Red Bulls':
      #New England Revolution stats and lineup
      team1 = Team('New England Revolution', 0, 0, 0, 77, 77, 77, 77, 77, ['Matt Turner', 'DeJuan Jones', 'Henry Kessler', 'Andrew Farrell', 'Brandon Bye', 'Matt Polster', 'Tommy McNamara', 'Sebastian Lletget', 'Carles Gil', 'Gustavo Bou', 'Adam Buksa'])
      #New York Red Bulls stats and lineup
      team2 = Team('New York Red Bulls', 0, 0, 0, 75, 75, 75, 75, 75, ['Carlos Miguel Coronel', 'Aaron Long', 'Sean Nealis', 'Tom Edwards', 'John Tolkin', 'Dru Yearwood', 'Frankie Amaya', 'Lewis Morgan', 'O.G.F. Mosso', 'Patryk Klimala', 'Tom Barlow'])
      break
    elif mls == '2' or mls == 'LAFC vs. LA Galaxy':
      #LAFC stats and lineup
      team1 = Team('LAFC', 0, 0, 0, 76, 76, 76, 76, 76, ['Maxime Crépeau', 'Diego Palacios', 'Mamadou Fall', 'Jesús Murillo', 'Ryan Hollingshead', 'Francisco Ginella', 'Ilie Sánchez', 'Letif Blessing', 'Brian Rodríguez', 'Cristian Arango', 'Carlos Vela'])
      #LA Galaxy stats and lineup
      team2 = Team('LA Galaxy', 0, 0, 0, 75, 75, 75, 75, 75, ['Jonathan Bond', 'Raheem Edwards', 'Derrick Williams', 'Nick DePuy', 'Kelvin Leerdam', 'Samuel Grandsir', 'Marco Delgado', 'Rayan Reveloson', 'Kévin Cabral', 'Efraín Álvarez', 'Javier Hernández'])
      break
    elif mls == '3' or mls == 'CF Montréal vs. Toronto FC':
      #CF Montréal stats and lineup
      team1 = Team('CF Montréal', 0, 0, 0, 75, 75, 75, 75, 75, ['Sebastian Breza', 'Kamal Miller', 'Rudy Camacho', 'Joel Waterman', 'Lassi Lappalainen', 'Victor Wanyama', 'Ismaël Koné', 'Alistair Johnston', 'Đorđe Mihailović', 'Joaquin Torres', 'Romell Quioto'])
      #Toronto FC stats and lineup
      team2 = Team('Toronto FC', 0, 0, 0, 74, 74, 74, 74, 74, ['Alex Bono', "Shane O'Neill", 'Carlos Salcedo', 'Lukas MacNaughton', 'Jacob Shaffelburg', 'Jonathan Osorio', 'Michael Bradley', 'Kosi Thompson', 'Luca Petrasso', 'Alejandro Pozuelo', 'Jesús Jiménez'])
      break
    else:
      #if user inputs anything other than '1', '2', or '3', the screen is cleared and user can return to menu
      os.system("clear")

  #user selects UCL Finals
  elif league == "7" or league == "UCL Finals":
    print(magenta + "Choose your matchup: (select a number)")
    print(green + "  1. Manchester City vs. Chelsea (2021)")
    print(green + "  2. PSG vs. Bayern Munich (2020)")
    print(green + "  3. Tottenham vs. Liverpool (2019)")
    print(green + "  4. Real Madrid vs. Liverpool (2018)")
    print(green + "  5. Juventus vs. Real Madrid (2017)")
    print(green + "  6. Real Madrid vs. Atlético Madrid (2016)")
    print(green + "  7. Juventus vs. Barcelona (2015)")
    uclfinals = input("> ")
    print(white + "")
    #user selects a matchup from UCL Finals
    if uclfinals == '1' or uclfinals == 'Manchester City vs. Chelsea':
      #Manchester City stats and lineup
      team1 = Team('Manchester City', 0, 0, 0, 89, 89, 89, 89, 89, ['Ederson', 'Oleksandr Zinchenko', 'Rúben Dias', 'John Stones', 'Kyle Walker', 'Phil Foden', 'İlkay Gündoğan', 'Bernardo Silva', 'Raheem Sterling', 'Kevin De Bruyne', 'Riyad Mahrez'])
      #Chelsea stats and lineup
      team2 = Team('Chelsea', 0, 0, 0, 88, 88, 88, 88, 88, ['Edouard Mendy', 'Antonio Rüdiger', 'Thiago Silva', 'César Azpilicueta', 'Ben Chilwell', 'Jorginho', "N'Golo Kanté", 'Reece James', 'Mason Mount', 'Kai Havertz', 'Timo Werner'])
      break
    elif uclfinals == '2' or uclfinals == 'PSG vs. Bayern Munich':
      #PSG stats and lineup
      team1 = Team('PSG', 0, 0, 0, 88, 88, 88, 88, 88, ['Keylor Navas', 'Juan Bernat', 'Presnel Kimpembe', 'Thiago Silva', 'Thilo Kehrer', 'Leandro Paredes', 'Marquinhos', 'Ander Herrera', 'Kylian Mbappé', 'Neymar', 'Ángel Di María'])
      #Bayern Munich stats and lineup
      team2 = Team('Bayern Munich', 0, 0, 0, 90, 90, 90, 90, 90, ['Manuel Neuer', 'Alphonso Davies', 'David Alaba', 'Jerome Boateng', 'Joshua Kimmich', 'Thiago Alcântara', 'Leon Goretzka', 'Kinglsey Coman', 'Thomas Müller', 'Serge Gnabry', 'Robert Lewandowski'])
      break
    elif uclfinals == '3' or uclfinals == 'Tottenham vs. Liverpool':
      #Tottenham stats and lineup
      team1 = Team('Tottenham', 0, 0, 0, 88, 88, 88, 88, 88, ['Hugo Lloris', 'Danny Rose', 'Jan Vertonghen', 'Toby Alderweireld', 'Kieran Trippier', 'Harry Winks', 'Moussa Sissoko', 'Heung-min Son', 'Dele Alli', 'Christian Eriksen', 'Harry Kane'])
      #Liverpool stats and lineup
      team2 = Team('Liverpool', 0, 0, 0, 89, 89, 89, 89, 89, ['Alisson', "Andy Robertson", 'Virgil van Dijk', 'Joel Matip', 'Trent Alexander-Arnold', 'Georginio Wijnaldum', 'Fabinho', 'Jordan Henderson', 'Sadio Mané', 'Roberto Firmino', 'Mohamed Salah'])
      break
    elif uclfinals == '4' or uclfinals == 'Real Madrid vs. Liverpool':
      #Real Madrid stats and lineup
      team1 = Team('Real Madrid', 0, 0, 0, 89, 89, 89, 89, 89, ['Keylor Navas', 'Marcelo', 'Sergio Ramos', 'Raphaël Varane', 'Dani Carvajal', 'Toni Kroos', 'Casemiro', 'Luka Modrić', 'Gareth Bale', 'Cristiano Ronaldo', 'Karim Benzema'])
      #Liverpool stats and lineup
      team2 = Team('Liverpool', 0, 0, 0, 88, 88, 88, 88, 88, ['Loris Karius', 'Andy Robertson', 'Virgil van Dijk', 'Dejan Lovren', 'Trent Alexander-Arnold', 'James Milner', 'Jordan Henderson', 'Georginio Wijnaldum', 'Sadio Mané', 'Roberto Firmino', 'Mohamed Salah'])
      break
    elif uclfinals == '5' or uclfinals == 'Juventus vs. Real Madrid':
      #Juventus stats and lineup
      team1 = Team('Juventus', 0, 0, 0, 87, 87, 87, 87, 87, ['Gianluigi Buffon', 'Alex Sandro', 'Giorgio Chiellini', 'Leonardo Bonucci', 'Andrea Barzagli', 'Sami Khedira', 'Miralem Pjanić', 'Mario Mandžukić', 'Paulo Dybala', 'Dani Alves', 'Gonzalo Higuaín'])
      #Real Madrid stats and lineup
      team2 = Team('Real Madrid', 0, 0, 0, 90, 90, 90, 90, 90, ['Keylor Navas', 'Marcelo', 'Sergio Ramos', 'Raphaël Varane', 'Dani Carvajal', 'Toni Kroos', 'Casemiro', 'Luka Modrić', 'Gareth Bale', 'Cristiano Ronaldo', 'Karim Benzema'])
      break
    elif uclfinals == '6' or uclfinals == 'Real Madrid vs. Atlético Madrid':
      #Real Madrid stats and lineup
      team1 = Team('Real Madrid', 0, 0, 0, 89, 89, 89, 89, 89, ['Keylor Navas', 'Marcelo', 'Sergio Ramos', 'Raphaël Varane', 'Dani Carvajal', 'Toni Kroos', 'Casemiro', 'Luka Modrić', 'Cristiano Ronaldo', 'Karim Benzema', 'Gareth Bale'])
      #Atlético Madrid stats and lineup
      team2 = Team('Atlético Madrid', 0, 0, 0, 87, 87, 87, 87, 89, ['Jan Oblak', 'Filipe Luís', 'Diego Godín', 'Stefan Savić', 'Juanfran', 'Koke', 'Augusto Fernández', 'Gabi', 'Saúl', 'Antoine Griezmann', 'Fernando Torres'])
      break
    elif uclfinals == '7' or uclfinals == 'Juventus vs. Barcelona':
      #Juventus stats and lineup
      team1 = Team('Juventus', 0, 0, 0, 87, 87, 87, 87, 87, ['Gianluigi Buffon', 'Patrice Evra', 'Leonardo Bonucci', 'Andrea Barzagli', 'Stephan Lichtsteiner', 'Paul Pogba', 'Andrea Pirlo', 'Claudio Marchisio', 'Arturo Vidal', 'Álvaro Morata', 'Carlos Teves'])
      #Barcelona stats and lineup
      team2 = Team('Barcelona', 0, 0, 0, 90, 90, 90, 90, 90, ['Marc-André ter Stegen', 'Jordi Alba', 'Javier Mascherano', 'Gerard Piqué', 'Dani Alves', 'Andrés Iniesta', 'Sergio Busquets', 'Ivan Rakitić', 'Neymar', 'Luis Suárez', 'Lionel Messi'])
      break
    else:
      #if user inputs anything other than '1', '2', or '3', the screen is cleared and user can return to menu
      os.system("clear")

  #user selects custom match and types in both teams
  elif league == "8" or league == "Custom match":
    os.system("clear")
    print(magenta + "Home team:")
    T1 = input(white + ">")
    print()
    print(magenta + "Away team:")
    T2 = input(white + ">")
    print("")
    #teams are automatically set to 70 for each stat
    team1 = Team(T1, 0, 0, 0, 70, 70, 70, 70, 70, [str(T1)])
    team2 = Team(T2, 0, 0, 0, 70, 70, 70, 70, 70, [str(T2)])
    break
  else:
    os.system("clear")
os.system("clear")

match = [team1, team2]
rand = random.randint(1, 10)

#goal procedure
def goal(team):
  if league == '1' or league == '2' or league == '3' or league == '4' or league == '5' or league == '6' or league == '7':
    rand = random.randint(1, 10)
    print(green + "Goal " + str(team.name) + "! " + team.player[rand] + " scores! ⚽" + white)
    team.score += 1
  else:
    print(green + "Goal! " + str(team.name) + " scores! ⚽"+white)
    team.score += 1
#yellow card procedure

def yellow(team):
  print(yellowc + "Yellow Card for " + grey_back + str(team.name) + yellowc + ' 🟡' + white)

rednum = 20

#red card procedure
def red(team):
  if team.red == False:
    #receiving a red card affects the team by weakening their attack, defense, luck, speed and stamina by -20
    print(redc + "Red Card for " + grey_back + str(team.name) + redc + ' 🔴' + white)
    team.red = True
    team.attack -= rednum
    team.defense -= rednum
    team.luck -= rednum
    team.speed -= rednum
    team.stamina -= rednum
  else:
    pass

#matchday procedure (goes through each minute, VAR decisions, half time, and full time)
def matchday(match):
  for i in range(1, 91):
    if i < 46:
      secondhalf = False
    elif i == 46:
      print(blue + 'Half Time! ⏱️'+ white)
      print(blue_back + str(match[0].name) + ' ' + str(match[0].score) + '-' + str(match[1].score) + ' ' + str(match[1].name) + white)
      time.sleep(8)
      secondhalf = True
    else:
      secondhalf = True
    n1 = random.randint(1, 300)
    n2 = random.randint(0, 1)

    event = ""
    if n1 < 283:
      if match[0].red == True or match[1].red == True:
        event = " "
      else:
        event = " "
    elif n1 < 284:
      print(blue_back + "VAR Decision: Possible Penalty Review! " + white + "📺")
      time.sleep(3)
      n_var = random.randint(0, 10)
      nvar_1 = random.randint(1, 100)
      nvar_2 = random.randint(1, 100)
      if (match[0].luck + nvar_1) > (match[1].luck + nvar_2):
        varteam = match[0]
      else:
        varteam = match[1]
      if n_var > 3:
        print(blue + "Penalty given for " + str(varteam.name) + "!")
        nvar_3 = random.randint(0, 4)
        if nvar_3 > 1:
          goal(varteam)
        else:
          print(redc + "Missed Penalty! ❌" + white)
      else:
        print(redc + "No Penalty Given! ❌" + white)

    #goal
    elif n1 < 295:
      #generate new random number here for each team (plus stats) to compare
      n3_1 = random.randint(1, 100)
      n3_2 = random.randint(1, 100)
      if secondhalf == True:
        if (match[0].attack + match[0].stamina + n3_1) > (match[1].attack + match[1].stamina + n3_2):
          goal(match[0])
        else:
          goal(match[1])
      else:
        if (match[0].attack + match[0].speed + n3_1) > (match[1].attack + match[1].speed + n3_2):
          goal(match[0])
        else:
          goal(match[1])
    #yellow card
    elif n1 < 299:
      yellow(match[n2])
    #red card
    else:
      red(match[n2])
    time.sleep(0.2)
    print(str(i) + """' """ + event)

  #prints full time with score
  print(blue + 'Full Time! ⏱️' + white)
  print(blue_back + str(match[0].name) + ' ' + str(match[0].score) + '-' + str(match[1].score) + ' ' + str(match[1].name) + white)

#the matchday screen
print("\n" * 15)
print(green + "Today's match...")
print(white + "______________________\n" + blue)
print(team1.name + yellowc + " vs. " + blue + team2.name)
print()
print('Press ENTER to continue:')
input(white + "")

#user makes match prediction
print(magenta + "Match prediction:")
print('How many goals will', team1.name, 'score?')
prediction1 = input()

#checks if each score prediction is indeed an integer
#if prediction is not an integer, the simulator restarts
if prediction1.isnumeric():
  pass
else:
  print('That is not an integer. Rerunning the simulator...')
  time.sleep(1.5)
  os.system("clear")
  os.system("python main.py")
print('How many goals will', team2.name, 'score?')
prediction2 = input()
if prediction2.isnumeric():
  pass
else:
  print('That is not an integer. Rerunning the simulator...')
  time.sleep(1.5)
  os.system("clear")
  os.system("python main.py")
  
print()
print('Your prediction is: ' + team1.name, prediction1 + '-' + prediction2, team2.name)
print('Kickoff will begin shortly...')
print('Do not press anything.')
time.sleep(2)
os.system("clear")

print(blue_back + team1.name + " - " + team2.name + white)
matchday(match)

#goes through user predictions and determines whether or not their predictions were correct
count = 0
for team in match:
  while count < 1:
    if str(prediction1) == str(match[0].score):
      if str(prediction2) == str(match[1].score):
        print('Your prediction was correct!')
        count = count + 1
      else:
        print("Your predicition wasn't correct.")
        count = count + 1
    else:
      print("Your predicition wasn't correct.")
      count = count + 1

#returns to menu after the match is finished
print(yellowc + "\n\n\nPress ENTER to return to menu:")
input()
os.system("clear")
os.system("python main.py")