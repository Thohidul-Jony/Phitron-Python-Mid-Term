class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()
    def _initialize_seats(self):
        for row in range(1, self._rows + 1):
            self._seats[row] = ['free'] * self._cols
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        allocated_seats = [['free' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[show_id] = allocated_seats
    def view_show_list(self):
        return self._show_list
    def view_available_seats(self, show_id):
        if show_id in self._seats:
            return [[(row, col) for col, status in enumerate(row_seats, start=1) if status == 'free'] 
                    for row, row_seats in enumerate(self._seats[show_id], start=1)]
        else:
            return "Invalid show ID"
    def book_seats(self, show_id, seats_to_book):
        if show_id in self._seats:
            for row, col in seats_to_book:
                if 1 <= row <= self._rows and 1 <= col <= self._cols:
                    if self._seats[show_id][row - 1][col - 1] == 'free':
                        self._seats[show_id][row - 1][col - 1] = 'booked'
                        print(f"Seat booked successfully: Row {row}, Col {col}")
                    else:
                        print(f"Seat at row {row}, col {col} is already booked.")
                else:
                    print(f"Invalid seat at row {row}, col {col}.")
        else:
            print("Invalid show ID.")
class TicketCounter:
    def __init__(self, hall):
        self._hall = hall
    def view_all_shows(self):
        print("All Shows:")
        for show in self._hall.view_show_list():
            print(show)
    def view_available_seats(self, show_id):
        print(f"Available Seats for Show {show_id}:")
        available_seats = self._hall.view_available_seats(show_id)
        if available_seats == "Invalid show ID":
            print("Invalid show ID.")
        else:
            for row, seats in enumerate(available_seats, start=1):
                for col in seats:
                    print(f"Row {row}, Col {col}")
    def book_tickets(self, show_id, seats_to_book):
        self._hall.book_seats(show_id, seats_to_book)