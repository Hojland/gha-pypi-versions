import sys
import requests
import jmespath
import operator

def versions(package_name: str, latest_num: int):
    url = f"https://pypi.org/pypi/{package_name}/json"
    data = requests.get(url).json()
    versions = list(data["releases"].keys())
    upload_times = list(data["releases"].values())
    upload_times = jmespath.search("[*][*].upload_time", upload_times)
    upload_times = [max(upload_time) for upload_time in upload_times]
    versions = dict(zip(versions, upload_times))
    if len(versions) > latest_num:
        versions = dict(sorted(versions.items(), key=operator.itemgetter(1), reverse=True)[:5])
    versions = list(versions.keys())
    return versions

if __name__ == "__main__":
    print(f"::debug :: Getting versions")
    vers = versions(str(sys.argv[1]), int(sys.argv[2]))
    print(f"::debug :: Got versions with length {len(vers)}")
    print(f"::set-output name=versions::{vers}")