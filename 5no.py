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