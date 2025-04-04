# 🐍 AI Snake Game

A **Snake Game AI** powered by **Deep Q-Learning**, implemented using **PyTorch**. The AI trains itself by learning to predict optimal moves based on the current game state, improving over time and reaching impressive scores within minutes of training.

---

## 🚀 Features
- Deep Q-Learning with experience replay
- Simple feedforward neural network
- Live training visualization
- Model saving and loading
- Fully playable snake environment using Pygame

---

## 📁 Project Structure
AI_Snake_Game/ │ ├── agents.py # Main script to train the AI agent ├── game.py # Snake game logic (game environment) ├── model.py # Neural network and Q-learning trainer ├── helper.py # Utility functions for plotting ├── model/ # Directory where trained models are saved └── README.md # Instructions for running the project

---

## 🛠️ How to Run

### 1. Prerequisites
Make sure you have the following installed:
- Python 3.7+
- pip (Python package manager)

### 2. Install Dependencies
Run the following command to install required libraries:

```bash
pip install pygame matplotlib torch torchvision
