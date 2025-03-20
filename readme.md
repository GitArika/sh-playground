# sh-playground

This project contains my personal scripts both pythonic and sh alike for
automate common tasks in daily development.

# Useful tips

## Creating an Alias

To make it easy to run a script, such as `setup-typescript.py` script from
anywhere in your terminal, you can create an alias.

_remember to change **{your-path-to-file}** for the content of:_

```sh
pwd # prints {your-path-to-file}
```

### For Bash

1. Open your `.bashrc` file in a text editor:

   ```sh
   nano ~/.bashrc
   ```

2. Add the following line to create an alias:

   ```sh
   alias setup-ts='python /{your-path-to-file}/sh-playground/setup-typescript.py'
   ```

3. Save the file and exit the text editor (Ctrl+X, then Y, then Enter).

4. Reload your `.bashrc` file to apply the changes:

   ```sh
   source ~/.bashrc
   ```

### For Zsh

1. Open your `.zshrc` file in a text editor:

   ```sh
   nano ~/.zshrc
   ```

2. Add the following line to create an alias:

   ```sh
   alias setup-ts='python /{your-path-to-file}/sh-playground/setup-typescript.py'
   ```

3. Save the file and exit the text editor (Ctrl+X, then Y, then Enter).

4. Reload your `.zshrc` file to apply the changes:

   ```sh
   source ~/.zshrc
   ```

### Usage

After setting up the alias, you can run the script from anywhere in your
terminal by simply typing:

```sh
setup-ts
```
