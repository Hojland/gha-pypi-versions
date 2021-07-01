import sys
import requests
from distutils.version import StrictVersion

def versions(package_name: str, latest_num: int):
    url = f"https://pypi.org/pypi/{package_name}/json"
    data = requests.get(url).json()
    versions = list(data["releases"].keys())[-latest_num:]
    return versions

if __name__ == "__main__":
    vers = versions(str(sys.argv[1]), int(sys.argv[2]))
    print(f"::set-output name=versions::${vers}")