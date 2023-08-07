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

#Hlavní rozdíl mezi seznamem (list) a nticí (tuple) v Pythonu je, že seznamy jsou měnitelné (mutable), 
#zatímco n-tice jsou neměnitelné (immutable).
#To znamená, že seznamy můžete měnit po jejich vytvoření: můžete přidávat, měnit nebo odstraňovat prvky.

#Na druhou stranu, n-tice, jakmile jsou vytvořeny, nemohou být změněny. 
#Nemůžete přidat, změnit nebo odstranit prvky v n-tici bez vytvoření nové n-tice.

#Díky této vlastnosti jsou n-tice obecně vhodné pro případy, kdy máte kolekci prvků, které se nemají měnit, 
#zatímco seznamy jsou vhodné pro kolekce prvků, které budou pravděpodobně měněny.

