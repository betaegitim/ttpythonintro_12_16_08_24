# %% [markdown]
# # Inheritance
# 

# %%
class A:
    def __init__(self):
        self.a = "a"
    
    def soyle(self):
        print("A sınıfından çalıştım")
    
    def soyleA(self):
        print(self.a)

class B(A):
    pass

# %%
obj1 = A()
obj2 = B()
print(type(obj1))
print(type(obj2))

# %%
a = A()
b = B()
a.soyle()
b.soyle()

# %%
class A: # parent super
    def __init__(self):
        self.a = "a"
    
    def soyle(self):
        print("A sınıfından çalıştım")
    
    def soyleA(self):
        print(self.a)

class B(A): # child 
    def __init__(self):
        super().__init__()
        self.b = "b"

    def soyleB(self):
        print(self.b)

a = A()
b = B()
b.soyleB()
a.soyleA()

# %% [markdown]
# ## Multiple Inheritance

# %%
class A: # parent super
    def __init__(self):
        self.a = "a"
    
    def soyle(self):
        print("A sınıfından çalıştım")
    
    def soyleA(self):
        print(self.a)

class B: # parent super
    def __init__(self):
        self.b = "b"
    
    def soyle(self):
        print("B sınıfından çalıştım")
    
    def soyleB(self):
        print(self.b)
    
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = "c"

    def soyleC(self):
        print(self.c)
    
c = C()
c.soyleA()
c.soyleB()
c.soyleC()
c.soyle()

# %% [markdown]
# ![alt text](diagram.svg "Title")

# %%



