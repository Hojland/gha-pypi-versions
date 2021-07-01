# GitHub Action for querying pypi versions of package

![gha-pypi-versions](https://socialify.git.ci/hojland/gha-pypi-versions/image?description=1&font=KoHo&forks=1&issues=1&language=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light) 
<p align="center">
<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white" align="center">
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white" align="center">
<img src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white "align="center">
</p>

GitHub actions can be integrated in any repository. Create a new folder called `.github/workflows/<any-name>.yml`. Paste the following starter code:

```yml
name: Update Projects
on:
  schedule:
    - cron: '0 0 * * *'
    # This makes the action to run at the end of every day. Customize this accordingly or you can also trigger this action for GitHub events (Pull, Push). Check the GitHub actions page for that.
  workflow_dispatch:
    # workflow_dispatch allows you to trigger the action any time manually

jobs:
  get-mlflow-versions:
    name: Grab the latest versions of mlflow from pypi package index
    runs-on: ubuntu-latest
    outputs:
      mlflow-versions: ${{ steps.mlflow-version.outputs.versions }}
    steps:
      - uses: actions/checkout@v2
      - uses: hojland/gha-pypi-versions
        id: mlflow-version
        with:
          pkg_name: mlflow
          latest_num: 5
  build_and_push:
    runs-on: ubuntu-latest
    needs: [tag_and_release]
    strategy:
      matrix:
        mlflow-versions:  ${{ steps.get-mlflow-versions.outputs.mlflow-versions }}
    steps:
      - uses: actions/checkout@v2
```

## License
The scripts and documentation in this project are released under the [MIT License](LICENSE)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/hojland/gha-pypi-versions/tags). 

## Authors

* **Martin Højand Hansen** - *Initial work* - [hojland](https://github.com/hojland)

See also the list of [contributors](https://github.com/hojland/gha-pypi-versions/contributors) who participated in this project.