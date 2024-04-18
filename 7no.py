class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.initialize_seats()
    def initialize_seats(self):
        for row in range(1, self.rows + 1):
            self.seats[row] = ['free'] * self.cols
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        allocated_seats = [['free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = allocated_seats
    def view_show_list(self):
        return self.show_list
    def view_available_seats(self, show_id):
        if show_id in self.seats:
            return [[(row, col) for col, status in enumerate(row_seats, start=1) if status == 'free'] 
                    for row, row_seats in enumerate(self.seats[show_id], start=1)]
        else:
            return "Invalid show ID"
    def book_seats(self, show_id, seats_to_book):
        if show_id in self.seats:
            for row, col in seats_to_book:
                if 0 < row <= self.rows and 0 < col <= self.cols:
                    if self.seats[show_id][row - 1][col - 1] == 'free':
                        self.seats[show_id][row - 1][col - 1] = 'booked'
                        print(f"Seat booked successfully: Row {row}, Col {col}")
                    else:
                        print(f"Seat at row {row}, col {col} is already booked.")
                else:
                    print(f"Invalid seat at row {row}, col {col}.")
        else:
            print("Invalid show ID.")
class TicketCounter:
    def __init__(self, hall):
        self.hall = hall
    def view_all_shows(self):
        print("All Shows:")
        for show in self.hall.view_show_list():
            print(show)
    def view_available_seats(self, show_id):
        print(f"Available Seats for Show {show_id}:")
        available_seats = self.hall.view_available_seats(show_id)
        for row, seats in enumerate(available_seats, start=1):
            for col in seats:
                print(f"Row {row}, Col {col}")
    def book_tickets(self, show_id, seats_to_book):
        self.hall.book_seats(show_id, seats_to_book)