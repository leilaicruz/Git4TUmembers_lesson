## The home folder of Git Bash is not the default C:/Users/USERNAME , thus the ssh-key does not work 

- use the WSl , where you can access the home folder where the key is stored. If using git bash , it is not possible to access the key in the folder that is stored by default. For instance the keys generated in the WSL terminal in the home folder are not in the home folder of git bash. 

- Also you can use the Github desktop, but still need to Generate a key pair and add it to your agent (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

- It seems that this is only happening is the TU laptop is on the TU network, at a home network , the git bash has the home folder where it should be. 

## when using WSL, if ~/.config does not exist 

If the gitconfig file is not at the home folder of WSL , we can just copy it from the C:/Users/USERNAME folder or from the H:/ folder 

```bash
cp /mnt/c/Users/USERNAME/.gitconfig ~/.gitconfig
```