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
