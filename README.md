# Gemma V.S. HumanEval Dataset: How good is Gemma on code generation?
Tianhao Qu

## Gemma: Quick Recap
- Decoder-Only model, context length 8192 tokens
- 2B & 7B parameters variant
- Trained on 2T and 6T tokens of primarily-English data from web documents, mathematics, and code
- Outperform other latest models in 11 different metrics

## Differences between 2B and 7B Variant?
- d_model: 2048 vs 3072
- Attention Mechanisms: Multi-Query vs Multi-Head
- Training Infrastructure: 512 vs 4096 TPUv5e Chips
- Training Data Tokens: 2T vs 6T

## Instruction-Tuned Model?
According to the Gemma Paper: **"We fine-tune Gemma 2B and 7B with supervised fine-tuning (SFT) on a mix of text-only English-only synthetic and human-generated prompt-response pairs and reinforcement learning from human feedback (RLHF) with the reward model trained on labelled English-only preference data and the policy based on a set of high-quality prompts. We find that both stages are important for improved performance on downstream automatic evaluations and human preference evaluations of model outputs."**

In other words? More chatty and better at following instructions.

