import sys
import requests
from distutils.version import StrictVersion

def versions(package_name: str, latest_num: int):
    url = f"https://pypi.org/pypi/{package_name}/json"
    data = requests.get(url).json()
    versions = list(data["releases"].keys())
    print(versions)
    if len(versions) > latest_num:
        versions = versions[-latest_num:]
    return versions

if __name__ == "__main__":
    print(sys.argv[1])
    vers = versions(str(sys.argv[1]), int(sys.argv[2]))
    print(f"::set-output name=versions::${vers}")