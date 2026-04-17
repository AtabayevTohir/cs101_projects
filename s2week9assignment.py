from dataclasses import dataclass, field

@dataclass
class Supply:
    name: str
    liters: float
    cost_per_liter: float

    def total_cost(self) -> float:
        return round(self.liters* self.cost_per_liter, 2)


@dataclass
class Event:
    title: str
    guests: int
    supplies: list[Supply] = field(default_factory=list)
    total_cost: float = field(init=False)

    def __post_init__(self):
        self.total_cost = 0.0
        self.cost_updater()

    def cost_updater(self):
        self.total_cost =0.0
        for item in self.supplies:
            self.total_cost += item.total_cost()
        round(self.total_cost,2)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)
        self.cost_updater()

    def cost_per_guest(self) -> float:
        return round(self.total_cost / self.guests, 2)

    def scale(self, new_guests: int):
        ratio = new_guests / self.guests
        for supply in self.supplies:
            supply.liters = round(supply.liters * ratio, 2)
        self.guests = new_guests
        self.cost_updater()

    def display(self) -> str:
        lines = [f"{self.title} ({self.guests} guests):"]
        for supply in self.supplies:
            lines.append(
                f"  {supply.name}: {supply.liters}L (${supply.total_cost()})"
            )

        lines.append(f"Per guest: ${self.cost_per_guest()}")
        return "\n".join(lines)


e = Event("Gala Dinner", 50)
e.add_supply(Supply("Juice", 25.0, 4.0))
e.add_supply(Supply("Water", 50.0, 1.5))
e.add_supply(Supply("Coffee", 15.0, 6.0))

print(e.total_cost)
print(e.cost_per_guest())
print(e.display())

e.scale(25)
print(e.display())