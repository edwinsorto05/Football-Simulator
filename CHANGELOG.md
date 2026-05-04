# Changelog

All notable changes to Football Simulator are documented here.

---

## [1.1.0] - 2025

### Added
- **Stoppage time** — 1 to 5 extra minutes are now generated randomly for each half and displayed as `90+1'`, `90+2'`, etc.
- **Full-time goal scorers log** — a sorted summary of every goal (scorer name + minute) is printed at full time
- **Stamina degradation** — each team's stamina drops by up to 10% at half-time, making the second half slightly harder
- **Custom match player entry** — you can now enter up to 11 real player names per side in custom matches instead of just a team name
- **Better prediction feedback** — if your prediction is wrong, the actual final score is shown alongside your guess

### Fixed
- **Goal scorer crash on custom matches** — `random.randint(1, 10)` replaced with `random.choice(team.player)`, which works for any squad size and no longer skips index 0
- **Broken prediction check** — the `for`/`while` loop that only ever checked `match[0]` replaced with a direct comparison
- **Infinite process spawning** — `os.system("python main.py")` at restart/return replaced with `os.execv()`, which replaces the current process rather than stacking new ones
- **Invalid prediction input** — the one-shot `isnumeric()` check replaced with a loop that keeps prompting until a valid integer is entered

---

## [1.0.0] - Initial release

### Added
- Minute-by-minute match simulation (90 minutes)
- 7 leagues: Premier League, Serie A, LaLiga, Bundesliga, Ligue 1, MLS, UCL Finals
- 3 matchups per league (7 for UCL Finals)
- Events: goals, yellow cards, red cards, VAR penalty reviews
- Score prediction before kickoff
- Custom match mode
- ANSI terminal colors
