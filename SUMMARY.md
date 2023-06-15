**Embrapa WGISD: Embrapa Wine Grape Instance Segmentation Dataset** is a dataset for semantic segmentation, object detection, and instance segmentation tasks. It is used in the agriculture industry.

The dataset consists of 300 images with 6451 labeled objects belonging to 2 different classes including *uva_bbox* and *uva*.

Each image in the WGISD dataset has bounding box annotations and some have both instance segmentation annotations with bounding boxes. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation task (only one mask for every class). All images are labeled (i.e. with bboxes, 137 of them with binary masks of a grape cluster). There are 2 splits in the dataset: *test* (58 images) and *train* (242 images). The dataset was released in 2019 by the [Embrapa Agricultural Informatics, Brazil](https://www.embrapa.br/en/agricultura-movida-a-ciencia) and the [Institute of Computing, University of Campinas, Brazil](https://ic.unicamp.br/en/).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/wgisd/raw/main/visualizations/side_annotations_grid.png">
