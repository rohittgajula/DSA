


class A:
    def feature1(self):
        print("Feature 1 is working.")

    def feature2(self):
        print("Feature 2 is working.")

# here class B is inheriting all the features of class A
# B is sub-class & A is super class
class B(A):
    def feature3(self):
        print("Feature 3 is working.")

    def feature4(self):
        print("Feature 4 is working.")

# multilevel inheritance
class C(B):             # this also can work class C(A, B) - inherit from both A,B
    def feature5(self):
        print("Feature 5 is working.")


a1 = A()
b1 = B()
c1 = C()

# a1.feature1()
# a1.feature2()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1.feature5()