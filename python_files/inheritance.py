# class Employee

class Employee():

    # this class will have two normal methods.

    def fullname(self, name): # name parameter

        return name

    def contact_number(self, number):

        return number

# now we create instance for our class Employee.

emp = Employee() # we don't need to pass any arguments here. We are not implementing __init__ method here

# now i can simply call both functions. > fullname and contact_number

print(emp.fullname('Guido Van Rossum')) # fullname takes one argument which the name parameter that we defined above.
print(emp.contact_number("845-585-8585")) # same concept goes here too.
# very impressive, you got 92 percent! great work anush. thansks Anna two questoins were given for the syntax of replace stmt
# don't lose hope, 92 is great. Try everyday, you will become a python wizard. Sure will do :)
# any questions so far?
# you can continue
# anydesk gets closed automatically and I didnt notice it. ok no issues.

# above is our class Employee has two methods.
# I can only access those 2 functions by creating new object for my class 
# emp is the object for our class Employee.

# what if i want to access fullname and contact_number in another class?
# how do i do that?
# here we can implement inheritace.

# creating new class named Employee_Inherited.
class Employee_Inherited(Employee):
    '''
    inside the brackets we need to pass the actual class name that
    we want to inherit from, in this case we are inheriting from 
    our base class or parent class Employee. 

    # This is the concept of inheritance.

    DEFINITION:

        A class simply extends another class behaviour or another class's
        methods or properties. This is the confusing definition given by our
        school teacher's often

        # property, attribute, function (same meaning only)
        justing copying or inheriting one's functionality.

    '''
    pass # just given pass here, means we are not doing anything here.

# now we can create object for this new class

emp_inher = Employee_Inherited()

print(emp_inher.contact_number('856-947-1259'))
print(emp_inher.fullname('Kenneth Reitz'))

# understood? Super i had got it anna 
