# All the employees for the customers
class Employee:

    def __init__(self, first, last, profession):
        self.first = first
        self.last = last
        self.profession = profession
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Alice', 'Aliceville', 'electrician')
emp_2 = Employee('Bob', 'Bobsville', 'painter')
emp_3 = Employee('Craig', 'Craigsville', 'plumber')

# Customers who are looking for employees
class Customers:

    def __init__(self, first, last, adres, needs):
        self.first = first
        self.last = last
        self.adres = adres
        self.needs = needs

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
customer_1 = Customers('Alfred', 'Alfredson', 'Alfredslane 123', ["painter", "plumber"])
customer_2 = Customers('Bert', 'Bertson', 'Bertslane 231', ["plumber"])
customer_3 = Customers('Candice', 'Candicedottir', 'Candicelane 312', ["electrician", "painter"])


# Connect the right employees with the right customers
def connect_employees(customers, employees):
    contracts = {}
    for customer in customers:
        contracts[customer.first] = []
        for need in customer.needs:
            for employee in employees:
                if need == employee.profession:
                    contracts[customer.first].append(employee.fullname())
    for customer, employees in contracts.items():
        return f"{customer}'s contracts: {employees}"

if __name__=="__main__":
    print(connect_employees([customer_1], [emp_1, emp_2, emp_3]))
    print(connect_employees([customer_2], [emp_1, emp_2, emp_3]))
    print(connect_employees([customer_3], [emp_1, emp_2, emp_3]))
