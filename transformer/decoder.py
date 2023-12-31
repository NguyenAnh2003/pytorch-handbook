import torch.nn as nn
from transformer_embedding import TransformerEmbedding
import torch.nn.functional as TF
class DecoderStack(nn.Module):
    """
    perform cross attention with Encoder hidden feature
    :parameter
    """
    def __init__(self, vocab_size: int, max_seq_len: int, d_model: int, nhead: int,
                 n_layers: int, dropout: float = 0.1):
        super().__init__()
        self.decoder_embedding = TransformerEmbedding(vocab_size=vocab_size,
                                                      d_model=d_model,
                                                      max_len=max_seq_len,
                                                      dropout=0.1)
        # d_model, nhead, dim_feedforward, dropout, activation
        self.decoder = nn.TransformerDecoder(
            # MHA,
            nn.TransformerDecoderLayer(
                d_model=d_model,
                nhead=nhead,
                dropout=dropout
            ),
            num_layers=n_layers
        )
    def forward(self, x):
        x = self.embedding(x)


