import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

class Linear_QNet(nn.Module):
    """
    Neural Network Architecture for Q-Learning
    Structure: Input Layer → Hidden Layer (ReLU) → Output Layer
    """
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        # Network layers
        self.linear1 = nn.Linear(input_size, hidden_size)   # Input to hidden
        self.linear2 = nn.Linear(hidden_size, output_size)  # Hidden to output

    def forward(self, x):
        x = F.relu(self.linear1(x))  # ReLU activation for non-linearity
        x = self.linear2(x)           # Raw Q-values output
        return x

    def save(self, file_name='model.pth'):
        """
        Saves model weights to ./model directory
        """
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)


class QTrainer:
    """
    Q-Learning Trainer with Experience Replay
    Implements:
    - Bellman equation updates
    - MSE loss optimization
    - Batch training support
    """
    def __init__(self, model, lr, gamma):
        # Hyperparameters
        self.lr = lr          # Learning rate
        self.gamma = gamma    # Discount factor
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        """
        Performs single training step with Q-learning update rule
        
        Args:
            state: Current game state
            action: Taken action
            reward: Received reward
            next_state: Subsequent game state
            done: Game termination flag
        """
        # Convert to tensors and ensure proper dimensions
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        # (n, x)

        # Handle single sample vs batch
        if len(state.shape) == 1:
            # (1, x)
            # Add batch dimension (n_samples, n_features)
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, )

        # 1: predicted Q values with current state
        pred = self.model(state)

        target = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))

            target[idx][torch.argmax(action[idx]).item()] = Q_new
    
        # 2: Q_new = r + y * max(next_predicted Q value) -> only do this if not done
        # pred.clone()
        # preds[argmax(action)] = Q_new
        
        # Optimization step
        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)  # MSE between targets and predictions
        
        loss.backward()         # Backpropagation
        self.optimizer.step()   # Update weights