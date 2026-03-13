# Hiragana Flashcards - Project Context

## Overview
Japanese hiragana flashcard web application with flip cards, shuffle, and category filtering.

## Tech Stack
- Plain HTML file
- Tailwind CSS (CDN)
- Alpine.js (CDN)

## Features Implemented

### 1. Flashcards Display
- Cards show hiragana on front, romaji on back
- Click to flip individual cards
- 3D flip animation using CSS transforms
- Responsive card sizes (w-24 h-32 / sm:w-28 sm:h-36)

### 2. All Hiragana Characters (103 total)
| Category | Count | Characters |
|----------|-------|------------|
| Basic | 46 | あ-お, か-こ, さ-そ, た-と, な-の, は-ほ, ま-も, や-よ, ら-ろ, わをん |
| Dakuon | 20 | が-ご, ざ-ぞ, だ-ど, ば-ぼ |
| Handakuon | 5 | ぱ-ぽ |
| Youon | 33 | きゃ/きゅ/きょ, しゃ/しゅ/しょ, etc. |

### 3. Shuffle Button
- Randomizes the order of visible cards
- Persists the new order in underlying data

### 4. Flip All / Unflip All Button
- Toggles all visible cards to show romaji
- Button text changes based on current state

### 5. Category Filter Buttons
- 4 toggle buttons: Basic, Dakuon, Handakuon, Youon
- Each shows count of characters in that category
- Active filters highlighted in indigo
- Filters combine (show cards matching ANY active filter)

## File Structure
```
/Users/thihathit/Desktop/kana/
├── index.html       # Landing page with links to flashcards
├── hiragana.html    # Hiragana flashcard application
├── katakana.html    # Katakana flashcard application
└── CONTEXT.md       # This file
```

## How to Use
1. Open `hiragana.html` in a browser
2. Click cards to flip between hiragana and romaji
3. Use Shuffle to randomize order
4. Use Flip All to reveal all answers
5. Toggle category buttons to include/exclude character types

## Future Enhancements (Potential)
- Add katakana flashcards
- Add progress tracking
- Add keyboard shortcuts
- Add "show only incorrect" mode
- Add audio pronunciation
