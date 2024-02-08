# pytorch-tips


### ModuleDict/ModuleList  

```torch.nn.ModuleDict``` and ```torch.nn.ModuleList``` let you organize layers in PyTorch models efficiently. 

```ModuleList``` is a list of layers you can loop through or access by index, useful when the order matters. 

```ModuleDict``` is like a dictionary for layers, where you can use names as keys to add or find layers. This is handy when you need to change parts of your model on the fly without restructuring the whole thing.

**Benefits**  
Simplifies adding/removing layers in neural networks.

**Impact**  
Accelerates model iteration and development speed.

**Use Case**  
Adapts architectures for different input sizes automatically.