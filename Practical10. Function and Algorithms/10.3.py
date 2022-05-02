class Staff:
    def first_name(self, first_name):
        print('first name: '+first_name)

    def last_name(self, last_name):
        print('last name: '+last_name)

    def location(self, location):
        print('location: '+location)

    def role(self, role):
        print('role: '+role)


X = Staff()
X.first_name('Tom')
X.last_name('Mike')
X.location('International Campus')
X.role('leadership')