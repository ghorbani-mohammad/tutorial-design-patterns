from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def calculate_tax(self) -> int:
        pass


class ProductA(Product):
    def calculate_tax(self) -> int:
        return 10


obj = ProductA()
print(obj.calculate_tax())
