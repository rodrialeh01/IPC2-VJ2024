from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass