# https://zenodo.org/record/3361736#.YkvzPH9Bzmg

import os

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "Wine Grape"
dataset_path = "./APP_DATA/wgisd-1.0.0/thsant-wgisd-ab223e5"
items_folder = "data"
batch_size = 30
images_ext = ".jpg"
anns_ext = ".txt"
mask_ext = ".npz"

all_data_path = os.path.join(dataset_path, items_folder)


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    mask_path = os.path.join(all_data_path, get_file_name(image_path) + mask_ext)
    if file_exists(mask_path):
        data = np.load(mask_path, allow_pickle=True)

        lst = data.files
        for item in lst:
            mask = data[item]  # [:, :, 0]
            for npz_slice in range(mask.shape[2]):
                obj_mask = mask[:, :, npz_slice] == 1
                if len(np.unique(obj_mask)) == 1:
                    continue
                curr_bitmap = sly.Bitmap(obj_mask)
                if curr_bitmap.area > 100:
                    curr_label = sly.Label(curr_bitmap, obj_class)
                    labels.append(curr_label)

    bbox_path = os.path.join(all_data_path, get_file_name(image_path) + anns_ext)

    if file_exists(bbox_path):
        with open(bbox_path) as f:
            content = f.read().split("\n")

            for curr_data in content:
                if len(curr_data) != 0:
                    curr_data = list(map(float, curr_data.split(" ")))

                    left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                    right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                    top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                    bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                    rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                    label = sly.Label(rectangle, obj_class_bbox)
                    labels.append(label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


obj_class = sly.ObjClass("uva", sly.Bitmap)
obj_class_bbox = sly.ObjClass("uva_bbox", sly.Rectangle)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class, obj_class_bbox])
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in ["train", "test"]:
        images_names_file = ds_name + anns_ext
        with open(os.path.join(dataset_path, images_names_file)) as f:
            images_names = f.read().split("\n")
            images_names = [im_name for im_name in images_names if len(im_name) > 0]

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for img_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [
                os.path.join(all_data_path, im_name + images_ext) for im_name in img_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(img_names_batch))

    return project
