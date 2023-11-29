# spack-repo
Repository of spack package configurations for CHM build

Clone this into a folder
```
git clone https://github.com/Chrismarsh/spack-repo.git
```

and then add this as the first repo as described [on Spack's readme](https://spack.readthedocs.io/en/latest/repositories.html#repos-yaml).

```
$ cat repos.yaml
	repos:
	  - /Users/myuser/spack-repo
	  - $spack/var/spack/repos/builtin

```