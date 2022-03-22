from abc import abstractmethod
class Musician:
    """
It's a template class that any type of musician will inherit.
    """
    def __init__(self):
        self.name = ""
        self.instrument = ""
    @abstractmethod
    def __str__(self):
        pass 
    @abstractmethod
    def __repr__(self):
        pass
    @abstractmethod
    def get_instrument(self):
        pass
    @abstractmethod
    def play_solo(self):
        pass
class Guitarist(Musician):
    """
It's a subclass that generates a guitar-playing musician.
    """
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def get_instrument(self):
        return self.instrument
    def play_solo(self):
        return "face melting guitar solo"
class Drummer(Musician):
    """
It's a subclass that gives you the ability to play the drums.
    """
    def __init__(self, name):
        self.name = name
        self.instrument = "drums"
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return self.instrument
    def play_solo(self):
        return "rattle boom crash"
class Bassist(Musician):
    """
It's a subclass that gives you the ability to play bass.
    """
    def __init__(self, name):
        self.name = name
        self.instrument = "bass"
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return self.instrument
    def play_solo(self):
        return "bom bom buh bom"
class Band:
    """
It's a class that assembles a band from the available musicians.
    """
    name, members, instances = "", [], []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def play_solos(x):
        return [member.play_solo() for member in x.members]
    @classmethod
    def to_list(x):
        return x.instances