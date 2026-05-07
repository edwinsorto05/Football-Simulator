#import modules: random, time, and os
import random
import time
import os

# ── Text colors ────────────────────────────────────────────────────────
redc       = "\033[0;91m"
yellowc    = "\033[0;93m"
green      = "\033[0;92m"
blue       = "\033[0;94m"
magenta    = "\033[0;95m"
white      = "\033[0;97m"
blue_back  = "\033[0;44m"
grey_back  = "\033[0;40m"
dark_grey  = "\033[0;90m"   # for live minute ticker

# ── Position-weighted scorer selection ────────────────────────────────
# Player list convention (index): 0=GK, 1-4=DEF, 5-7=MID, 8-10=ATT
# Weights reflect real-world scoring likelihood per position.
SCORER_WEIGHTS = [
    1,   # 0  GK  — almost never scores
    3,   # 1  DEF
    3,   # 2  DEF
    3,   # 3  DEF
    3,   # 4  DEF
    8,   # 5  MID
    8,   # 6  MID
    8,   # 7  MID
    20,  # 8  ATT
    20,  # 9  ATT
    20,  # 10 ATT
]

def pick_scorer(players):
    """Return a player name weighted by position (attackers most likely)."""
    n = len(players)
    if n == 1:
        return players[0]
    # Trim weights list to however many players are actually in the squad
    weights = SCORER_WEIGHTS[:n]
    return random.choices(players, weights=weights, k=1)[0]

# ── Team class ─────────────────────────────────────────────────────────
class Team:
    def __init__(self, name, score, goaldif, goals, attack, defense, luck, speed, stamina, player):
        self.name       = name
        self.score      = score
        self.goaldif    = goaldif
        self.goals      = goals
        self.attack     = attack
        self.defense    = defense
        self.luck       = luck
        self.speed      = speed
        self.stamina    = stamina   # degrades each half
        self.red        = False
        self.player     = player
        self.scorers    = []        # log of (minute, player_name)

# ── League / matchup selection ─────────────────────────────────────────
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
    league = input("> " + dark_grey)
    os.system("clear")

    if league == "1" or league == "Premier League":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. Manchester United vs. Manchester City")
        print(green + "  2. Tottenham vs. Arsenal")
        print(green + "  3. Chelsea vs. Liverpool")
        premierleague = input("> ")
        print(white + "")
        if premierleague == '1' or premierleague == 'Manchester United vs. Manchester City':
            team1 = Team('Manchester United', 0, 0, 0, 85, 85, 85, 85, 85, ['Senne Lammens', 'Luke Shaw', 'Lisandro Martínez', 'Harry Maguire', 'Diogo Dalot', 'Kobbie Mainoo', 'Casemiro', 'Patrick Dorgu', 'Bruno Fernandes', 'Amad Diallo', 'Bryan Mbeumo'])
            team2 = Team('Manchester City', 0, 0, 0, 88, 88, 88, 88, 88, ['Gianluigi Donnarumma', 'Nathan Aké', 'Max Alleyne', 'Abdukodir Khusanov', 'Rico Lewis', 'Rodri', 'Jérémy Doku', 'Bernardo Silva', 'Phil Foden', 'Antoine Semenyo', 'Erling Haaland'])
            break
        elif premierleague == '2' or premierleague == 'Tottenham vs. Arsenal':
            team1 = Team('Tottenham', 0, 0, 0, 82, 82, 82, 82, 82, ['Guglielmo Vicario', 'Micky van de Ven', 'Radu Drăgușin', 'João Palhinha', 'Djed Spence', 'Pape Matar Sarr', 'Conor Gallagher', 'Yves Bissouma', 'Archie Gray', 'Xavi Simons', 'Randal Kolo Muani'])
            team2 = Team('Arsenal', 0, 0, 0, 89, 89, 89, 89, 89, ['David Raya', 'Piero Hincapié', 'Gabriel', 'William Saliba', 'Jurrien Timber', 'Declan Rice', 'Martín Zubimendi', 'Leandro Trossard', 'Eberechi Eze', 'Bukayo Saka', 'Viktor Gyökeres'])
            break
        elif premierleague == '3' or premierleague == 'Chelsea vs. Liverpool':
            team1 = Team('Chelsea', 0, 0, 0, 85, 85, 85, 85, 85, ['Robert Sánchez', 'Marc Cucurella', 'Benoît Badiashile', 'Josh Acheampong', 'Malo Gusto', 'Moisés Caicedo', 'Reece James', 'Alejandro Garnacho', 'Enzo Fernández', 'Pedro Neto', 'João Pedro'])
            team2 = Team('Liverpool', 0, 0, 0, 87, 87, 87, 87, 87, ['Giorgi Mamardashvili', 'Milos Kerkez', 'Virgil van Dijk', 'Ibrahima Konaté', 'Conor Bradley', 'Alexis Mac Allister', 'Ryan Gravenberch', 'Cody Gakpo', 'Dominik Szoboszlai', 'Mohamed Salah', 'Alexander Isak'])
            break
        else:
            os.system("clear")

    elif league == "2" or league == "Serie A":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. Inter Milan vs. AC Milan")
        print(green + "  2. Juventus vs. Roma")
        print(green + "  3. Napoli vs. Juventus")
        seriea = input("> ")
        print(white + "")
        if seriea == '1' or seriea == 'Inter Milan vs. AC Milan':
            team1 = Team('Inter Milan', 0, 0, 0, 87, 87, 87, 87, 87, ['Yann Sommer', 'Alessandro Bastoni', 'Francesco Acerbi', 'Manuel Akanji', 'Federico Dimarco', 'Petar Sučić', 'Hakan Çalhanoğlu', 'Nicolò Barella', 'Carlos Augusto', 'Marcus Thuram', 'Lautaro Martínez'])
            team2 = Team('AC Milan', 0, 0, 0, 84, 84, 84, 84, 84, ['Mike Maignan', 'Strahinja Pavlović', 'Matteo Gabbia', 'Fikayo Tomori', 'Davide Bartesaghi', 'Adrien Rabiot', 'Luka Modrić', 'Youssouf Fofana', 'Alexis Saelemaekers', 'Rafael Leão', 'Christian Pulisic'])
            break
        elif seriea == '2' or seriea == 'Juventus vs. Roma':
            team1 = Team('Juventus', 0, 0, 0, 84, 84, 84, 84, 84, ['Michele Di Gregorio', 'Lloyd Kelly', 'Gleison Bremer', 'Pierre Kalulu', 'Andrea Cambiaso', 'Khéphren Thuram', 'Manuel Locatelli', 'Weston McKennie', 'Kenan Yıldız', 'Francisco Conceição', 'Loïs Openda'])
            team2 = Team('Roma', 0, 0, 0, 84, 84, 84, 84, 84, ['Mile Svilar', 'Devyne Rensch', 'Jan Ziółkowski', 'Gianluca Mancini', 'Wesley França', 'Manu Koné', 'Bryan Cristante', 'Mehmet Zeki Çelik', 'Lorenzo Pellegrini', 'Matías Soulé', 'Paulo Dybala'])
            break
        elif seriea == '3' or seriea == 'Napoli vs. Juventus':
            team1 = Team('Napoli', 0, 0, 0, 85, 85, 85, 85, 85, ['Alex Meret', 'Juan Jesus', 'Alessandro Buongiorno', 'Giovanni Di Lorenzo', 'Leonardo Spinazzola', 'Scott McTominay', 'Stanislav Lobotka', 'Miguel Gutiérrez', 'Eljif Elmas', 'Rasmus Højlund', 'Antonio Vergara'])
            team2 = Team('Juventus', 0, 0, 0, 84, 84, 84, 84, 84, ['Michele Di Gregorio', 'Andrea Cambiaso', 'Lloyd Kelly', 'Gleison Bremer', 'Pierre Kalulu', 'Manuel Locatelli', 'Khéphren Thuram', 'Kenan Yıldız', 'Weston McKennie', 'Francisco Conceição', 'Jonathan David'])
            break
        else:
            os.system("clear")

    elif league == "3" or league == "LaLiga":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. Real Madrid vs. Barcelona")
        print(green + "  2. Atlético Madrid vs Real Madrid")
        print(green + "  3. Barcelona vs. Atlético Madrid")
        laliga = input("> ")
        print(white + "")
        if laliga == '1' or laliga == 'Real Madrid vs. Barcelona':
            team1 = Team('Real Madrid', 0, 0, 0, 88, 88, 88, 88, 88, ['Thibaut Courtois', 'Álvaro Carreras', 'Dean Huijsen', 'Raúl Asencio', 'Federico Valverde', 'Jude Bellingham', 'Aurélien Tchouaméni', 'Eduardo Camavinga', 'Vinícius Júnior', 'Kylian Mbappé', 'Rodrygo'])
            team2 = Team('Barcelona', 0, 0, 0, 88, 88, 88, 88, 88, ['Joan García', 'Alejandro Balde', 'Eric García', 'Pau Cubarsí', 'Jules Koundé', 'Pedri', 'Frenkie de Jong', 'Fermín López', 'Raphinha', 'Robert Lewandowski', 'Lamine Yamal'])
            break
        elif laliga == '2' or laliga == 'Atlético Madrid vs Real Madrid':
            team1 = Team('Atlético Madrid', 0, 0, 0, 87, 87, 87, 87, 87, ['Jan Oblak', 'Matteo Ruggeri', 'Dávid Hancko', 'Marc Pubill', 'Marcos Llorente', 'Álex Baena', 'Pablo Barrios', 'Koke', 'Giuliano Simeone', 'Julián Alvarez', 'Alexander Sørloth'])
            team2 = Team('Real Madrid', 0, 0, 0, 88, 88, 88, 88, 88, ['Thibaut Courtois', 'Álvaro Carreras', 'Antonio Rüdiger', 'Raúl Asencio', 'Federico Valverde', 'Jude Bellingham', 'Aurélien Tchouaméni', 'Eduardo Camavinga', 'Rodrygo', 'Vinícius Júnior', 'Gonzalo García'])
            break
        elif laliga == '3' or laliga == 'Barcelona vs. Atlético Madrid':
            team1 = Team('Barcelona', 0, 0, 0, 88, 88, 88, 88, 88, ['Joan García', 'Alejandro Balde', 'Gerard Martín', 'Pau Cubarsí', 'Jules Koundé', 'Dani Olmo', 'Eric García', 'Pedri', 'Raphinha', 'Robert Lewandowski', 'Lamine Yamal'])
            team2 = Team('Atlético Madrid', 0, 0, 0, 87, 87, 87, 87, 87, ['Jan Oblak', 'Dávid Hancko', 'Clément Lenglet', 'José María Giménez', 'Nahuel Molina', 'Pablo Barrios', 'Johnny Cardoso', 'Nicolás González', 'Álex Baena', 'Giuliano Simeone', 'Julián Alvarez'])
            break
        else:
            os.system("clear")

    elif league == "4" or league == "Bundesliga":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + " 1. Bayern Munich vs. Borussia Dortmund")
        print(green + " 2. Borussia Dortmund vs. RB Leipzig")
        print(green + " 3. RB Leipzig vs. Bayern Munich")
        bundesliga = input("> ")
        print(white + "")
        if bundesliga == '1' or bundesliga == 'Bayern Munich vs. Borussia Dortmund':
            team1 = Team('Bayern Munich', 0, 0, 0, 89, 89, 89, 89, 89, ['Manuel Neuer', 'Konrad Laimer', 'Jonathan Tah', 'Dayot Upamecano', 'Sacha Boey', 'Aleksandar Pavlović', 'Joshua Kimmich', 'Luis Díaz', 'Serge Gnabry', 'Michael Olise', 'Harry Kane'])
            team2 = Team('Borussia Dortmund', 0, 0, 0, 84, 84, 84, 84, 84, ['Gregor Kobel', 'Nico Schlotterbeck', 'Waldemar Anton', 'Niklas Süle', 'Daniel Svensson', 'Felix Nmecha', 'Pascal Groß', 'Marcel Sabitzer', 'Julian Ryerson', 'Karim Adeyemi', 'Serhou Guirassy'])
            break
        elif bundesliga == '2' or bundesliga == 'Borussia Dortmund vs. RB Leipzig':
            team1 = Team('Borussia Dortmund', 0, 0, 0, 84, 84, 84, 84, 84, ['Gregor Kobel', 'Ramy Bensebaini', 'Waldemar Anton', 'Luca Reggiani', 'Daniel Svensson', 'Jobe Bellingham', 'Julian Ryerson', 'Marcel Sabitzer', 'Felix Nmecha', 'Serhou Guirassy', 'Maximilian Beier'])
            team2 = Team('RB Leipzig', 0, 0, 0, 84, 84, 84, 84, 84, ['Maarten Vandevoordt', 'David Raum', 'Castello Lukeba', 'Willi Orbán', 'Ridle Baku', 'Nicolas Seiwald', 'Xaver Schlager', 'Yan Diomande', 'Christoph Baumgartner', 'Brajan Gruda', 'Rômulo Cardoso'])
            break
        elif bundesliga == '3' or bundesliga == 'RB Leipzig vs. Bayern Munich':
            team1 = Team('RB Leipzig', 0, 0, 0, 84, 84, 84, 84, 84, ['Maarten Vandevoordt', 'David Raum', 'Castello Lukeba', 'Willi Orbán', 'Ridle Baku', 'Christoph Baumgartner', 'Xaver Schlager', 'Nicolas Seiwald', 'Antonio Nusa', 'Rômulo Cardoso', 'Yan Diomande'])
            team2 = Team('Bayern Munich', 0, 0, 0, 89, 89, 89, 89, 89, ['Manuel Neuer', 'Alphonso Davies', 'Jonathan Tah', 'Dayot Upamecano', 'Josip Stanišić', 'Aleksandar Pavlović', 'Joshua Kimmich', 'Luis Díaz', 'Serge Gnabry', 'Michael Olise', 'Harry Kane'])
            break
        else:
            os.system("clear")

    elif league == "5" or league == "Ligue 1":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. PSG vs. Lyon")
        print(green + "  2. Marseille vs. PSG")
        print(green + "  3. Lyon vs. Monaco")
        ligue1 = input("> ")
        print(white + "")
        if ligue1 == '1' or ligue1 == 'PSG vs. Lyon':
            team1 = Team('PSG', 0, 0, 0, 88, 88, 88, 88, 88, ['Lucas Chevalier', 'Lucas Hernández', 'Willian Pacho', 'Illia Zabarnyi', 'Warren Zaïre-Emery', 'Vitinha', 'Fabián Ruiz', 'João Neves', 'Senny Mayulu', 'Khvicha Kvaratskhelia', 'Lee Kang-in'])
            team2 = Team('Lyon', 0, 0, 0, 83, 83, 83, 83, 83, ['Dominik Greif', 'Moussa Niakhaté', 'Clinton Mata', 'Ruben Kluivert', 'Nicolás Tagliafico', 'Tyler Morton', 'Tanner Tessmann', 'Ainsley Maitland-Niles', 'Afonso Moreira', 'Khalis Merah', 'Rachid Ghezzal'])
            break
        elif ligue1 == '2' or ligue1 == 'Marseille vs. PSG':
            team1 = Team('Marseille', 0, 0, 0, 82, 82, 82, 82, 82, ['Jeffrey de Lange', 'Facundo Medina', 'Leonardo Balerdi', 'Benjamin Pavard', 'Emerson', 'Pierre-Emile Højbjerg', 'Quinten Timber', 'Timothy Weah', 'Ethan Nwaneri', 'Mason Greenwood', 'Amine Gouiri'])
            team2 = Team('PSG', 0, 0, 0, 88, 88, 88, 88, 88, ['Matvei Safonov', 'Nuno Mendes', 'Willian Pacho', 'Marquinhos', 'Warren Zaïre-Emery', 'João Neves', 'Vitinha', 'Senny Mayulu', 'Bradley Barcola', 'Ousmane Dembélé', 'Désiré Doué'])
            break
        elif ligue1 == '3' or ligue1 == 'Lyon vs. Monaco':
            team1 = Team('Lyon', 0, 0, 0, 83, 83, 83, 83, 83, ['Dominik Greif', 'Nicolás Tagliafico', 'Clinton Mata', 'Ruben Kluivert', 'Abner Vinícius', 'Tyler Morton', 'Corentin Tolisso', 'Ainsley Maitland-Niles', 'Khalis Merah', 'Pavel Šulc', 'Afonso Moreira'])
            team2 = Team('Monaco', 0, 0, 0, 83, 83, 83, 83, 83, ['Lukas Hradecky', 'Caio Henrique', 'Mohammed Salisu', 'Thilo Kehrer', 'Christian Mawissa', 'Aleksandr Golovin', 'Jordan Teze', 'Mamadou Coulibaly', 'Maghnes Akliouche', 'Folarin Balogun', 'Mika Biereth'])
            break
        else:
            os.system("clear")

    elif league == "6" or league == "MLS":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. New England Revolution vs. New York Red Bulls")
        print(green + "  2. LAFC vs. Inter Miami")
        print(green + "  3. CF Montréal vs. Toronto FC")
        mls = input("> ")
        print(white + "")
        if mls == '1' or mls == 'New England Revolution vs. New York Red Bulls':
            team1 = Team('New England Revolution', 0, 0, 0, 75, 75, 75, 75, 75, ['Aljaž Ivačič', 'Tanner Beason', 'Keegan Hughes', 'Brayan Ceballos', 'Brandon Bye', 'Alhassan Yusuf', 'Matt Polster', 'Peyton Miller', 'Carles Gil', 'Luca Langoni', 'Leonardo Campana'])
            team2 = Team('New York Red Bulls', 0, 0, 0, 75, 75, 75, 75, 75, ['Carlos Coronel', 'Omar Velencia', 'Noah Eile', 'Sean Nealis', 'Kyle Duncan', 'Ronald Donkor', 'Daniel Edelman', 'Wikelman Carmona', 'Emil Forsberg', 'Mohammed Sofo', 'Eric Maxim Choupo-Moting'])
            break
        elif mls == '2' or mls == 'LAFC vs. Inter Miami':
            team1 = Team('LAFC', 0, 0, 0, 79, 79, 79, 79, 79, ['Hugo Lloris', 'Eddie Segura', 'Ryan Porteous', 'Nkosi Tafari', 'Sergi Palencia', 'Marco Delgaldo', 'Stephen Eustáquio', 'Timothy Tillman', 'Denis Bouanga', 'Son Heung-min', 'David Martínez'])
            team2 = Team('Inter Miami', 0, 0, 0, 79, 79, 79, 79, 79, ['Dayne St. Clair', 'Noah Allen', 'Micael', 'Maximiliano Falcón', 'Ian Fray', 'Yannick Bright', 'Rodrigo De Paul', 'Telasco Segovia', 'Lionel Messi', 'Mateo Silvetti', 'Germán Berterame'])
            break
        elif mls == '3' or mls == 'CF Montréal vs. Toronto FC':
            team1 = Team('CF Montréal', 0, 0, 0, 72, 72, 72, 72, 72, ['Thomas Gillier', 'Luca Petrasso', 'Efraín Morales', 'Brandan Craig', 'Dawid Bugaj', 'Victor Loturi', 'Olger Escobar', 'Matty Longstaff', 'Dante Sealy', 'Prince Owusu', 'Hennadiy Synchuk'])
            team2 = Team('Toronto FC', 0, 0, 0, 74, 74, 74, 74, 74, ['Sean Johnson', 'Richie Laryea', 'Kosi Thompson', 'Kevin Long', 'Kobe Franklin', 'Maxime Dominguez', 'Jonathan Osorio', 'Alonso Coello', 'Đorđe Mihailović', 'Ola Brynhildsen', 'Theo Corbeanu'])
            break
        else:
            os.system("clear")

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
        if uclfinals == '1' or uclfinals == 'Manchester City vs. Chelsea':
            team1 = Team('Manchester City', 0, 0, 0, 89, 89, 89, 89, 89, ['Ederson', 'Oleksandr Zinchenko', 'Rúben Dias', 'John Stones', 'Kyle Walker', 'Phil Foden', 'İlkay Gündoğan', 'Bernardo Silva', 'Raheem Sterling', 'Kevin De Bruyne', 'Riyad Mahrez'])
            team2 = Team('Chelsea', 0, 0, 0, 88, 88, 88, 88, 88, ['Edouard Mendy', 'Antonio Rüdiger', 'Thiago Silva', 'César Azpilicueta', 'Ben Chilwell', 'Jorginho', "N'Golo Kanté", 'Reece James', 'Mason Mount', 'Kai Havertz', 'Timo Werner'])
            break
        elif uclfinals == '2' or uclfinals == 'PSG vs. Bayern Munich':
            team1 = Team('PSG', 0, 0, 0, 88, 88, 88, 88, 88, ['Keylor Navas', 'Juan Bernat', 'Presnel Kimpembe', 'Thiago Silva', 'Thilo Kehrer', 'Leandro Paredes', 'Marquinhos', 'Ander Herrera', 'Kylian Mbappé', 'Neymar', 'Ángel Di María'])
            team2 = Team('Bayern Munich', 0, 0, 0, 90, 90, 90, 90, 90, ['Manuel Neuer', 'Alphonso Davies', 'David Alaba', 'Jerome Boateng', 'Joshua Kimmich', 'Thiago Alcântara', 'Leon Goretzka', 'Kinglsey Coman', 'Thomas Müller', 'Serge Gnabry', 'Robert Lewandowski'])
            break
        elif uclfinals == '3' or uclfinals == 'Tottenham vs. Liverpool':
            team1 = Team('Tottenham', 0, 0, 0, 88, 88, 88, 88, 88, ['Hugo Lloris', 'Danny Rose', 'Jan Vertonghen', 'Toby Alderweireld', 'Kieran Trippier', 'Harry Winks', 'Moussa Sissoko', 'Heung-min Son', 'Dele Alli', 'Christian Eriksen', 'Harry Kane'])
            team2 = Team('Liverpool', 0, 0, 0, 89, 89, 89, 89, 89, ['Alisson', 'Andy Robertson', 'Virgil van Dijk', 'Joel Matip', 'Trent Alexander-Arnold', 'Georginio Wijnaldum', 'Fabinho', 'Jordan Henderson', 'Sadio Mané', 'Roberto Firmino', 'Mohamed Salah'])
            break
        elif uclfinals == '4' or uclfinals == 'Real Madrid vs. Liverpool':
            team1 = Team('Real Madrid', 0, 0, 0, 89, 89, 89, 89, 89, ['Keylor Navas', 'Marcelo', 'Sergio Ramos', 'Raphaël Varane', 'Dani Carvajal', 'Toni Kroos', 'Casemiro', 'Luka Modrić', 'Gareth Bale', 'Cristiano Ronaldo', 'Karim Benzema'])
            team2 = Team('Liverpool', 0, 0, 0, 88, 88, 88, 88, 88, ['Loris Karius', 'Andy Robertson', 'Virgil van Dijk', 'Dejan Lovren', 'Trent Alexander-Arnold', 'James Milner', 'Jordan Henderson', 'Georginio Wijnaldum', 'Sadio Mané', 'Roberto Firmino', 'Mohamed Salah'])
            break
        elif uclfinals == '5' or uclfinals == 'Juventus vs. Real Madrid':
            team1 = Team('Juventus', 0, 0, 0, 87, 87, 87, 87, 87, ['Gianluigi Buffon', 'Alex Sandro', 'Giorgio Chiellini', 'Leonardo Bonucci', 'Andrea Barzagli', 'Sami Khedira', 'Miralem Pjanić', 'Mario Mandžukić', 'Paulo Dybala', 'Dani Alves', 'Gonzalo Higuaín'])
            team2 = Team('Real Madrid', 0, 0, 0, 90, 90, 90, 90, 90, ['Keylor Navas', 'Marcelo', 'Sergio Ramos', 'Raphaël Varane', 'Dani Carvajal', 'Toni Kroos', 'Casemiro', 'Luka Modrić', 'Gareth Bale', 'Cristiano Ronaldo', 'Karim Benzema'])
            break
        elif uclfinals == '6' or uclfinals == 'Real Madrid vs. Atlético Madrid':
            team1 = Team('Real Madrid', 0, 0, 0, 89, 89, 89, 89, 89, ['Keylor Navas', 'Marcelo', 'Sergio Ramos', 'Raphaël Varane', 'Dani Carvajal', 'Toni Kroos', 'Casemiro', 'Luka Modrić', 'Cristiano Ronaldo', 'Karim Benzema', 'Gareth Bale'])
            team2 = Team('Atlético Madrid', 0, 0, 0, 87, 87, 87, 87, 87, ['Jan Oblak', 'Filipe Luís', 'Diego Godín', 'Stefan Savić', 'Juanfran', 'Koke', 'Augusto Fernández', 'Gabi', 'Saúl', 'Antoine Griezmann', 'Fernando Torres'])
            break
        elif uclfinals == '7' or uclfinals == 'Juventus vs. Barcelona':
            team1 = Team('Juventus', 0, 0, 0, 87, 87, 87, 87, 87, ['Gianluigi Buffon', 'Patrice Evra', 'Leonardo Bonucci', 'Andrea Barzagli', 'Stephan Lichtsteiner', 'Paul Pogba', 'Andrea Pirlo', 'Claudio Marchisio', 'Arturo Vidal', 'Álvaro Morata', 'Carlos Teves'])
            team2 = Team('Barcelona', 0, 0, 0, 90, 90, 90, 90, 90, ['Marc-André ter Stegen', 'Jordi Alba', 'Javier Mascherano', 'Gerard Piqué', 'Dani Alves', 'Andrés Iniesta', 'Sergio Busquets', 'Ivan Rakitić', 'Neymar', 'Luis Suárez', 'Lionel Messi'])
            break
        else:
            os.system("clear")

    elif league == "8" or league == "Custom match":
        os.system("clear")
        print(magenta + "Home team name:")
        T1 = input(dark_grey + "> ")
        print(magenta + "Away team name:")
        T2 = input(dark_grey + "> ")
        print()
        # Let the user enter up to 11 players per side (or fewer)
        print(magenta + f"Enter up to 11 players for {T1} (press ENTER on empty line to stop):")
        players1 = []
        for _ in range(11):
            p = input(dark_grey + "  > ").strip()
            if p == "":
                break
            players1.append(p)
        if not players1:
            players1 = [T1]   # fallback so scorer display always works

        print(magenta + f"Enter up to 11 players for {T2} (press ENTER on empty line to stop):")
        players2 = []
        for _ in range(11):
            p = input(dark_grey + "  > ").strip()
            if p == "":
                break
            players2.append(p)
        if not players2:
            players2 = [T2]

        team1 = Team(T1, 0, 0, 0, 70, 70, 70, 70, 70, players1)
        team2 = Team(T2, 0, 0, 0, 70, 70, 70, 70, 70, players2)
        break
    else:
        os.system("clear")

os.system("clear")

match = [team1, team2]

# ── Event procedures ───────────────────────────────────────────────────

def goal(team, minute):
    """Credit a goal to a position-weighted player and log it for the match summary."""
    scorer = pick_scorer(team.player)   # attackers most likely, GK almost never
    print(green + f"Goal {team.name}! {scorer} scores! ⚽" + white)
    team.score  += 1
    team.scorers.append((minute, scorer))

def yellow(team):
    print(yellowc + "Yellow Card for " + grey_back + team.name + yellowc + " 🟡" + white)

def red(team):
    if not team.red:
        print(redc + "Red Card for " + grey_back + team.name + redc + " 🔴" + white)
        team.red     = True
        team.attack  -= 20
        team.defense -= 20
        team.luck    -= 20
        team.speed   -= 20
        team.stamina -= 20

# ── Matchday ───────────────────────────────────────────────────────────

def matchday(match):
    # Store original stamina so we can degrade it over the match
    base_stamina = [match[0].stamina, match[1].stamina]

    # Stoppage time: 1–5 extra minutes per half
    ht_stoppage = random.randint(1, 5)
    ft_stoppage = random.randint(1, 5)
    total_mins  = 90 + ft_stoppage

    minute = 1
    while minute <= total_mins:

        # ── Half-time break ─────────────────────────────────────────
        if minute == 46:
            print(blue + f"Half Time! +{ht_stoppage}' stoppage time played ⏱️" + white)
            print(blue_back + f"{match[0].name} {match[0].score}-{match[1].score} {match[1].name}" + white)
            time.sleep(8)
            # Stamina drops by up to 10% heading into the second half
            for i, team in enumerate(match):
                drain = int(base_stamina[i] * 0.10)
                team.stamina = max(team.stamina - drain, 1)

        # ── Minute label (show "+N'" in stoppage time) ───────────────
        if minute > 90:
            min_label = f"90+{minute - 90}'"
        elif minute == 46 and ht_stoppage:
            min_label = f"45+{ht_stoppage}' (HT)"
        else:
            min_label = f"{minute}'"

        n1 = random.randint(1, 300)
        n2 = random.randint(0, 1)

        if n1 < 283:
            pass  # quiet minute

        elif n1 < 284:
            # VAR penalty review
            print(blue_back + "VAR Decision: Possible Penalty Review! " + dark_grey + "📺")
            time.sleep(3)
            nvar_1 = random.randint(1, 100)
            nvar_2 = random.randint(1, 100)
            varteam = match[0] if (match[0].luck + nvar_1) > (match[1].luck + nvar_2) else match[1]
            if random.randint(0, 10) > 3:
                # Penalty taker is also position-weighted (attackers step up)
                penalty_taker = pick_scorer(varteam.player)
                print(blue + f"Penalty given for {varteam.name}! {penalty_taker} steps up...")
                if random.randint(0, 4) > 1:
                    print(green + f"Goal {varteam.name}! {penalty_taker} scores! ⚽" + white)
                    varteam.score += 1
                    varteam.scorers.append((minute, penalty_taker))
                else:
                    print(redc + "Missed Penalty! ❌" + white)
            else:
                print(redc + "No Penalty Given! ❌" + white)

        elif n1 < 295:
            # Goal chance — speed matters in 1st half, stamina in 2nd
            n3_1 = random.randint(1, 100)
            n3_2 = random.randint(1, 100)
            second_half = minute >= 46
            stat = "stamina" if second_half else "speed"
            score0 = match[0].attack + getattr(match[0], stat) + n3_1
            score1 = match[1].attack + getattr(match[1], stat) + n3_2
            goal(match[0] if score0 > score1 else match[1], minute)

        elif n1 < 299:
            yellow(match[n2])

        else:
            red(match[n2])

        time.sleep(0.2)
        print(dark_grey + min_label + white)
        minute += 1

    # ── Full-time summary ────────────────────────────────────────────
    print(blue + f"\nFull Time! +{ft_stoppage}' stoppage time played ⏱️" + white)
    print(blue_back + f"{match[0].name} {match[0].score}-{match[1].score} {match[1].name}" + white)
    print()

    # Goal scorers log
    all_goals = [(t, m, s) for t in match for m, s in t.scorers]
    all_goals.sort(key=lambda x: x[1])
    if all_goals:
        print(green + "⚽ Goal scorers:" + white)
        for team, minute, scorer in all_goals:
            extra = f"90+{minute-90}" if minute > 90 else str(minute)
            print(dark_grey + f"  {team.name}: {scorer} ({extra}')" + white)
    else:
        print(yellowc + "No goals scored." + white)

# ── Pre-match screen ───────────────────────────────────────────────────
print("\n" * 15)
print(green + "Today's match...")
print(dark_grey + "______________________\n" + blue)
print(team1.name + yellowc + " vs. " + blue + team2.name)
print()
print(dark_grey + "Press ENTER to continue:")
input(dark_grey + "")

# ── Predictions ────────────────────────────────────────────────────────
def get_int_prediction(team_name):
    """Keep asking until the user enters a valid non-negative integer."""
    while True:
        raw = input(f"How many goals will {team_name} score? ")
        if raw.strip().isnumeric():
            return int(raw.strip())
        print(redc + "Please enter a whole number (e.g. 0, 1, 2...)." + white)

print(magenta + "Match prediction:")
pred1 = get_int_prediction(team1.name)
pred2 = get_int_prediction(team2.name)

print()
print(dark_grey + f"Your prediction: {team1.name} {pred1}-{pred2} {team2.name}")
print(dark_grey + "Kickoff will begin shortly... Do not press anything.")
time.sleep(2)
os.system("clear")

# ── Kick off ───────────────────────────────────────────────────────────
print(blue_back + team1.name + " - " + team2.name + white)
matchday(match)

# ── Prediction verdict ─────────────────────────────────────────────────
print()
if pred1 == match[0].score and pred2 == match[1].score:
    print(green + "🎉 Your prediction was correct!" + white)
else:
    print(yellowc + f"Your prediction wasn't correct. "
          f"(You predicted {pred1}-{pred2}, "
          f"actual {match[0].score}-{match[1].score})" + white)

# ── Return to menu (no spawning chain) ────────────────────────────────
print(yellowc + "\n\nPress ENTER to return to menu:")
input()
os.system("clear")
# Replace this process with a fresh run of the same script — no stacking
os.execv(__import__("sys").executable, [__import__("sys").executable, __file__])
