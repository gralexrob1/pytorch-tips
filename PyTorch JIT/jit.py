import torch
import torch.nn as nn


class Model(nn.Module):
    def __init__(self):
        super().__init__()

        self.linears = nn.ModuleList(
            [
                nn.Linear(8, 16),
                nn.Linear(16, 2),
            ]
        )

    def forward(self, x):
        for linear in self.linears:
            x = linear(x)
        return x


input = torch.randn(10, 8)
model = Model()
output = model(input)

traced_model = torch.jit.trace(model, input)
traced_model.save("traced_model.pt")

scripted_model = torch.jit.script(model)
scripted_model.save("scripted_model.pt")
