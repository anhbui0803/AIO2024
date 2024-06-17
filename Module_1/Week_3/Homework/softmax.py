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

    # data1 = torch.Tensor([1, 2, 3])
    # softmax_func = nn.Softmax(dim=0)
    # output1 = softmax_func(data1)
    # assert round(output1[0].item(), 2) == 0.09
    # print(output1)  # [0.0900, 0.2447, 0.6652]

    # data2 = torch.Tensor([5, 2, 4])
    # softmax = Softmax()
    # output2 = softmax(data2)
    # assert round(output2[-1].item(), 2) == 0.26
    # print(output2)  # [0.7054, 0.0351, 0.2595]

    # data3 = torch.Tensor([1, 2, 300000000])
    # output3 = softmax(data3)
    # assert round(output3[0].item(), 2) == 0.0
    # print(output3)  # [0., 0., nan]

    # softmax_stable = SoftmaxStable()
    # output4 = softmax_stable(data1)
    # assert round(output4[-1].item(), 2) == 0.67
    # print(output4)  # [0.0900, 0.2447, 0.6652]
