# spack-repo
Repository of spack package configurations for CHM build

Clone this into a folder
```
git clone https://github.com/Chrismarsh/spack-repo.git
```

and then add this as the first repo as described [on Spack's readme](https://spack.readthedocs.io/en/latest/repositories.html#repos-yaml).

This repo now conforms to the v2 api for Spack 1.0.

To use the packages defined in this repository, add the following to your user spack config under:
`~/.spack/repos.yaml`

```
repos:
  - /Users/myuser/spack-repo/spack_repo/chm
```
