
"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""

"""
1) Create class User with:
    name,
    method say_hi() which prints "Hello, I am {name}"
"""


"""
2) BankAccount
Create class `BankAccount` with:
- `__init__(self, owner: str, balance: float = 0.0) -> None`
- `deposit(self, amount: float) -> None`
- `withdraw(self, amount: float) -> None`
Rules:
- Initial negative balance becomes `0.0`.
- Non-positive `deposit`/`withdraw` amounts are ignored.
- `withdraw` bigger than current balance is ignored.
"""


"""
3) Team
Create class `Team` with:
- `__init__(self) -> None`
- `add(self, name: str) -> None`
- `__len__(self) -> int`
Rules:
- Members are stored in insertion order.
- Each instance has independent member storage.
"""

""" (Advanced, optional)
5) QueueState
Create class `QueueState`:
- `__init__(self) -> None` (initialize empty `items` list)
Methods:
- `push(self, item: str) -> None`
- `pop(self) -> str | None`
Rules:
- FIFO behavior.
- `pop` returns `None` when empty.
"""


""" (Advanced, optional)
6) Wallet + custom errors
Create:
- `class PaymentError(Exception): ...`
- `class InsufficientFunds(PaymentError): ...`
- `class Wallet` with:
  - `__init__(self, balance: float = 0.0) -> None`
  - `top_up(self, amount: float) -> None`
  - `pay(self, amount: float) -> None`
Rules:
- Initial balance must be >= 0.
- `top_up` and `pay` require amount > 0.
- If `pay` exceeds balance, raise `InsufficientFunds`.
"""


"""
7) ShoppingCart
Create class `ShoppingCart` with:
- `__init__(self) -> None`
- `add_item(self, name: str, price: float, qty: int = 1) -> None`
- `total_items(self) -> int`
- `total_price(self) -> float`
Rules:
- `price < 0` or `qty <= 0` items are ignored.
- `repr` must include `ShoppingCart`.
"""


"""
8) Classroom (class attribute)
Create class `Classroom` with class attribute:
- `school_name = "Harbour Space"`
Methods:
- `__init__(self, group_name: str) -> None`
- `add_student(self, name: str) -> None`
- `__len__(self) -> int`
- `set_school_name(self, new_name: str) -> None`
Rules:
- `set_school_name` must update shared class attribute for all instances.
"""


"""
9) Rectangle
Create class `Rectangle` with:
- `__init__(self, width: float, height: float) -> None`
- `area(self) -> float`
- `perimeter(self) -> float`
Rules:
- Store positive dimensions using absolute values.
"""


"""
10) Playlist
Create class `Playlist` with:
- `__init__(self) -> None`
- `add(self, song: str) -> None`
- `__len__(self) -> int`
- `__iter__(self)`
- `__contains__(self, song: str) -> bool`
Rules:
- Preserve insertion order.
"""


"""
11) Product
Create class `Product` with:
- `__init__(self, name: str, price: float) -> None`
- `get_price(self) -> float`
- `set_price(self, value: float) -> None`
- `apply_discount(self, percent: float) -> None`
Rules:
- Negative price is clamped to `0`.
- Discount percent is clamped to `[0, 100]`.
"""


"""
12) Person + Student (inheritance)
Create:
- `class Person` with `__init__(name)` and `describe()`
- `class Student(Person)` with `__init__(name, group)` and overridden `describe()`
Required format:
- `Person(name=Ana)`
- `Student(name=Bo, group=G2)`
"""
"""


"""
"""
13) Point2D (magic methods)
Create class `Point2D` with:
- `__init__(self, x: float, y: float) -> None`
- `distance_to(self, other: "Point2D") -> float`
- `__eq__(self, other: object) -> bool`
Rules:
- Euclidean distance.
- `repr` format: `Point2D(x, y)`.
"""


"""
14) Inventory
Create class `Inventory` with:
- `__init__(self) -> None`
- `add(self, name: str, qty: int = 1) -> None`
- `remove(self, name: str, qty: int = 1) -> None`
- `count(self, name: str) -> int`
- `__contains__(self, name: str) -> bool`
- `__len__(self) -> int`
Rules:
- Non-positive `qty` is ignored.
- Removing too much removes item completely (count becomes `0`).
"""


"""
15) CourseCatalog
Create class `CourseCatalog` with:
- `__init__(self) -> None`
- `add_course(self, code: str, title: str) -> None`
- `get_title(self, code: str) -> str | None`
- `__iter__(self)` returning `(code, title)` sorted by code
- `__len__(self) -> int`
"""


"""
16) DefaultDict (magic methods)
Create class `DefaultDict` with:
- `__init__(self, default_factory=None) -> None`
- `__getitem__(self, key)`
- `__setitem__(self, key, value) -> None`
- `__contains__(self, key) -> bool`
- `__len__(self) -> int`
Rules:
- On missing key:
  - if `default_factory` is `None`, return `None`.
  - otherwise create value using `default_factory()`, store, return.
- If `default_factory` is not callable, treat it as `None`.
"""
#1
class User:
  def __init__(self, name):
    self.name = name

  def say_hi(self):
        print(f"Hello, I am {self.name}")

#2
class BankAccount:
  def __init__(self,owner,balance):
    self.owner = owner
    if balance >= 0:
      self.balance = balance
    else:
      self.balance = 0.0
      
      
  def deposit(self,amount):
    if amount > 0: 
      self.balance += amount
    
    
  def withdraw(self,amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= amount

#3
class Team:
  def __init__(self):
    self.store = []
  
  def add(self,name):
    self.store.append(name)
    
  def __len(self):
    return len(self.store)
        
        
#7
class ShopingCart:
  def __init__(self):
    self.total_qty = 0
    self.total_pric = 0
    
  def add_item(self,name,price,qty):
    if price < 0 or qty <= 0:
      return
    self.total_qty += qty
    self.total_pric += price * qty
    
  def total_items(self):
    return self.total_qty
  
    
  def total_price (self):
    return self.total_pric
  
  def __repr__(self):
    return "ShopingCart"



#8
class Classroom:
    school_name = "Harbour Space" 

    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def __len__(self):
        return len(self.students)

    def set_school_name(self, new_name):
        Classroom.school_name = new_name
  
#9
class Rectangle:
  def __init__(self,width,height):
        if height >= 0 and width >= 0:
          self.width = width
          self.height = height
  
  def area(self):
    self.a = self.width * self.height
    return self.a
  
  def perimeter(self):
    self.p = (self.width + self.height) * 2
    return self.p

    
#10
class Playlist:
 def __init__(self):
  self.songs = []

 def add(self, song):
  self.songs.append(song)

 def __contains__(self, song):
  return song in self.songs

 def __len__(self):
  return len(self.songs)

 def __iter__(self):
  return iter(self.songs)


#11
class Product:
  def __init__(self, name, price):
    self.name = name
    if price < 0:
      self.price = 0.0
    else:
      self.price = price

  def get_price(self):
    return self.price

  def set_price(self, value):
    if value < 0:
      self.price = 0.0
    else:
      self.price = value

  def apply_discount(self, percent):
    if percent < 0:
      percent = 0.0
    elif percent > 100:
      percent = 100.0

    discount_amount = self.price * (percent / 100)
    self.price = self.price - discount_amount

#12
class Person:
  def __init__(self, name):
    self.name = name

  def describe(self):
    return f"Person(name={self.name})"


class Student(Person):
  def __init__(self, name, group):
    super().__init__(name)
    self.group = group

  def describe(self):
    return f"Student(name={self.name}, group={self.group})"

#13
class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance_to(self, other):
    dx = self.x - other.x
    dy = self.y - other.y
    return (dx * dx + dy * dy) ** 0.5

  def __eq__(self, other):
    if not isinstance(other, Point2D):
        return False
    return self.x == other.x and self.y == other.y

  def __repr__(self):
    return f"Point2D({self.x}, {self.y})"

#14
class Inventory:
  def __init__(self):
    self.items = {}

  def add(self, name, qty=1):
    if qty <= 0:
        return
    if name in self.items:
        self.items[name] += qty
    else:
        self.items[name] = qty

  def remove(self, name, qty=1):
    if qty <= 0 or name not in self.items:
        return
    if self.items[name] <= qty:
        del self.items[name]
    else:
        self.items[name] -= qty

  def count(self, name):
    if name in self.items:
        return self.items[name]
    return 0

  def __contains__(self, name):
    return name in self.items

  def __len__(self):
    total = 0
    for qty in self.items.values():
      total += qty
      return total


#15
class CourseCatalog:
  def __init__(self):
    self.courses = {}

  def add_course(self, code, title):
    self.courses[code] = title

  def get_title(self, code):
    if code in self.courses:
        return self.courses[code]
    return None

  def __iter__(self):
    sorted_list = []
    for code in sorted(self.courses):
        sorted_list.append((code, self.courses[code]))
    return iter(sorted_list)

  def __len__(self):
    return len(self.courses)
  
#16
class DefaultDict:
  def __init__(self, default_factory=None):
    self.default_factory = default_factory if callable(default_factory) else None
    self.data = {}

  def __getitem__(self, key):
    if key in self.data:
        return self.data[key]

    if self.default_factory is None:
        return None

    value = self.default_factory()
    self.data[key] = value
    return value

  def __setitem__(self, key, value):
    self.data[key] = value

  def __contains__(self, key):
    return key in self.data

  def __len__(self):
    return len(self.data)