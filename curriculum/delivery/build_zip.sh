#!/bin/bash
# Assemble the single delivery zip. usage: build_zip.sh WEB_DIR OUT_ZIP
# WEB_DIR holds the standalone flip book (index.html + pages/, see ../flip/standalone.py).
set -e
here="$(cd "$(dirname "$0")" && pwd)"; out="$here/../../output"; web="$1"; zipf="$2"
tmp="$(mktemp -d)"; top="$tmp/Beyond-the-Manger"
mkdir -p "$top/1 Teacher Edition" "$top/2 Flip Book" "$top/3 Student Pages by Lesson"
cp "$here/START-HERE.pdf" "$top/START HERE.pdf"
cp "$out/Beyond-the-Manger-Flip-Book.pdf" "$top/1 Teacher Edition/Beyond-the-Manger-Teacher-Edition.pdf"
cp -r "$web/index.html" "$web/pages" "$top/2 Flip Book/"
names=("The Promised King" "The Announcement" "The Lamb in the Manger" "Forty Days Old" "Wise Men from the East" "Gifts for the King" "Out of Egypt, Home to Nazareth")
for i in 1 2 3 4 5 6 7; do cp "$out/Printable-Lesson-$i-Student-Pages.pdf" "$top/3 Student Pages by Lesson/Lesson $i - ${names[$((i-1))]}.pdf"; done
rm -f "$zipf"; (cd "$tmp" && zip -qr "$zipf" "Beyond-the-Manger"); rm -rf "$tmp"
