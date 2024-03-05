from os \
    import (
        listdir,
        walk
)

from os.path import (
    isdir,
    join
)

from TrainingAndEvaluation.stage \
    import (
        get_label_annotations,
        get_label_images,
        get_label_xml,
        get_label_jpeg,
        get_label_jpg
)


def is_file_jpg(
    file_name: str
) -> bool:
    return (
        file_name.endswith(
            get_label_jpeg()
        )
        or
        file_name.endswith(
            get_label_jpg()
        )
    )


def setup_of_paths_to_dataset(
    location_of_dataset: str
) -> tuple:
    dataset_annotation_path: str | None = None
    dataset_images_path: str | None = None

    location_of_dataset = str(
        location_of_dataset
    )

    found_directories_in_dataset = listdir(
        location_of_dataset
    )

    for found_file in found_directories_in_dataset:
        full_path = join(
            location_of_dataset,
            found_file
        )

        found_file = found_file.lower()

        if isdir(
            full_path
        ):
            if found_file == get_label_annotations():
                dataset_annotation_path = full_path

            if found_file == get_label_images():
                dataset_images_path = full_path

    return (
        dataset_annotation_path,
        dataset_images_path
    )


def retrieve_annotations(
    location: str
) -> list:
    annotations: list = list()

    for root, dirs, files \
        in walk(
            location
    ):
        for file in files:
            full_path = join(
                root,
                file
            )

            tmp_filename: str = file.lower()

            if tmp_filename.endswith(
                get_label_xml()
            ):
                annotations.append(
                    full_path
                )


    return annotations

def generate_dataset_setup(
    location_of_dataset: str
) -> tuple:
    dataset_path = setup_of_paths_to_dataset(
        location_of_dataset
    )

    annotations = retrieve_annotations(
        dataset_path[0]
    )

    annotations.sort()

    for idx in range(len(annotations)):
        annotations[idx] = parsing_annotation(annotations[idx])

        file_name: str = annotations[idx][0]
        full_path_to_image: str = join(location_of_dataset, get_label_images())
        full_path_to_image = join(full_path_to_image, file_name)
        annotations[idx][0] = full_path_to_image

    return tuple(annotations)



def parsing_annotation(
    location_for_annotation: str
) -> list:
    import xml.etree.ElementTree as eT

    tree = eT.parse(
        location_for_annotation
    )

    root = tree.getroot()

    filename = root.find(
        'filename'
    ).text

    boxes: list = []
    classes: list = []

    for obj in root.iter(
        "object"
    ):
        cls = obj.find(
            "name"
        ).text

        classes.append(
            cls
        )

        bounding_box = obj.find(
            "bndbox"
        )

        xMin: float = float(
            bounding_box.find(
                'xmin'
            ).text
        )

        yMin: float = float(
            bounding_box.find(
                'ymin'
            ).text
        )

        xMax: float = float(
            bounding_box.find(
                'xmax'
            ).text
        )

        yMax: float = float(
            bounding_box.find(
                'ymax'
            ).text
        )

        boxes.append(
            [
                xMin,
                yMin,
                xMax,
                yMax
            ]
        )

    return [filename, boxes, classes]


