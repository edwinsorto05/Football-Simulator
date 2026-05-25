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
dark_grey  = "\033[0;90m"

# ── Position-weighted scorer selection ────────────────────────────────
# Index: 0=GK, 1-4=DEF, 5-7=MID, 8-10=ATT
SCORER_WEIGHTS = [1, 3, 3, 3, 3, 8, 8, 8, 20, 20, 20]

def pick_scorer(players, sent_off=None):
    """Return a weighted random player, skipping anyone sent off."""
    if sent_off is None:
        sent_off = set()
    available = [(p, SCORER_WEIGHTS[min(i, 10)]) for i, p in enumerate(players)
                 if p not in sent_off]
    if not available:
        return players[0]  # fallback — shouldn't normally happen
    names, weights = zip(*available)
    return random.choices(names, weights=weights, k=1)[0]

# ── Team class ─────────────────────────────────────────────────────────
class Team:
    def __init__(self, name, score, goaldif, goals, attack, defense, luck, speed, stamina, player, bench=None):
        self.name         = name
        self.score        = score
        self.goaldif      = goaldif
        self.goals        = goals
        self.attack       = attack
        self.defense      = defense
        self.luck         = luck
        self.speed        = speed
        self.stamina      = stamina
        self.player       = list(player)        # active XI
        self.bench        = list(bench or [])   # available substitutes
        self.scorers      = []                  # (minute, name)
        self.yellow_cards = {}                  # name → count (1 or 2)
        self.sent_off     = set()               # players with red or 2nd yellow
        self.subs_used    = 0                   # max 5 per FIFA rules
        self.sub_windows  = 0                   # max 3 windows per FIFA rules

# ── Substitution screen ────────────────────────────────────────────────
SUB_MINUTES = {46, 61, 76}   # windows: HT, ~60', ~75'

def do_substitutions(match, minute):
    """Pause and offer substitutions to both teams at natural break points."""
    for team in match:
        # Skip if used all 5 subs or all 3 windows or no bench left
        if team.subs_used >= 5 or team.sub_windows >= 3 or not team.bench:
            continue

        remaining = 5 - team.subs_used
        print(blue + f"\n── Substitution window for {team.name} ──" + white)
        print(dark_grey + f"  Subs used: {team.subs_used}/5  |  Windows used: {team.sub_windows}/3")
        print(dark_grey + f"  Available bench: {', '.join(team.bench)}")
        print(dark_grey + f"  On the pitch: {', '.join(p for p in team.player if p not in team.sent_off)}")
        print(blue + f"  Make a substitution? (y/n)" + white)
        ans = input(dark_grey + "  > ").strip().lower()

        if ans != 'y':
            continue

        team.sub_windows += 1
        subs_this_window = 0
        max_this_window  = min(3, remaining, len(team.bench))  # up to 3 at once

        while subs_this_window < max_this_window and team.subs_used < 5 and team.bench:
            # Choose who comes OFF
            active = [p for p in team.player if p not in team.sent_off]
            print(magenta + f"\n  Who comes OFF? (enter name, or leave blank to stop)")
            for i, p in enumerate(active):
                yc = team.yellow_cards.get(p, 0)
                yc_str = f" 🟡" if yc == 1 else ""
                print(dark_grey + f"    {i+1}. {p}{yc_str}")
            off_input = input(dark_grey + "  > ").strip()
            if off_input == "":
                break

            # Match by number or name
            player_out = None
            if off_input.isdigit():
                idx = int(off_input) - 1
                if 0 <= idx < len(active):
                    player_out = active[idx]
            else:
                for p in active:
                    if off_input.lower() in p.lower():
                        player_out = p
                        break

            if not player_out:
                print(redc + "  Player not found, skipping." + white)
                continue

            # Choose who comes ON
            print(magenta + f"  Who comes ON?")
            for i, p in enumerate(team.bench):
                print(dark_grey + f"    {i+1}. {p}")
            on_input = input(dark_grey + "  > ").strip()

            player_in = None
            if on_input.isdigit():
                idx = int(on_input) - 1
                if 0 <= idx < len(team.bench):
                    player_in = team.bench[idx]
            else:
                for p in team.bench:
                    if on_input.lower() in p.lower():
                        player_in = p
                        break

            if not player_in:
                print(redc + "  Substitute not found, skipping." + white)
                continue

            # Execute the sub
            pitch_idx = team.player.index(player_out)
            team.player[pitch_idx] = player_in
            team.bench.remove(player_in)
            team.subs_used    += 1
            subs_this_window  += 1
            # Transfer yellow card count to new player slot (new player starts clean)
            print(green + f"  ↕  {player_out} ➜ {player_in}  (sub {team.subs_used}/5)" + white)

        print()

# ── Card procedures ────────────────────────────────────────────────────

def give_yellow(team, minute):
    """Give a yellow card to a random active player. 2nd yellow = red."""
    active = [p for p in team.player if p not in team.sent_off]
    if not active:
        return
    player = random.choice(active)
    team.yellow_cards[player] = team.yellow_cards.get(player, 0) + 1

    if team.yellow_cards[player] >= 2:
        # Double yellow — treat as red
        print(yellowc + f"Yellow Card for {player} ({team.name}) 🟡" + white)
        print(redc + f"Second yellow! {player} is sent off! 🟡🔴" + white)
        team.sent_off.add(player)
        _apply_red_penalty(team)
    else:
        print(yellowc + f"Yellow Card for {player} ({team.name}) 🟡" + white)

def give_red(team, minute):
    """Give a straight red card to a random active player."""
    active = [p for p in team.player if p not in team.sent_off]
    if not active:
        return
    # Slightly more likely to be a defender or midfielder on a bad tackle
    weights = [SCORER_WEIGHTS[min(i, 10)] for i, p in enumerate(team.player)
               if p not in team.sent_off]
    # Invert attacker bias — defenders/mids more likely to foul badly
    inv_weights = [max(1, 21 - w) for w in weights]
    player = random.choices(active, weights=inv_weights, k=1)[0]

    print(redc + f"Red Card! {player} ({team.name}) is sent off! 🔴" + white)
    team.sent_off.add(player)
    _apply_red_penalty(team)

def _apply_red_penalty(team):
    """Weaken the team after losing a player to a red card."""
    team.attack  = max(team.attack  - 20, 1)
    team.defense = max(team.defense - 20, 1)
    team.luck    = max(team.luck    - 20, 1)
    team.speed   = max(team.speed   - 20, 1)
    team.stamina = max(team.stamina - 20, 1)

# ── Goal procedure ─────────────────────────────────────────────────────

def goal(team, minute):
    scorer = pick_scorer(team.player, team.sent_off)
    print(green + f"Goal {team.name}! {scorer} scores! ⚽" + white)
    team.score += 1
    team.scorers.append((minute, scorer))

# ── Matchday ───────────────────────────────────────────────────────────

def matchday(match):
    base_stamina  = [match[0].stamina, match[1].stamina]
    ht_stoppage   = random.randint(1, 5)
    ft_stoppage   = random.randint(1, 5)
    total_mins    = 90 + ft_stoppage

    minute = 1
    while minute <= total_mins:

        # ── Substitution windows (46, 61, 76) ───────────────────────
        if minute in SUB_MINUTES:
            do_substitutions(match, minute)

        # ── Half-time break ──────────────────────────────────────────
        if minute == 46:
            print(blue + f"Half Time! +{ht_stoppage}' stoppage time played ⏱️" + white)
            print(blue_back + f"{match[0].name} {match[0].score}-{match[1].score} {match[1].name}" + white)
            time.sleep(8)
            for i, team in enumerate(match):
                drain = int(base_stamina[i] * 0.10)
                team.stamina = max(team.stamina - drain, 1)

        # ── Minute label ─────────────────────────────────────────────
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
            nvar_1  = random.randint(1, 100)
            nvar_2  = random.randint(1, 100)
            varteam = match[0] if (match[0].luck + nvar_1) > (match[1].luck + nvar_2) else match[1]
            if random.randint(0, 10) > 3:
                taker = pick_scorer(varteam.player, varteam.sent_off)
                print(blue + f"Penalty given for {varteam.name}! {taker} steps up...")
                if random.randint(0, 4) > 1:
                    print(green + f"Goal {varteam.name}! {taker} scores! ⚽" + white)
                    varteam.score += 1
                    varteam.scorers.append((minute, taker))
                else:
                    print(redc + "Missed Penalty! ❌" + white)
            else:
                print(redc + "No Penalty Given! ❌" + white)

        elif n1 < 295:
            # Goal
            n3_1       = random.randint(1, 100)
            n3_2       = random.randint(1, 100)
            stat       = "stamina" if minute >= 46 else "speed"
            score0     = match[0].attack + getattr(match[0], stat) + n3_1
            score1     = match[1].attack + getattr(match[1], stat) + n3_2
            goal(match[0] if score0 > score1 else match[1], minute)

        elif n1 < 299:
            give_yellow(match[n2], minute)

        else:
            give_red(match[n2], minute)

        time.sleep(0.2)
        print(dark_grey + min_label + white)
        minute += 1

    # ── Full-time summary ────────────────────────────────────────────
    print(blue + f"\nFull Time! +{ft_stoppage}' stoppage time played ⏱️" + white)
    print(blue_back + f"{match[0].name} {match[0].score}-{match[1].score} {match[1].name}" + white)
    print()

    all_goals = [(t, m, s) for t in match for m, s in t.scorers]
    all_goals.sort(key=lambda x: x[1])
    if all_goals:
        print(green + "⚽ Goal scorers:" + white)
        for team, m, scorer in all_goals:
            extra = f"90+{m-90}" if m > 90 else str(m)
            print(dark_grey + f"  {team.name}: {scorer} ({extra}')" + white)
    else:
        print(yellowc + "No goals scored." + white)

# ══════════════════════════════════════════════════════════════════════
# ── League / matchup selection ────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════
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

    # ── Premier League ───────────────────────────────────────────────
    if league == "1" or league == "Premier League":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. Manchester United vs. Manchester City")
        print(green + "  2. Tottenham vs. Arsenal")
        print(green + "  3. Chelsea vs. Liverpool")
        premierleague = input("> ")
        print(white + "")
        if premierleague == '1' or premierleague == 'Manchester United vs. Manchester City':
            team1 = Team('Manchester United', 0,0,0, 85,85,85,85,85,
                         ['Senne Lammens','Luke Shaw','Lisandro Martínez','Harry Maguire','Diogo Dalot','Kobbie Mainoo','Casemiro','Patrick Dorgu','Bruno Fernandes','Amad Diallo','Bryan Mbeumo'],
                         bench=['Altay Bayındır','Ayden Heaven','Manuel Ugarte','Mason Mount','Matheus Cunha'])
            team2 = Team('Manchester City', 0,0,0, 88,88,88,88,88,
                         ['Gianluigi Donnarumma','Nathan Aké','Max Alleyne','Abdukodir Khusanov','Rico Lewis','Rodri','Jérémy Doku','Bernardo Silva','Phil Foden','Antoine Semenyo','Erling Haaland'],
                         bench=['James Trafford', "Nico O'Reilly",'Matheus Nunes','Tijjani Reijnders','Rayan Cherki'])
            break
        elif premierleague == '2' or premierleague == 'Tottenham vs. Arsenal':
            team1 = Team('Tottenham', 0,0,0, 80,80,80,80,80,
                         ['Guglielmo Vicario','Micky van de Ven','Radu Drăgușin','João Palhinha','Djed Spence','Pape Matar Sarr','Conor Gallagher','Yves Bissouma','Archie Gray','Xavi Simons','Randal Kolo Muani'],
                         bench=['Brandon Austin','Ben Davies','Emerson Royal','Richarlison','Dominic Solanke'])
            team2 = Team('Arsenal', 0,0,0, 89,89,89,89,89,
                         ['David Raya','Piero Hincapié','Gabriel','William Saliba','Jurrien Timber','Declan Rice','Martín Zubimendi','Leandro Trossard','Eberechi Eze','Bukayo Saka','Viktor Gyökeres'],
                         bench=['Kepa Arrizabalaga','Riccardo Calafiori','Martin Ødegaard','Gabriel Martinelli','Noni Madueke'])
            break
        elif premierleague == '3' or premierleague == 'Chelsea vs. Liverpool':
            team1 = Team('Chelsea', 0,0,0, 83,83,83,83,83,
                         ['Robert Sánchez','Marc Cucurella','Benoît Badiashile','Josh Acheampong','Malo Gusto','Moisés Caicedo','Reece James','Alejandro Garnacho','Enzo Fernández','Pedro Neto','João Pedro'],
                         bench=['Filip Jørgensen','Trevoh Chalobah','Roméo Lavia','Cole Palmer','Liam Delap'])
            team2 = Team('Liverpool', 0,0,0, 86,86,86,86,86,
                         ['Alisson Becker','Milos Kerkez','Virgil van Dijk','Ibrahima Konaté','Conor Bradley','Alexis Mac Allister','Ryan Gravenberch','Cody Gakpo','Dominik Szoboszlai','Mohamed Salah','Alexander Isak'],
                         bench=['Giorgi Mamardashvili','Joe Gomez','Andrew Robertson','Curtis Jones','Alexander Isak'])
            break
        else:
            os.system("clear")

    # ── Serie A ──────────────────────────────────────────────────────
    elif league == "2" or league == "Serie A":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. Inter Milan vs. AC Milan")
        print(green + "  2. Juventus vs. Roma")
        print(green + "  3. Napoli vs. Juventus")
        seriea = input("> ")
        print(white + "")
        if seriea == '1' or seriea == 'Inter Milan vs. AC Milan':
            team1 = Team('Inter Milan', 0,0,0, 87,87,87,87,87,
                         ['Yann Sommer','Alessandro Bastoni','Francesco Acerbi','Manuel Akanji','Federico Dimarco','Petar Sučić','Hakan Çalhanoğlu','Nicolò Barella','Carlos Augusto','Marcus Thuram','Lautaro Martínez'],
                         bench=['Josep Martínez','Stefan de Vrij','Denzel Dumfries','Piotr Zieliński','Pio Esposito'])
            team2 = Team('AC Milan', 0,0,0, 84,84,84,84,84,
                         ['Mike Maignan','Strahinja Pavlović','Matteo Gabbia','Fikayo Tomori','Davide Bartesaghi','Adrien Rabiot','Luka Modrić','Youssouf Fofana','Alexis Saelemaekers','Rafael Leão','Christian Pulisic'],
                         bench=['Pietro Terracciano','Samuele Ricci','Pervis Estupiñán','Ruben Loftus-Cheek','Christopher Nkunku'])
            break
        elif seriea == '2' or seriea == 'Juventus vs. Roma':
            team1 = Team('Juventus', 0,0,0, 84,84,84,84,84,
                         ['Michele Di Gregorio','Lloyd Kelly','Gleison Bremer','Pierre Kalulu','Andrea Cambiaso','Khéphren Thuram','Manuel Locatelli','Weston McKennie','Kenan Yıldız','Francisco Conceição','Loïs Openda'],
                         bench=['Mattia Perin','Daniele Rugani','Fabio Miretti','Jonathan David','Dusan Vlahović'])
            team2 = Team('Roma', 0,0,0, 84,84,84,84,84,
                         ['Mile Svilar','Devyne Rensch','Jan Ziółkowski','Gianluca Mancini','Wesley França','Manu Koné','Bryan Cristante','Mehmet Zeki Çelik','Lorenzo Pellegrini','Matías Soulé','Paulo Dybala'],
                         bench=['Pierluigi Gollini','Mario Hermoso','Konstantinos Tsimikas','Stephan El Shaarawy','Evan Ferguson'])
            break
        elif seriea == '3' or seriea == 'Napoli vs. Juventus':
            team1 = Team('Napoli', 0,0,0, 85,85,85,85,85,
                         ['Alex Meret','Juan Jesus','Alessandro Buongiorno','Giovanni Di Lorenzo','Leonardo Spinazzola','Scott McTominay','Stanislav Lobotka','Miguel Gutiérrez','Eljif Elmas','Rasmus Højlund','Antonio Vergara'],
                         bench=['Vanja Milinković-Savić','Mathías Olivera','Sam Beukema','Giovane','Romelu Lukaku'])
            team2 = Team('Juventus', 0,0,0, 84,84,84,84,84,
                         ['Michele Di Gregorio','Andrea Cambiaso','Lloyd Kelly','Gleison Bremer','Pierre Kalulu','Manuel Locatelli','Khéphren Thuram','Kenan Yıldız','Weston McKennie','Francisco Conceição','Jonathan David'],
                         bench=['Mattia Perin','Federico Gatti','Fabio Miretti','Teun Koopmeiners','Federico Gatti'])
            break
        else:
            os.system("clear")

    # ── LaLiga ───────────────────────────────────────────────────────
    elif league == "3" or league == "LaLiga":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. Real Madrid vs. Barcelona")
        print(green + "  2. Atlético Madrid vs Real Madrid")
        print(green + "  3. Barcelona vs. Atlético Madrid")
        laliga = input("> ")
        print(white + "")
        if laliga == '1' or laliga == 'Real Madrid vs. Barcelona':
            team1 = Team('Real Madrid', 0,0,0, 86,86,86,86,86,
                         ['Thibaut Courtois','Álvaro Carreras','Dean Huijsen','Raúl Asencio','Federico Valverde','Jude Bellingham','Aurélien Tchouaméni','Eduardo Camavinga','Vinícius Júnior','Kylian Mbappé','Rodrygo'],
                         bench=['Andriy Lunin','Éder Militão','Trent Alexander-Arnold','Brahim Díaz','Gonzalo García'])
            team2 = Team('Barcelona', 0,0,0, 88,88,88,88,88,
                         ['Joan García','Alejandro Balde','Eric García','Pau Cubarsí','Jules Koundé','Pedri','Frenkie de Jong','Fermín López','Raphinha','Robert Lewandowski','Lamine Yamal'],
                         bench=['Wojciech Szczęsny','Gerard Martín','Marc Bernal','Marcus Rashford','Ferran Torres'])
            break
        elif laliga == '2' or laliga == 'Atlético Madrid vs Real Madrid':
            team1 = Team('Atlético Madrid', 0,0,0, 86,86,86,86,86,
                         ['Jan Oblak','Matteo Ruggeri','Dávid Hancko','Marc Pubill','Marcos Llorente','Álex Baena','Pablo Barrios','Koke','Giuliano Simeone','Julián Alvarez','Alexander Sørloth'],
                         bench=['Juan Musso','José María Giménez','Nahuel Molina','Thiago Almada','Antoine Griezmann'])
            team2 = Team('Real Madrid', 0,0,0, 86,86,86,86,86,
                         ['Thibaut Courtois','Álvaro Carreras','Antonio Rüdiger','Raúl Asencio','Federico Valverde','Jude Bellingham','Aurélien Tchouaméni','Eduardo Camavinga','Rodrygo','Vinícius Júnior','Gonzalo García'],
                         bench=['Andriy Lunin','Éder Militão','Fran García','Franco Mastantuono','Arda Güler'])
            break
        elif laliga == '3' or laliga == 'Barcelona vs. Atlético Madrid':
            team1 = Team('Barcelona', 0,0,0, 88,88,88,88,88,
                         ['Joan García','Alejandro Balde','Gerard Martín','Pau Cubarsí','Jules Koundé','Dani Olmo','Eric García','Pedri','Raphinha','Robert Lewandowski','Lamine Yamal'],
                         bench=['Iñaki Peña','Andreas Christensen','Marc Casadó','Marcus Rashford','Ferran Torres'])
            team2 = Team('Atlético Madrid', 0,0,0, 87,87,87,87,87,
                         ['Jan Oblak','Dávid Hancko','Clément Lenglet','José María Giménez','Nahuel Molina','Pablo Barrios','Johnny Cardoso','Nicolás González','Álex Baena','Giuliano Simeone','Julián Alvarez'],
                         bench=['Juan Musso','Matteo Ruggeri','Conor Gallagher','Koke','Antoine Griezmann'])
            break
        else:
            os.system("clear")

    # ── Bundesliga ───────────────────────────────────────────────────
    elif league == "4" or league == "Bundesliga":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + " 1. Bayern Munich vs. Borussia Dortmund")
        print(green + " 2. Borussia Dortmund vs. RB Leipzig")
        print(green + " 3. RB Leipzig vs. Bayern Munich")
        bundesliga = input("> ")
        print(white + "")
        if bundesliga == '1' or bundesliga == 'Bayern Munich vs. Borussia Dortmund':
            team1 = Team('Bayern Munich', 0,0,0, 89,89,89,89,89,
                         ['Manuel Neuer','Konrad Laimer','Jonathan Tah','Dayot Upamecano','Sacha Boey','Aleksandar Pavlović','Joshua Kimmich','Luis Díaz','Serge Gnabry','Michael Olise','Harry Kane'],
                         bench=['Jonas Urbig','Alphonso Davies','Min-jae Kim','Leon Goretzka','Lennart Karl'])
            team2 = Team('Borussia Dortmund', 0,0,0, 84,84,84,84,84,
                         ['Gregor Kobel','Nico Schlotterbeck','Waldemar Anton','Niklas Süle','Daniel Svensson','Felix Nmecha','Pascal Groß','Marcel Sabitzer','Julian Ryerson','Karim Adeyemi','Serhou Guirassy'],
                         bench=['Alexander Meyer','Ramy Bensebaini','Jobe Bellingham','Julian Brandt','Maximilian Beier'])
            break
        elif bundesliga == '2' or bundesliga == 'Borussia Dortmund vs. RB Leipzig':
            team1 = Team('Borussia Dortmund', 0,0,0, 84,84,84,84,84,
                         ['Gregor Kobel','Ramy Bensebaini','Waldemar Anton','Luca Reggiani','Daniel Svensson','Jobe Bellingham','Julian Ryerson','Marcel Sabitzer','Felix Nmecha','Serhou Guirassy','Maximilian Beier'],
                         bench=['Alexander Meyer','Nico Schlotterbeck','Yan Couto','Fábio Silva','Karim Adeyemi'])
            team2 = Team('RB Leipzig', 0,0,0, 84,84,84,84,84,
                         ['Maarten Vandevoordt','David Raum','Castello Lukeba','Willi Orbán','Ridle Baku','Nicolas Seiwald','Xaver Schlager','Yan Diomande','Christoph Baumgartner','Brajan Gruda','Rômulo Cardoso'],
                         bench=['Péter Gulácsi','Benjamin Henrichs','Ezechiel Banzuzi','Antonio Nusa','Johan Bakayokko'])
            break
        elif bundesliga == '3' or bundesliga == 'RB Leipzig vs. Bayern Munich':
            team1 = Team('RB Leipzig', 0,0,0, 84,84,84,84,84,
                         ['Maarten Vandevoordt','David Raum','Castello Lukeba','Willi Orbán','Ridle Baku','Christoph Baumgartner','Xaver Schlager','Nicolas Seiwald','Antonio Nusa','Rômulo Cardoso','Yan Diomande'],
                         bench=['Péter Gulácsi','El Chadaille Bitshiabu','Conrad Harder','Brajan Gruda','Tidiam Gomis'])
            team2 = Team('Bayern Munich', 0,0,0, 89,89,89,89,89,
                         ['Manuel Neuer','Alphonso Davies','Jonathan Tah','Dayot Upamecano','Josip Stanišić','Aleksandar Pavlović','Joshua Kimmich','Luis Díaz','Serge Gnabry','Michael Olise','Harry Kane'],
                         bench=['Jonas Urbig','Min-jae Kim','Konrad Laimer','Leon Goretzka','Jamal Musiala'])
            break
        else:
            os.system("clear")

    # ── Ligue 1 ──────────────────────────────────────────────────────
    elif league == "5" or league == "Ligue 1":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. PSG vs. Lyon")
        print(green + "  2. Marseille vs. PSG")
        print(green + "  3. Lyon vs. Monaco")
        ligue1 = input("> ")
        print(white + "")
        if ligue1 == '1' or ligue1 == 'PSG vs. Lyon':
            team1 = Team('PSG', 0,0,0, 88,88,88,88,88,
                         ['Lucas Chevalier','Lucas Hernández','Willian Pacho','Illia Zabarnyi','Warren Zaïre-Emery','Vitinha','Fabián Ruiz','João Neves','Senny Mayulu','Khvicha Kvaratskhelia','Lee Kang-in'],
                         bench=['Matvei Safonov','Nuno Mendes','Marquinhos','Ousmane Dembélé','Désiré Doué'])
            team2 = Team('Lyon', 0,0,0, 83,83,83,83,83,
                         ['Dominik Greif','Moussa Niakhaté','Clinton Mata','Ruben Kluivert','Nicolás Tagliafico','Tyler Morton','Tanner Tessmann','Ainsley Maitland-Niles','Afonso Moreira','Khalis Merah','Rachid Ghezzal'],
                         bench=['Rémy Descamps','Teo Barišić','Mathys De Carvalho','Corentin Tolisso','Adam Karabec'])
            break
        elif ligue1 == '2' or ligue1 == 'Marseille vs. PSG':
            team1 = Team('Marseille', 0,0,0, 82,82,82,82,82,
                         ['Jeffrey de Lange','Facundo Medina','Leonardo Balerdi','Benjamin Pavard','Emerson','Pierre-Emile Højbjerg','Quinten Timber','Timothy Weah','Ethan Nwaneri','Mason Greenwood','Amine Gouiri'],
                         bench=['Gerónimo Rulli','CJ Egan-Riley','Bilal Nadir','Igor Paixão','Pierre-Emerick Aubameyang'])
            team2 = Team('PSG', 0,0,0, 88,88,88,88,88,
                         ['Matvei Safonov','Nuno Mendes','Willian Pacho','Marquinhos','Warren Zaïre-Emery','João Neves','Vitinha','Senny Mayulu','Bradley Barcola','Ousmane Dembélé','Désiré Doué'],
                         bench=['Lucas Chevalier','Lucas Hernández','Illia Zabarnyi','Lee Kang-in','Khvicha Kvaratskhelia'])
            break
        elif ligue1 == '3' or ligue1 == 'Lyon vs. Monaco':
            team1 = Team('Lyon', 0,0,0, 83,83,83,83,83,
                         ['Dominik Greif','Nicolás Tagliafico','Clinton Mata','Ruben Kluivert','Abner Vinícius','Tyler Morton','Corentin Tolisso','Ainsley Maitland-Niles','Khalis Merah','Pavel Šulc','Afonso Moreira'],
                         bench=['Rémy Descamps','Hans Hateboer','Orel Mangala','Tanner Tessmann','Adam Karabec'])
            team2 = Team('Monaco', 0,0,0, 83,83,83,83,83,
                         ['Lukas Hradecky','Caio Henrique','Mohammed Salisu','Thilo Kehrer','Christian Mawissa','Aleksandr Golovin','Jordan Teze','Mamadou Coulibaly','Maghnes Akliouche','Folarin Balogun','Mika Biereth'],
                         bench=['Philipp Köhn','Eric Dier','Kassoum Ouattara','Stanis Idumbo','George Ilenikhena'])
            break
        else:
            os.system("clear")

    # ── MLS ──────────────────────────────────────────────────────────
    elif league == "6" or league == "MLS":
        print(magenta + "Choose your matchup: (select a number)")
        print(green + "  1. New England Revolution vs. New York Red Bulls")
        print(green + "  2. LAFC vs. Inter Miami")
        print(green + "  3. CF Montréal vs. Toronto FC")
        mls = input("> ")
        print(white + "")
        if mls == '1' or mls == 'New England Revolution vs. New York Red Bulls':
            team1 = Team('New England Revolution', 0,0,0, 75,75,75,75,75,
                         ['Matt Turner','Will Sands','Mamadou Fofana','Brayan Ceballos','Ilay Feingold','Brooklyn Raines','Matt Polster','Griffin Yow','Carles Gil','Luca Langoni','Dor Turgeman'],
                         bench=['Donovan Parisian','Tanner Beason','Alhassan Yusuf','Tommy McNamara','Malcolm Fry'])
            team2 = Team('New York Red Bulls', 0,0,0, 75,75,75,75,75,
                         ['Ethan Horvath','Matthew Dos Santos','Dylan Nealis','Justin Che','Jahkeele Marshall-Rutty','Emil Forsberg','Adri Mehmeti','Ronald Donkor','Jorge Ruvalcaba','Julian Hall','Cade Cowell'],
                         bench=['John McCarthy','Omar Valencia','Andy Rojas','Tanner Rosborough','Eric Maxim Choupo-Moting'])
            break
        elif mls == '2' or mls == 'LAFC vs. Inter Miami':
            team1 = Team('LAFC', 0,0,0, 79,79,79,79,79,
                         ['Hugo Lloris','Eddie Segura','Ryan Porteous','Nkosi Tafari','Sergi Palencia','Marco Delgaldo','Stephen Eustáquio','Timothy Tillman','Denis Bouanga','Son Heung-min','David Martínez'],
                         bench=['Thomas Hasal','Ryan Hollingshead','Mathieu Choinière','Tyler Boyd','Nathan Ordaz'])
            team2 = Team('Inter Miami', 0,0,0, 79,79,79,79,79,
                         ['Dayne St. Clair','Noah Allen','Micael','Maximiliano Falcón','Ian Fray','Yannick Bright','Rodrigo De Paul','Telasco Segovia','Lionel Messi','Mateo Silvetti','Germán Berterame'],
                         bench=['Rocco Ríos Novo','Gonzalo Luján','David Ayala','Tadeo Allende','Luis Suárez'])
            break
        elif mls == '3' or mls == 'CF Montréal vs. Toronto FC':
            team1 = Team('CF Montréal', 0,0,0, 72,72,72,72,72,
                         ['Thomas Gillier','Luca Petrasso','Efraín Morales','Brandan Craig','Dawid Bugaj','Victor Loturi','Olger Escobar','Matty Longstaff','Dante Sealy','Prince Owusu','Hennadiy Synchuk'],
                         bench=['Jonathan Sirois','Fernando Álvarez','Bode Hidalgo','Bryce Duke','Romell Quioto'])
            team2 = Team('Toronto FC', 0,0,0, 74,74,74,74,74,
                         ['Sean Johnson','Richie Laryea','Kosi Thompson','Kevin Long','Kobe Franklin','Maxime Dominguez','Jonathan Osorio','Alonso Coello','Đorđe Mihailović','Ola Brynhildsen','Theo Corbeanu'],
                         bench=['Luka Gavran','Lazar Stefanovic','Jose Cifuentes','Derrick Etienne Jr.','Deandre Kerr'])
            break
        else:
            os.system("clear")

    # ── UCL Finals ───────────────────────────────────────────────────
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
            team1 = Team('Manchester City', 0,0,0, 89,89,89,89,89,
                         ['Ederson','Oleksandr Zinchenko','Rúben Dias','John Stones','Kyle Walker','Phil Foden','İlkay Gündoğan','Bernardo Silva','Raheem Sterling','Kevin De Bruyne','Riyad Mahrez'],
                         bench=['Zack Steffen','Aymeric Laporte','Benjamin Mendy','Fernandinho','Gabriel Jesus'])
            team2 = Team('Chelsea', 0,0,0, 88,88,88,88,88,
                         ['Edouard Mendy','Antonio Rüdiger','Thiago Silva','César Azpilicueta','Ben Chilwell','Jorginho',"N'Golo Kanté",'Reece James','Mason Mount','Kai Havertz','Timo Werner'],
                         bench=['Kepa Arrizabalaga','Andreas Christensen','Marcos Alonso','Mateo Kovačić','Callum Hudson-Odoi'])
            break
        elif uclfinals == '2' or uclfinals == 'PSG vs. Bayern Munich':
            team1 = Team('PSG', 0,0,0, 88,88,88,88,88,
                         ['Keylor Navas','Juan Bernat','Presnel Kimpembe','Thiago Silva','Thilo Kehrer','Leandro Paredes','Marquinhos','Ander Herrera','Kylian Mbappé','Neymar','Ángel Di María'],
                         bench=['Sergio Rico','Layvin Kurzawa','Colin Dagba','Pablo Sarabia','Edinson Cavani'])
            team2 = Team('Bayern Munich', 0,0,0, 90,90,90,90,90,
                         ['Manuel Neuer','Alphonso Davies','David Alaba','Jerome Boateng','Joshua Kimmich','Thiago Alcântara','Leon Goretzka','Kinglsey Coman','Thomas Müller','Serge Gnabry','Robert Lewandowski'],
                         bench=['Sven Ulreich','Benjamin Pavard','Lucas Hernández','Philippe Coutinho','Ivan Perišić'])
            break
        elif uclfinals == '3' or uclfinals == 'Tottenham vs. Liverpool':
            team1 = Team('Tottenham', 0,0,0, 88,88,88,88,88,
                         ['Hugo Lloris','Danny Rose','Jan Vertonghen','Toby Alderweireld','Kieran Trippier','Harry Winks','Moussa Sissoko','Heung-min Son','Dele Alli','Christian Eriksen','Harry Kane'],
                         bench=['Paulo Gazzaniga','Ben Davies','Juan Foyth','Fernando Llorente','Lucas Moura'])
            team2 = Team('Liverpool', 0,0,0, 89,89,89,89,89,
                         ['Alisson','Andy Robertson','Virgil van Dijk','Joel Matip','Trent Alexander-Arnold','Georginio Wijnaldum','Fabinho','Jordan Henderson','Sadio Mané','Roberto Firmino','Mohamed Salah'],
                         bench=['Adrián','Joël Matip','James Milner','Divock Origi','Xherdan Shaqiri'])
            break
        elif uclfinals == '4' or uclfinals == 'Real Madrid vs. Liverpool':
            team1 = Team('Real Madrid', 0,0,0, 89,89,89,89,89,
                         ['Keylor Navas','Marcelo','Sergio Ramos','Raphaël Varane','Dani Carvajal','Toni Kroos','Casemiro','Luka Modrić','Gareth Bale','Cristiano Ronaldo','Karim Benzema'],
                         bench=['Kiko Casilla','Nacho','Achraf Hakimi','Isco','Marco Asensio'])
            team2 = Team('Liverpool', 0,0,0, 88,88,88,88,88,
                         ['Loris Karius','Andy Robertson','Virgil van Dijk','Dejan Lovren','Trent Alexander-Arnold','James Milner','Jordan Henderson','Georginio Wijnaldum','Sadio Mané','Roberto Firmino','Mohamed Salah'],
                         bench=['Simon Mignolet','Alberto Moreno','Joe Gomez','Emre Can','Dominic Solanke'])
            break
        elif uclfinals == '5' or uclfinals == 'Juventus vs. Real Madrid':
            team1 = Team('Juventus', 0,0,0, 87,87,87,87,87,
                         ['Gianluigi Buffon','Alex Sandro','Giorgio Chiellini','Leonardo Bonucci','Andrea Barzagli','Sami Khedira','Miralem Pjanić','Mario Mandžukić','Paulo Dybala','Dani Alves','Gonzalo Higuaín'],
                         bench=['Gianluigi Donnarumma','Mehdi Benatia','Stephan Lichtsteiner','Claudio Marchisio','Juan Cuadrado'])
            team2 = Team('Real Madrid', 0,0,0, 90,90,90,90,90,
                         ['Keylor Navas','Marcelo','Sergio Ramos','Raphaël Varane','Dani Carvajal','Toni Kroos','Casemiro','Luka Modrić','Gareth Bale','Cristiano Ronaldo','Karim Benzema'],
                         bench=['Kiko Casilla','Nacho','Achraf Hakimi','Isco','Marco Asensio'])
            break
        elif uclfinals == '6' or uclfinals == 'Real Madrid vs. Atlético Madrid':
            team1 = Team('Real Madrid', 0,0,0, 89,89,89,89,89,
                         ['Keylor Navas','Marcelo','Sergio Ramos','Raphaël Varane','Dani Carvajal','Toni Kroos','Casemiro','Luka Modrić','Cristiano Ronaldo','Karim Benzema','Gareth Bale'],
                         bench=['Kiko Casilla','Nacho','Álvaro Arbeloa','Isco','Álvaro Morata'])
            team2 = Team('Atlético Madrid', 0,0,0, 87,87,87,87,87,
                         ['Jan Oblak','Filipe Luís','Diego Godín','Stefan Savić','Juanfran','Koke','Augusto Fernández','Gabi','Saúl','Antoine Griezmann','Fernando Torres'],
                         bench=['Miguel Ángel Moyá','Sime Vrsaljko','Jesús Gámez','Óliver Torres','Kevin Gameiro'])
            break
        elif uclfinals == '7' or uclfinals == 'Juventus vs. Barcelona':
            team1 = Team('Juventus', 0,0,0, 87,87,87,87,87,
                         ['Gianluigi Buffon','Patrice Evra','Leonardo Bonucci','Andrea Barzagli','Stephan Lichtsteiner','Paul Pogba','Andrea Pirlo','Claudio Marchisio','Arturo Vidal','Álvaro Morata','Carlos Teves'],
                         bench=['Marco Storari','Giorgio Chiellini','Kwadwo Asamoah','Roberto Pereyra','Fernando Llorente'])
            team2 = Team('Barcelona', 0,0,0, 90,90,90,90,90,
                         ['Marc-André ter Stegen','Jordi Alba','Javier Mascherano','Gerard Piqué','Dani Alves','Andrés Iniesta','Sergio Busquets','Ivan Rakitić','Neymar','Luis Suárez','Lionel Messi'],
                         bench=['Claudio Bravo','Adriano','Jeremy Mathieu','Xavi','Pedro'])
            break
        else:
            os.system("clear")

    # ── Custom match ─────────────────────────────────────────────────
    elif league == "8" or league == "Custom match":
        os.system("clear")
        print(magenta + "Home team name:")
        T1 = input(dark_grey + "> ")
        print(magenta + "Away team name:")
        T2 = input(dark_grey + "> ")
        print()

        def get_players(team_name, role):
            print(magenta + f"Enter up to 11 {role} for {team_name} (blank line to stop):")
            lst = []
            for _ in range(11):
                p = input(dark_grey + "  > ").strip()
                if not p:
                    break
                lst.append(p)
            return lst or [team_name]

        def get_bench(team_name):
            print(magenta + f"Enter up to 5 bench players for {team_name} (blank line to stop):")
            lst = []
            for _ in range(5):
                p = input(dark_grey + "  > ").strip()
                if not p:
                    break
                lst.append(p)
            return lst

        players1 = get_players(T1, "starting players")
        bench1   = get_bench(T1)
        players2 = get_players(T2, "starting players")
        bench2   = get_bench(T2)

        team1 = Team(T1, 0,0,0, 70,70,70,70,70, players1, bench=bench1)
        team2 = Team(T2, 0,0,0, 70,70,70,70,70, players2, bench=bench2)
        break
    else:
        os.system("clear")

os.system("clear")
match = [team1, team2]

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

# ── Return to menu ─────────────────────────────────────────────────────
print(yellowc + "\n\nPress ENTER to return to menu:")
input()
os.system("clear")
os.execv(__import__("sys").executable, [__import__("sys").executable, __file__])
