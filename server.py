from mcp.server.fastmcp import FastMCP
import subprocess

mcp = FastMCP("iptables")


def run_iptables(*args):
    result = subprocess.run(
        ["sudo", "iptables", *args],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    return result.stdout


@mcp.tool()
def list_rules() -> str:
    """List the current IPv4 iptables rules with counters."""

    return run_iptables("-L", "-n", "-v", "--line-numbers")


@mcp.tool()
def list_rules_save() -> str:
    """Return the current IPv4 rules in iptables-save format."""

    return run_iptables("-S")


if __name__ == "__main__":
    mcp.run()
