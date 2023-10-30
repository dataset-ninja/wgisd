The authors of the **Embrapa WGISD** dataset aim to provide images and annotations for studying object detection and instance segmentation in viticulture for image-based monitoring and field robotics. The dataset includes instances from five different grape varieties captured in the field, exhibiting variations in grape pose, illumination, and focus, as well as genetic and phenological characteristics such as shape, color, and compactness.

The mentioned challenges of automation in agriculture, particularly in outdoor environments and uncertain plant structures, require advanced monitoring systems capable of fine-grained detection and localization of plant structures and fruits. Accurate fruit detection and localization are essential for various agricultural applications, including fruit counting, yield estimation, precision agriculture, disease monitoring, nutrient deficiency detection, and actuation tasks like automated spraying and harvesting.

Embrapa WGISD consists of 300 RGB images showcasing 4,432 grape clusters from five different grape varieties, as summarized in Table 1. The images were captured from a single winery, which employed dual pruning for shaping and production, resulting in canopies of lower density. The dataset represents real-world, trellis system-based wine grape production, and no specific intervention was performed for dataset construction. The camera captures frontal pose images, where the principal axis is approximately perpendicular to the wires of the trellis system and plant rows.

| Prefix     | Variety            | Date       | Images   | Boxed clusters | Masked clusters |
| ---------- | ------------------ | ---------- | -------- | --------------- | --------------- |
| CDY        | ***chardonnay***         | 2018-04-27 | 65       | 840             | 308             |
| CFR        | ***cabernet eranc***     | 2018-04-27 | 65       | 1,069           | 513             |
| CSV        | ***cabernet sauvignon*** | 2018-04-27 | 57       | 643             | 306             |
| SVB        | ***sauvignon blanc***    | 2018-04-27 | 65       | 1,317           | 608             |
| SYH        | ***syrah***              | 2017-04-27 | 48       | 563             | 285             |
| **Total** |                    |            | **300** | **4,432**      | **2,020**      |

The dataset provides binary masks for 2,020 clusters out of 4,432, used for supervised instance segmentation training. 

The images were captured at the vineyards of Guaspari Winery in São Paulo, Brazil, with dual pruning performed by the winery staff. A Canon EOS REBEL T3i DSLR camera and a Motorola Z2 Play smartphone were used to capture the images. The cameras were positioned between the vine lines, facing the vines at distances of around 1-2 meters. The REBEL camera captured 240 images, including all Syrah pictures, while the Z2 smartphone captured 60 images covering all other varieties except Syrah. The REBEL images were scaled to 2048 × 1365 pixels, and the Z2 images were scaled to 2048 × 1536 pixels. More detailed information about the capture process can be found in the Exif data in the original image files, which are part of the dataset.
