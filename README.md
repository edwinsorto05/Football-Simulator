# ⚽ Football Simulator

A terminal-based football (soccer) match simulator written in Python. Pick a league, choose a matchup, make your own score prediction, and watch the match play out minute by minute — complete with goals, cards, VAR decisions, and stoppage time.

---

## 📸 Preview

```
Welcome to Football Simulator! ⚽
Press ENTER to continue:

 Select a league: (select a number)
  1. Premier League (England)
  2. Serie A (Italy)
  3. LaLiga (Spain)
  4. Bundesliga (Germany)
  5. Ligue 1 (France)
  6. MLS (USA)
  7. UCL Finals (Europe)
  8. Custom match
```

---

## 🌍 Leagues & Matchups

| League | Matchups |
|---|---|
| Premier League | Man United vs Man City · Tottenham vs Arsenal · Chelsea vs Liverpool |
| Serie A | Inter vs AC Milan · Juventus vs Roma · Napoli vs Juventus |
| LaLiga | Real Madrid vs Barcelona · Atlético vs Real Madrid · Barcelona vs Atlético |
| Bundesliga | Bayern vs Dortmund · Dortmund vs RB Leipzig · RB Leipzig vs Bayern |
| Ligue 1 | PSG vs Lyon · Marseille vs PSG · Lyon vs Monaco |
| MLS | NE Revolution vs NY Red Bulls · LAFC vs Inter Miami · CF Montréal vs Toronto FC |
| UCL Finals | 7 classic finals from 2015–2021 |
| Custom Match | Create your own teams and players |

---

## ✨ Features

- **Minute-by-minute simulation** across a full 90-minute match
- **Stoppage time** — 1 to 5 extra minutes generated randomly per half
- **Stamina degradation** — teams get slightly slower in the second half
- **Dynamic events** — goals, yellow cards, red cards, and VAR penalty reviews
- **Named goal scorers** — each goal is credited to a real squad player
- **Full-time summary** — sorted goal scorer log with exact minutes
- **Score prediction** — make your prediction before kickoff and find out if you're right
- **Custom matches** — enter your own team names and up to 11 players per side

---

## 🚀 Getting Started

### Requirements
- Python 3.6 or higher
- No external libraries required — uses only the Python standard library

### Run

```bash
git clone https://github.com/yourusername/football-simulator.git
cd football-simulator
python main.py
```

> On some systems you may need to use `python3` instead of `python`.

---

## 🎮 How to Play

1. Run `main.py`
2. Select a league by entering its number
3. Select a matchup
4. Enter your score prediction for each team
5. Watch the match simulate in real time
6. See if your prediction was correct at full time

---

## 📁 Project Structure

```
football-simulator/
├── main.py          # All simulator logic
├── README.md        # This file
├── CHANGELOG.md     # Version history
├── requirements.txt # Dependencies (stdlib only)
└── .gitignore       # Files excluded from version control
```

---

## 🤝 Contributing

Contributions are welcome! Some ideas if you want to help:

- Add more leagues or matchups
- Add an extra time / penalty shootout mode for drawn UCL finals
- Add player ratings that influence individual goal probability
- Add a season/tournament mode

Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
