{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "fcaef671",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyaudio in d:\\anocordia\\lib\\site-packages (0.2.13)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pyaudio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "500022d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recording...\n",
      "Recording finished.\n",
      "Audio saved as 'C:\\Users\\HP\\Desktop\\Azure\\Voiceoutput\\MRaza_Intro.wav'\n"
     ]
    }
   ],
   "source": [
    "import pyaudio\n",
    "import wave\n",
    "\n",
    "# Define the path to save the WAV file\n",
    "output_path = r'C:\\Users\\HP\\Desktop\\Azure\\Voiceoutput\\MRaza_Intro.wav'\n",
    "\n",
    "# Set the audio parameters\n",
    "FORMAT = pyaudio.paInt16\n",
    "CHANNELS = 1\n",
    "RATE = 44100  # Samples per second\n",
    "CHUNK = 1024  # Number of audio frames per buffer\n",
    "RECORD_SECONDS = 40  # Duration of recording (in seconds)\n",
    "\n",
    "# Initialize the audio stream\n",
    "audio = pyaudio.PyAudio()\n",
    "\n",
    "try:\n",
    "    # Create a new audio stream\n",
    "    stream = audio.open(format=FORMAT, channels=CHANNELS,\n",
    "                        rate=RATE, input=True,\n",
    "                        frames_per_buffer=CHUNK)\n",
    "\n",
    "    print(\"Recording...\")\n",
    "\n",
    "    frames = []\n",
    "\n",
    "    # Record audio for the specified duration\n",
    "    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):\n",
    "        data = stream.read(CHUNK)\n",
    "        frames.append(data)\n",
    "\n",
    "    print(\"Recording finished.\")\n",
    "\n",
    "    # Stop and close the audio stream\n",
    "    stream.stop_stream()\n",
    "    stream.close()\n",
    "\n",
    "    # Terminate the PyAudio object\n",
    "    audio.terminate()\n",
    "\n",
    "    # Save the recorded audio to a WAV file\n",
    "    with wave.open(output_path, 'wb') as wf:\n",
    "        wf.setnchannels(CHANNELS)\n",
    "        wf.setsampwidth(audio.get_sample_size(FORMAT))\n",
    "        wf.setframerate(RATE)\n",
    "        wf.writeframes(b''.join(frames))\n",
    "\n",
    "    print(f\"Audio saved as '{output_path}'\")\n",
    "\n",
    "except KeyboardInterrupt:\n",
    "    # Handle Ctrl+C gracefully\n",
    "    print(\"Recording interrupted.\")\n",
    "\n",
    "except Exception as e:\n",
    "    print(f\"An error occurred: {str(e)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "a9fc4e7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: azure-cognitiveservices-speech==1.28.0 in d:\\anocordia\\lib\\site-packages (1.28.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install azure-cognitiveservices-speech==1.28.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "f402fa9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from datetime import datetime\n",
    "\n",
    "# Import namespaces\n",
    "import azure.cognitiveservices.speech as speech_sdk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "5d548719",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ready to use speech service in: eastus\n"
     ]
    }
   ],
   "source": [
    "# Configure speech service\n",
    "cog_key = \"c1dd951f6f7f491cb311193de321f5d5\"\n",
    "cog_region = \"eastus\"\n",
    "\n",
    "speach_config = speech_sdk.SpeechConfig(cog_key, cog_region)\n",
    "print('Ready to use speech service in:', speach_config.region)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "518e2bab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Configure speech recognition\n",
    "audio_config = speech_sdk.AudioConfig(filename=r'C:\\Users\\HP\\Desktop\\Azure\\Voiceoutput\\MRaza_Intro.wav')\n",
    "speech_recognizer = speech_sdk.SpeechRecognizer(speach_config, audio_config)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "e63a3034",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello I am Raza. I am currently studying at GB NASB boot camp training institute. I am interested in Deep learning and Artificial intelligence project. Currently I am working on the speech recognition and translation by using Azure speech and translator services in which speak speech clip in English language will be converted into Urdu language. This task is given by facility and will be.'"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Process speech input\n",
    "speech = speech_recognizer.recognize_once_async().get()\n",
    "speech.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "030a0b0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{<PropertyId.SpeechServiceResponse_JsonResult: 5000>: '{\"Id\":\"4fc8bd50f19547a88d9360a830db4cb2\",\"RecognitionStatus\":\"Success\",\"DisplayText\":\"I am Reza. I am currently studying at GB Nask Boot Camp Training Institute in GB.\",\"Offset\":6800000,\"Duration\":76600000,\"Channel\":0}',\n",
       " <PropertyId.SpeechServiceResponse_RecognitionLatencyMs: 5002>: '2250'}"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "speech.properties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "e4395ec5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ready to translate from en-US\n"
     ]
    }
   ],
   "source": [
    "cog_key = \"c1dd951f6f7f491cb311193de321f5d5\"\n",
    "cog_region = \"eastus\"\n",
    "\n",
    "# Configure translation\n",
    "translation_config = speech_sdk.translation.SpeechTranslationConfig(cog_key, cog_region)\n",
    "translation_config.speech_recognition_language = 'en-US'\n",
    "translation_config.add_target_language('fr')\n",
    "translation_config.add_target_language('es')\n",
    "translation_config.add_target_language('hi')\n",
    "translation_config.add_target_language('ur')\n",
    "print('Ready to translate from',translation_config.speech_recognition_language)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "486ab26b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Getting speech from file...\n",
      "Translating \"Hello I am Raza. I am currently studying at GB NASB boot camp training institute. I am interested in Deep learning and Artificial intelligence project. Currently I am working on speech recognition and translation by using Azure speech and translator services in which speak speech clip in English language will be converted into Urdu language. This task is given by facility and will be.\"\n"
     ]
    }
   ],
   "source": [
    "# Translate speech\n",
    "audio_config = speech_sdk.AudioConfig(filename=r'C:\\Users\\HP\\Desktop\\Azure\\Voiceoutput\\MRaza_Intro.wav')\n",
    "translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config = audio_config)\n",
    "print(\"Getting speech from file...\")\n",
    "result = translator.recognize_once_async().get()\n",
    "print('Translating \"{}\"'.format(result.text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "0231ef6e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'fr': 'Bonjour, je suis Raza. J’étudie actuellement à l’institut de formation du camp d’entraînement GB NASB. Je suis intéressé par le projet d’apprentissage profond et d’intelligence artificielle. Actuellement, je travaille sur la reconnaissance vocale et la traduction à l’aide des services de reconnaissance vocale et de traduction Azure dans lesquels le clip vocal en langue anglaise sera converti en langue ourdou. Cette tâche est donnée par facilité et sera.',\n",
       " 'es': 'Hola soy Raza. Actualmente estoy estudiando en el instituto de entrenamiento de campo de entrenamiento GB NASB. Estoy interesado en el proyecto de Deep learning e Inteligencia Artificial. Actualmente estoy trabajando en el reconocimiento y la traducción de voz mediante el uso de los servicios de voz y traductor de Azure en los que el clip de voz en inglés se convertirá al idioma urdu. Esta tarea viene dada por facilidad y será.',\n",
       " 'hi': 'हैलो मैं रजा हूँ. मैं वर्तमान में जीबी एनएएसबी बूट कैंप प्रशिक्षण संस्थान में अध्ययन कर रहा हूं। मुझे डीप लर्निंग और आर्टिफिशियल इंटेलिजेंस प्रोजेक्ट में दिलचस्पी है। वर्तमान में मैं Azure भाषण और अनुवादक सेवाओं का उपयोग करके भाषण पहचान और अनुवाद पर काम कर रहा हूं जिसमें अंग्रेजी भाषा में स्पीच क्लिप को उर्दू भाषा में परिवर्तित किया जाएगा। यह कार्य सुविधा द्वारा दिया गया है और होगा।',\n",
       " 'ur': 'ہیلو میں رضا ہوں۔ میں فی الحال جی بی این اے ایس بی بوٹ کیمپ ٹریننگ انسٹی ٹیوٹ میں تعلیم حاصل کر رہا ہوں۔ میں ڈیپ لرننگ اور مصنوعی ذہانت کے منصوبے میں دلچسپی رکھتا ہوں۔ فی الحال میں ایزور اسپیچ اینڈ ٹرانسلیٹر سروسز کا استعمال کرتے ہوئے تقریر کی شناخت اور ترجمہ پر کام کر رہا ہوں جس میں انگریزی زبان میں تقریر کلپ کو اردو زبان میں تبدیل کیا جائے گا۔ یہ ٹاسک سہولت کے ذریعہ دیا گیا ہے اور ہوگا۔'}"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result.translations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "6130a7a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ہیلو میں رضا ہوں۔ میں فی الحال آخری بوسٹ کیمپ ٹریننگ انسٹی ٹیوٹ میں تعلیم حاصل کر رہا ہوں۔ میں مصنوعی ذہانت اور گہری سیکھنے کے منصوبوں میں دلچسپی رکھنے میں دلچسپی رکھتا ہوں. فی الحال میں ایزور اسپیچ اور مترجم کی خدمات کا استعمال کرتے ہوئے تقریر کی شناخت اور ترجمہ پر کام کر رہا ہوں جس میں ہم ایک کلپ کو انگریزی میں تبدیل کریں گے۔'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Data\n",
    "response_text = 'ہیلو میں رضا ہوں۔ میں فی الحال آخری بوسٹ کیمپ ٹریننگ انسٹی ٹیوٹ میں تعلیم حاصل کر رہا ہوں۔ میں مصنوعی ذہانت اور گہری سیکھنے کے منصوبوں میں دلچسپی رکھنے میں دلچسپی رکھتا ہوں. فی الحال میں ایزور اسپیچ اور مترجم کی خدمات کا استعمال کرتے ہوئے تقریر کی شناخت اور ترجمہ پر کام کر رہا ہوں جس میں ہم ایک کلپ کو انگریزی میں تبدیل کریں گے۔'\n",
    "response_text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "ccdb44d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Configure speech synthesis\n",
    "speech_synthesizer = speech_sdk.SpeechSynthesizer(speach_config)\n",
    "\n",
    "# Synthesize spoken output\n",
    "speak = speech_synthesizer.speak_text_async(response_text).get()\n",
    "\n",
    "# Saving Output\n",
    "with open(r\"C:\\Users\\HP\\Desktop\\Azure\\Voiceoutput\\Translation.wav\",\"wb\") as audio_file:\n",
    "    audio_file.write(speak.audio_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "14c3d805",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "हैलो मैं रजा हूँ. मैं वर्तमान में पिछले बूस्ट कैंप प्रशिक्षण संस्थान में अध्ययन कर रहा हूं। मैं आर्टिफिशियल इंटेलिजेंस और गहरी सीखने की परियोजनाओं में रुचि रखने में दिलचस्प हूं। वर्तमान में मैं Azure स्पीच और अनुवादक सेवाओं का उपयोग करके भाषण पहचान और अनुवाद पर काम कर रहा हूं जिसमें हम एक क्लिप को अंग्रेजी में परिवर्तित करेंगे।\n"
     ]
    }
   ],
   "source": [
    "translation = result.translations['hi']\n",
    "print(translation)\n",
    "\n",
    "\n",
    "# Synthesize translation\n",
    "voices = {\n",
    "        \"fr\": \"fr-FR-HenriNeural\",\n",
    "        \"es\": \"es-ES-ElviraNeural\",\n",
    "        \"hi\": \"hi-IN-MadhurNeural\",\n",
    "        \"ur\":  \"ur-PK-AsadNeural\"\n",
    "}\n",
    "\n",
    "# Configure speech\n",
    "speach_config = speech_sdk.SpeechConfig(cog_key, cog_region)\n",
    "speach_config.speech_synthesis_voice_name = \"ur-PK-AsadNeural\"\n",
    "\n",
    "speech_synthesizer = speech_sdk.SpeechSynthesizer(speach_config)\n",
    "speak = speech_synthesizer.speak_text_async('ہیلو میں رضا ہوں۔ میں فی الحال آخری بوسٹ کیمپ ٹریننگ انسٹی ٹیوٹ میں تعلیم حاصل کر رہا ہوں۔ میں مصنوعی ذہانت اور گہری سیکھنے کے منصوبوں میں دلچسپی رکھنے میں دلچسپی رکھتا ہوں. فی الحال میں ایزور اسپیچ اور مترجم کی خدمات کا استعمال کرتے ہوئے تقریر کی شناخت اور ترجمہ پر کام کر رہا ہوں جس میں ہم ایک کلپ کو انگریزی میں تبدیل کریں گے۔').get()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "a759d80f",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(r\"C:\\Users\\HP\\Desktop\\Azure\\Voiceoutput\\Translation.wav\", \"wb\") as audio_file:\n",
    "    audio_file.write(speak.audio_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8997a959",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
