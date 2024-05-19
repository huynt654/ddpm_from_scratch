
from dataset.custom import create_custom_dataset


def create_dataset(dataset: str, **kwargs):

    if dataset == "custom":
        return create_custom_dataset(**kwargs)
    else:
        raise ValueError(f"dataset except one of {'mnist', 'cifar', 'custom'}, but got {dataset}")