num = 6  
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end=" ")
    print()


num = 6  
for i in range(1, num + 1):
    print(f"{i:>3}", end=" ")
    for j in range(1, num + 1):
        print(f"{i * j:>3}", end=" ")
    print()




