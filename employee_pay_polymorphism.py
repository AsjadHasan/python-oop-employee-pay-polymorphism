
"""
Demonstrate inheritance, method overriding, and
polymorphism using full-time and part-time employees.
"""


class Employee:
    """Base class representing an employee."""

    def __init__(self, name):
        """Initialize the employee's name."""
        self.name = name

    def calculate_pay(self):
        """Calculate employee pay (override in subclasses)."""
        raise NotImplementedError(
            "Subclasses must implement calculate_pay()."
        )


class FullTimeEmployee(Employee):
    """Represent a full-time employee with an annual salary."""

    def __init__(self, name, annual_salary):
        """Initialize name and annual salary."""
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        """Calculate monthly pay from annual salary."""
        return self.annual_salary / 12


class PartTimeEmployee(Employee):
    """Represent a part-time employee paid hourly."""

    def __init__(self, name, hourly_rate, hours_worked):
        """Initialize name, hourly rate, and hours worked."""
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        """Calculate pay based on hours worked."""
        return self.hourly_rate * self.hours_worked


def main():
    """Create employee objects and display their pay."""
    full_time = FullTimeEmployee("Alice", 60000)
    part_time = PartTimeEmployee("Bob", 500, 20)

    print(
        f"{full_time.name}'s monthly pay: "
        f"{full_time.calculate_pay()}"
    )
    print(
        f"{part_time.name}'s monthly pay: "
        f"{part_time.calculate_pay()}"
    )


if __name__ == "__main__":
    main()