# Neural-machine-thesis

In order to run the first neural network, you should follow this steps (the example will be based on a unix machine, since it was created in docker):
1. go to the directory named deep-neural-model -> `cd deep-neural-model`
2. then run one of those command, depending on your choice, remembering that, the first one will use the default open-nmt Transformer model, the second one will be based on my custom model. 
    - `<onmt-main --model_type Transformer --config data.yml --auto_config train>`
    - `<onmt-main --model model/config/custom_transformer.py --config data.yml --auto_config train>` (not working yet)

## Important note!

In the data.yml file, I set the parameter: `batch_size:0`, in the train label, it means that he will automatically search for the larger batch size avaiable. This parameter can give some problems, so if the training won't start my advice is to change it to `batch_size: 64`
