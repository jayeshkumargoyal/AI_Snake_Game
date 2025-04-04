# 🐍 AI Snake Game - Deep Q-Learning Implementation

[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An artificial intelligence agent that masters the Snake game using Deep Q-Learning with PyTorch. Achieves competitive performance in just 10 minutes of training.

## Features

- 🧠 Deep Q-Learning with experience replay
- 📊 Real-time training metrics dashboard
- 💾 Auto-saving of best-performing models
- ⚙️ Customizable hyperparameters
- 🔄 Dynamic epsilon-greedy exploration
- ⚡ CUDA acceleration support

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

## Project Structure
### AI_Snake_Game
│
<br> ├── agents.py          # Main training script
<br> ├── game.py            # Game environment logic
<br> ├── model.py           # Q-network implementation
<br> ├── helper.py          # Visualization utilities
<br> ├── model/             # Saved models directory
<br> ├── requirements.txt   # Dependency list
<br> └── README.md          # Project documentation

## How It Works
### State Representation
- The AI observes 11-dimensional state space:
- Current movement direction
- Relative food position (x, y)
- Danger detection in 8 directions
- Body proximity awareness

## Running the Project
To start training the AI, simply run the agents.py file:
<br> python agents.py
