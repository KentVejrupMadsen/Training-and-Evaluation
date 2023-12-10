from src.TrainingAndEvaluation.stage.datasets.setup_of_dataset \
    import setup

def test_generation_of_datasets() -> None:
    setup(
        '/mnt/d/Workspace/KentVejrupMadsen/Training And Evaluation/dataset'
    )

    assert True