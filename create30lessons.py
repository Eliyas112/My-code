from PIL import Image, ImageDraw, ImageFont
import os
import random

# Ensure the output directory exists
output_dir = 'C:\\Users\\Unique\\Downloads\\english_learning_images'
os.makedirs(output_dir, exist_ok=True)

# Sample data: Urdu, Hindi, and English text and answers
lessons =[
    {
        "id": 1,
        "urdu": "آپ کیسے ہیں؟",
        "english": "How are you?",
        "hindi": "आप कैसे हैं?",
        "urdu_answer": "میں ٹھیک ہوں، آپ کیسے ہیں؟",
        "english_answer": "I'm fine, how are you?",
        "hindi_answer": "मैं ठीक हूँ, आप कैसे हैं?"
    },
    {
        "id": 2,
        "urdu": "آپ کی پسندیدہ فلم کون سی ہے؟",
        "english": "What is your favorite movie?",
        "hindi": "आपकी पसंदीदा फिल्म कौन सी है?",
        "urdu_answer": "میری پسندیدہ فلم 'دل و دل' ہے۔",
        "english_answer": "My favorite movie is 'Dilwale'.",
        "hindi_answer": "मेरी पसंदीदा फिल्म 'दिलवाले' है।"
    },
    {
        "id": 3,
        "urdu": "کیا آپ کو کھانے میں کیا پسند ہے؟",
        "english": "What do you like to eat?",
        "hindi": "आपको खाने में क्या पसंद है?",
        "urdu_answer": "مجھے بریانی بہت پسند ہے۔",
        "english_answer": "I really like biryani.",
        "hindi_answer": "मुझे बिरयानी बहुत पसंद है।"
    },
    {
        "id": 4,
        "urdu": "آپ کا دل کس چیز کو ترجیح دیتا ہے؟",
        "english": "What does your heart prefer?",
        "hindi": "आपका दिल किस चीज़ को पसंद करता है?",
        "urdu_answer": "میرا دل دوستی کو ترجیح دیتا ہے۔",
        "english_answer": "My heart prefers friendship.",
        "hindi_answer": "मेरा दिल दोस्ती को पसंद करता है।"
    },
    {
        "id": 5,
        "urdu": "کیا آپ نے کوئی نیا گانا سنا ہے؟",
        "english": "Have you heard any new songs?",
        "hindi": "क्या आपने कोई नया गाना सुना है?",
        "urdu_answer": "ہاں، میں نے حال ہی میں ایک نیا گانا سنا۔",
        "english_answer": "Yes, I heard a new song recently.",
        "hindi_answer": "हां, मैंने हाल ही में एक नया गाना सुना।"
    },
    {
        "id": 6,
        "urdu": "کیا آپ کو چاہیے کہ کوئی کام کیا جائے؟",
        "english": "Do you need something to be done?",
        "hindi": "क्या आपको कुछ काम करवाना है?",
        "urdu_answer": "جی ہاں، مجھے اپنی گاڑی کی ریپئر کرانی ہے۔",
        "english_answer": "Yes, I need to get my car repaired.",
        "hindi_answer": "हां, मुझे अपनी कार की मरम्मत करवानी है।"
    },
    {
        "id": 7,
        "urdu": "آپ کا دن کیسا گزرا؟",
        "english": "How was your day?",
        "hindi": "आपका दिन कैसा था?",
        "urdu_answer": "میرا دن بہت اچھا گزرا، آپ کا کیسا گزرا؟",
        "english_answer": "My day was very good, how was yours?",
        "hindi_answer": "मेरा दिन बहुत अच्छा था, आपका कैसा था?"
    },
    {
        "id": 8,
        "urdu": "آپ کا پسندیدہ رنگ کون سا ہے؟",
        "english": "What is your favorite color?",
        "hindi": "आपका पसंदीदा रंग कौन सा है?",
        "urdu_answer": "میرا پسندیدہ رنگ نیلا ہے۔",
        "english_answer": "My favorite color is blue.",
        "hindi_answer": "मेरा पसंदीदा रंग नीला है।"
    },
    {
        "id": 9,
        "urdu": "آپ کی عمر کیا ہے؟",
        "english": "How old are you?",
        "hindi": "आपकी उम्र क्या है?",
        "urdu_answer": "میری عمر بیس برس ہے۔",
        "english_answer": "I am twenty years old.",
        "hindi_answer": "मेरी उम्र बीस साल है।"
    },
    {
        "id": 10,
        "urdu": "آپ کو بچپن میں کیا خواب ہے؟",
        "english": "Do you have any dreams of your childhood?",
        "hindi": "क्या आपके बचपन में कोई सपने हैं?",
        "urdu_answer": "جی ہاں، میرا خواب ہے کہ میں کھیل کا ٹائم کیا کریں گا۔",
        "english_answer": "Yes, I dreamed that I would play time.",
        "hindi_answer": "हां, मुझे सपना था कि मैं खेल का समय खेलूंगा।"
    },
    {
        "id": 11,
        "urdu": "آپ کے پاس کتنے بھائی ہیں؟",
        "english": "How many brothers do you have?",
        "hindi": "आपके पास कितने भाई हैं?",
        "urdu_answer": "میرے پاس دو بھائی ہیں۔",
        "english_answer": "I have two brothers.",
        "hindi_answer": "मेरे पास दो भाई हैं।"
    },
    {
        "id": 12,
        "urdu": "کیا آپ کو کوئی حسین خواب دیکھنا پسند ہے؟",
        "english": "Do you like to see a beautiful dream?",
        "hindi": "क्या आपको एक सुंदर सपना देखना पसंद है?",
        "urdu_answer": "جی ہاں، میں ہر وقت خوبصورت خواب دیکھتا ہوں۔",
        "english_answer": "Yes, I always see beautiful dreams.",
        "hindi_answer": "हां, मैं हमेशा खूबसूरत सपने देखता हूं।"
    },
    {
        "id": 13,
        "urdu": "کیا آپ نے نئے دوست کو دیکھا؟",
        "english": "Did you see a new friend?",
        "hindi": "क्या आपने एक नए दोस्त को देखा?",
        "urdu_answer": "ہاں، میں نے اپنے پڑوسی کو دیکھا۔",
        "english_answer": "Yes, I saw my neighbor.",
        "hindi_answer": "हां, मैंने अपने पड़ोसी को देखा।"
    },
    {
        "id": 14,
        "urdu": "آپ کی دعاؤں کی گئی ہیں؟",
        "english": "Have your prayers been answered?",
        "hindi": "क्या आपकी दुआएँ कबूल हो गईं हैं?",
        "urdu_answer": "جی ہاں، میری دعاؤں کی گئی ہیں۔",
        "english_answer": "Yes, my prayers have been answered.",
        "hindi_answer": "हां, मेरी दुआएँ कबूल हो गईं हैं।"
    },
    {
        "id": 15,
        "urdu": "آپ کو بھوک ہوتی ہے؟",
        "english": "Are you hungry?",
        "hindi": "क्या आप भूखे हैं?",
        "urdu_answer": "جی ہاں، مجھے بھوک لگی ہے۔",
        "english_answer": "Yes, I am hungry.",
        "hindi_answer": "हां, मुझे भूख लगी है।"
    },
    {
        "id": 16,
        "urdu": "آپ کے پاس کتنے بچے ہیں؟",
        "english": "How many children do you have?",
        "hindi": "आपके पास कितने बच्चे हैं?",
        "urdu_answer": "میرے پاس تین بچے ہیں۔",
        "english_answer": "I have three children.",
        "hindi_answer": "मेरे पास तीन बच्चे हैं।"
    },
    {
        "id": 17,
        "urdu": "آپ کے کتاب کے بارے میں کیا ہے؟",
        "english": "What about your book?",
        "hindi": "आपकी किताब के बारे में क्या है?",
        "urdu_answer": "میں ایک کتاب پڑھ رہا ہوں۔",
        "english_answer": "I am reading a book.",
        "hindi_answer": "मैं एक किताब पढ़ रहा हूँ।"
    },
    {
        "id": 18,
        "urdu": "کیا آپ کو میں اپنی دعائیں کر سکتا ہوں؟",
        "english": "Can I say my prayers?",
        "hindi": "मैं क्या अपनी प्रार्थनाएं कह सकता हूँ?",
        "urdu_answer": "جی ہاں، آپ دعائیں کر سکتے ہیں۔",
        "english_answer": "Yes, you can pray.",
        "hindi_answer": "हां, आप प्रार्थना कर सकते हैं।"
    },
    {
        "id": 19,
        "urdu": "کیا آپ کو گرمی لگتی ہے؟",
        "english": "Do you feel hot?",
        "hindi": "क्या आपको गर्मी लगती है?",
        "urdu_answer": "جی ہاں، مجھے گرمی لگ رہی ہے۔",
        "english_answer": "Yes, I feel hot.",
        "hindi_answer": "हां, मुझे गर्मी लग रही है।"
    },
    {
        "id": 20,
        "urdu": "آپ کے گھر کے بارے میں کیا ہے؟",
        "english": "What about your house?",
        "hindi": "आपके घर के बारे में क्या है?",
        "urdu_answer": "میرا گھر بڑا ہے اور اس میں بہت سارے کمرے ہیں۔",
        "english_answer": "My house is big and it has many rooms.",
        "hindi_answer": "मेरा घर बड़ा है और इसमें कई कमरे हैं।"
    },
    {
        "id": 21,
        "urdu": "آپ کے پاس کوئی پالتو جانور ہے؟",
        "english": "Do you have any pets?",
        "hindi": "क्या आपके पास कोई पालतू जानवर है?",
        "urdu_answer": "جی ہاں، میرے پاس ایک بلی ہے۔",
        "english_answer": "Yes, I have a cat.",
        "hindi_answer": "हां, मेरे पास एक बिल्ली है।"
    },
    {
        "id": 22,
        "urdu": "آپ کے کتنے بچے ہیں؟",
        "english": "How many children do you have?",
        "hindi": "आपके कितने बच्चे हैं?",
        "urdu_answer": "میرے پاس دو بچے ہیں۔",
        "english_answer": "I have two children.",
        "hindi_answer": "मेरे पास दो बच्चे हैं।"
    },
    {
        "id": 23,
        "urdu": "کیا آپ کو کھانے میں کیا پسند ہے؟",
        "english": "What do you like to eat?",
        "hindi": "आपको खाने में क्या पसंद है?",
        "urdu_answer": "مجھے بریانی بہت پسند ہے۔",
        "english_answer": "I really like biryani.",
        "hindi_answer": "मुझे बिरयानी बहुत पसंद है।"
    },
    {
        "id": 24,
        "urdu": "آپ کے پاس کیتنے دوست ہیں؟",
        "english": "How many friends do you have?",
        "hindi": "आपके पास कितने दोस्त हैं?",
        "urdu_answer": "میرے پاس پانچ دوست ہیں۔",
        "english_answer": "I have five friends.",
        "hindi_answer": "मेरे पास पांच दोस्त हैं।"
    },
    {
        "id": 25,
        "urdu": "آپ کے پاس کوئی ہوبی ہے؟",
        "english": "Do you have any hobbies?",
        "hindi": "क्या आपके पास कोई शौक है?",
        "urdu_answer": "جی ہاں، میرے پاس گٹکا ہوبی ہے۔",
        "english_answer": "Yes, I have a kite hobby.",
        "hindi_answer": "हां, मेरे पास एक गुब्बारा शौक है।"
    },
    {
        "id": 26,
        "urdu": "آپ کی نیکی کیوں کی؟",
        "english": "Why did you do good?",
        "hindi": "आपने अच्छा क्यों किया?",
        "urdu_answer": "میں نیکی اسلیے کرتا ہوں کیونکہ مجھے دوسروں کی مدد کرنے کا موقع ملتا ہے۔",
        "english_answer": "I do good because I get the opportunity to help others.",
        "hindi_answer": "मैं अच्छा इसलिए करता हूँ क्योंकि मुझे दूसरों की मदद करने का मौका मिलता है।"
    },
    {
        "id": 27,
        "urdu": "آپ کے خواب کیا ہے؟",
        "english": "What is your dream?",
        "hindi": "आपका सपना क्या है?",
        "urdu_answer": "میرا خواب ہے کہ میں اپنے والدین کی خوشی دیکھوں۔",
        "english_answer": "My dream is to see my parents happiness.",
        "hindi_answer": "मेरा सपना है कि मैं अपने माता-पिता की खुशी देखूं।"
    },
    {
        "id": 28,
        "urdu": "کیا آپ نے کبھی کوئی کام کیا ہے؟",
        "english": "Have you ever done anything?",
        "hindi": "क्या आपने कभी कुछ किया है?",
        "urdu_answer": "ہاں، میں نے بہت کچھ کیا ہے۔",
        "english_answer": "Yes, I have done a lot.",
        "hindi_answer": "हां, मैंने बहुत कुछ किया है।"
    },
    {
        "id": 29,
        "urdu": "آپ کی پسندیدہ شہر کون سا ہے؟",
        "english": "What is your favorite city?",
        "hindi": "आपका पसंदीदा शहर कौन सा है?",
        "urdu_answer": "میرا پسندیدہ شہر نیو یارک ہے۔",
        "english_answer": "My favorite city is New York.",
        "hindi_answer": "मेरा पसंदीदा शहर न्यूयॉर्क है।"
    },
    {
        "id": 30,
        "urdu": "آپ کا ڈراؤنا کیا ہے؟",
        "english": "What is your dream?",
        "hindi": "आपका सपना क्या है?",
        "urdu_answer": "میرا خواب ہے کہ میں اپنے والدین کی خوشی دیکھوں۔",
        "english_answer": "My dream is to see my parents happiness.",
        "hindi_answer": "मेरा सपना है कि मैं अपने माता-पिता की खुशी देखूं।"
    }
]

# Default font settings
font_size_urdu = 36
font_size_hindi = 42
font_size_english = 32

# Function to convert Western digits to Urdu digits in a string
def convert_digits_to_urdu(text):
    urdu_digits = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    urdu_text = ''.join(urdu_digits.get(char, char) for char in text)
    return urdu_text

# Function to create an image for each set of questions and answers
def create_image(day_num, urdu_text, english_text, hindi_text, urdu_answer_text, english_answer_text, hindi_answer_text):
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    img = Image.new('RGB', (800, 800), color=background_color)
    d = ImageDraw.Draw(img)
    
    try:
        font_urdu = ImageFont.truetype("C:\\Users\\Unique\\Downloads\\NotoNastaliqUrdu-Regular.ttf", font_size_urdu)
        font_hindi = ImageFont.truetype("C:\\Users\\Unique\\Downloads\\NotoSansDevanagari-Regular.ttf", font_size_hindi)
        font_english = ImageFont.truetype("C:\\Users\\Unique\\Downloads\\arial.ttf", font_size_english)
    except IOError:
        print("Error: Cannot load system fonts. Ensure the fonts are installed on your system.")
        return
    
    urdu_text = convert_digits_to_urdu(urdu_text)
    urdu_answer_text = convert_digits_to_urdu(urdu_answer_text)

    urdu_text_position = (50, 50)
    english_text_position = (50, 150)
    hindi_text_position = (50, 200)
    urdu_answer_text_position = (50, 350)
    english_answer_text_position = (50, 450)
    hindi_answer_text_position = (50, 500)

    d.text(urdu_text_position, urdu_text, font=font_urdu, fill='black')
    d.text(english_text_position, english_text, font=font_english, fill='black')
    d.text(hindi_text_position, hindi_text, font=font_hindi, fill='black')
    d.text(urdu_answer_text_position, urdu_answer_text, font=font_urdu, fill='black')
    d.text(english_answer_text_position, english_answer_text, font=font_english, fill='black')
    d.text(hindi_answer_text_position, hindi_answer_text, font=font_hindi, fill='black')

    img.save(os.path.join(output_dir, f"day_{day_num}.png"))

for i, lesson in enumerate(lessons):
    urdu_text = lesson["urdu"]
    english_text = lesson["english"]
    hindi_text = lesson["hindi"]
    urdu_answer_text = lesson["urdu_answer"]
    english_answer_text = lesson["english_answer"]
    hindi_answer_text = lesson["hindi_answer"]
    create_image(i + 1, urdu_text, english_text, hindi_text, urdu_answer_text, english_answer_text, hindi_answer_text)

print(f"{len(lessons)} images created successfully in '{output_dir}' directory.")
