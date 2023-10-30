## Programs to be installed prior the workshop 


- Git
- WSL (for Windows , recommended)

### Things to pay attention 

- After installing Git, check that the HOME folder in Git Bash is in C:\Users\USERNAME

```bash
cd ~ 
pwd

```
    - if it is not the case, then we can have problems with establishing the SSH connection to a github repo 
    - solution 1: install WSL (Windows Subsystem for Linux) and work in a linux terminal 
    - solution 2: generate the key in a predetermined folder 