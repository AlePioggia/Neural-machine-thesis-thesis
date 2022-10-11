# Neural-machine-thesis

## German-English translation

In order to run the first neural network, you should follow this steps (the example will be based on a unix machine, since it was created in docker):
1. go to the directory named deep-neural-model -> `cd deep-neural-model`
2. then run -> `<onmt-main --model_type Transformer --config data.yml --auto_config train>`

## Chinese-Italian translation

1. go to the directory named chinese_italian -> `cd chinese_italian`
2. run this command -> `onmt-main --model_type Transformer --config data.yml --auto_config train`

## Italian-Chinese translation

1. go to the directory named italian_chinese -> `cd italian_chinese`
2. run this command -> `onmt-main --model_type Transformer --config data.yml --auto_config train`

## Important note!

In the data.yml file, I set the parameter: `batch_size:0`, in the train label, it means that he will automatically search for the larger batch size avaiable. This parameter can give some problems, so if the training won't start my advice is to change it to `batch_size: 64`.
