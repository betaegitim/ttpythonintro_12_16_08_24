# %% [markdown]
# # Hata Ayıklama
# * try-except
# * Exception
# * Exception Hierarchy
# * finally
# * raise

# %%
a = int(input("1. Sayıyı Giriniz:"))
b = int(input("2. Sayıyı Giriniz:"))
a/b
print("Çalışmaya devam etti")

# %% [markdown]
# ## try-except

# %%
try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
    print(a/b)
except:
    print("Hata Verdi")
print("Çalışmaya devam etti")

# %% [markdown]
# ## Exception

# %%
try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
    print(a/b)
except Exception as hata:
    print("Hata Verdi Hata Mesajı=>",hata)
print("Çalışmaya devam etti")

# %%
try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
    print(a/b)
except ZeroDivisionError:
    print("Sıfıra Bölme")
except ValueError:
    print("Değer Hatası")
print("Çalışmaya devam etti")

# %% [markdown]
# ## Exception Hierarchy

# %%
try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
    print(a/b)
except Exception as hata:
    print("Hata Mesajı:",hata)
except ZeroDivisionError:
    print("Sıfıra Bölme")
except ValueError:
    print("Değer Hatası")
print("Çalışmaya devam etti")

# %%
try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
    print(a/b)
except ZeroDivisionError:
    print("Sıfıra Bölme")
except ValueError:
    print("Değer Hatası")
except Exception as hata:
    print("Hata Mesajı:",hata)
print("Çalışmaya devam etti")

# %% [markdown]
# <pre><span></span>BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup [BaseExceptionGroup]
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError
#       │    ├── BlockingIOError
#       │    ├── ChildProcessError
#       │    ├── ConnectionError
#       │    │    ├── BrokenPipeError
#       │    │    ├── ConnectionAbortedError
#       │    │    ├── ConnectionRefusedError
#       │    │    └── ConnectionResetError
#       │    ├── FileExistsError
#       │    ├── FileNotFoundError
#       │    ├── InterruptedError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── PermissionError
#       │    ├── ProcessLookupError
#       │    └── TimeoutError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    └── RecursionError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       └── Warning
#            ├── BytesWarning
#            ├── DeprecationWarning
#            ├── EncodingWarning
#            ├── FutureWarning
#            ├── ImportWarning
#            ├── PendingDeprecationWarning
#            ├── ResourceWarning
#            ├── RuntimeWarning
#            ├── SyntaxWarning
#            ├── UnicodeWarning
#            └── UserWarning
# </pre>

# %% [markdown]
# ## finally

# %%
try:
    a = int(input("1. Sayıyı Giriniz:"))
    b = int(input("2. Sayıyı Giriniz:"))
    print(a/b)
except ZeroDivisionError:
    print("Sıfıra Bölme")
except ValueError:
    print("Değer Hatası")
except Exception as hata:
    print("Hata Mesajı:",hata)
finally:
    print("Her durumda sonda çalışır") 
print("Çalışmaya devam etti")
    

# %%
def fonk():
    try:
        a = int(input("1. Sayıyı Giriniz:"))
        b = int(input("2. Sayıyı Giriniz:"))
        return a/b
    except ZeroDivisionError:
        return "Sıfıra Bölme"
    except ValueError:
        return "Değer Hatası"
    except Exception as hata:
        return "Hata Mesajı:" + hata
    finally:
        print("Her durumda sonda çalışır") 
    print("Çalışmaya devam etti")
fonk()

# %%



