# Asteroids

This is my second Boot.Dev project.

Using `pygame`, I will be building a version of the game, 'Asteroids.'

## How To Run

1. Clone Repository

`gh repo clone smail1111/Asteroids`

2. Run `main.py`

`python3 main.py`
* This game will work on `python 3.14`, but `pygame` as a whole does not support `python` versions after 3.13.

## Game Info

1. Controls

Start Game/Retry -> ENTER

Move forward/backward -> W/S

Turn left/right -> A/D

Shoot -> SPACE

2. Health

You have 3 health.
Whenever you get hit by an asteroid, you lose one health and the asteroid breaks.
When your health is 0, the game ends.

3. Score

You gain 30 points every second.
Whenever you shoot an asteroid, you gain 50 points.

4. Asteroids

When an asteroid breaks, it explodes, and, if it is large enough, it splits into two smaller asteroids.

## Notes

You can change the values set in `constants.py` if you want to mess around with the game.