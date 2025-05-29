from speechbrain.pretrained import EncoderClassifier
import torch


def classify_audio(audio_path: str):
    """
    Classify the audio file using the pre-trained accent identification model.

    Model: CommonAccent
    Source: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa
    Zuluaga-Gomez, J., Ahmed, S., Visockas, D., & Subakan, C. (2023). CommonAccent: Exploring large acoustic pretrained models for accent classification based on common voice. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2305.18283
    """
    try:
        model = EncoderClassifier.from_hparams(source="pretrained_models")

        logits, _, index, pred = model.classify_file(audio_path)
        predicted_accent = pred[0]

        # Convert logits to probabilities (softmax)
        probabilities_per_accent = torch.softmax(logits, dim=1).squeeze(0)
        probability = float(probabilities_per_accent[index][0])

        return predicted_accent, probability
    except Exception as e:
        raise Exception(f"Failed to classify audio: {e}")
