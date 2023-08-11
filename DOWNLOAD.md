Dataset **WGISD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/F/G/j9/v81S9ls8VgepmFv6eOzybr1juhDWyfqEr4RqmKG8fyH0WMxteAwoOiVBjJxLscNNPatRWOxDYbGWgeGrSyB4PIRC3kSgQxtEWH55n1Oef7DT2eVIvbGb2Hdbtggx.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='WGISD', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://zenodo.org/record/3361736/files/thsant/wgisd-1.0.0.zip?download=1).