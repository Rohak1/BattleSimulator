from player import Player
from actions import basic_attack, critical_attack, heal

alice = Player("Alice", 10, 5, 10, 5)
bob = Player("Bob", 5, 10, 5, 5)

print("Initial HP")
print(alice.health)
print(bob.health)

print()

print("Alice attacks Bob")

print(basic_attack(alice, bob))

print()

print("Bob HP")

print(bob.health)

print()

print("Bob heals")

print(heal(bob))

print()

print("Bob HP")

print(bob.health)

print()

print("Alice uses Critical")

print(critical_attack(alice, bob))

print()

print("Bob HP")

print(bob.health)