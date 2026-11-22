# Maze Runner

Navigate a generated maze using Pygame. The completed implementation includes shortest-path hints, fog of war, a timer leaderboard and difficulty selection.

## Run

```bash
python -m pip install -r requirements.txt
python main.py
```

## Controls

- Select Easy (10 x 8), Medium (15 x 13) or Hard (20 x 18) at the menu.
- Move with WASD or arrow keys.
- Press H to toggle the shortest-path hint, calculated with breadth-first search.
- Press R to generate another maze.
- Press Escape to return to the difficulty menu.

Fog of war reveals the area near the player. Completion times are saved in `leaderboard.json`, with the five best entries retained. The before/after videos and development history PDF are in the parent Lab4 folder.
