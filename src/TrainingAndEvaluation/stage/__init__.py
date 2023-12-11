from TrainingAndEvaluation.stage.singletons import (
    get_location_to_training_data,
    set_location_to_training_data,
    get_location_to_validation_data,
    set_location_to_validation_data,
    get_classes,
    set_classes
)

from TrainingAndEvaluation.stage.labels \
    import (
    get_label_annotations,
    get_label_images,
    get_label_xml,
    get_label_jpeg,
    get_label_jpg,
    set_label_jpg,
    set_label_images,
    set_label_jpeg,
    set_label_xml,
    set_label_annotations
)

from TrainingAndEvaluation.stage.training \
    import (
    training
)


from TrainingAndEvaluation.stage.evaluation \
    import (
    evaluation
)


from TrainingAndEvaluation.stage.dataset \
    import (
    generate_training_dataset,
    generate_validation_dataset
)
