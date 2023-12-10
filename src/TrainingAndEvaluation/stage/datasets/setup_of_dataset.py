from os import listdir

from os.path import (
    isdir,
    join
)

from TrainingAndEvaluation.stage.labels \
    import get_label_annotations

def setup(
    location_of_dataset: str
):
    dataset_annotation_path: str | None = None
    dataset_images_path: str | None = None

    files_in_dataset: list = listdir(
        location_of_dataset
    )

    for file_name in files_in_dataset:
        full_path = join(location_of_dataset, file_name)

        if isdir(
            full_path
        ):
            file_name = file_name.lower()

            if file_name == get_label_annotations():
                dataset_annotation_path = full_path



