from abstract_factory import Rugs

class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate
    
    def exchange(self, product):
        return self.rate * product._price

if __name__ == "__main__":
    r1 = Rugs('persian rugs', 20)
    r2 = Rugs('nain rugs', 23)
    r3 = Rugs('morrocco rugs', 19)

    adapter =PriceAdapter(rate=28000)

    rugs = [r1, r2, r3]
    
    for rug in rugs:
        print(f"{rug._name}: {adapter.exchange(rug)}")