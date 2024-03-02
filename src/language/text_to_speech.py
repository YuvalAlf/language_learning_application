import os
import random
from dataclasses import dataclass
from functools import lru_cache

import pygame
from gtts import gTTS

from utils.os_utils import GlobalTemporaryDirectory


@dataclass
class TextToSpeech:
    @staticmethod
    @lru_cache(maxsize=128)
    def phrase_to_french_audio_file(phrase: str) -> str:
        tts = gTTS(text=phrase, lang='fr')
        phrase_prefix = phrase.replace(' ', '_')[:20]
        random_int = random.randint(0, 1000000)
        global_temp_dir = GlobalTemporaryDirectory.get_temporary_directory()
        audio_file_path = os.path.join(global_temp_dir, f'{phrase_prefix}_{random_int}.mp3')
        tts.save(audio_file_path)
        return audio_file_path

    @staticmethod
    def speak(phrase: str) -> None:
        mp3_path = TextToSpeech.phrase_to_french_audio_file(phrase)
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_path)
        pygame.mixer.music.play()
