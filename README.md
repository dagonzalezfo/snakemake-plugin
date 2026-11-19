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

This plugin requires Snakemake with software deployment plugin support and an EESSI
native installation.

- EESSI configured using native installation
- A Snakemake release that includes [software deployment plugin support](https://github.com/snakemake/snakemake/pull/3339)

**Compatibility note:** Snakemake 9.27.1 does not include this support, so the
plugin will not work with 9.27.x. According to Snakemake pull request [#4313](https://github.com/snakemake/snakemake/pull/4313),
this feature will be available in Snakemake 10.0.0. For development and end-to-end testing, use the merged
Snakemake commit `91763d644db0a6051c40014fa8ffad340f7d39a0`. Installing this
plugin does not check or upgrade the Snakemake version in the host environment.
Releasing the plugin depends on the Snakemake 10.0.0 release.  

## Example usage

```python
rule test_eessi_module:
    output:
        "results/gcc_version.txt"
    threads: 1
    software:
        'eessi(eessi_version="2023.06", modules=["GCC/12.2.0"])'
    shell:
        "gcc --version > {output}"
```

Or from the CLI:

```bash
snakemake --snakefile tests/Snakefile --sdm eessi --cores 1 --forceall
```

## Notes

- The plugin sources the EESSI bash init script before loading modules.
- It validates the environment with `eessi check` and module availability checks.
- The repository includes a small end-to-end Snakefile in `tests/` for verification.
