import torch.nn as nn
import torch

X =torch.tensor([1,2,3,4], dtype=torch.float32)
Y =torch.tensor([2,4,6,8], dtype=torch.float32)

w = torch.tensor([2,4,6,8], requires_grad=True, dtype=torch.float32)

# model prediction
def forward(x):
    return w * x

print(f'Prediction before training: f(5) = {forward(5):.3f}')

## Training 
learning_rate = 0.01
n_iters = 10


## loss 
loss = nn.MSELoss()
optimizer = torch.optim.SGD([w], lr=learning_rate)


for epoch in range(n_iters):
    # prediction = forward pass
    y_pred = forward(X)

    # loss
    l = loss(Y, y_pred)

    # gradient
    l.backward()
## update weights

    optimizer.step()
    # zero gradients

    optimizer.zero_grad()

    if epoch % 1 == 0:
        print(f'epoch {epoch + 1}: w = {w:.3f}, loss = {l:.8f}')


print(f'Prediction After training: f(5) = {forward(5):.3f}')