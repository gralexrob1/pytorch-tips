# Pytorch JIT

Model inference can be slow due to Python's overhead in PyTorch. A powerful way to optimizer performance is to use **Just In Time (JIT) compilation**, allowing models to be converted into a format optimized for production environment, independent of Python runtime.

JIT converts the model into **TorchScript** by either **tracing** or **scripting** it. Once transformed the model can be run independently of the Python environment.

- **Tracing** captures the operations performed during a forward pass, resulting in a static computational graph.

- **Scripting** converts the model directly into TorchScript by inspecting Python code, allowing for more complex operations like conditionals and loops.
