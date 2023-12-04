A = "1"
B = ""
C = "2"
D = ""
E = "3"

print(A,B,C,D,E)

B=A
A=""

print(A,B,C,D,E)

D=C
C=""

print(A,B,C,D,E)

C=E
E=""

print(A,B,C,D,E)

A=C
C=""

print(A,B,C,D,E)

C=B
B=""

print(A,B,C,D,E)

E=C
C=""

print(A,B,C,D,E)

C=D
D=""

print(A,B,C,D,E)
