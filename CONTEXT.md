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
- **Sound mode (default)**: Shows 🔊 icon, clicking card plays native Japanese audio
- **Text mode**: Shows romaji (hiragana/katakana) or reading (kanji), clicking card flips back to character
- Small 🔄 flip icon at bottom center of card back in sound mode to flip back
- Uses local pre-downloaded audio files from `google-tts/` folder (no API calls)

### 6. Category Filters
- Toggle buttons to include/exclude character categories
- Each shows count of characters in that category
- Active filters highlighted in indigo

## File Structure
```
/Users/thihathit/Desktop/kana/
├── index.html          # Landing page with links to flashcards
├── hiragana.html       # Hiragana flashcard application
├── katakana.html       # Katakana flashcard application
├── combined.html       # Combined Hiragana + Katakana
├── kanji.html          # Kanji flashcard application (JLPT N5-N1)
├── download_audio.py   # Script to refresh audio files
├── google-tts/        # Local audio files (run `download_audio.py` to refresh)
│   ├── hiragana/       # 104 hiragana audio files
│   ├── katakana/       # 104 katakana audio files
│   └── kanji/          # 661 kanji reading audio files
└── CONTEXT.md         # This file
```

## Features by Application

### Combined (Hiragana + Katakana)
- **208 characters** (104 hiragana + 104 katakana)
- Cards color-coded: rose for hiragana, emerald for katakana
- **Type filters**: Hiragana, Katakana
- **Category filters**: Basic (92), Dakuon (40), Handakuon (10), Youon (66)
- **Buttons**: Shuffle, Flip All/Unflip All, Layout Toggle, Sound/Romaji Toggle

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

## Visual Design
- Mobile-first responsive design
- Reduced side padding for better mobile readability
- Larger card sizes with rounded padding
- Color-coded by type: Hiragana (rose), Katakana (emerald), Kanji (amber), Combined (violet)
- Gradient backgrounds
- All pages vertically centered

## How to Use
1. Open `index.html` to choose character type
2. Click cards to flip between character and answer
3. Use Shuffle to randomize order
4. Use Flip All to reveal all answers
5. Toggle category buttons to filter characters
6. Use Layout toggle to switch between grid/single view
7. In Single view, use Prev/Next buttons to navigate
8. Toggle Sound/Romaji to switch between audio mode and text mode
9. In Sound mode, click card back to play audio, click 🔄 to flip back

## Future Enhancements (Potential)
- Add progress tracking
- Add keyboard shortcuts
- Add "show only incorrect" mode
