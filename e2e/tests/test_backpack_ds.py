from pytest import mark
from models.test_base import TestBase, default_timeout


@mark.backpack
class TestBackpackDaemonSet(TestBase):
    workload = "backpack_ds"
    indices = [
        "cpu_vulnerabilities-metadata",
        "cpuinfo-metadata",
        "dmidecode-metadata",
        "k8s_nodes-metadata",
        "lspci-metadata",
        "meminfo-metadata",
        "sysctl-metadata",
        "ocp_network_operator-metadata",
        "ocp_install_config-metadata",
        "ocp_kube_apiserver-metadata",
        "ocp_dns-metadata", 
        "ocp_kube_controllermanager-metadata"
    ]

    
    def test_backpack_daemonset(self, run):
        self.run_and_check_benchmark(run, desired_running_state="Metadata Collecting", desired_complete_state="Metadata Collecting")