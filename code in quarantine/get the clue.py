msgs = []
n = int(input())
if ((n >= 1)and(n <= 10)):

    for i in range(n):
        msgs.append(input())
    for msg in msgs:
        if(msg[0] == "y"or msg[0] == "Y"):

            if(msg[1] == "o" or msg[1] == "O"):

                if (msg[2] == "u" or msg[2] == "U"):

                    if (msg[3] == " "):

                        if (msg[4] == "w" or msg[4] == "W"):
                            print(msg)

                        else:
                            break
