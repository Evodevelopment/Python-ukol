Dependency Injection (DI) je návrhový vzor, který umožňuje objektům přijímat závislosti (jiné objekty, které potřebují ke svému běhu) 
místo toho, aby si je samy vytvářely. Tímto způsobem můžete dosáhnout lepší modularity a oddělení zájmů v aplikacích.

Samozřejmě, rád vám pomohu!

**Dependency Injection** (DI) je návrhový vzor, který umožňuje objektům přijímat závislosti (jiné objekty, které potřebují ke svému běhu) místo toho, aby si je samy vytvářely. Tímto způsobem můžete dosáhnout lepší modularity a oddělení zájmů v aplikacích.

Důvody pro použití DI:

1. **Oddělení zájmů**: Objekty se nemusí starat o vytváření a řízení svých závislostí.
2. **Zvýšená testovatelnost**: Můžete jednoduše vkládat mock (simulované) objekty pro testování.
3. **Flexibilita a rozšiřitelnost**: Závislosti můžete měnit bez změny třídy, která je používá.

Zde je jednoduchý příklad Dependency Injection v Pythonu:

```python
class LightBulb:
    def turn_on(self):
        print("Světlo se rozsvítilo")

    def turn_off(self):
        print("Světlo zhaslo")

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        print("Ovládání světla")
        self.bulb.turn_on()

# Použití:
bulb = LightBulb()
switch = Switch(bulb)
switch.operate()
```

V tomto příkladu je třída `Switch` závislá na třídě `LightBulb`. Místo toho, aby třída `Switch` vytvořila instanci třídy `LightBulb` sama, přijímá ji jako závislost přes konstruktor (`__init__`). To je základní forma Dependency Injection.

Pokud byste chtěli použít knihovnu pro Dependency Injection v Pythonu, můžete se podívat na knihovny jako `injector` nebo `dependency_injector`.

Doufám, že to pomáhá! Máte ještě další otázky k tomuto tématu?
