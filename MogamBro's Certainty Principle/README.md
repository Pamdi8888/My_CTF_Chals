# MogamBro's Certainty Principle

## Description

MogamBro's Certainty Principle states that the more accurate you are the more delay you'll face. Δt • Δp ≥ frustration /
ram_space; where p is precission and t is time.

> Pamdi

## Instance Link

A netcat ip was provided to connect to the challenge.
The server code is provided in [cpu.py](./cpu.py), which was not provided during the ctf.

## Solution

- When we input a password, we observe that the time taken is returned to us.
- By guessing different passwords, we can observe that if the password starts with the letter 's', the time taken is
  significantly more than other passwords.
- According to the question, the more accurate we are, the more delay we'll face.

```
Enter password: a
Incorrect password
Time taken:  3.987795464382974e-05

Enter password: s
Incorrect password
Time taken:  0.10009485227287533
```

- We can write a script to brute force the password.
- After getting the first password, we realize there are more levels
  to this challenge. There are a total of 5 levels, each having a different password and a different time delay buffer.
- The script to solve this challenge is provided in [solve.py](./solve.py).
- The output of the script will look something like this:

```
[+] Starting local process './cpu.py': pid 5555
Found passwords:  ['sloppytoppywithatwist']
gingerdangerhermoinegrangep
2.6819376057307664e-05
[*] Stopped process './cpu.py' (pid 5555)
[+] Starting local process './cpu.py': pid 5557
Found passwords:  ['sloppytoppywithatwist']
gingerdangerhermoinegrangeq
2.6230198239218794e-05
[*] Stopped process './cpu.py' (pid 5557)
[+] Starting local process './cpu.py': pid 5559
Found passwords:  ['sloppytoppywithatwist', 'gingerdangerhermoinegranger']
[*] Stopped process './cpu.py' (pid 5559)
[+] Starting local process './cpu.py': pid 5561
Found passwords:  ['sloppytoppywithatwist', 'gingerdangerhermoinegranger']
a
1.6173810485567395e-05
[*] Stopped process './cpu.py' (pid 5561)
[+] Starting local process './cpu.py': pid 5563
Found passwords:  ['sloppytoppywithatwist', 'gingerdangerhermoinegranger']
b
7.233274605283463e-05
[*] Stopped process './cpu.py' (pid 5563)
```

- However, this script takes hours to find the flag.
- A faster way to solve this challenge is to use multithreading. This has been done
  in [solve_multithread.py](./solve_multithread.py).
- Using the multi-threaded script, we can complete the 5 levels and get the flag in a few minutes.

## Flag

```
BITSCTF{c0n6r47ul4710n5_0n_7h3_5ucc355ful_3n7ry}
```

## Author

[**@Pamdi**](https://github.com/Pamdi8888)
