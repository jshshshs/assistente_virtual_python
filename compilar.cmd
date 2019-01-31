cd C:\Users\Manoel Vitor\Documents\Algoritmos\Python\Inteligência Artificial
cls
gcc -c -DBUILD_DLL math2.c -o out.o
gcc -shared -o biblioteca.dll out.o -Wl,--out-implib,math2.a
del out.o
gcc exe.c -o math2.exe math2.a


//
gcc -shared -o libhello.so -fPIC hello.c
gcc -shared -o libhello.so -fPIC hello.c