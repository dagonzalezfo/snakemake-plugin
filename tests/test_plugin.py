from typing import Optional, Type
from snakemake_interface_software_deployment_plugins.tests import (
    TestSoftwareDeploymentBase,
)
from snakemake_interface_software_deployment_plugins import (
    EnvSpecBase,
    EnvBase,
    ShellExecutable,
)
from snakemake_interface_software_deployment_plugins.settings import (
    SoftwareDeploymentSettingsBase,
)

from snakemake_software_deployment_plugin_eessi import Env, EnvSpec, SoftwareDeploymentSettings


# There can be multiple subclasses of SoftwareDeploymentProviderBase here.
# This way, you can implement multiple test scenarios.
# For each subclass, the test suite tests the environment activation and execution
# within, and, if applicable, environment deployment and archiving.
class TestSoftwareDeployment(TestSoftwareDeploymentBase):
    __test__ = True  # activate automatic testing
    # Use ShellExecutable object for shell_executable
    shell_executable = ShellExecutable("bash", args=["-l"], command_arg="-c")

    def get_env_spec(self) -> EnvSpecBase:
        # Return an EESSI EnvSpec with common modules for testing
        # These should be modules available in EESSI 2023.06
        return EnvSpec(names=["GCC/12.2.0", "Python/3.10.8"])

    def get_env_cls(self) -> Type[EnvBase]:
        # Return the Env class from the EESSI plugin to be tested
        return Env

    def get_settings(self) -> Optional[SoftwareDeploymentSettingsBase]:
        # Return EESSI plugin settings
        # myparam is optional, so we can set it to None
        return SoftwareDeploymentSettings(myparam=None)

    def get_settings_cls(self) -> Optional[Type[SoftwareDeploymentSettingsBase]]:
        # Return the settings class
        return SoftwareDeploymentSettings

    def get_test_cmd(self) -> str:
        # Return a simple test command that should work in the EESSI environment
        # This command will be executed within the loaded modules
        return "python --version"

    def get_contained_executable(self) -> str:
        # Return an executable that should be available in the environment
        return "python"
