"""
On the first line, you will receive a sequence of pizza orders. Each order contains a different number of pizzas,
separated by comma and space ", ". On the second line, you will receive a sequence of employees with pizzamaking
capacities (how much pizzas an employee could make), separated by comma and space ", ".
Your task is to check if all pizza orders are completed.
To do that, you should take the first order and the last employee and see:
 If the number of pizzas in the order is less than or equal to the employee's pizza making capacity, the order
is completed. Remove both the order and the employee.
 If the number of pizzas in the order is greater than the employee's pizza making capacity, the remaining
pizzas from the order are going to be made by the next employees until the order is completed.
o If there are no more employees to finish the order, consider it not completed.
 The restaurant does not take orders for more than 10 pizzas at once.
 If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee.
You should keep track of the total pizzas that are being made.
Input
 On the first line you will be given a sequence of pizza orders each represented as a number – integers
separated by comma and space ", "
 On the second line you will be given a sequence of employees with pizza‐making capacities – integers
separated by comma and space ", "
Output
 If all orders are successfully completed, print:
All orders are successfully completed!
Total pizzas made: {total count}
Employees: {left employees joined by ", "}
 Otherwise, if you ran out of employees and there are still some orders left print:
Not all orders are completed.
Orders left: {left orders joined by ", "}
Constraints
 You will always have at least one order and at least one employee
 All integers will be in range [‐100, 100]

Input               Output
11, 6, 8, 1
3, 1, 9, 10, 5, 9, 1
                    All orders are successfully completed!
                    Total pizzas made: 15
                    Employees: 3, 1
10, 9, 8, 7, 5
5, 10, 9, 8, 7
                    Not all orders are completed.
                    Orders left: 2, 5
12, -3, 14, 3, 2, 0
10, 15, 4, 6, 3, 1, 22, 1
                    All orders are successfully completed!
                    Total pizzas made: 5
                    Employees: 10, 15, 4, 6
"""
from collections import deque


def valid_order(order):
    if order not in range(1, 11):
        return False
    return True


def valid_employee(employee):
    if employee > 0:
        return True
    return False


pizza_orders = deque(int(x) for x in input().split(', '))
employers = [int(x) for x in input().split(', ')]

pizzas_made = 0
next_order = pizza_orders.popleft()
next_employee = employers.pop()
while True:
    try:
        while not valid_order(next_order):
            next_order = pizza_orders.popleft()

        while not valid_employee(next_employee):
            next_employee = employers.pop()
    except IndexError:
        break

    pizzas_made += next_order

    if next_order <= next_employee:
        next_order, next_employee = 0, 0

    elif next_order > next_employee:
        next_order -= next_employee
        next_employee = 0

    pizzas_made -= next_order

if valid_order(next_order):
    pizza_orders.appendleft(next_order)

if valid_employee(next_employee):
    employers.append(next_employee)

if not employers:
    employers.append(0)

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")

else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join(map(str, employers))}")

