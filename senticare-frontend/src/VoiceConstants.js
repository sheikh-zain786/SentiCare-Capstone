// voiceConstants.js

export const VOICE_UI = {
  en: {
    checkin_title:   "How are you feeling today?",
    checkin_sub:     "Speak freely for a few seconds. Tell us in your own words what's on your mind. We'll understand your emotional state from your voice.",
    skip:            "Skip — go straight to chat",
    start:           "Start speaking",
    stop:            "Done speaking",
    recording:       "Listening… speak freely",
    processing:      "Analysing your voice…",
    result_title:    "I heard you",
    result_said:     "You said:",
    result_emotion:  "Voice emotion detected:",
    continue_btn:    "Continue to assessment →",
    retry:           "Try again",
    unavailable:     "Voice analysis unavailable. Continuing with text assessment.",
    continue_anyway: "Continue anyway",
    emotions: {
      anxious:   "Anxious",
      stressed:  "Stressed",
      sad:       "Sad",
      depressed: "Depressed",
      tense:     "Tense",
      excited:   "Excited",
      neutral:   "Neutral",
      unknown:   "Voice noted",
    },
  },

  ur: {
    checkin_title:   "آج آپ کیسا محسوس کر رہے ہیں؟",
    checkin_sub:     "چند سیکنڈ کے لیے آزادانہ بولیں۔ اپنے الفاظ میں بتائیں کہ آپ کے ذہن میں کیا ہے۔ ہم آپ کی آواز سے آپ کی کیفیت سمجھیں گے۔",
    skip:            "چھوڑیں — سیدھا چیٹ پر جائیں",
    start:           "بولنا شروع کریں",
    stop:            "بولنا بند کریں",
    recording:       "سن رہے ہیں… آزادانہ بولیں",
    processing:      "آپ کی آواز تجزیہ ہو رہی ہے…",
    result_title:    "میں نے سنا",
    result_said:     "آپ نے کہا:",
    result_emotion:  "آواز سے محسوس ہوا:",
    continue_btn:    "جائزہ جاری رکھیں ←",
    retry:           "دوبارہ کوشش کریں",
    unavailable:     "آواز کا تجزیہ دستیاب نہیں۔ متنی جائزے پر جاری ہے۔",
    continue_anyway: "جاری رکھیں",
    emotions: {
      anxious:   "گھبراہٹ",
      stressed:  "دباؤ",
      sad:        "اداسی",
      depressed:   "ڈپریشن",
      tense:       "تناؤ",
      excited:     "جوش",
      neutral:     "پرسکون",
      unknown: "نامعلوم",
    },
  },
};

export const VOICE_INTRO_URL = "http://localhost:5000/voice-intro";

export function getEmotionDisplay(emotionKey, lang = "en") {           //default
  const ui = VOICE_UI[lang] ?? VOICE_UI["en"]; 
  return ui.emotions[emotionKey] ?? ui.emotions["unknown"];
}
