## Checklist

- Init Nix flake with simple devshell of python3 and uv?
- init uv workspace
- use uv2nix to integrate uv workspace into the flake.

## Build Backends

Python needs a build backend to package the code into a wheel or tarball.

You define this in `pyproject.toml`, defining what the build backend requires and where the code that builds the package lives.

Build systems like `setuptools`:

- read `pyproject.toml`
- builds the project with either `build_sdist()` or `build_wheel()`
- output packages into a `dist/` folder

## Workspaces

A workspace is a top level folder containing a `uv.lock` that may contain one or more Python projects (each defined by a `pyproject.toml`).

## pyproject.nix

`pyproject.nix` provides generic Nix builders for Python projects a.k.a. translate Python build instructions (`pyproject.toml`) into Nix derivations.

## Nix Functions used in uv2nix

A "Python package set" or "scope" is a collection of Python packages for one interpreter version.

`pkgs.callPackage` calls a Nix file with dependencies, aka `{lib, ...}`, from the Nixpkgs pkgs.

`lib.composeManyExtension` just merges a list of overlays into one.

`overrideScope` rebuilds a Python package set with extra overlays, for example a overlay merge with `composeManyExtension` into a base python package set e.g. the uv deps + build system.
