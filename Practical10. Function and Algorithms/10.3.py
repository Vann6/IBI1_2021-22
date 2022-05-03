class Staff_1:
    def first_name(self, first_name):
        print('first name: '+first_name)

    def last_name(self, last_name):
        print('last name: '+last_name)

    def location(self, location):
        print('location: '+location)

    def role(self, role):
        print('role: '+role)
# define a class and four functions
class Staff_2:
    def __init__(self,a,b,c,d):
        self.first_name = a
        self.last_name = b
        self.location = c
        self.role = d
    def staff_info(self):
        print("The first name for the staff is %s.\nThe last name for the staff is %s.\nThe location for the staff is %s.\nThe role for the staff is %s"%(self.first_name,self.last_name,self.location,self.role))
# define a class and a function

X = Staff_1()
X.first_name('Tom')
X.last_name('Mike')
X.location('International Campus')
X.role('leadership')

Y = Staff_2('Tom','Mike','International Campus','leadership')
Y.staff_info()
# report the required information use these two classes
# the information can be changed