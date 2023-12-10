from TrainingAndEvaluation.stage \
    import (
        set_location_to_training_data,
        set_location_to_validation_data
)

from workspace \
    import location_to_dataset


def initialise() -> None:
    print('Initialise')

    set_location_to_training_data(
        location_to_dataset
    )

    set_location_to_validation_data(
        location_to_dataset
    )