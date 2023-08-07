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

# • What are context managers and when would you use it? Co jsou to context managers a jak byste je použili?

Context managers jsou v Pythonu mechanismy, které umožňují správně a konzistentně alokovat a dealokovat zdroje. 
Nejběžnějším použitím context managerů je při práci se soubory, databázovými připojeními nebo zámky (locks).

V Pythonu je context manager obvykle používán s příkazem with. Klíčovým rysem context managerů je, že automaticky zajistí, 
aby byly zdroje správně uvolněny po opuštění bloku with.

Příklad:
Když pracujete se soubory, můžete použít context manager k otevření souboru, 
čtení nebo zápisu a následně k automatickému zavření souboru po dokončení operace:

#python
with open('myfile.txt', 'r') as f:
    content = f.read()
# Soubor je nyní automaticky uzavřen
Context manager zajistí, že soubor je uzavřen správně, i když dojde k výjimce během zpracování.

Jak vytvořit vlastní context manager:
Můžete vytvořit vlastní context manager implementací dvou metod: __enter__() a __exit__().

__enter__: Tato metoda je volána při vstupu do bloku with. Může vrátit objekt, který je používán v rámci bloku.

__exit__: Tato metoda je volána při opuštění bloku with. Zajistí uvolnění zdrojů a může také řešit výjimky, pokud k nim došlo.

Příklad vlastního context manageru:

#python
class MyContextManager:

    def __enter__(self):
        # Vytvoření a vrácení zdroje
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Uvolnění zdroje
        pass

with MyContextManager() as cm:
    # Práce se zdrojem
    pass
Mimo třídní implementace můžete vytvořit context manager také pomocí generátorů a dekorátoru contextlib.contextmanager z modulu contextlib.

# • When would you implement a custom exception? Kdy byste implementovali vlastní výjimku?


Implementing a custom exception is useful in various situations to make your code more readable, maintainable, and user-friendly. 
Here are some reasons and scenarios when you might want to implement a custom exception:

Domain-Specific Errors: When you're developing domain-specific software, the built-in exceptions might not convey the exact nature 
of the problem. Custom exceptions can help capture specific error conditions related to your domain.

Better Error Messages: Custom exceptions allow you to provide more detailed and specific error messages compared to generic built-in 
exceptions.

#Hierarchical Exceptions: You can create a hierarchy of exceptions to represent errors at different levels of granularity. 
This structure allows callers to catch exceptions at various levels and handle them differently if needed.

Third-party Library Limitations: If you're working with third-party libraries that don't raise specific exceptions for certain error 
conditions, you can create your own exceptions to handle those cases.

#Consistent Error Handling: By defining custom exceptions, you can ensure that errors in your application are handled consistently. 
This approach is particularly useful in larger projects or libraries that are used by multiple applications.

Logging and Monitoring: Custom exceptions can be tailored to include additional information that might be useful for logging or monitoring. 
For instance, you could include debug information, timestamps, or other metadata in your custom exception classes.

Example of a Custom Exception:
Suppose you're building a banking application. You might define a custom exception for when a withdrawal exceeds the available balance:

#python
Copy code
class InsufficientFundsException(Exception):
    def __init__(self, account, amount_requested, balance):
        super().__init__(f"Account {account} does not have sufficient funds. "
                         f"Requested: {amount_requested}, Available: {balance}")
        self.account = account
        self.amount_requested = amount_requested
        self.balance = balance
By creating custom exceptions like InsufficientFundsException, you can provide more detailed information about the error and make it 
easier for other parts of the software (or other developers) to understand and handle specific error scenarios.

Implementace vlastní výjimky je užitečná v různých situacích, aby váš kód byl čitelnější, udržitelnější a uživatelsky přívětivější. 
de je několik důvodů a scénářů, kdy byste mohli chtít implementovat vlastní výjimku:

Specifické chyby v oboru: Pokud vyvíjíte software specifický pro určitý obor, vestavěné výjimky nemusí přesně vyjádřit povahu problému. 
Vlastní výjimky mohou pomoci zachytit specifické chybové stavy související s vaším oborem.

Lepší chybové zprávy: Vlastní výjimky vám umožňují poskytnout podrobnější a specifičtější chybové zprávy ve srovnání 
s obecnými vestavěnými výjimkami.

Hierarchické výjimky: Můžete vytvořit hierarchii výjimek, které reprezentují chyby na různých úrovních granularitu. 
Tato struktura umožňuje zachytávat výjimky na různých úrovních a případně je různě zpracovávat.

Omezení knihovny třetích stran: Pokud pracujete s knihovnami třetích stran, které nevyvolávají specifické výjimky pro určité chybové stavy, 
můžete vytvořit své vlastní výjimky pro tyto případy.

Konsekventní zacházení s chybami: Definováním vlastních výjimek můžete zajistit, že chyby ve vaší aplikaci budou konzistentně zpracovány.
Tento přístup je obzvláště užitečný ve větších projektech nebo knihovnách, které jsou používány více aplikacemi.

Protokolování a monitorování: Vlastní výjimky mohou být přizpůsobeny tak, aby zahrnovaly další informace, které by mohly být užitečné pro protokolování nebo monitorování. Například byste mohli do svých vlastních tříd výjimek zahrnout ladící informace, časová razítka nebo jiná metadata.

Příklad vlastní výjimky:
Představte si, že vytváříte bankovní aplikaci. Mohli byste definovat vlastní výjimku pro případ, kdy výběr překročí dostupný zůstatek:

class NedostatekProstředkůVýjimka(Exception):
    def __init__(self, účet, požadovaná_částka, zůstatek):
        super().__init__(f"Účet {účet} nemá dostatek prostředků. "
                         f"Požadováno: {požadovaná_částka}, Dostupné: {zůstatek}")
        self.účet = účet
        self.požadovaná_částka = požadovaná_částka
        self.zůstatek = zůstatek

Vytvořením vlastních výjimek, jako je NedostatekProstředkůVýjimka, můžete poskytnout podrobnější informace o chybě a usnadnit ostatním 
částem softwaru (nebo jiným vývojářům) pochopení a zacházení se specifickými chybovými scénáři.

Vytvořením vlastních výjimek, jako je NedostatekProstředkůVýjimka, můžete poskytnout podrobnější informace o chybě a usnadnit ostatním 
částem softwaru (nebo jiným vývojářům) pochopení a zacházení se specifickými chybovými scénáři.

# • What are decorators? Please provide at least one example of their usage. Is it possible to stack multiple different decorators?
Co jsou to dekorátory? Vymenujte alespoň jeden příklad jejich použití. Je možné aplikovat více dekorátorů najednou?

Dekorátory jsou v Pythonu mocný nástroj, který umožňuje modifikovat nebo rozšiřovat funkčnost funkcí či tříd bez nutnosti měnit jejich kód. Dekorátor je ve své podstatě funkce, která přijímá funkci (nebo třídu) jako argument a vrací novou funkci (nebo třídu) s rozšířenou nebo modifikovanou funkcionalitou.

Příklad dekorátoru:
Představme si, že chceme měřit dobu běhu našich funkcí:
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkce {func.__name__} běžela {end_time - start_time} sekund.")
        return result
    return wrapper

@timer_decorator
def example_function():
    time.sleep(2)
    print("Funkce dokončena.")

example_function()

#Když spustíte výše uvedený kód, funkce example_function bude "dekorována" funkcí timer_decorator, což způsobí, že při jejím volání 
se vypíše doba jejího běhu.

Aplikace více dekorátorů:
Ano, je možné aplikovat více dekorátorů na jednu funkci. Dekorátory se aplikují ve pořadí od nejspodnějšího k nejvyššímu.

@decorator1
@decorator2
@decorator3
def my_function():
    pass

V tomto příkladu my_function bude nejprve dekorována decorator3, poté decorator2 a nakonec decorator1. 
Můžete si to představit tak, že dekorátor obalí funkci vrstvou za vrstvou, podobně jako cibule.
