def is_prime(n):
    """
    input:
      n - numarul dat
    output:
      True  - n este un numar prim
      False - n nu este un numar prim
    """
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def get_goldbach(n):
    """
    input:
      n - numarul pentru care se genereaza p1 si p2
        astfel incat suma acestora sa fie egala cu numarul n
    output:
      [p1, p2] - daca exista 2 astfel de numere
      -1 - in caz ca nu exista 2 numere sa satisfaca
            conditia data
    """
    for i in range(2, n):
        for j in range(2, n):
            if (i + j == n) and is_prime(i) and is_prime(j):
                return [i, j]
    return -1

def test_get_goldbach():
    print("Pentru numarul : 1")
    assert get_goldbach(1) == -1, "it is impossible"
    print("Pentru numarul : 19")
    assert get_goldbach(19) == [2, 17], "it is [2, 17]"
    print("It's alright")

def get_newton_sqrt(n, steps):
  """
  input:
    n - numarul pentru care trebuie calculat radicalul
    steps - numarul de aproximari
  output:
    radicalul numarului n
  """
  if n < 0:
      return None
  x0 = 2
  while steps > 0:
    x0 = 0.5 * (x0 + n/x0)
    steps = steps - 1
  return x0

def test_get_newton_sqrt():
  print("Test sqrt of -1 with 3 aproximations")
  assert get_newton_sqrt(-1, 3) == None
  print("Test sqrt of 4 with 1 aproximations")
  assert round(get_newton_sqrt(4, 1), 1) == 2.0

def get_leap_years(start, end):
    '''
    afiseaza toti anii bisecti intre 2 ani dati.
    :param start: primul an
    :param end: al doilea an
    :return: anii bisecti aflati intre cei doi ani introdusi, inclusiv.
    '''
    rezultat = []
    for i in range(start, end + 1):
        if i % 4 == 0:
            rezultat.append(i)
    return rezultat
def test_get_leap_years():
    assert get_leap_years(2015, 2021) == [2016, 2020]
    assert get_leap_years(2001, 2003) == []
def main():
    test_get_goldbach()
    test_get_newton_sqrt()
    test_get_leap_years()
    while True:
        print("1. Afiseaza numerele prime care indeplinesc conditia.")
        print("2. Afiseaza radicalul numarului.")
        print("3. Afiseaza anii bisecti dintre 2 numere date.")
        print("4. Iesire")
        command = int(input("Introduceti optiunea:"))
        if command == 1:
            start = int(input("Numarul este: "))
            print("Numerele prime sunt ", get_goldbach(start))
        elif command == 2:
            start = int(input("Numarul este: "))
            end = int(input("Numarul de aproximari: "))
            print("Radicalul numarului este ", get_newton_sqrt(start, end))
        elif command == 3:
            start = int(input("Primul an este: "))
            end = int(input("Al doilea an este: "))
            print("Anii bisecti sunt ", get_leap_years(start, end))
        elif command == 4:
            break
main()