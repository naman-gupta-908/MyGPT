# MyGPT 
GPT from Scratch

## Transformer from Scratch (Attention Is All You Need)

This project implements the Transformer architecture from the paper "Attention Is All You Need" using PyTorch and NumPy.

## Motivation
To understand how modern LLMs work beyond APIs by building
the core architecture from first principles.

## What’s implemented
- Multi-head self attention
- Positional encoding
- Decoder only architecture
- Attention masking
- Custom training loop

## Training setup
- Dataset: TinyStories
- Parameters: ~30M
- Hardware: Colab T4 (free tier)

## Results
Training and validation loss decrease steadily, indicating
successful learning despite limited scale.

(Output quality is partially coherent, as expected with
small data and model size.)

## Key learnings
- Attention math in practice
- Importance of scaling
- Data > architecture
- Debugging tensor shapes & masks

## Limitations
- Small dataset
- Minimal preprocessing
- Limited compute

## How to run
Collab Link:
https://colab.research.google.com/drive/1fEi8xNb28_d9-dHeVOcnL6X-q2isMNAQ?authuser=1#scrollTo=Nx_kEEfKwDCv
