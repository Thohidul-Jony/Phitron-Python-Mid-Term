class Star_Cinema:
    hall_list = []
    def entry_hall(self, hall):
        self.hall_list.append(hall)
class Hall:
    def __init__(self, name):
        self.name = name
hall1 = Hall("Hall 1")
hall2 = Hall("Hall 2")
star_cinema = Star_Cinema()
star_cinema.entry_hall(hall1)
star_cinema.entry_hall(hall2)
print(Star_Cinema.hall_list)