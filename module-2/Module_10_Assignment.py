# Garvin Stewart
# 3/8/2026
# Module 10.2

# Stores general employee information: name, gender, pay rate, and employee number.
class Employee:
    """Base class representing a general employee."""

    def __init__(self, name, gender, pay_rate, emp_number):
        self.__name = name
        self.__gender = gender
        self.__pay_rate = pay_rate
        self.__emp_number = emp_number

    # --- Setters ---
    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    # --- Getters ---
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_pay_rate(self):
        return self.__pay_rate

    def get_emp_number(self):
        return self.__emp_number

# Extends Employee with a shift number field (1=Day, 2=Swing, 3=Graveyard).
# Setter validates that only accepted shift values are assigned.
class ProductionWorker(Employee):
    """Subclass of Employee representing a shift-based production worker."""

    SHIFT_LABELS = {1: "Day", 2: "Swing", 3: "Graveyard"}

    def __init__(self, name, gender, pay_rate, emp_number, shift_number):
        Employee.__init__(self, name, gender, pay_rate, emp_number)
        self.__shift_number = shift_number

    # Setter
    def set_shift_number(self, shift_number):
        if shift_number not in ProductionWorker.SHIFT_LABELS:
            raise ValueError(f"Invalid shift. Must be 1 (Day), 2 (Swing), or 3 (Graveyard).")
        self.__shift_number = shift_number

    # Getter
    def get_shift_number(self):
        return self.__shift_number

    def get_shift_label(self):
        return ProductionWorker.SHIFT_LABELS.get(self.__shift_number, "Unknown")

# display the shift field only when the object is a ProductionWorker.
def display_employee(emp):
    print(f"  Name        : {emp.get_name()}")
    print(f"  Gender      : {emp.get_gender()}")
    print(f"  Employee ID : {emp.get_emp_number()}")
    print(f"  Hourly Pay  : ${emp.get_pay_rate():.2f}")
    if isinstance(emp, ProductionWorker):
        shift = emp.get_shift_number()
        label = emp.get_shift_label()
        print(f"  Shift       : {label} (Shift {shift})")


def main():
    # Instantiate all four objects with empty/default values before populating via setters
    emp1    = Employee("", "", 0.0, 0)
    emp2    = Employee("", "", 0.0, 0)
    worker1 = ProductionWorker("", "", 0.0, 0, 1)
    worker2 = ProductionWorker("", "", 0.0, 0, 1)

    # Assign field values for all four instances using setters
    emp1.set_name("John Doe")
    emp1.set_gender("Male")
    emp1.set_pay_rate(25.00)
    emp1.set_emp_number(101)

    emp2.set_name("Jane Smith")
    emp2.set_gender("Female")
    emp2.set_pay_rate(28.50)
    emp2.set_emp_number(102)

    worker1.set_name("Mike Johnson")
    worker1.set_gender("Male")
    worker1.set_pay_rate(18.00)
    worker1.set_emp_number(201)
    worker1.set_shift_number(1)   # Day shift

    worker2.set_name("Emily Davis")
    worker2.set_gender("Female")
    worker2.set_pay_rate(20.50)
    worker2.set_emp_number(202)
    worker2.set_shift_number(3)   # Graveyard shift

    # Group instances by type and print each section of the roster
    employees       = [emp1, emp2]
    production_staff = [worker1, worker2]

    print("=" * 45)
    print("         COMPANY EMPLOYEE ROSTER")
    print("=" * 45)

    print("\n[ General Employees ]\n")
    for emp in employees:
        display_employee(emp)
        print("-" * 45)

    print("\n[ Production Workers ]\n")
    for worker in production_staff:
        display_employee(worker)
        print("-" * 45)


if __name__ == "__main__":
    main()