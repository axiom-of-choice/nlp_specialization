class BaseLayer:
    def __init__(self, name='') -> None:
        self.name = name
    
    def __repr__(self) -> str:
        return f"{self.name} Layer"
    
class ActivationLayer(BaseLayer):
    def __init__(self, size) -> None:
        super().__init__("Activation")
        self.size = size

class FCLayer(BaseLayer):
    def __init__(self, size) -> None:
        super().__init__("FullyConnected")
        self.size = size
        
#print(ActivationLayer.name)
#print(BaseLayer)
print(ActivationLayer(23).name)