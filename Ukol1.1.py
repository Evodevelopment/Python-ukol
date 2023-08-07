• What is dependency injection and how would you implement it? 
Co to je dependency injection a jak byste ji implementovali?

Dependency Injection (DI) je návrhový vzor používaný v objektově orientovaném programování, který se týká způsobu, 
jakým jsou komponenty (nebo objekty) aplikace poskytovány závislostem. Místo toho, aby komponenta vytvářela svou závislost nebo 
získávala závislost z globálního stavu, je jí závislost "injektována" (poskytnuta) z vnějšku, často přes konstruktor, metodu nebo vlastnost.

DI pomáhá dosáhnout:

Větší modularity a oddělení zájmů.
Zvýšené testování, protože závislosti mohou být snadno nahrazeny mock objekty.
Snížení závislosti na konkrétních implementacích tříd.
Jak implementovat Dependency Injection:

Ruční injektáž: Nejjednodušší forma DI. Závislost je vytvořena mimo třídu a poté je předána třídě prostřednictvím konstruktoru nebo metody.
DI kontejnery: To jsou nástroje/frameworky, které automatizují vytváření a vkládání závislostí.

Příklad ruční injektáže v Pythonu:
class Database:
    def fetch_data(self):
        return "Some data from the database"

class Service:
    def __init__(self, db):
        self._db = db

    def get_data(self):
        return self._db.fetch_data()

# Vytvoření instance Database třídy
db_instance = Database()

# Injektáž závislosti do Service třídy
service = Service(db_instance)
print(service.get_data())

V tomto příkladu je Database závislostí třídy Service. Místo toho, aby Service vytvořila svoji vlastní instanci Database, 
je jí instance poskytnuta z vnějšku přes konstruktor.

Existují různé DI frameworky pro Python, které mohou usnadnit a automatizovat injektáž závislostí, 
např. injector nebo dependency_injector.


#• What is the difference between instance, static, and class method? Jaký je rozdíl mezi instanční, statickou a třídní metodou?

V Pythonu můžeme definovat tři různé typy metod v rámci třídy: instanční metody, statické metody a třídní metody. Každá z nich má svůj vlastní účel a způsob, jakým se chová v rámci třídy:

Instanční metoda:

Nejběžnější typ metody.

Přijímá instanci třídy jako svůj první argument (zvykle nazývaný self).

Může měnit stav objektu a také může měnit třídní stav.

#python
Copy code
class MyClass:
    def inst_method(self, arg1, arg2):
        pass
Statická metoda:

Deklarována pomocí dekorátoru @staticmethod.

Nepřijímá žádné speciální první argument (ani self ani cls).

Nemůže měnit stav objektu ani třídní stav, protože nemá přístup k žádnému z nich.

Funguje spíše jako běžná funkce, ale je vázána na třídu kvůli své logice.

#python
Copy code
class MyClass:
    @staticmethod
    def static_method(arg1, arg2):
        pass
Třídní metoda:

Deklarována pomocí dekorátoru @classmethod.

Přijímá třídu jako svůj první argument místo instance (zvykle nazývaný cls).

Může měnit třídní stav, ale nemůže měnit stav jednotlivých instancí třídy.

#python
Copy code
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2):
        pass
Kdy je vhodné použít který typ metody?

Instanční metody jsou vhodné, když potřebujete pracovat s instancemi a jejich atributy.
Statické metody se používají, když chcete provádět nějakou funkci, která nezávisí na instančních ani třídních atributech.
Třídní metody se často používají, když potřebujete pracovat s třídními atributy nebo když potřebujete vytvořit alternativní konstruktory.
