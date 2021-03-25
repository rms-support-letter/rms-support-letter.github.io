# An open letter in support of RMS.

Optional for *nix users, before add sign can add pre-commit hook, for validated sign:

```sh
$ cp ./pre-commit .git/hooks/pre-commit
```

To sign, create a file in `_data/signed/` folder named `<username>.yaml` with the following content:

```yaml
name: <your name here>
link: <link to your profile or site>
```

Without the `<>`.

Example:
```yaml
name: Example name
link: https://example.com/
```

Don't use `<>` in this file, as well as non-ascii symbols in file name.
If you are able to, please use your real name and add projects and affiliatied organizations in parentheses.

When youre done, create a pull request.

Let's keep the tone firm, but professional.

If you can, please consider sharing this letter on your forums and social media and notify journalists who might be helpful to our cause.

**Pull requests merged within 12 hours - due to a huge volume of PRs they will be merged in batches**
