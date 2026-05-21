# nlu.py

import re

# Whisper STT often outputs curly/smart quotes. Normalise before any matching.

def _normalise(text: str) -> str:
    return (
        text
        .replace("\u2019", "'")   # right single quotation mark  →  '
        .replace("\u2018", "'")   # left  single quotation mark  →  '
        .replace("\u201C", '"')   # left  double quotation mark  →  "
        .replace("\u201D", '"')   # right double quotation mark  →  "
        .replace("\u2014", " ")   # em-dash                      →  space
        .replace("\u2013", " ")   # en-dash                      →  space
    )

# ── Clinical keyword banks
_ANXIETY_KEYWORDS_EN = [
    "panic", "panic attack", "anxiety", "anxious", "nervous", "worried",
    "worry", "fear", "scared", "terrified", "racing heart", "palpitation",
    "chest tight", "can't breathe", "shortness of breath", "dizzy",
    "trembling", "shaking", "sweating", "overwhelmed", "doom", "dread",
    "phobia", "restless", "on edge", "keyed up", "tense",
]

_STRESS_KEYWORDS_EN = [
    "stress", "stressed", "pressure", "deadline", "overload", "burnout",
    "exhausted", "drained", "frustrated", "irritable", "snapping",
    "workload", "too much", "can't cope", "can't manage", "falling behind",
    "academic pressure", "exam", "assignment", "no time", "overwhelmed",
    "headache", "sleep problems", "insomnia", "can't sleep",
]

_SADNESS_KEYWORDS_EN = [
    "sad", "cry", "crying", "tears", "hopeless", "helpless", "empty",
    "numb", "worthless", "lonely", "alone", "depressed", "depression",
    "miserable", "grief", "loss", "heartbroken", "low mood", "dark",
]

_HELP_KEYWORDS_EN = [
    "help", "need help", "support", "talk to someone", "counselor",
    "therapist", "doctor", "professional", "hotline", "crisis",
    "don't know what to do", "please help",
]

_ANXIETY_KEYWORDS_UR = [
    "گھبراہٹ", "پریشانی", "بے چینی", "خوف", "ڈر", "دھڑکن", "کانپنا",
    "سانس", "دباؤ محسوس", "گھبرا", "نروس",
]
_STRESS_KEYWORDS_UR = [
    "دباؤ", "ذہنی دباؤ", "تھکاوٹ", "پریشان", "نیند نہیں", "سر درد",
    "چڑچڑاپن", "غصہ", "امتحان", "کام کا بوجھ", "وقت نہیں",
]
_SADNESS_KEYWORDS_UR = [
    "اداسی", "اداس", "رونا", "مایوسی", "ناامید", "تنہا", "اکیلا",
    "بے بس", "بے کار", "خالی پن", "ڈپریشن",
]
_HELP_KEYWORDS_UR = [
    "مدد", "مدد چاہیے", "کسی سے بات", "ڈاکٹر", "ماہر", "ہیلپ لائن",
]

# ── Wellbeing keyword bank
# Negated form ("I am not good/fine/okay") → distress signal.

_WELLBEING_KEYWORDS_EN = [
    "good", "fine", "okay", "ok", "well", "alright",
    "great", "happy", "calm", "relaxed", "better",
]
_WELLBEING_KEYWORDS_UR = [
    "بہتر", "ٹھیک", "اچھا", "خوش", "سکون", "پرسکون",
]

# ── Positive keyword bank 
# Bare words — runtime anchor check ensures only first-person uses count.

_POSITIVE_KEYWORDS_EN = frozenset({
    "happy", "happiness", "glad", "pleased", "content", "fine",
    "okay", "good", "great", "better", "well", "calm", "relaxed",
    "relieved", "grateful", "thankful", "hopeful", "alright",
    "excited", "exciting", "excitement", "thrilled", "elated",
    "joyful", "joy", "wonderful", "fantastic", "amazing", "excellent",
    "awesome", "cheerful", "enthusiastic", "energized", "motivated",
    "inspired", "optimistic", "proud", "confident",
    "improving", "recovering", "progress",
    "nice", "love", "loving", "enjoy", "enjoying",
})

_POSITIVE_KEYWORDS_UR = frozenset({
    "خوش", "بہتر", "اچھا", "ٹھیک", "سکون", "پرسکون",
    "شکرگزار", "امیدوار", "پرجوش", "اچھا محسوس",
})

# First-person anchors — positive keyword must appear near one of these.
_FP_ANCHORS_EN = frozenset({
    "i", "i'm", "im", "i've", "ive", "i'd", "id",
    "we", "we're", "we've", "my", "me", "myself", "our",
})
_FP_ANCHORS_UR = frozenset({"میں", "ہم", "مجھے", "ہمیں", "میرا", "ہمارا"})

_ANCHOR_WINDOW = 6   # tokens left/right to search for anchor

# ── Negation patterns 

_NEGATION_EN = re.compile(
    r"\b(not|no|never|don't|dont|didn't|didnt|isn't|isnt|"
    r"wasn't|wasnt|won't|wont|can't|cant|couldn't|couldnt|"
    r"hardly|barely|neither|nor|am not|i'm not|i am not)\b",
    re.IGNORECASE,
)
_NEGATION_UR = re.compile(
    r"(نہیں|نہ|کبھی نہیں|مت|بالکل نہیں)"
)


INTENT_DISTRESS  = "distress"
INTENT_DENIAL    = "denial"
INTENT_HELP_SEEK = "help_seeking"
INTENT_POSITIVE  = "positive_engagement"
INTENT_NEUTRAL   = "neutral"



class NLU:

    def __init__(self):
        self.intent:            str   = INTENT_NEUTRAL
        self.sentiment:         str   = "neutral"
        self.sentiment_score:   float = 0.0
        self.keywords:          dict  = {"anxiety": [], "stress": [], "sadness": [], "help": []}
        self.positive_keywords: list  = []
        self.language:          str   = "en"
        self.negation_found:    bool  = False
        self.negated_wellbeing: bool  = False

    # ── Public entry point 

    def analyze(self, text: str, language: str = "en") -> dict:
        self.language = language

        text = _normalise((text or "").strip())

        if not text:
            return self._empty_result()

        self.keywords          = self._extract_keywords(text, language)
        self.negation_found, \
        self.negated_wellbeing = self._detect_negation(text, language)
        self.positive_keywords = self._extract_positive_keywords(text, language)
        self.sentiment, \
        self.sentiment_score   = self._score_sentiment()
        self.intent            = self._classify_intent()
        boosts                 = self._compute_boosts()

        result = {
            "intent":            self.intent,
            "sentiment":         self.sentiment,
            "sentiment_score":   round(self.sentiment_score, 3),
            "keywords":          self.keywords,
            "positive_keywords": self.positive_keywords,
            "language":          self.language,
            "negation_found":    self.negation_found,
            "negated_wellbeing": self.negated_wellbeing,
            "anxiety_boost":     boosts["anxiety"],
            "stress_boost":      boosts["stress"],
            "sadness_boost":     boosts["sadness"],
        }

        print(
            f"[NLU] intent={result['intent']}  sentiment={result['sentiment']}  "
            f"score={result['sentiment_score']}  negation={result['negation_found']}  "
            f"negated_wellbeing={result['negated_wellbeing']}  "
            f"pos_kw={result['positive_keywords']}  "
            f"anxiety_boost={result['anxiety_boost']}  "
            f"stress_boost={result['stress_boost']}  "
            f"sadness_boost={result['sadness_boost']}",
            flush=True,
        )
        return result

    # ── Public aliases 

    def detectIntent(self, text: str, language: str = "en") -> str:
        self.analyze(text, language)
        return self.intent

    def analyzeSentiment(self, text: str, language: str = "en") -> dict:
        self.analyze(text, language)
        return {"sentiment": self.sentiment, "score": self.sentiment_score}

    def extractKeywords(self, text: str, language: str = "en") -> dict:
        self.language = language
        return self._extract_keywords(_normalise(text), language)

    # ── Private: keyword extraction 

    def _extract_keywords(self, text: str, language: str) -> dict:
        text_lower = text.lower()

        if language == "ur":
            banks = {
                "anxiety": _ANXIETY_KEYWORDS_UR,
                "stress":  _STRESS_KEYWORDS_UR,
                "sadness": _SADNESS_KEYWORDS_UR,
                "help":    _HELP_KEYWORDS_UR,
            }
        else:
            banks = {
                "anxiety": _ANXIETY_KEYWORDS_EN,
                "stress":  _STRESS_KEYWORDS_EN,
                "sadness": _SADNESS_KEYWORDS_EN,
                "help":    _HELP_KEYWORDS_EN,
            }

        found = {cat: [kw for kw in bank if kw in text_lower]
                 for cat, bank in banks.items()}

        if any(found.values()):
            print(f"[NLU] Clinical keywords: {found}", flush=True)

        return found

    # ── Private: positive keyword extraction

    def _extract_positive_keywords(self, text: str, language: str) -> list:

        if language == "ur":
            pos_bank    = _POSITIVE_KEYWORDS_UR
            anchors     = _FP_ANCHORS_UR
            neg_pattern = _NEGATION_UR
        else:
            pos_bank    = _POSITIVE_KEYWORDS_EN
            anchors     = _FP_ANCHORS_EN
            neg_pattern = _NEGATION_EN

        tokens  = text.lower().split()
        matched = []

        for i, token in enumerate(tokens):
            clean = re.sub(r"[^\w']", "", token)
            if clean not in pos_bank:
                continue

            lo  = max(0, i - _ANCHOR_WINDOW)
            hi  = min(len(tokens), i + _ANCHOR_WINDOW + 1)
            win_tokens = tokens[lo:hi]
            win_str    = " ".join(win_tokens)

            # Must have a first-person anchor in window
            if not any(re.sub(r"[^\w']", "", t) in anchors for t in win_tokens):
                print(
                    f"[NLU] '{clean}' skipped — no first-person anchor "
                    f"in window '{win_str}'",
                    flush=True,
                )
                continue

            # Must NOT be negated
            if neg_pattern.search(win_str):
                print(
                    f"[NLU] '{clean}' skipped — negated in window '{win_str}'",
                    flush=True,
                )
                continue

            print(f"[NLU] Positive keyword accepted: '{clean}'", flush=True)
            matched.append(clean)

        return matched

    # ── Private: negation detection 

    def _detect_negation(self, text: str, language: str) -> tuple:

        pattern = _NEGATION_UR if language == "ur" else _NEGATION_EN
        tokens  = text.lower().split()

        clinical_all = (
            _ANXIETY_KEYWORDS_EN + _STRESS_KEYWORDS_EN + _SADNESS_KEYWORDS_EN +
            _ANXIETY_KEYWORDS_UR + _STRESS_KEYWORDS_UR + _SADNESS_KEYWORDS_UR
        )
        wellbeing = (
            _WELLBEING_KEYWORDS_UR if language == "ur" else _WELLBEING_KEYWORDS_EN
        )

        negation_found    = False
        negated_wellbeing = False

        for i, token in enumerate(tokens):
            if not pattern.search(token):
                continue

            window = " ".join(tokens[i: i + 5])

            if not negation_found:
                for kw in clinical_all:
                    if kw in window:
                        print(
                            f"[NLU] Negation near clinical keyword '{kw}' "
                            f"in window: '{window}'",
                            flush=True,
                        )
                        negation_found = True
                        break

            if not negated_wellbeing:
                for kw in wellbeing:
                    if kw in window:
                        print(
                            f"[NLU] Negated wellbeing word '{kw}' "
                            f"in window: '{window}'",
                            flush=True,
                        )
                        negated_wellbeing = True
                        break

            if negation_found and negated_wellbeing:
                break

        return negation_found, negated_wellbeing

    # ── Private: sentiment scoring 

    def _score_sentiment(self) -> tuple:

        negative_count = (
            len(self.keywords.get("anxiety", [])) +
            len(self.keywords.get("stress",  [])) +
            len(self.keywords.get("sadness", []))
        )
        if self.negated_wellbeing:
            negative_count += 1

        positive_count = len(self.positive_keywords)
        total          = negative_count + positive_count

        if total == 0:
            return "neutral", 0.0

        score = max(-1.0, min(1.0, (positive_count - negative_count) / total))

        if score > 0.1:
            label = "positive"
        elif score < -0.1:
            label = "negative"
        else:
            label = "neutral"

        return label, score

    # ── Private: intent classification
    def _classify_intent(self) -> str:
        
        has_clinical = (
            len(self.keywords.get("anxiety", [])) > 0 or
            len(self.keywords.get("stress",  [])) > 0 or
            len(self.keywords.get("sadness", [])) > 0
        )
        has_help = len(self.keywords.get("help", [])) > 0

        if has_help:
            return INTENT_HELP_SEEK
        if self.negation_found and has_clinical:
            return INTENT_DENIAL
        if has_clinical:
            return INTENT_DISTRESS
        if self.negated_wellbeing:
            return INTENT_DISTRESS
        if self.positive_keywords:
            return INTENT_POSITIVE
        return INTENT_NEUTRAL

    # ── Private: EmotionAnalyzer boost values

    def _compute_boosts(self) -> dict:
        
        def _boost(count: int) -> float:
            raw = min(count * 0.08, 0.30)
            return round(raw * 0.5, 3) if self.negation_found else round(raw, 3)

        boosts = {
            "anxiety": _boost(len(self.keywords.get("anxiety", []))),
            "stress":  _boost(len(self.keywords.get("stress",  []))),
            "sadness": _boost(len(self.keywords.get("sadness", []))),
        }

        if self.negated_wellbeing and not any([
            self.keywords.get("anxiety"),
            self.keywords.get("stress"),
            self.keywords.get("sadness"),
        ]):
            boosts["stress"]  = max(boosts["stress"],  0.08)
            boosts["sadness"] = max(boosts["sadness"], 0.08)

        return boosts

    # ── Private: empty result

    def _empty_result(self) -> dict:
        return {
            "intent":            INTENT_NEUTRAL,
            "sentiment":         "neutral",
            "sentiment_score":   0.0,
            "keywords":          {"anxiety": [], "stress": [], "sadness": [], "help": []},
            "positive_keywords": [],
            "language":          self.language,
            "negation_found":    False,
            "negated_wellbeing": False,
            "anxiety_boost":     0.0,
            "stress_boost":      0.0,
            "sadness_boost":     0.0,
        }


