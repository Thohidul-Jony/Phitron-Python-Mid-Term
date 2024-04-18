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
            for col in range(1, self.cols + 1):
                seat_id = f"{row}{chr(64 + col)}"
                self.seats[seat_id] = {'status': 'available'}
class Star_Cinema:
    hall_list = []
    def __init__(self, hall):
        self.hall_list.append(hall)
