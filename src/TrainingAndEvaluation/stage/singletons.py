training_dataset = None

def retrieve_training_data():
    global training_dataset
    return training_dataset


def update_training_data(
    update_training_dataset_with
) -> None:
    global training_dataset
    training_dataset = update_training_dataset_with

validation_dataset = None

def retrieve_validation_data():
    global validation_dataset
    return validation_dataset


def update_validation_data(
    update_validation_dataset_with
) -> None:
    global validation_dataset
    validation_dataset = update_validation_dataset_with


location_to_training_dataset: str | None = None

def get_location_to_training_data() -> str | None:
    global location_to_training_dataset
    return location_to_training_dataset

def set_location_to_training_data(
    update_with_location: str
) -> None:
    global location_to_training_dataset
    location_to_training_dataset = update_with_location

location_to_validation_dataset: str | None = None

def get_location_to_validation_data() -> str | None:
    global location_to_validation_dataset
    return location_to_validation_dataset

def set_location_to_validation_data(
    update_with_location: str
) -> None:
    global location_to_validation_dataset
    location_to_validation_dataset = update_with_location