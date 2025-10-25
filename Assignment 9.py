from pathlib import Path
import csv
import json
from math import pi
from typing import List, Dict, Any, Iterable, Tuple, Optional

# 1) Student
class Student:
    def __init__(self, name: str, age: int, grades: Optional[List[float]] = None) -> None:
        self.name = name
        self.age = age
        self.grades = grades or []

    def add_grade(self, grade: float) -> None:
        if not (0 <= grade <= 100):
            raise ValueError("grade must be between 0 and 100")
        self.grades.append(float(grade))

    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, age={self.age}, grades={self.grades})"


# 2) Employee + CSV
class Employee:
    def __init__(self, name: str, position: str, salary: float) -> None:
        self.name = name
        self.position = position
        self.salary = float(salary)

    def give_raise(self, percent: float) -> None:
        self.salary *= (1 + percent / 100.0)

    @classmethod
    def from_csv_row(cls, row: Dict[str, str]) -> "Employee":
        return cls(
            name=row.get("name", "").strip(),
            position=row.get("position", "").strip(),
            salary=float(row.get("salary", "0") or 0),
        )

    def __repr__(self) -> str:
        return f"Employee(name={self.name!r}, position={self.position!r}, salary={self.salary:,.2f})"


def load_employees_from_csv(path: Path) -> List[Employee]:
    employees: List[Employee] = []
    if not path.exists():
        return employees
    for enc in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            with path.open(newline="", encoding=enc, errors="strict") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        employees.append(Employee.from_csv_row(row))
                    except Exception:
                        continue
            return employees
        except Exception:
            continue
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                employees.append(Employee.from_csv_row(row))
            except Exception:
                continue
    return employees


# 3) BankAccount
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def transfer(self, other: "BankAccount", amount: float) -> None:
        self.withdraw(amount)
        other.deposit(amount)

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance:,.2f})"


# 4) Rectangle
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


# 5) Car
class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = int(year)

    def age(self, current_year: int) -> int:
        return max(0, current_year - self.year)

    def __repr__(self) -> str:
        return f"Car({self.year} {self.make} {self.model})"


# 6) Customer + JSON
class Customer:
    def __init__(self, name: str, email: str, purchases: Optional[List[Dict[str, Any]]] = None) -> None:
        self.name = name
        self.email = email
        self.purchases = purchases or []

    def add_purchase(self, item: str, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.purchases.append({"item": item, "amount": float(amount)})

    def total_spent(self) -> float:
        return sum(p["amount"] for p in self.purchases)

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name, "email": self.email, "purchases": self.purchases}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Customer":
        return cls(name=data.get("name", ""), email=data.get("email", ""), purchases=data.get("purchases", []))

    def __repr__(self) -> str:
        return f"Customer(name={self.name!r}, email={self.email!r}, total_spent={self.total_spent():.2f})"


def load_customers_from_json(path: Path) -> List[Customer]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return [Customer.from_dict(c) for c in data]


def save_customers_to_json(customers: List[Customer], path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in customers], f, indent=2)


# 7) Person
class Person:
    def __init__(self, name: str, age: int, address: str) -> None:
        self.name = name
        self.age = int(age)
        self.address = address

    def update_address(self, new_address: str) -> None:
        self.address = new_address

    def birthday(self) -> None:
        self.age += 1

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age}, address={self.address!r})"


# 8) Circle
class Circle:
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = float(radius)

    def area(self) -> float:
        return pi * self.radius ** 2

    def circumference(self) -> float:
        return 2 * pi * self.radius

    @staticmethod
    def bulk_calculate(radii: Iterable[float]) -> List[Tuple[float, float, float]]:
        results: List[Tuple[float, float, float]] = []
        for r in radii:
            if r > 0:
                c = Circle(r)
                results.append((c.radius, c.area(), c.circumference()))
        return results

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


# 9) Product + CSV
class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def restock(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("restock amount must be non-negative")
        self.quantity += amount

    def sell(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("sell amount must be positive")
        if amount > self.quantity:
            raise ValueError("not enough inventory")
        self.quantity -= amount

    def inventory_value(self) -> float:
        return self.price * self.quantity

    @classmethod
    def from_csv_row(cls, row: Dict[str, str]) -> "Product":
        return cls(
            name=row.get("name", "").strip(),
            price=float(row.get("price", "0") or 0),
            quantity=int(row.get("quantity", "0") or 0),
        )

    def __repr__(self) -> str:
        return f"Product(name={self.name!r}, price={self.price:.2f}, qty={self.quantity})"


def load_products_from_csv(path: Path) -> List[Product]:
    products: List[Product] = []
    if not path.exists():
        return products
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                products.append(Product.from_csv_row(row))
            except Exception:
                continue
    return products


# 10) Movie
class Movie:
    def __init__(self, title: str, director: str, rating: float) -> None:
        self.title = title
        self.director = director
        self.rating = float(rating)

    def update_rating(self, new_rating: float) -> None:
        if not (0 <= new_rating <= 10):
            raise ValueError("rating must be between 0 and 10")
        self.rating = float(new_rating)

    def __repr__(self) -> str:
        return f"Movie(title={self.title!r}, director={self.director!r}, rating={self.rating:.1f}/10)"


# Utilities / Demo
def ensure_sample_files(base: Path) -> Dict[str, Path]:
    base.mkdir(parents=True, exist_ok=True)
    paths = {
        "employee_csv": base / "Employee Data.csv",
        "customers_json": base / "customers.json",
        "products_csv": base / "products.csv",
    }
    if not paths["customers_json"].exists():
        sample_customers = [
            {"name": "Alice Doe", "email": "alice@example.com", "purchases": [{"item": "Book", "amount": 19.99}]},
            {"name": "Bob Ray", "email": "bob@example.com", "purchases": [{"item": "Headphones", "amount": 59.95}]},
        ]
        with paths["customers_json"].open("w", encoding="utf-8") as f:
            json.dump(sample_customers, f, indent=2)
    if not paths["products_csv"].exists():
        with paths["products_csv"].open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
            writer.writeheader()
            writer.writerows(
                [
                    {"name": "USB-C Cable", "price": 9.99, "quantity": 50},
                    {"name": "Laptop Stand", "price": 29.99, "quantity": 20},
                ]
            )
    return paths


def demo() -> Dict[str, Any]:
    base = Path(__file__).parent / "data"
    paths = ensure_sample_files(base)

    s = Student("Nick", 19, [90, 85, 92]); s.add_grade(88)
    employees = load_employees_from_csv(paths["employee_csv"])

    a = BankAccount("Nick", 500); b = BankAccount("Savings", 100); a.transfer(b, 150)
    rect = Rectangle(5, 3)
    car = Car("Honda", "Civic", 2020)

    customers = load_customers_from_json(paths["customers_json"])
    if customers:
        customers[0].add_purchase("Notebook", 4.50)
        save_customers_to_json(customers, paths["customers_json"])

    p = Person("Elena Gilbert", 18, "123 Mystic Ave")
    p.update_address("456 Whitmore Ln")
    p.birthday()

    circles = Circle.bulk_calculate([1, 2.5, 4])

    products = load_products_from_csv(paths["products_csv"])
    if products:
        products[0].sell(5); products[1].restock(10)

    mv = Movie("The Originals", "Julie Plec", 8.7); mv.update_rating(9.1)

    return {
        "student": {"repr": repr(s), "avg": s.average()},
        "employees_loaded": [repr(e) for e in employees] if employees else "No employee CSV found",
        "accounts": {"a": repr(a), "b": repr(b)},
        "rectangle": {"area": rect.area(), "perimeter": rect.perimeter()},
        "car": {"repr": repr(car), "age_from_2025": car.age(2025)},
        "customers": [repr(c) for c in customers],
        "person": repr(p),
        "circles": [{"radius": r, "area": A, "circumference": C} for (r, A, C) in circles],
        "products": [repr(prod) for prod in products],
        "movie": repr(mv),
        "paths": {k: str(v) for k, v in paths.items()},
    }


if __name__ == "__main__":
    print(demo())