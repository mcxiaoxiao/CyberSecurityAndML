import torch.nn.functional as F
from mlmodelwatermarking.marktorch import Trainer
from mlmodelwatermarking import TrainingWMArgs

from utils import LeNet, load_MNIST


def MNIST_merrer():
    """Testing of watermarking for MNIST model."""

    # WATERMARKED
    model = LeNet()
    trainset, valset, testset = load_MNIST()

    args = TrainingWMArgs(
                trigger_technique='merrer',
                optimizer='SGD',
                lr=0.01,
                gpu=True,
                epochs=10,
                nbr_classes=10,
                batch_size=64)

    trainer = Trainer(
                model=model,
                args=args,
                trainset=trainset,
                valset=valset,
                testset=testset)

    ownership = trainer.train()
    accuracy_wm_regular = trainer.test()
    verification = trainer.verify(ownership)
    assert verification['is_stolen'] is True

    # CLEAN
    model = LeNet()
    args.watermark = False
    trainer_clean = Trainer(
                    model=model,
                    args=args,
                    trainset=trainset,
                    valset=valset,
                    testset=testset)

    trainer_clean.train()
    accuracy_clean_regular = trainer_clean.test()
    accuracy_loss = round(accuracy_clean_regular - accuracy_wm_regular, 4)
    print(f'Accuracy loss: {accuracy_loss}')
    clean_model = trainer_clean.get_model()

    verification = trainer.verify(ownership, suspect=clean_model)
    assert verification['is_stolen'] is False


if __name__ == '__main__':
    MNIST_merrer()
