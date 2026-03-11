#!/usr/bin/env bash
# Check image URLs and download to assets/

ASSETS="/Users/sqazi/Desktop/Moodboard-gulrez/assets"
BASE="https://googleusercontent.com/image_collection/image_retrieval"
BASE_LH3="https://lh3.googleusercontent.com/image_collection/image_retrieval"

IDS=(
  1660434070519425278
  10749187554219394810
  16830104177656545138
  7054665880080602508
  17443243058972104744
  11575605945054986872
  4690442685846599394
  3502435851240108956
  11074218762704002438
  13209422346381664063
  15083829527990905793
  6496355583278441282
  16827753687575721240
  4395695859930384527
  12576380756935526788
  7253864474158714971
  11215838818492134524
  14397535987421783017
  1557970410616345560
  12542283665653774910
  4876393190812208449
  13666006397116776536
  3434757036040257686
  6077732292454324074
  17789610899839261522
  4511725011977293386
  16980669779398786941
  1694914808791743645
  9901053667724136200
  7480153467304931638
)

OK=0
FAIL=0

for i in "${!IDS[@]}"; do
  id="${IDS[$i]}"
  out="$ASSETS/image_${i}_${id}"
  # Try main domain first
  code=$(curl -s -o "${out}.tmp" -w "%{http_code}" -L --max-time 10 "${BASE}/${id}" 2>/dev/null)
  if [[ "$code" == "200" ]]; then
    # Check if we got actual image data (not HTML error page)
    if file "${out}.tmp" | grep -qE 'image|JPEG|PNG|GIF|WebP'; then
      ext=".jpg"
      content=$(file -b "${out}.tmp")
      [[ "$content" == *PNG* ]] && ext=".png"
      [[ "$content" == *GIF* ]] && ext=".gif"
      [[ "$content" == *WebP* ]] && ext=".webp"
      mv "${out}.tmp" "${out}${ext}"
      echo "OK  $id -> ${out}${ext}"
      ((OK++))
    else
      rm -f "${out}.tmp"
      echo "FAIL $id (HTTP 200 but not image)"
      ((FAIL++))
    fi
  else
    rm -f "${out}.tmp"
    # Try lh3 subdomain
    code2=$(curl -s -o "${out}.tmp" -w "%{http_code}" -L --max-time 10 "${BASE_LH3}/${id}" 2>/dev/null)
    if [[ "$code2" == "200" ]] && file "${out}.tmp" | grep -qE 'image|JPEG|PNG|GIF|WebP'; then
      ext=".jpg"
      content=$(file -b "${out}.tmp")
      [[ "$content" == *PNG* ]] && ext=".png"
      [[ "$content" == *GIF* ]] && ext=".gif"
      [[ "$content" == *WebP* ]] && ext=".webp"
      mv "${out}.tmp" "${out}${ext}"
      echo "OK  $id (lh3) -> ${out}${ext}"
      ((OK++))
    else
      rm -f "${out}.tmp"
      echo "FAIL $id (HTTP $code / $code2)"
      ((FAIL++))
    fi
  fi
done

echo ""
echo "Summary: $OK downloaded, $FAIL failed"
