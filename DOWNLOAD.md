Dataset **WGISD** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/B/Z/JG/uygV62xCvFVgeOIxzTYtFDW3YKhHX7ApR34Q7AWZjq7YEGGRAVvROFnCWgSJHUesjIkxc68ecZAazEXWobcJVksOBbN4IFDOoFWyEtUS56SwRAjDTN1qA49RneIQ.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='WGISD', dst_path='~/dtools/datasets/WGISD.tar')
```
The data in original format can be 🔗[downloaded here](https://zenodo.org/record/3361736/files/thsant/wgisd-1.0.0.zip?download=1)