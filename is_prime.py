def is_prime(num):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        return False
  else:
    return True


print(is_prime(1))