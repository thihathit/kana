# Japanese Flashcards - Project Context

## Overview
Japanese flashcard web application with flip cards, shuffle, category filtering, and multiple layout views.

## Tech Stack
- Plain HTML file
- Tailwind CSS (CDN)
- Alpine.js (CDN)

## Features Implemented

### 1. Flashcards Display
- Cards show character on front, answer on back
- Click to flip individual cards
- 3D flip animation using CSS transforms
- Responsive card sizes optimized for mobile/desktop

### 2. Layout Options
- **Grid View**: Multiple cards displayed in a grid
- **Single View**: One large card in center with Prev/Next navigation
- Toggle button to switch between views
- Navigation wraps around (last → first, first → last)

### 3. Character Sets

#### Hiragana (103 characters)
| Category | Count | Characters |
|----------|-------|------------|
| Basic | 46 | あ-お, か-こ, さ-そ, た-と, な-の, は-ほ, ま-も, や-よ, ら-ろ, わをん |
| Dakuon | 20 | が-ご, ざ-ぞ, だ-ど, ば-ぼ |
| Handakuon | 5 | ぱ-ぽ |
| Youon | 33 | きゃ/きゅ/きょ, しゃ/しゅ/しょ, etc. |

#### Katakana (103 characters)
- Same categories as hiragana but with katakana characters

#### Kanji (~900+ characters)
- Organized by JLPT levels: N5, N4, N3, N2, N1
- Default: N5 and N4 enabled
- Card back shows reading + meaning

### 4. Buttons
- **Shuffle**: Randomizes the order of visible cards
- **Flip All/Unflip All**: Toggles all cards to show answers
- **Layout Toggle**: Switches between Grid and Single view
- **Sound/Romaji Toggle**: Switches between audio pronunciation mode and text display (Hiragana, Katakana, Combined, Kanji)

### 5. Audio Pronunciation
- Toggle button to switch between Sound mode and text mode
- **Sound mode (default)**: Clicking card plays native Japanese audio
- **Text mode**: Shows romaji (hiragana/katakana) or reading (kanji), clicking card flips back to character
- Small flip icon at bottom center of card back in sound mode to flip back
- **Voice Selection**: Cycling button to switch voices (Nanami → Google → Keita) - appears only in sound mode. Default: Nanami
- Uses local pre-downloaded audio files from `google-tts/`, `edge-tts-keita/`, or `edge-tts-nanami/` folders (no API calls)
- In Single View, navigating to Prev/Next automatically plays audio when sound mode is on
- Switching to sound mode in Single View also plays audio automatically
- **Listen button** in Single View: Listen button appears between Prev/Next controls (only in sound mode)

### 6. Category Filters
- Toggle buttons to include/exclude character categories
- Each shows count of characters in that category
- Active filters highlighted in black (#111111)

## File Structure
```
/home/debian/projects/kana/
├── index.html              # Landing page with links to flashcards
├── hiragana.html           # Hiragana flashcard application
├── katakana.html           # Katakana flashcard application
├── combined.html           # Combined Hiragana + Katakana
├── kanji.html              # Kanji flashcard application (JLPT N5-N1)
├── kotoba.html             # Vocabulary flashcard application (JLPT N5-N1)
├── lookalike.html          # Lookalike kanas - distinguish similar characters
├── common.css              # Shared styles (variables, dark mode, components)
├── jlpt_kotoba_data.json  # Vocabulary data (8385 words)
├── download_from_edgetts.py   # Script to refresh audio files using Edge TTS
├── download_from_google.py    # Script to refresh audio files using Google TTS
├── character_lists.py         # Shared character lists (imports from JSON)
├── google-tts/        # Google TTS audio files
│   ├── hiragana/       # 104 hiragana audio files
│   ├── katakana/       # 104 katakana audio files
│   ├── kanji/          # Kanji reading audio files
│   └── kotoba/         # Kotoba vocabulary audio files
├── edge-tts-keita/    # Edge TTS Keita voice audio files
├── edge-tts-nanami/   # Edge TTS Nanami voice audio files
└── CONTEXT.md         # This file
```

## Features by Application

### Combined (Hiragana + Katakana)
- **104 character pairs** (hiragana + katakana grouped together)
- Cards show both glyphs: hiragana (rose) and katakana (emerald) stacked vertically
- Grid view: both glyphs displayed vertically on card front
- Single view: both glyphs displayed side-by-side
- **Category filters**: Basic (46), Dakuon (20), Handakuon (5), Youon (33)
- **Buttons**: Shuffle, Flip All/Unflip All, Layout Toggle, Sound/Romaji Toggle
- Audio uses hiragana files (both scripts share the same pronunciation)

### Hiragana & Katakana (similar features)
- **103 characters** each with flip cards
- **Categories**: Basic (46), Dakuon (20), Handakuon (5), Youon (33)
- **Buttons**: Shuffle, Flip All/Unflip All, Layout Toggle, Sound/Romaji Toggle
- **Category filter toggles**

### Kanji Flashcards
- **~900+ kanji** with readings and meanings
- **Categories by JLPT level**: N5, N4, N3, N2, N1
- Default: N5 and N4 enabled
- Card back shows reading + meaning
- **Buttons**: Shuffle, Flip All/Unflip All, Layout Toggle, Sound/Reading Toggle

### Kotoba (Vocabulary)
- **8,385 vocabulary words** from JLPT N5 to N1 (loaded from `jlpt_kotoba_data.json`)
- Cards show Japanese word on front, reading + meaning on back
- Card back displays: kanji (word), reading (furigana), meaning (English)
- **Categories by JLPT level**: N5 (662), N4 (632), N3 (1797), N2 (1831), N1 (3463)
- Default: N5 and N4 enabled
- Cards are wider in grid view to fit words
- **Buttons**: Shuffle, Flip All/Unflip All, Layout Toggle, Voice Selector (always visible)
- Grid view: listen button on card back plays audio
- Single view: 🔊 Listen button always visible in navigation
- Click any card to flip; use Listen button to play audio
- Audio files stored in `kotoba/` folder using vocabulary readings
- Data is fetched dynamically from JSON, using `furigana` field (falls back to `word` if empty)

### Lookalike Kanas
- **28 lookalike pairs** of confusing character pairs
- Cards show 2 similar characters on front, answers + tips on back
- Cards include pairs with different sounds (hiragana-hiragana, katakana-katakana, hiragana-katakana cross)
- **Buttons**: Shuffle, Reveal/Hide All, Layout Toggle
- Tips on card back explain the differences between characters
- Marked as BETA

## Visual Design (Premium Utilitarian Minimalism)
- **Color Palette**: Warm monochrome
  - Background: #F7F6F3 (warm bone/off-white)
  - Surface: #FFFFFF (white)
  - Borders: #EAEAEA (ultra-light gray)
  - Text: #111111 (charcoal)
  - Secondary: #787774 (muted gray)
- Typography: DM Sans (body) + Instrument Serif (headings)
- 1px solid borders, no heavy shadows
- Solid black buttons (#111111), white text
- Pill-shaped tags with uppercase text
- SVG icons (no emojis)
- Subtle ambient background blobs (low opacity)
- Fade-in animations on page load
- No gradients, no glassmorphism
- Grid layout with sticky home button at bottom
- All pages vertically centered using CSS Grid

## How to Use
1. Open `index.html` to choose character type
2. Click cards to flip between character and answer
3. Use Shuffle to randomize order
4. Use Reveal All to reveal all answers
5. Toggle category buttons to filter characters (not available on Lookalikes)
6. Use Layout toggle to switch between grid/single view
7. In Single view, use Prev/Next buttons to navigate. Use the Listen button to play audio anytime.
8. Toggle Sound/Text(Romaji or Reading) to switch between audio mode and text mode (not available on Lookalikes or Kotoba)
9. Click the Voice button to cycle between Nanami, Google, or Keita voices
10. In Single view, use Left/Right arrow keys to navigate

## Future Enhancements (Potential)
- Add progress tracking
- Add "show only incorrect" mode
