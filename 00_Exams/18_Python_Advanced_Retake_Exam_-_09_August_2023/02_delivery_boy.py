"""
Today, we have an exciting programming task that will take you on a pizza delivery adventure in a neighborhood
represented by a matrix. Get ready to navigate a delivery boy through the streets, avoid obstacles, and make timely
pizza deliveries!
You are a pizza delivery boy with a motorized vehicle that delivers pizza in a neighborhood. The neighborhood is
represented by a matrix ‐ field. Each cell in the field represents a part of the neighborhood, and it can contain one
of the following elements:
 'B' ‐ Represents the starting position of the delivery boy.
 'A' ‐ Represents an address where a pizza needs to be delivered.
 '*' ‐ Represents an obstacle or an area where the delivery boy cannot drive.
 'P' ‐ Represents the pizza restaurant.
 '‐' – Represents the road, the delivery boy can drive over it.
In the beginning, you will be given N and M – integers, separated by a single space ‐ " ", indicating the field’s
dimensions. On the next N lines, you will receive strings, representing the rows of the area, with M columns.
The delivery boy must carefully navigate through the streets, following the commands that will be received on each
of the following lines‐ "up", "down", "right", and "left", moving one position at a time.
In this pizza delivery adventure, the delivery boy starts his journey from the position marked as 'B' on the
neighborhood field. His first task is to make his way to the pizza restaurant marked as 'P' and collect the delicious
pizza. Once he collects the pizza, the position 'P' is marked as 'R' and a message is displayed on the Console:
"Pizza is collected. 10 minutes for delivery."
However, the neighborhood is not without obstacles. Whenever the delivery boy encounters a cell marked with '*',
it signifies an obstacle, and he cannot make a move in that direction. He must remain in his current position and
find an alternative route. The delivery boy should wait for the next command.
If, at any point during his journey, the delivery boy steps out of the neighborhood field (matrix boundaries), it
means he has ventured beyond the streets of the neighborhood. In such a case, the delivery boy will be considered
late for the delivery, and unfortunately, the delivery will be canceled. The following message should be displayed
on the Console: "The delivery is late. Order is canceled."
Once the delivery boy successfully reaches an address marked as 'A', he joyfully delivers the pizza, completing his
mission. The position 'A' is marked as 'P'. A message will be displayed on the Console: "Pizza is delivered on
time! Next order..."
With each step he takes, the '‐'(dash) cells he passes (road) through become '.' (dot) to indicate his path.
Remember, the delivery boy must follow the commands, avoid obstacles, and ensure timely pizza deliveries to the
addresses. Good luck!
In the end, print the final state of the matrix (neighborhood area) with the delivery boy in its starting position. If
the boy has been out of the field, mark his starting position with an empty space. Each row is on a new line.
Input
 On the first line, you will get the number of rows and columns of the matrix, separated by a single space.
 On the next N lines, you will receive strings, representing each row of the matrix.
 On each of the following lines, you will receive the possible directions for the delivery boy to move ‐ "up",
"down", "right", and "left".
Output
 On the first line:
o When the boy collects the pizza:
"Pizza is collected. 10 minutes for delivery."
o If the pizza is delivered successfully:
"Pizza is delivered on time! Next order..."
o If the boy leaves the field boundaries:
"The delivery is late. Order is canceled."
 On the next lines, print the final state of the matrix with the delivery boy in its starting position. If the boy
has been out of the field, mark his starting position with an empty space. Each row ‐ on a new line.
Constraints
 The commands are guaranteed to lead him either to a successful delivery or out of the field, ensuring that
the commands are sufficient in all cases.
 Each row of the matrix will have the same length.
Input       Output
5 6
*‐‐‐‐A
*B***‐
*‐***‐
*‐‐‐‐P
******
down
down
right
right
right
right
up
up
up
            Pizza is collected. 10 minutes for delivery.
            Pizza is delivered on time! Next order...
            *‐‐‐‐P
            *B***.
            *.***.
            *....R
            ******
5 6
*‐‐‐‐A
*B***‐
*‐***‐
*‐‐‐‐P
******
down
down
left
right
right
right
right
right
up
            Pizza is collected. 10 minutes for delivery.
            The delivery is late. Order is canceled.
            *‐‐‐‐A
            * ***‐
            *.***‐
            *....R
            ******
5 6
*‐‐‐‐A
*****‐
*‐***‐
*‐‐‐BP
******
"""


def read_area(n):
    return [[x for x in list(input())] for _ in range(n)]


def print_area():
    for row in area:
        print(''.join(row))


def boy_position():
    for idx, row in enumerate(area):
        if 'B' in row:
            col = row.index('B')
            row = idx
            return row, col


def valid_position(row, col):
    if row not in range(rows) or col not in range(cols):
        return False
    return True


def deliver_the_pizza():
    or_r, or_c = boy_position()
    row, col = boy_position()
    command = input()
    while True:
        drow, dcol = direction_mapper[command]
        next_row, next_col = row + drow, col + dcol
        if valid_position(next_row, next_col):
            cell = area[next_row][next_col]
            if cell == '*':
                command = input()
                continue
            elif cell == 'P':
                area[next_row][next_col] = 'R'
                print("Pizza is collected. 10 minutes for delivery.")
            elif cell == 'A':
                area[next_row][next_col] = 'P'
                print("Pizza is delivered on time! Next order...")
                area[or_r][or_c] = 'B'
                print_area()
                raise SystemExit
            else:
                area[next_row][next_col] = '.'
        else:
            print("The delivery is late. Order is canceled.")
            area[or_r][or_c] = ' '
            print_area()
            raise SystemExit

        row, col = next_row, next_col
        command = input()


if __name__ == "__main__":
    direction_mapper = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    rows, cols = [int(x) for x in input().split()]
    area = read_area(rows)
    deliver_the_pizza()
