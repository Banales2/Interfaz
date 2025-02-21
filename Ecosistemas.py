from abc import ABC, abstractmethod

class Ecosistema(ABC):
    @abstractmethod
    def getFauna(self):
        pass

    @abstractmethod
    def getFlora(self):
        pass

    @abstractmethod
    def cambioClimatico(self):
        pass

class Fauna(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

class Flora(ABC):
    @abstractmethod
    def Fotosintesis(self):
        pass

class Mono_Araña(Fauna):
    def comer(self):
        return "El mono araña esta comiendo"

    def dormir(self):
        return "El mono araña esta durmiendo"
    
class Tiburon_Blanco(Fauna):
    def comer(self):
        return "El tiburón blanco esta comiendo"

    def dormir(self):
        return "El tiburón blanco esta durmiendo"
    
class Zebra(Fauna):
    def comer(self):
        return "La zebra esta comiendo"

    def dormir(self):
        return "La zebra esta durmiendo"

class Mezquite(Flora):
    def Fotosintesis(self):
        return "El mezquite esta hacinedo fotosíntesis"
    
class Alga_Verde(Flora):
    def Fotosintesis(self):
        return "El alga verde esta hacinedo fotosíntesis"
    
class Acacia(Flora):
    def Fotosintesis(self):
        return "La acacia esta hacinedo fotosíntesis"

class Jungla(Ecosistema):
    def getFauna(self):
        return [Mono_Araña()]
    
    def getFlora(self):
        return [Mezquite()]
    
    def cambioClimatico(self):
        return "Caluroso, muy húmedo y lluvia constante"
    
class Oceano(Ecosistema):
    def getFauna(self):
        return [Tiburon_Blanco()]
    
    def getFlora(self):
        return [Alga_Verde()]
    
    def cambioClimatico(self):
        return "Suave y húmedo, sin extremos de calor o frío"
    
class Savana(Ecosistema):
    def getFauna(self):
        return [Zebra()]
    
    def getFlora(self):
        return [Acacia()]
    
    def cambioClimatico(self):
        return "Soleado, cálido y seco"
    
def main():
    
    ecosistemas = [Jungla(), Oceano(), Savana()]
    
    for ecosistema in ecosistemas:
        print(f"Fauna en {ecosistema._class.name_}:")
        for animal in ecosistema.getFauna():
            print(f" - {animal.comer()}")
            print(f" - {animal.dormir()}")
        
        print(f"Flora en {ecosistema._class.name_}:")
        for planta in ecosistema.getFlora():
            print(f" - {planta.Fotosintesis()}")
        
        print(f"Clima en {ecosistema._class.name_}:")
        print(f" - {ecosistema.cambioClimatico()}")
        print()

if _name_ == "_main_":
    main()