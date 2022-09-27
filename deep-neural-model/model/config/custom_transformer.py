import opennmt

class MyCustomTransformer(opennmt.models.Transformer):
    def __init__(self):
        super().__init__(
            source_inputter=opennmt.inputters.WordEmbedder(embedding_size=700),
            target_inputter=opennmt.inputters.WordEmbedder(embedding_size=700),
            num_layers=10,
            num_units=700,
            num_heads=10,
            pre_norm= True,
            ffn_inner_dim=3000,
            dropout=0.1,
            attention_dropout=0.3,
            ffn_dropout=0.3,
            share_embeddings=opennmt.models.EmbeddingsSharingLevel.ALL,
        )

model = MyCustomTransformer