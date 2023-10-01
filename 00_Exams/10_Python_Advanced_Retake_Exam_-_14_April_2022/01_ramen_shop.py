"""
You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if
you can serve all the customers.
Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have
no more ramen or customers left:
 Each time the value of the ramen is equal to the value of the customer, remove them both and continue with
the next bowl of ramen and the next customer.
 Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen
with the value of that customer and remove the customer. Then try to match the same bowl of ramen (which
has been decreased) with the next customer.
 Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the
customer with the value of the ramen bowl and remove the bowl. Then try to match the same customer
(which has been decreased) with the next bowl of ramen.
Look at the examples provided for a better understanding of the problem.
Input
 On the first line, you will receive integers representing the bowls of ramen, separated by a single space and
a comma ", ".
 On the second line, you will receive integers representing the customers, separated by a single space and a
comma ", ".
Output
 If all customers are served, print: "Great job! You served all the customers."
o Print all of the left ramen bowls (if any) separated by comma and space in the format: "Bowls of
ramen left: {bowls of ramen left}"
 Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
o Print all customers left separated by comma and space in the format "Customers left:
{customers left}"
Input                   Output                          Comment
14, 25, 37, 43, 19
58, 23, 37
                        Great job! You served all the customers
                        Bowls of ramen left: 14, 6

                                                        Start by taking the last bowl 19 and the first customer 58. The customer value is higher, so we remove the bowl and
                                                        decrease the value of the customer by 19. Now the two lists should look like this:
                                                        Bowls = [14, 25, 37, 43]
                                                        Customers = [39, 23, 37]
                                                        Next, we take the following bowl (43) and continue with the same customer who is 39 now. The value of the bowl
                                                        with ramen is higher than the customer's value, so we remove the customer and decrease the value of the ramen
                                                        bowl. Now the two lists should look like this:
                                                        Bowls = [14, 25, 37, 4]
                                                        Customers = [23, 37]
                                                        We take the last bowl of ramen, which is 4 now, and compare it with the next customer (23). The value of the
                                                        customer is higher, so we decrease his value by 4 and remove the last bowl. Now the two lists should look like this:
                                                        Bowls = [14, 25, 37]
                                                        Customers = [19, 37]
                                                        Then we continue with the ball 37 and customer 19. The bowl is higher. We remove the customer and decrease the
                                                        bowl value with the value of the customer 19. Now the two lists should look like this:
                                                        Bowls = [14, 25, 18]
                                                        Customers = [37]
                                                        Then we continue with bowl 18 and customer 37. The customer value is higher. We remove the bowl and decrease
                                                        the customer value with the value of bowl 18. Now the two lists should look like this:
                                                        Bowls = [14, 25]
                                                        Customers = [19]
                                                        Then we continue with the ball 25 and customer 19. The bowl is higher. We remove the customer and decrease the
                                                        bowl value with the value of the customer 19. Now the two lists should look like this:
                                                        Bowls = [14, 6]
                                                        Customers = []
                                                        We see that we served all of the customers and print the appropriate string for that case. After that, we print the
                                                        leftover bowls of ramen.
30, 13, 45
70, 25, 55, 15
                        Out of ramen! You didn't manage to serve all customers.
                        Customers left: 7, 55, 15
30, 25
20, 35
                        Great job! You served all the customers.
"""
from collections import deque

ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

current_ramen = ramen.pop()
current_customer = customers.popleft()
while True:

    if current_ramen == current_customer:
        current_ramen = 0
        current_customer = 0
        if ramen and customers:
            current_ramen = ramen.pop()
            current_customer = customers.popleft()
        else:
            break

    elif current_ramen > current_customer:
        current_ramen -= current_customer
        current_customer = 0
        if customers:
            current_customer = customers.popleft()
        else:
            break

    elif current_ramen < current_customer:
        current_customer -= current_ramen
        current_ramen = 0
        if ramen:
            current_ramen = ramen.pop()
        else:
            break


if not customers and current_customer == 0:
    if current_ramen > 0:
        ramen.append(current_ramen)
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen)}")
else:
    customers.appendleft(current_customer)
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
