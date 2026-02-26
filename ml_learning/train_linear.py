import torch
import torch.nn as nn
import torch.optim as optim

# synthetic data y=2x
def generate_data(n=100):
    x = torch.randn(n, 1)
    y = 2 * x
    return x, y

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


if __name__ == "__main__":
    model = SimpleModel()
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    x_train, y_train = generate_data(1000)
    for epoch in range(50):
        optimizer.zero_grad()
        preds = model(x_train)
        loss = criterion(preds, y_train)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, loss {loss.item():.4f}")

    # print learned parameters
    for name, param in model.named_parameters():
        print(name, param.data)
