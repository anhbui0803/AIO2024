import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        return exp_x / torch.sum(exp_x)


if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    print(softmax(data))

    softmax_stable = SoftmaxStable()
    print(softmax_stable(data))
