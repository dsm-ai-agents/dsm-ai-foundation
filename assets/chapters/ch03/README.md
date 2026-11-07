# Chapter 03 — How machines learn

Why it matters: understand learning and testing so you can distinguish genuine improvement from memorization.

| Order | Concept | Image |
| --- | --- | --- |
| Index | Chapter introduction and topic list | [Chapter index](00-chapter-index.png) |
| 017 | Supervised learning | [Image](017-supervised-learning.png) |
| 018 | Unsupervised learning | [Image](018-unsupervised-learning.png) |
| 019 | Reinforcement learning | [Image](019-reinforcement-learning.png) |
| 020 | Neural networks and deep learning | [Image](020-neural-networks-and-deep-learning.png) |
| 021 | Training versus inference | [Approved pilot](021-training-versus-inference.png) |
| 022 | Training, validation, and test sets | [Image](022-training-validation-and-test-sets.png) |
| 023 | Overfitting | [Image](023-overfitting.png) |
| 024 | Fine-tuning | [Image](024-fine-tuning.png) |

## Teaching qualifications

- Supervised learning uses labels or target values; predictions on new examples still need evaluation.
- Unsupervised groups depend on the chosen representation and method, not necessarily an objectively correct categorization.
- Reinforcement learning optimizes reward signals; poorly chosen rewards can lead to unwanted behavior.
- Neural-network layers are mathematical transformations, not evidence of human-like consciousness. The processing illustration is deliberately simplified.
- Training updates parameters. Inference can use changing context or external memory without necessarily updating the model's weights.
- Validation informs model or setting selection; keep test data held out from that process. Real split strategies depend on time, leakage risks, and the application.
- Overfitting is excessive adaptation to training specifics, including noise. Generalization must be assessed on suitable unseen examples.
- Fine-tuning changes learned behavior through additional training and does not guarantee better performance. Compare against a baseline and evaluate.

## Sources

- [Microsoft: techniques of machine learning](https://github.com/microsoft/ML-For-Beginners/blob/main/1-Introduction/4-techniques-of-ML/README.md)
- [Microsoft: reinforcement learning](https://github.com/microsoft/ML-For-Beginners/tree/main/8-Reinforcement)
- [Microsoft: fine-tuning](https://github.com/microsoft/generative-ai-for-beginners/blob/main/18-fine-tuning/README.md)

## Production and review

Flattened PNGs use the approved dark navy, amber, and teal APEX identity. Exact prompts and actual native dimensions are recorded in `manifest.json`. Concept 021 reuses the approved pilot unchanged. Review status is recorded per image in the manifest; audience comprehension and projector readability require live review.
