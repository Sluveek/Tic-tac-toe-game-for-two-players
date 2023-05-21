# Tic-tac-toe for Two Players
## Introduction

This is a command-line implementation of the classic Tic-tac-toe game designed for two players. The players take turns marking their symbols ('X' or 'O') on a 3x3 grid, aiming to get three of their symbols in a horizontal, vertical, or diagonal row. The game continues until one player wins or the board is filled

## Site Goals

The goal of this application is to provide a Tic-tac-toe game for two users with a score of up to 10 tries. 

## Target Audience
---
Anyone who enjoys playing strategy games.

### Starting a New Game
- The user can start a new game by running the program. The program will ask the user to choose a number between 1 and 9 for player X.

![img](/readme-img/Run.png)

- Players take turns entering the number corresponding to the cell where they want to place their symbol ('X' or 'O').

-The game will validate the input and notify the players if the selected cell is already occupied or if the input is invalid.

-If a player successfully places their symbols in a winning pattern, they will be declared the winner.

-The game keeps track of scores for each player, and the first player to reach the specified score goal wins the game.

![img](/readme-img/Score.png)

-After each game, the scores will be displayed, and players have the option to play again or exit.

![img](/readme-img/Win.png)