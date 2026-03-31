#!/usr/bin/env python3
"""
Purge orphaned audio files that are not in the current data lists.
Run this to clean up old audio files after updating character lists or vocabulary data.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from character_lists import (
    hiragana_list,
    katakana_list,
    kanji_list,
    kotoba_list,
    true_kotoba_list,
)


def purge_old_files():
    print("=== Purging old audio files not in data ===\n")

    dirs = {
        "google-tts/hiragana": hiragana_list,
        "google-tts/katakana": katakana_list,
        "google-tts/kanji": list(set(kanji_list)),
        "google-tts/kotoba": list(set(kotoba_list)),
        "google-tts/true_kotoba": list(set(true_kotoba_list)),
        "edge-tts-nanami/hiragana": hiragana_list,
        "edge-tts-nanami/katakana": katakana_list,
        "edge-tts-nanami/kanji": list(set(kanji_list)),
        "edge-tts-nanami/kotoba": list(set(kotoba_list)),
        "edge-tts-nanami/true_kotoba": list(set(true_kotoba_list)),
        "edge-tts-keita/hiragana": hiragana_list,
        "edge-tts-keita/katakana": katakana_list,
        "edge-tts-keita/kanji": list(set(kanji_list)),
        "edge-tts-keita/kotoba": list(set(kotoba_list)),
        "edge-tts-keita/true_kotoba": list(set(true_kotoba_list)),
    }

    total_deleted = 0
    for dir_path, expected_list in dirs.items():
        if not os.path.exists(dir_path):
            continue
        expected_set = set(f"{item}.mp3" for item in expected_list)
        for filename in os.listdir(dir_path):
            if ":" in filename:
                continue
            if not filename.endswith(".mp3"):
                continue
            if filename not in expected_set:
                filepath = os.path.join(dir_path, filename)
                os.remove(filepath)
                print(f"Deleted: {filepath}")
                total_deleted += 1

    print(f"\nTotal files deleted: {total_deleted}")
    print("=== Purge complete ===")


if __name__ == "__main__":
    purge_old_files()
