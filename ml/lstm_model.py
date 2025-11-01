# ============================================
# 🧠 LSTM MODEL - Predict Price Direction
# ============================================

import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pickle
import os
from utils.logger import logger
from config import Config

class LSTMPredictor(nn.Module):
    """
    LSTM Model dự đoán hướng giá (UP/DOWN)
    
    Input: (batch, seq_len, features)
    Output: (batch, 1) - Probability of UP
    """
    
    def __init__(self, input_size, hidden_size=64, num_layers=2, dropout=0.2):
        super(LSTMPredictor, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # LSTM layers
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0
        )
        
        # Fully connected layers
        self.fc1 = nn.Linear(hidden_size, 32)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)
        self.fc2 = nn.Linear(32, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        """
        Forward pass
        
        Args:
            x: (batch, seq_len, features)
            
        Returns:
            (batch, 1) - Probability
        """
        # LSTM
        lstm_out, (h_n, c_n) = self.lstm(x)
        
        # Lấy hidden state cuối cùng
        last_hidden = h_n[-1]  # (batch, hidden_size)
        
        # FC layers
        out = self.fc1(last_hidden)
        out = self.relu(out)
        out = self.dropout(out)
        out = self.fc2(out)
        out = self.sigmoid(out)
        
        return out

class LSTMTrainer:
    """Training và inference cho LSTM model"""
    
    def __init__(self, input_size, hidden_size=None, num_layers=None):
        self.input_size = input_size
        self.hidden_size = hidden_size or Config.LSTM_HIDDEN_SIZE
        self.num_layers = num_layers or Config.LSTM_NUM_LAYERS
        
        self.model = LSTMPredictor(
            input_size=input_size,
            hidden_size=self.hidden_size,
            num_layers=self.num_layers
        )
        
        self.scaler = MinMaxScaler()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        
        logger.info(f"🧠 LSTM Model initialized on {self.device}")
        logger.info(f"   Input: {input_size}, Hidden: {self.hidden_size}, Layers: {self.num_layers}")
    
    def train(self, X_train, y_train, epochs=None, batch_size=32, lr=0.001):
        """
        Train model
        
        Args:
            X_train: (n_samples, seq_len, features)
            y_train: (n_samples,)
            epochs: Số epochs
            batch_size: Batch size
            lr: Learning rate
        """
        epochs = epochs or Config.LSTM_EPOCHS
        
        # Convert to tensors
        X_tensor = torch.FloatTensor(X_train).to(self.device)
        y_tensor = torch.FloatTensor(y_train).view(-1, 1).to(self.device)
        
        # Loss and optimizer
        criterion = nn.BCELoss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        
        # Training loop
        self.model.train()
        n_batches = len(X_train) // batch_size
        
        logger.info(f"🏋️ Training started: {epochs} epochs, {n_batches} batches/epoch")
        
        for epoch in range(epochs):
            total_loss = 0
            correct = 0
            total = 0
            
            # Shuffle data
            indices = torch.randperm(len(X_train))
            
            for i in range(0, len(X_train), batch_size):
                batch_indices = indices[i:i+batch_size]
                X_batch = X_tensor[batch_indices]
                y_batch = y_tensor[batch_indices]
                
                # Forward
                outputs = self.model(X_batch)
                loss = criterion(outputs, y_batch)
                
                # Backward
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                # Stats
                total_loss += loss.item()
                predicted = (outputs > 0.5).float()
                correct += (predicted == y_batch).sum().item()
                total += y_batch.size(0)
            
            # Epoch stats
            avg_loss = total_loss / n_batches
            accuracy = 100 * correct / total
            
            if (epoch + 1) % 10 == 0:
                logger.info(f"Epoch [{epoch+1}/{epochs}] Loss: {avg_loss:.4f} Acc: {accuracy:.2f}%")
        
        logger.info("✅ Training completed!")
    
    def predict(self, X):
        """
        Predict probability
        
        Args:
            X: (seq_len, features) hoặc (batch, seq_len, features)
            
        Returns:
            float hoặc array: Probability of UP
        """
        self.model.eval()
        
        with torch.no_grad():
            # Ensure 3D input
            if len(X.shape) == 2:
                X = X[np.newaxis, :, :]
            
            X_tensor = torch.FloatTensor(X).to(self.device)
            output = self.model(X_tensor)
            
            return output.cpu().numpy().flatten()
    
    def save(self, model_path=None, scaler_path=None):
        """Lưu model và scaler"""
        model_path = model_path or Config.MODEL_PATH
        scaler_path = scaler_path or Config.SCALER_PATH
        
        # Create directory
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Save model
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'input_size': self.input_size,
            'hidden_size': self.hidden_size,
            'num_layers': self.num_layers
        }, model_path)
        
        # Save scaler
        with open(scaler_path, 'wb') as f:
            pickle.dump(self.scaler, f)
        
        logger.info(f"💾 Model saved to {model_path}")
    
    def load(self, model_path=None, scaler_path=None):
        """Load model và scaler"""
        model_path = model_path or Config.MODEL_PATH
        scaler_path = scaler_path or Config.SCALER_PATH
        
        if not os.path.exists(model_path):
            logger.warning(f"Model file not found: {model_path}")
            return False
        
        # Load model
        checkpoint = torch.load(model_path, map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.model.eval()
        
        # Load scaler
        if os.path.exists(scaler_path):
            with open(scaler_path, 'rb') as f:
                self.scaler = pickle.load(f)
        
        logger.info(f"✅ Model loaded from {model_path}")
        return True

