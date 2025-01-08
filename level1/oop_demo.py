

#########################################
# Question 1 - do not delete this comment
#########################################
class Minibar:
    def __init__(self, drinks, snacks):
        self.drinks: dict = drinks  # [str:int]
        self.snacks: dict = snacks  # [str:int]
        self.bill: int = 0

    def __repr__(self):
        output = ''
        if not self.drinks:  # checks if dict is empty
            output += 'No drinks left\n'
        else:
            output += 'Drinks:'
            for drink in self.drinks:
                output += ' ' + drink + ' (' + str(self.drinks[drink]) + '),'
            output = output[:-1]
            output += '\n'

        if not self.snacks:
            output += 'No snacks left\n'
        else:
            output += 'Snacks:'
            for snack in self.snacks:
                output += ' ' + snack + ' (' + str(self.snacks[snack]) + '),'
            output = output[:-1]
            output += '\n'

        if self.bill == 0:
            output += 'No bill yet'
        else:
            output += 'Bill: ' + str(self.bill)

        return output

    def eat(self, snack):
        keys = self.snacks.keys()  # keys = [key1,M&M,key3...]
        key = ''
        for item in keys:
            if item.lower() == snack.lower():
                key = item
                break

        if key in self.snacks:
            self.bill += self.snacks[key]
            self.snacks.pop(key)
        else:
            print('The snack ' + snack.lower() + ' was not found.')

    def drink(self, drink):
        keys = self.drinks.keys()  # keys = [key1,WaTer,key3...]
        key = ''
        for item in keys:
            if item.lower() == drink.lower():
                key = item
                break

        if key in self.drinks:
            self.bill += 21
            self.drinks[key] -= 1
            if self.drinks[key] == 0:
                self.drinks.pop(key)
        else:
            print('The drink ' + drink.lower() + ' was not found.')


#########################################
# Question 2 - do not delete this comment
#########################################
class Room:
    def __init__(self, minibar, number, guests, clean_level, is_suite, satisfaction=0.5):

        flag_type = True
        if type(number) is not int and flag_type:
            flag_type = False
            print('type error')
        if type(is_suite) is not bool and flag_type:
            flag_type = False
            print('type error')
        if not (type(satisfaction) is float or type(satisfaction) is int) and flag_type:
            flag_type = False
            print('type error')
        if type(guests) is not list:
            if flag_type:
                print('type error')
            flag_type = False
        else:
            for i in range(len(guests)):
                if type(guests[i]) is not str:
                    if flag_type:
                        print('type error')
                    flag_type = False
                else:
                    guests[i] = guests[i].lower()

        flag_value = True
        if number < 100 or number > 1000 and flag_value:
            flag_value = False
            print('value error')
        if number % 100 > 40 or number % 100 < 1 and flag_value:
            flag_value = False
            print('value error')
        if satisfaction > 1 or satisfaction < 0 and flag_value:
            flag_value = False
            print('value error')

        self.minibar: Minibar = minibar
        self.number: int = number  # first digit is for floor and the other two is for room number, example: 617-> floor 6 and room 17
        self.guests: list[str] = guests
        self.clean_level: int = clean_level  #  1 <= clean_level <= 10
        self.is_suite: bool = is_suite
        self.satisfaction: float = float(satisfaction)

    def __repr__(self):
        output: str = ''
        output += f'Room number: {self.number}\n'
        if not self.guests:
            output += 'Guests: empty\n'
        else:
            output += f'Guests:'
            copy_list = self.guests.copy()
            copy_list.sort()
            for guest in copy_list:
                output += f' {guest},'
            output = output[:-1] + '\n'


        output += f'Clean level: {self.clean_level}\n'
        output += f'Is suite: {self.is_suite}\n'
        output += f'Satisfaction: {self.satisfaction}\n'
        output += f'Minibar:\n{self.minibar}'

        return output

    def is_occupied(self):
        if self.guests:
            return True
        else:
            return False

    def clean(self):
        self.clean_level = min(10, self.clean_level + 1 + int(self.is_suite))

    def better_than(self, other):
        if self.is_suite and not other.is_suite:
            return True
        elif not self.is_suite and other.is_suite:
            return False
        else:
            if self.number//100 > other.number//100:
                return True
            elif self.number//100 < other.number//100:
                return False
            else:
                if self.clean_level > other.clean_level:
                    return True
                elif self.clean_level < other.clean_level:
                    return False
        return False

    def check_in(self, guests):
        if self.guests:
            print('Cannot check-in new guests to an occupied room')
        else:
            self.guests = guests
            for i in range(len(self.guests)):
                self.guests[i] = self.guests[i].lower()
            self.satisfaction = 0.5
            self.minibar.bill = 0

    def check_out(self):
        if not self.guests:
            print('Cannot check-out an empty room')
        else:
            self.guests = []

    def move_to(self, other):
        if not self.guests:
            print('Cannot move guests from an empty room')
        elif other.guests:
            print('Cannot move guests into an occupied room')
        else:
            other.guests = self.guests
            other.minibar.bill = self.minibar.bill
            if other.better_than(self):
                other.satisfaction = min(1.0, self.satisfaction + 0.1)
            else:
                other.satisfaction = self.satisfaction
            self.guests = []

#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.occupied_rooms = 0
        for room in rooms:
            if room.guests:
                self.occupied_rooms += 1

    def __repr__(self):
        return f'{self.name} Hotel has: {self.occupied_rooms}/{len(self.rooms)} occupied rooms.'

    def check_in(self, guests, is_suite):
        for room in self.rooms:
            if not room.guests and room.is_suite == is_suite:
                room.check_in(guests)
                self.occupied_rooms += 1
                return room
        return None

    def check_out(self, guest):
        for room in self.rooms:
            for guest_in_room in room.guests:
                if guest.lower() == guest_in_room:
                    room.check_out()
                    self.occupied_rooms -= 1
                    return room
        return None

    def upgrade(self, guest):

        guest_room = None
        for room in self.rooms:
            for guest_in_room in room.guests:
                if guest.lower() == guest_in_room:
                    guest_room = room
        if guest_room is None:
            return None

        for room in self.rooms:
            if room != guest_room and not room.guests and room.better_than(guest_room):
                guest_room.move_to(room)
                return room
        return None

    def send_cleaner(self, guest):
        for room in self.rooms:
            for guest_in_room in room.guests:
                if guest.lower() == guest_in_room:
                    room.clean()
                    return room
        return None


#########################################
# Question 4 - do not delete this comment
#########################################
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients: list[int] = coefficients

    def __repr__(self):
        output = ''
        power = len(self.coefficients) - 1
        for i in range(len(self.coefficients)):
            coeff = self.coefficients[i]
            if coeff != 0:
                if output:  # Add '+' (except the first term)
                    output += ' + '

                if power > 1:
                    if coeff == 1:
                        output += f'x^{power}'
                    elif coeff == -1:
                        output += f'-x^{power}'
                    else:
                        output += f'{coeff}x^{power}'
                elif power == 1:
                    if coeff == 1:
                        output += 'x'
                    elif coeff == -1:
                        output += '-x'
                    else:
                        output += f'{coeff}x'
                else:  # power == 0
                    output += f'{coeff}'

            power -= 1  # Always decrement power, regardless of coefficient

        return output or '0'  # Return '0' for a zero polynomial

    def __add__(self, other):
        output = []
        n = len(self.coefficients)
        m = len(other.coefficients)
        i, j = 0, 0
        while n > m:
            output.append(self.coefficients[i])
            i += 1
            n -= 1
        while n < m:
            output.append(other.coefficients[j])
            j += 1
            m -= 1

        while n > 0:
            output.append(self.coefficients[i] + other.coefficients[j])
            i += 1
            j += 1
            n -= 1

        return Polynomial(output)

    def __sub__(self, other):
        output = []
        n = len(self.coefficients)
        m = len(other.coefficients)
        i, j = 0, 0
        while n > m:
            output.append(self.coefficients[i])
            i += 1
            n -= 1
        while n < m:
            output.append(-other.coefficients[j])
            j += 1
            m -= 1

        while n > 0:
            output.append(self.coefficients[i] - other.coefficients[j])
            i += 1
            j += 1
            n -= 1

        result = Polynomial(output)
        result.verify_zero()
        return result

    def __mul__(self, other):
        # Initialize a list of zeros for the resulting coefficients
        result_coefficients = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        # Multiply each coefficient from self by each coefficient from other
        for i, coeff1 in enumerate(self.coefficients):
            for j, coeff2 in enumerate(other.coefficients):
                result_coefficients[i + j] += coeff1 * coeff2

        # Return a new Polynomial instance with the resulting coefficients
        return Polynomial(result_coefficients)

    def __gt__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            return True
        elif len(self.coefficients) < len(other.coefficients):
            return False
        else:
            for i in range(len(self.coefficients)):
                if self.coefficients[i] > other.coefficients[i]:
                    return True
                elif self.coefficients[i] < other.coefficients[i]:
                    return False
        return False

    def verify_zero(self):
        count = 0
        for i in range(len(self.coefficients)):
            if self.coefficients[i] != 0:
                break
            else:
                count += 1

        if count != 0:
            if count == len(self.coefficients):
                self.coefficients = [0]
            else:
                self.coefficients = self.coefficients[count:]

    def calc(self, x):
        return sum(coeff * (x ** power) for power, coeff in enumerate(reversed(self.coefficients)))


if __name__ == '__main__':
    def test_hotel():
        m1 = Minibar({'Coke': 10, 'Lemonade': 1}, {'Bamba': 8, 'Mars': 12})
        m2 = Minibar({'Beer': 10, 'Lemonade': 4}, {'m&m': 6})
        rooms = [Room(m2, 514, [], 5, True),
                 Room(m2, 210, ["Ronen", "Shir"], 6, True),
                 Room(m1, 102, ["Liat"], 7, False),
                 Room(m2, 223, [], 6, True)]
        h = Hotel("Dan", rooms)
        test_sep = '\n------------------'
        print('PRINT m1:\n', m1, test_sep, sep="")
        print('PRINT m2:\n', m2, test_sep, sep="")
        print('PRINT h:\n', h, test_sep, sep="")
        liat_room = h.send_cleaner('Liat')
        print('CALL: h.send_cleaner("Liat")\n', liat_room, test_sep, sep="")
        print('CALL: liat_room.eat("bamba")\n', liat_room.minibar.eat("bamba"), test_sep, sep="")
        print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
        print('CALL: liat_room.drink("lemonade")\n', liat_room.minibar.drink("lemonade"), test_sep, sep="")
        print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
        print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")

        print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
        print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
        print('CALL: h.check_in(["Alice", "Wonder"], True)\n',
              h.check_in(["Alice", "Wonder"], True), test_sep, sep="")
        print('CALL: h.check_in(["Alex"], True)\n', h.check_in(["Alex"], True), test_sep,
              sep="")
        print('PRINT h:\n', h, test_sep, sep="")
        print('CALL: h.check_in(["Oded", "Shani"], False)\n',
              h.check_in(["Oded", "Shani"], False), test_sep, sep="")
        print('CALL: h.check_in(["Oded", "Shani"], False)\n',
              h.check_in(["Oded", "Shani"], False), test_sep, sep="")
        print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
        print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
        print('PRINT h:\n', h, test_sep, sep="")


    print('==== Q1: Part a Basic tests/output====')
    drinks1 = {'Coke': 3, 'BEER': 5, 'WaTeR': 10}
    snacks1 = {'M&M': 10, 'Cake': 40, 'cookies': 23}

    m1 = Minibar(drinks1, snacks1)
    print(m1.drinks == drinks1 and m1.snacks == snacks1 and m1.bill == 0)
    print(Minibar({}, {}).snacks == {})

    print('==== Q1: Part b Basic tests/output====')
    m2 = Minibar({'Coke': 3, 'BEER': 5, 'WaTeR': 10}, {'M&M': 10, 'Cake': 40, 'cookies': 23})
    m2.eat('m&m')
    print('M&M' not in m2.snacks and m2.bill == 10)
    m2.drink('coke')
    print(m2.drinks.get('Coke') == 2 and m2.bill == 31)

    print('==== Q1: Part c Basic tests/output====')
    print(repr(Minibar({}, {})) == 'No drinks left\nNo snacks left\nNo bill yet')
    print(repr(m2) == 'Drinks: Coke (2), BEER (5), WaTeR (10)\nSnacks: Cake (40), cookies (23)\nBill: 31')

    print('==== Q2: Part b Basic tests/output====')
    room1 = Room(Minibar({}, {}), 922, [], 9, True, 1)
    print(repr(
        room1) == 'Room number: 922\nGuests: empty\nClean level: 9\nIs suite: True\nSatisfaction: 1.0\nMinibar:\nNo drinks left\nNo snacks left\nNo bill yet')
    room2 = Room(Minibar({}, {}), 923, ['Eyal', 'Rinat', 'Amit'], 2, True)
    print(repr(
        room2) == 'Room number: 923\nGuests: amit, eyal, rinat\nClean level: 2\nIs suite: True\nSatisfaction: 0.5\nMinibar:\nNo drinks left\nNo snacks left\nNo bill yet')

    print('==== Q2: Part c Basic tests/output====')
    print(not room1.is_occupied())
    print(room2.is_occupied())

    room1.clean()
    print(room1.clean_level == 10)
    room2.clean()
    print(room2.clean_level == 4)

    print(room1.better_than(room2))

    room1.check_in(['Omer', 'Liav', 'Eden'])
    print(room1.guests == ['omer', 'liav', 'eden'])
    print(room1.satisfaction == 0.5)

    room1.check_out()
    print(room1.guests == [])

    room2.move_to(room1)
    print(room2.guests == [])
    print(room1.guests == ['eyal', 'rinat', 'amit'])
    print(room1.satisfaction == 0.6)

    # Question 3 - compare by yourself to 'test_hotel_output.txt'
    # After you are done implementing all classes and methods, you may call to test_hotel() and
    # compare the results with the file test_hotel_output.txt
    # you should get the same text printed between START and END of Q3 (not including the start and end message)
    print('==== Q3: test hotel START (not included)====')
    test_hotel()
    print('==== Q3: test hotel END (not included)====')

    print('==== Q4: Basic tests/output====')
    p1 = Polynomial([3, 2, 1])
    p2 = Polynomial([1, 2])
    p3 = Polynomial([2, 0, 6, 0])

    print(p1)
    print(p2)
    print(p3)
    print(p1 + p2)
    print(p1 - p2)
    print(p3 - p3)
    print(p1 * p2)
    print(p1 > p2)
    print(p1 > p3)
    print(p1.calc(2))
    print(p2.calc(2))
    print(p3.calc(2))
