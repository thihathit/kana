#!/usr/bin/env python3
"""
Generate Japanese audio files using Edge TTS for hiragana, katakana, and kanji lists.
Save them in voice-specific directories (edge-tts-<voice>/) with subdirectories hiragana, katakana, kanji.
Same data as download_audio.py but using Edge TTS instead of Google Translate.
"""

import asyncio
import os
import sys

# Import the lists from character_lists.py (assumed to be in the same directory)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from character_lists import hiragana_list, katakana_list, kanji_list

import edge_tts

# Define the voices we want to use: (full voice name, short name for directory)
VOICES = [
    ("ja-JP-NanamiNeural", "nanami"),
    ("ja-JP-KeitaNeural", "keita"),
    ("ja-JP-MasaruNeural", "masaru"),
]


async def generate_audio(text, filepath, voice):
    """
    Convert Japanese text to speech using Edge TTS

    Args:
        text (str): Japanese text to synthesize
        filepath (str): Output audio file path (mp3)
        voice (str): Voice identifier (e.g., ja-JP-NanamiNeural)

    Returns:
        bool: True if successful, False otherwise, None if skipped
    """
    if os.path.exists(filepath):
        return None

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filepath)

    file_size = os.path.getsize(filepath)
    if file_size < 1000:
        os.remove(filepath)
        print(f"Empty/short audio for '{text}' ({file_size} bytes), skipping")
        return False

    return True


async def main():
    """Main function to generate all audio files for each voice"""
    print("Starting Edge TTS audio generation for all voices...")

    for voice_full, voice_short in VOICES:
        voice_output_dir = os.path.join(".", f"edge-tts-{voice_short}")
        print(
            f"\n=== Generating for voice: {voice_full} (directory: edge-tts-{voice_short}) ==="
        )

        # --- Hiragana ---
        print("\n--- Generating Hiragana ---")
        h_count = 0
        h_skipped = 0
        for i, h in enumerate(hiragana_list, 1):
            filepath = os.path.join(voice_output_dir, "hiragana", f"{h}.mp3")
            if i % 20 == 0 or i <= 5:
                print(f"[{i}/{len(hiragana_list)}] Generating: {h}")
            try:
                result = await generate_audio(h, filepath, voice_full)
                if result is None:
                    h_skipped += 1
                elif result:
                    h_count += 1
                    if i % 20 == 0 or i <= 5:
                        print(f"  -> Saved: {filepath}")
                else:
                    if i % 20 == 0 or i <= 5:
                        print(f"  -> Failed: {h}")
            except Exception as e:
                if os.path.exists(filepath):
                    os.remove(filepath)
                print(f"Error for '{h}': {e}")
        print(
            f"Done hiragana: {h_count} generated, {h_skipped} skipped (total {len(hiragana_list)})"
        )

        # --- Katakana ---
        print("\n--- Generating Katakana ---")
        k_count = 0
        k_skipped = 0
        for i, k in enumerate(katakana_list, 1):
            filepath = os.path.join(voice_output_dir, "katakana", f"{k}.mp3")
            if i % 20 == 0 or i <= 5:
                print(f"[{i}/{len(katakana_list)}] Generating: {k}")
            try:
                result = await generate_audio(k, filepath, voice_full)
                if result is None:
                    k_skipped += 1
                elif result:
                    k_count += 1
                    if i % 20 == 0 or i <= 5:
                        print(f"  -> Saved: {filepath}")
                else:
                    if i % 20 == 0 or i <= 5:
                        print(f"  -> Failed: {k}")
            except Exception as e:
                if os.path.exists(filepath):
                    os.remove(filepath)
                print(f"Error for '{k}': {e}")
        print(
            f"Done katakana: {k_count} generated, {k_skipped} skipped (total {len(katakana_list)})"
        )

        # --- Kanji ---
        unique_kanji = list(set(kanji_list))
        print(f"\n--- Generating Kanji (unique count: {len(unique_kanji)}) ---")
        c_count = 0
        c_skipped = 0
        for i, kj in enumerate(unique_kanji, 1):
            filepath = os.path.join(voice_output_dir, "kanji", f"{kj}.mp3")
            if i % 50 == 0 or i <= 5:
                print(f"[{i}/{len(unique_kanji)}] Generating: {kj}")
            try:
                result = await generate_audio(kj, filepath, voice_full)
                if result is None:
                    c_skipped += 1
                elif result:
                    c_count += 1
                    if i % 50 == 0 or i <= 5:
                        print(f"  -> Saved: {filepath}")
                else:
                    if i % 50 == 0 or i <= 5:
                        print(f"  -> Failed: {kj}")
            except Exception as e:
                if os.path.exists(filepath):
                    os.remove(filepath)
                print(f"Error for '{kj}': {e}")
        print(
            f"Done kanji: {c_count} generated, {c_skipped} skipped (total {len(unique_kanji)})"
        )

        print(f"\n=== Completed for voice: {voice_full} ===")
        print(f"Hiragana: {h_count} generated, {h_skipped} skipped")
        print(f"Katakana: {k_count} generated, {k_skipped} skipped")
        print(f"Kanji: {c_count} generated, {c_skipped} skipped")
        print(
            f"Total for {voice_short}: {h_count + k_count + c_count} generated, {h_skipped + k_skipped + c_skipped} skipped"
        )

    print("\n=== Generation Complete for All Voices ===")


if __name__ == "__main__":
    asyncio.run(main())
