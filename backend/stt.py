# stt.py
import logging      #Used for error logging.
import whisper


#Sometimes Whisper hallucinates text when audio is silent.Instead of returning empty text, Whisper may return
_SILENCE_TOKENS = {
    "\u2026",
    "...",
    ". . .",
    "[ Silence ]",
    "[silence]",
    "(silence)",
    "[BLANK_AUDIO]",
    "(BLANK_AUDIO)",
    "\u062e\u0627\u0645\u0648\u0634",   # خاموش
}

_MIN_CONFIDENCE = -0.7     #Higher = better confidence


class STT:
    _model = None

    @staticmethod
    def _get_model():
        if STT._model is None:
            MODEL_SIZE = "small"           #Good balance for production
            print(f"[STT] Loading Whisper '{MODEL_SIZE}' model…", flush=True)
            STT._model = whisper.load_model(MODEL_SIZE)
            print("[STT] Whisper model ready.", flush=True)
        return STT._model

    get_model = _get_model

    def __init__(self):
        self.transcript:     str   = ""
        self.stt_confidence: float = 0.0

    def convert_to_text(self, audio_path: str, language: str = "en") -> dict:

        import os
        if not audio_path or not os.path.exists(audio_path):
            return {
                "transcript": "",
                "confidence": 0.0,
                "language":   language,
                "error":      f"Audio file not found: {audio_path}",
            }

        model   = self._get_model()
        options = {"fp16": False, "language": language}         #bcz fp16 works on GPUs

        print(f"[STT] Transcribing with language='{language}'…", flush=True)         #text on exact time in mili sec, No waiting ,Buffering logic

        try:
            result         = model.transcribe(audio_path, **options)          #returns dict with meta-data
            raw_transcript = (result.get("text") or "").strip()               #remove spaces

            if raw_transcript in _SILENCE_TOKENS:
                print(f"[STT] Silence placeholder '{raw_transcript}' → empty.", flush=True)
                raw_transcript = ""

            #Whisper splits audio into chunks.like  {"text": "Hello", "avg_logprob": -0.2},
            segments = result.get("segments", [])
            if segments:
                probs = [s.get("avg_logprob", 0.0) for s in segments]         #Collects all confidence scores
                self.stt_confidence = sum(probs) / len(probs)                 #Computes mean confidence
            else:
                self.stt_confidence = 0.0

            if self.stt_confidence < _MIN_CONFIDENCE and raw_transcript:
                print(
                    f"[STT] Low confidence ({self.stt_confidence:.3f}) — "
                    "clearing hallucinated transcript.",
                    flush=True,
                )
                raw_transcript = ""

            self.transcript = raw_transcript
            detected_lang   = result.get("language") or language

            print(
                f"[STT] Result → transcript='{self.transcript[:80]}'  "
                f"lang={detected_lang}  conf={self.stt_confidence:.3f}",
                flush=True,
            )

            return {
                "transcript": self.transcript,
                "confidence": self.stt_confidence,
                "language":   detected_lang,
            }

        except Exception as exc:
            logging.exception(f"[STT] Transcription failed: {exc}")
            return {
                "transcript": "",
                "confidence": 0.0,
                "language":   language,
                "error":      str(exc),
            }