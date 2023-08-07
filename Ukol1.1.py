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

# • What are dunder/magic methods? Provide and briefly describe few of them. 
# Co jsou to dunder/magické metody? Vyjmenujte a stručně popište pár z nich.

#"Dunder" metody (zkratka pro "double underscore" metody) nebo také "magické" metody jsou speciální metody v Pythonu, které mají dvojité podtržítka na začátku i konci jejich názvů (např. __init__, __call__). Tyto metody umožňují implementovat a upravit vlastní chování určitých operátorů a funkcí pro vlastní třídy.

Několik častých dunder/magických metod:

__init__(self, ...):

Konstruktor třídy. Volá se, když je vytvořena nová instance třídy.
__str__(self):

Vrací reprezentaci objektu jako řetězec. Volá se například při použití funkce print() na objektu.
__repr__(self):

#Vrací "oficiální" reprezentaci objektu. Ideálně by měla vracet řetězec, který, pokud by byl předán funkci eval(), vytvoří objekt stejného typu s týmiž daty.
__add__(self, other):

Umožňuje definovat vlastní chování pro operátor +.
__eq__(self, other):

Umožňuje definovat vlastní chování pro operátor ==.
__len__(self):

Vrací délku objektu, pokud má smysl. Volá se při použití funkce len() na objektu.
__getitem__(self, key):

Umožňuje přístup k položkám objektu pomocí hranatých závorek, např. obj[key].
__setitem__(self, key, value):

Umožňuje nastavení hodnoty položky pomocí hranatých závorek, např. obj[key] = value.
__call__(self, ...):

Umožňuje "volat" instanci třídy jako funkci.
__del__(self):

Destruktor, volá se, když je instance třídy zničena.
Tyto metody poskytují mocnou možnost modifikace chování objektů a poskytují Pythonu jeho charakteristickou flexibilitu a dynamiku.


#What are, and how would you implement private, protected, and public class attributes in Python? 
What about class inheritance when using them?
Co jsou a jak byste implementovali privátní, chráněné, a veřejné atributy třídy v Pythonu? 
Co jejich použití znamená pro třídní dědičnost?

V Pythonu je konvence pro definování privátních, chráněných a veřejných atributů třídy založena na prefixech:

Veřejné atributy:

Standardní atributy třídy bez jakýchkoli prefixů.

Přístupné odkudkoli.

Příklad: my_attribute

python
Copy code
class MyClass:
    def __init__(self):
        self.my_attribute = "I'm public!"
Chráněné atributy:

Atributy s jedním podtržítkem jako prefix.

Konvence naznačuje, že by neměly být přímo přistupovány mimo třídu, ale technicky jsou stále přístupné.

Příklad: _my_protected_attribute

python
Copy code
class MyClass:
    def __init__(self):
        self._my_protected_attribute = "I'm protected!"
Privátní atributy:

Atributy s dvojitým podtržítkem jako prefix.

Python změní název těchto atributů, aby je skutečně "skryl" (name mangling).

Tyto atributy nejsou snadno přístupné z vnějšího kódu, ale stále je možné je získat pokud víte, jak.

Příklad: __my_private_attribute

python
Copy code
class MyClass:
    def __init__(self):
        self.__my_private_attribute = "I'm private!"
Dědičnost:

Veřejné atributy: Dědí se a jsou volně přístupné v potomkovských třídách.

Chráněné atributy: Dědí se a by měly být přístupné pouze v potomkovských třídách (ačkoli v Pythonu je stále technicky možné 
je přistupovat odkudkoli).

Privátní atributy: Dědí se, ale díky name manglingu nejsou přímo přístupné v potomkovských třídách (musíte znát změněný název).

Je důležité si uvědomit, že v Pythonu je vše založeno na důvěře a konvencích. 
I když můžete použít chráněné a privátní atributy, Python nesnaží skrýt je silně, jak je tomu v některých jiných jazycích. 
Místo toho Python spoléhá na konvenci "jsme všichni dospělí zde" 
a očekává se, že vývojáři budou respektovat hranice nastavené těmito konvencemi.


