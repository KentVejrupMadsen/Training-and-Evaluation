from TrainingAndEvaluation.stage.datasets.setup_of_dataset \
    import (
        setup_of_paths_to_dataset,
        generate_dataset_setup,
        parsing_for_annotations
)

test_location: str = '/mnt/d/Workspace/KentVejrupMadsen/Training And Evaluation/dataset'

def test_generation_of_dataset_paths() -> None:
    global test_location
    paths = setup_of_paths_to_dataset(
        test_location
    )

    assert isinstance(
        paths,
        tuple
    )

def test_generation_of_dataset_setup() -> None:
    global test_location

    result = generate_dataset_setup(
        test_location
    )

    assert isinstance(
        result,
        dict
    )

def test_parsing_annotations() -> None:
    global test_location

    file_locations: dict = generate_dataset_setup(
        test_location
    )

    dataset = parsing_for_annotations(
        file_locations
    )

    print(
        dataset
    )

    assert True