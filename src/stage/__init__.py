from stage.labels \
    import (
        get_label_images,
        get_label_annotations,
        set_label_images,
        set_label_annotations
)


from stage.singletons \
    import (
        retrieve_validation_data,
        retrieve_training_data,
        update_training_data,
        update_validation_data,
        get_location_to_training_data,
        set_location_to_training_data,
        get_location_to_validation_data,
        set_location_to_validation_data
)


from stage.training \
    import (
    training
)


from stage.evaluation \
    import (
    evaluation
)


from stage.dataset \
    import (
    generate_training_dataset,
    generate_validation_dataset
)
