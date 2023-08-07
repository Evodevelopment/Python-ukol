#Mutable / Immutable
# • Name at least three mutable and immutable built-in types.
#   Vyjmenuj alespoň tři “proměnlivé” (mutable) a “nezměnitelné” (immutable) vestavěné (built-in) typy.

Řešení:
#Proměnné typy jsou takové, které umožňují měnit obsah "na místě" (in-place). Na druhou stranu, nezměnitelné typy neumožňují změny 
#existujících objektů, ale vždy, když je provedena změna, vytvoří se nový objekt.

Proměnné (mutable) vestavěné typy v Pythonu:

Seznamy (Lists)
Slovníky (Dictionaries)
Množiny (Sets)
Byte Arrays
Třídy (Classes) - pokud jsou definovány uživatelem, mohou být také měněny
Nezměnitelné (immutable) vestavěné typy v Pythonu:

Celá čísla (Integers)
Desetinná čísla (Floats)
Řetězce (Strings)
Ntice (Tuples)
Množiny s pevnou hodnotou (Frozen sets)

# • What is a difference between list and tuple? 
#   Jaký je rozdíl mezi list a tuple?

Reseni:
#Hlavní rozdíl mezi seznamem (list) a nticí (tuple) v Pythonu je, že seznamy jsou měnitelné (mutable), 
#zatímco n-tice jsou neměnitelné (immutable).
#To znamená, že seznamy můžete měnit po jejich vytvoření: můžete přidávat, měnit nebo odstraňovat prvky.

#Na druhou stranu, n-tice, jakmile jsou vytvořeny, nemohou být změněny. 
#Nemůžete přidat, změnit nebo odstranit prvky v n-tici bez vytvoření nové n-tice.

#Díky této vlastnosti jsou n-tice obecně vhodné pro případy, kdy máte kolekci prvků, které se nemají měnit, 
#zatímco seznamy jsou vhodné pro kolekce prvků, které budou pravděpodobně měněny.

What happens if you pass an argument to a function and modify the argument inside? 
Will the value of this argument be changed after calling this function? (See also the second example in section Code Snippets.)
Co se stane, pokud předáte argument do funkce a uvnitř ho změníte? 
Změní se hodnota tohoto argumentu po zavolání dané funkce? (viz druhý příklad v sekci Code Snippets.)

Reseni:
#Odpověď na tuto otázku závisí na tom, zda je argument, který předáváte funkci, měnitelný (mutable) nebo neměnitelný (immutable).

#Pokud je argument neměnitelný (jako například číslo, řetězec nebo n-tice), jakoukoli změnu hodnoty tohoto argumentu uvnitř funkce neovlivní hodnotu argumentu mimo funkci. 
#To je proto, že neměnitelné typy vytvářejí nový objekt, když je provedena změna.

#Pokud je argument měnitelný (jako například seznam, slovník nebo množina), změny provedené uvnitř funkce ovlivní hodnotu argumentu mimo funkci. 
#To je proto, že měnitelné typy umožňují změny "na místě" (in-place).

#Toto je známé jako koncept "předávání odkazů" (pass by reference) pro měnitelné objekty a "předávání hodnot" (pass by value) 
#pro neměnitelné objekty v Pythonu, ačkoli technicky vzato Python vždy předává odkaz na objekt (tj., je to vždy "pass by reference"), 
#ale u neměnitelných objektů tento odkaz ukazuje na nový objekt po jakékoliv změně.

Shallow / Deep Copy
• What is a difference between shallow1 and deep copy2 of an object in Python? 
Jaký je rozdíl mezi shallow a deep kopií v Pythone?

Reseni:
V Pythonu existují dva typy kopírování objektů: mělká kopie (shallow copy) a hluboká kopie (deep copy). 

1. **Mělká kopie (Shallow Copy)**: Vytvoření mělké kopie objektu znamená vytvoření nového objektu, který je kopie původního objektu. 
Oba objekty (původní a kopie) sdílejí stejné hodnoty a změny v jednom objektu se projeví i v druhém. 
Toto je proto, že mělká kopie vytvoří nový objekt a poté do něj vloží odkazy na původní objekty.

2. **Hluboká kopie (Deep Copy)**: Na druhou stranu, hluboká kopie vytváří nový objekt a rekurzivně vkládá kopie původních objektů do něj. 
Na rozdíl od mělké kopie, hluboká kopie vytvoří nové objekty pro všechny hodnoty v původním objektu, takže původní a kopírovaný objekt 
mohou být měněny nezávisle na sobě.

Jednoduše řečeno, mělká kopie vytváří nový objekt, který sdílí odkazy na vnořené objekty s původním objektem. 
Hluboká kopie vytváří nový objekt a rekurzivně kopíruje všechny vnořené objekty. 
Proto jsou změny v hluboké kopii nezávislé na původním objektu.

#V Pythonu můžete vytvořit mělkou kopii pomocí metody `copy()` a hlubokou kopii pomocí metody `deepcopy()` z modulu `copy`.

Concurrent Computation in Python
• What are the possibilities of implementing concurrent computation that Python offers? Briefly describe them.
Jaké možnosti nabízí Python pro implementování konkurentních výpočtů? Stručně je popište.

Python poskytuje několik možností pro implementaci konkurenčního programování. Zde jsou některé z nich:

Threading: Modul threading v Pythonu se používá pro vícevláknové programování, což je technika, 
která umožňuje pro výkon více operací současně. V Pythonu, kvůli globálnímu interpretu zámku (GIL), 
vlákna nejsou skutečně prováděna současně, jsou multiplexována mezi jednotlivými jádry na procesoru. 
Tato metoda je obzvláště užitečná pro I/O-bound úlohy.

Multiprocessing: Modul multiprocessing umožňuje vytváření procesů. Každý proces v Pythonu má vlastní Python interpreter 
a každý proces má svůj vlastní samostatný paměťový prostor, takže procesy nejsou ovlivněny GIL. To znamená, 
že můžeme dosáhnout skutečného paralelního zpracování a konkrétního zlepšení výkonu pro CPU-bound úlohy.

Asyncio: Tento modul umožňuje psaní jednovláknových konkurenčních programů pomocí asynchronních I/O operací. 
Asyncio poskytuje infrastrukturu pro vytváření a správu korutin (asynchronních funkcí), které umožňují efektivní 
multitasking pomocí jediného vlákna.

Concurrent.futures: Tento modul poskytuje vysokoúrovňové rozhraní pro asynchronní spouštění volání funkcí pomocí threading
nebo multiprocessing. Modul poskytuje třídy ThreadPoolExecutor a ProcessPoolExecutor, které umožňují paralelní a konkurenční 
spuštění funkcí.

Greenlet a Gevent: Greenlet je nízkoúrovňová knihovna pro přepínání kontextu v Pythonu, zatímco Gevent je knihovna 
pro síťové I/O operace, která používá greenlet pro poskytnutí vysokoúrovňového, synchronního API na vrchu libevent event loop.

Tyto nástroje lze použít samostatně nebo kombinovat, v závislosti na konkrétních potřebách vaší aplikace.



