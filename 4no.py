class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.initialize_seats()
    def initialize_seats(self):
        for row in range(1, self.rows + 1):
            self.seats[row] = ['free'] * self.cols
    def book_seats(self, show_id, seats_to_book):
        if show_id in self.seats:
            for row, col in seats_to_book:
                if 0 < row <= self.rows and 0 < col <= self.cols:
                    if self.seats[show_id][row - 1][col - 1] == 'free':
                        self.seats[show_id][row - 1][col - 1] = 'booked'
                    else:
                        print(f"Seat at row {row}, col {col} is already booked.")
                else:
                    print(f"Invalid seat at row {row}, col {col}.")
        else:
            print("Invalid show ID.")