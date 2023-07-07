import torch
import torch.nn as nn
import torch.optim as optim


# Define the DQN architecture
class DQN(nn.Module):
    def __init__(self, input_size, output_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# Define the Federated Averaging algorithm
def federated_averaging(parties, num_epochs, learning_rate):
    global_model = DQN(input_size, output_size)
    global_model.train()

    for epoch in range(num_epochs):
        local_models = []
        local_losses = []

        # Local training on each party
        for party in parties:
            local_model = DQN(input_size, output_size)
            local_model.train()
            optimizer = optim.SGD(local_model.parameters(), lr=learning_rate)

            # Training loop for each party
            for i in range(num_local_epochs):
                # Obtain local dataset and perform training
                local_data = party.get_data()
                local_states, local_actions, local_rewards, local_next_states = local_data

                # Compute Q-values
                q_values = local_model(local_states)
                q_values = q_values.gather(1, local_actions.unsqueeze(1)).squeeze(1)

                # Compute target Q-values using the global model
                with torch.no_grad():
                    target_q_values = local_rewards + gamma * global_model(local_next_states).max(1)[0]

                # Compute the loss and perform gradient descent
                loss = nn.MSELoss()(q_values, target_q_values)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                local_losses.append(loss.item())

            local_models.append(local_model)

        # Perform aggregation of local models to update the global model
        global_model.load_state_dict(
            sum([local_model.state_dict() for local_model in local_models]) / len(local_models))

        # Print average loss for this epoch
        print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {sum(local_losses) / len(local_losses):.4f}")

    return global_model


# Usage example
input_size = 4
output_size = 2
num_epochs = 10
learning_rate = 0.001
num_local_epochs = 5
gamma = 0.99

parties = [...]  # List of parties with their respective dataset

global_model = federated_averaging(parties, num_epochs, learning_rate)

# Save or use the trained global model as desired
