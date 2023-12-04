A = "1"
B = ""
C = "2"
D = ""
E = "3"

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))

B=A
A=""

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))

D=C
C=""

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))

C=E
E=""

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))

A=C
C=""

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))

C=B
B=""

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))

E=C
C=""

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))

C=D
D=""

print("{}, {}, {}, {}, {}" .format(A,B,C,D,E))
