"""
parametre olarak gönderilen sayının kontrollerini 
tamamladıktan sonra o sayıya kadar olan tüm asal sayıların toplamını geri gönderen python fonkisyonunu yazınız
"""
def fonk(sayi:int)->int:
    """
    sayıya kadar olan 
    tüm asal sayıların 
    toplamını geri gönderen 
    python fonkisyonu
    """
    toplam = 0
    if isinstance(sayi,int):
        for i in range(2,sayi+1):
            # asal kontrol
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                toplam += i
        else:
            return toplam
    else:
        return 0

print(fonk(sayi=9))


def fonk(sayi:int)->int:
    """
    This function takes an integer 'sayi' as input and returns the sum of all
    prime numbers up to 'sayi'.

    Args:
        sayi (int): The upper limit for the prime numbers.

    Returns:
        int: The sum of all prime numbers up to 'sayi'. If 'sayi' is not an integer,
            0 is returned.
    """
    # Initialize the sum to 0
    toplam = 0

    # Check if the input is an integer
    if isinstance(sayi,int):
        # Iterate from 2 to 'sayi'
        for i in range(2,sayi+1):
            # Check if 'i' is prime

            # Iterate from 2 to 'i-1'
            for j in range(2,i):
                # If 'i' is divisible by 'j', it is not prime
                if i % j == 0:
                    # Break the inner loop
                    break
            else:
                # If 'i' is not divisible by any number from 2 to 'i-1', it is prime

                # Add 'i' to the sum
                toplam += i
        else:
            # Return the sum
            return toplam
    else:
        # If 'sayi' is not an integer, return 0
        return 0

print(fonk(sayi=9))