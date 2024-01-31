a = input()
b = input()
c = input()


if a == b and b == c:
  print("OK")
elif a!=b and b!= c:
  print("BOTH MISMATCH")
elif a == b and b!=c:
  print("ENTRY 3 MISMATCH")
elif a != b and b == c:
  print("ENTRY 2 MISMATCH")
