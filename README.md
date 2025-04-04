# AI_Snake_Game

****Snake Game AI with Deep Q-Learning (using Pytorch)***
This project implements a Snake game AI using Deep Q-Learning. The AI learns to play the game by training a neural network to predict the best moves based on the current state of the game. The model improves over time as it trains, reaching competitive scores in about 10 minutes.

***How to Run the Project***
1. Prerequisites
Before running the project, ensure you have the following installed:
Python 3.7+
Pip (Python package manager)

***2. Install Required Libraries***
Run the following command to install all necessary dependencies:
bash
pip install pygame matplotlib torch torchvision

***3. Project Files***
Make sure all the following files are in the same folder:

agents.py - The main file that trains the AI agent.

game.py - Contains the Snake game logic.

model.py - Defines the neural network and training logic.

helper.py - Contains utility functions for plotting training progress.

***4. Running the Project***
To start training the AI, simply run the agents.py file:
bash
python agents.py

***5. Training Process***
The training process will begin, and you will see logs in the terminal showing:

The current game number.

The score achieved in that game.

The highest score (record) so far.

A live plot will also appear, showing:

Scores from each game.

The average score over time.

The model will start with random moves and gradually improve as it learns from its experiences.

***6. Approximate Training Time***
It takes approximately 10 minutes for the AI to reach a good score (depending on your computer's hardware).

You can stop training anytime by closing the terminal or interrupting execution.

***7. Saved Model***
Once the AI achieves a new high score, it automatically saves the trained model in a folder called model/ as model.pth.

You can use this saved model for inference or further training.

Project Structure
text
project/
│
├── agents.py      # Main script to train the AI agent
├── game.py        # Snake game logic (game environment)
├── model.py       # Neural network and Q-learning trainer
├── helper.py      # Utility functions for plotting
├── model/         # Directory where trained models are saved
└── README.md      # Instructions for running the project

How It Works
State Representation:

The game state is represented as an array of 11 features, including snake direction, food location, and collision risks.

***Neural Network:***
A simple feedforward neural network predicts Q-values (expected rewards) for each possible action: [straight, right turn, left turn].

Training:

Uses Deep Q-Learning with experience replay and a discount factor (gamma) to optimize future rewards.

Exploration vs Exploitation:

Starts with random moves (exploration) and gradually shifts to making decisions based on learned knowledge (exploitation).

Reward System:

+10 for eating food.

-10 for collisions or losing.

Encourages longer survival and higher scores.

Customizing Training Parameters
You can modify hyperparameters like learning rate, batch size, or exploration rate in agents.py:

python
MAX_MEMORY = 100_000    # Replay buffer size
BATCH_SIZE = 1000       # Number of samples per training step
LR = 0.001              # Learning rate
GAMMA = 0.9             # Discount factor for future rewards
Troubleshooting
If you encounter issues with pygame, ensure your Python version is compatible with your operating system.

For performance issues during training, try reducing BATCH_SIZE or increasing SPEED in game.py.
