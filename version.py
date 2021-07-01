import sys
import requests
from distutils.version import StrictVersion

def versions(package_name: str, latest_num: int):
    url = f"https://pypi.org/pypi/{package_name}/json"
    data = requests.get(url).json()
    versions = list(data["releases"].keys())
    if len(versions) > latest_num:
        versions = versions[-latest_num:]
    return versions

if __name__ == "__main__":
    print(f"::debug :: Getting versions")
    vers = versions(str(sys.argv[1]), int(sys.argv[2]))
    print(f"::debug :: Got versions with length {len(vers)}")
    print(f"::set-output name=versions::{vers}")