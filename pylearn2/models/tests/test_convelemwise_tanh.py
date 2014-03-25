from theano import config
from theano.sandbox import cuda

from pylearn2.config import yaml_parse


def test_conv_tanh_basic():

    # Tests that we can load a convolutional tanh model
    # and train it for a few epochs (without saving) on a dummy
    # dataset-- tiny model and dataset
    yaml_file = "conv_elemwise_tanh.yaml"
    with open(yaml_file) as yamlh:
        yaml_lines = yamlh.readlines()
        yaml_str = "".join(yaml_lines)

    train = yaml_parse.load(yaml_str)
    train.main_loop()

if __name__ == "__main__":
    test_conv_tanh_basic()
