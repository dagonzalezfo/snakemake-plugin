# Snakemake software deployment plugin for EESSI support

This project provides a Snakemake software deployment plugin for EESSI environments.
It lets workflows request modules from the EESSI software stack through Snakemake's
software deployment plugin API.

## What it does

- registers a Snakemake software deployment plugin named `eessi`
- validates that EESSI is correctly initialized
- checks that the requested modules are available
- loads the required EESSI modules before each shell command

## Requirements

This plugin depends on the Snakemake feature branch that includes software deployment
plugins support:

- GitHub: https://github.com/snakemake/snakemake/tree/feat/software-deployment-plugins
- The project uses a pinned commit in `pixi.toml` for reproducible builds.

## Install

```bash
pixi install --environment dev
```

## Example usage

```python
rule test_eessi_module:
    output:
        "results/gcc_version.txt"
    threads: 1
    software:
        "eessi(names=[\"GCC/12.2.0\"])"
    shell:
        "gcc --version > {output}"
```

Or from the CLI:

```bash
pixi run --environment dev snakemake --snakefile tests/Snakefile --sdm eessi --cores 1 --forceall
```

## Notes

- The plugin sources the EESSI bash init script before loading modules.
- It validates the environment with `eessi check` and module availability checks.
- The repository includes a small end-to-end Snakefile in `tests/` for verification.
=======
