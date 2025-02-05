attack1 = int(input("Give attack power for 1st figher: "))
attack2 = int(input("Give attack power for 2nd figher: "))
health1 = int(input("Give health for 1st figher: "))
health2 = int(input("Give health for 2nd figher: "))

if attack1>attack2:
    print("fighter 1 wins")
elif attack1==attack2:
    if health1 > health2:
        print("fighter 1 wins")
    elif health1==health2:
        print("draw")
    else:
        print("figther 2 wins")
else:
    print("figther 2 wins")