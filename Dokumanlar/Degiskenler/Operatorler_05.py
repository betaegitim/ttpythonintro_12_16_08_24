# %% [markdown]
# # Operatorler

# %%


# %% [markdown]
# ## Aritmetik Operatörler

# %%
a = 5
b = 2
a + b 
a - b
a * b
a / b
a % b # 1
a ** b # 25
a // b # 2

# %% [markdown]
# ## Karşılaştırma Operatörleri

# %%
a = 5
b = 2 
a > b
a < b
a >= b
a <= b

# %%
"a" > "A"

# %%
ord("A")

# %% [markdown]
# ## Mantıksal Operatörler

# %%
"""
and
or
not
"""

# %% [markdown]
# ## Kimlik Operator `is`

# %%
a = 258
b = 258
a is b

# %%
a = 2
b = 2.0
a is b,a is not b

# %%
a = 2
b = 2.0
a == b

# %% [markdown]
# ## Üyelik Operatörü `in`

# %%
var1 = "Türk Telekom"
"ü" in var1

# %%
liste = [1,2,3,1,3,4,100]
100 in liste,100 not in liste

# %% [markdown]
# ## Bitwise Operatörleri ` & ^ ~ >> << | `

# %%
a = 10 # 01010
b = 4  # 00100 
a & b,a | b,a ^ b,~a,a>>2,a<<2

# %% [markdown]
# ## Unary Operatörleri

# %%
a = 2
a = a + 4
a

# %%
a = 2
a += 4
a

# %% [markdown]
# ## Mors Operatörü `:=`

# %%
def fonk(a):
    return a**2
if (t := fonk(3)) and t > 6:
    print("Doğru")

# %% [markdown]
# https://www.geeksforgeeks.org/precedence-and-associativity-of-operators-in-python/

# %% [markdown]
# 


