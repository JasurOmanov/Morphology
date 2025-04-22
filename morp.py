import streamlit as st

# 1. Leksik baza (hozircha bo'sh, lemmalar bazasi bo'lmasligi mumkin)
lemmalar = {}  # Bu bo'sh, lekin siz kelajakda to'ldirishingiz mumkin

# 2. Qo‘shimchalar bazasi
suffixes = [
    {"suffix": "lar", "feats": {"Number": "Plural"}, "pos": ["NOUN"]},
    {"suffix": "ning", "feats": {"Case": "Genitive"}, "pos": ["NOUN"]},
    {"suffix": "ni", "feats": {"Case": "Accusative"}, "pos": ["NOUN"]},
    {"suffix": "da", "feats": {"Case": "Locative"}, "pos": ["NOUN"]},
    {"suffix": "di", "feats": {"Tense": "Past"}, "pos": ["VERB"]},
    {"suffix": "miz", "feats": {"Person": "1", "Number": "Plural"}, "pos": ["VERB", "NOUN"]},
]


# 3. Tahlil funksiyasi
def analyze(word):
    # 3.1 Agar lemmalar bazasidan topilsa
    if word in lemmalar:
        return {
            "word": word,
            "lemma": word,
            "pos": lemmalar[word],
            "feats": None
        }

    # 3.2 Agar lemmalar bazasidan topilmasa, qo‘shimchalarni ajratib, qolgan qismini lemma deb olish
    for suffix in suffixes:
        if word.endswith(suffix["suffix"]):
            # Qo‘shimchalarni ajratib olish
            base = word[:-len(suffix["suffix"])]
            pos = suffix["pos"][0]  # Default POS ning birinchi turini olish
            feats = suffix["feats"]
            return {
                "word": word,
                "lemma": base,
                "pos": pos,
                "feats": feats
            }

    return {"word": word, "error": "No analysis found"}


# 4. Streamlit interfeysi
st.title("O'zbek Tili Morfologik Tahlilator")
st.write("Bu dastur yordamida O'zbek tilidagi so'zlarni morfologik tahlil qilishingiz mumkin.")

# Foydalanuvchi so'zi kiritish
word_input = st.text_input("So'zni kiriting:")

# Tahlil qilish va natijalarni chiqarish
if word_input:
    result = analyze(word_input)
    if "error" in result:
        st.error(result["error"])
    else:
        st.success(f"So'z: {result['word']}")
        st.write(f"Lemma (asos): {result['lemma']}")
        st.write(f"So'z turi: {result['pos']}")
        if result['feats']:
            st.write(f"Grammatik xususiyatlar: {result['feats']}")
        else:
            st.write("Grammatik xususiyatlar topilmadi.")
