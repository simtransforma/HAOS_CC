---
name: youtube-content-generator
description: >
  Complete YouTube content generation with advanced SEO and thumbnails.
  Creates titles, descriptions, tags, scripts, and launch strategy for any
  niche (tech, programming, business, lifestyle, education, etc.). Includes
  competitor analysis and mobile-first optimization (70% of viewers on mobile).
---

# YouTube Content Generator

Skill for complete YouTube content generation, including advanced SEO and automatic thumbnail generation via API.

## Triggers

This skill should be activated when the user mentions:
- "Create YouTube content"
- "Generate title/description/tags for video"
- "Optimize video for YouTube"
- "YouTube SEO"
- "Create thumbnail"
- "Prepare video launch"
- "Complete content for video"
- "/youtube"

## Channel Context

Before starting, ask the user for channel context:
- **Channel name**
- **Niche** (tech, business, lifestyle, education, etc.)
- **Audience** (beginners, intermediate, advanced)
- **Primary access platform** (typically ~70% mobile)
- **Brand hashtags** (for consistent branding)

---

## MANDATORY WORKFLOW

### PHASE 1: Information Gathering

Before generating any content, ask the user:

1. **Video topic:** What is the main subject?
2. **Content type:** Tutorial, Review, News, Comparison, Tips?
3. **Main tool/technology:** (if applicable)
4. **Specific target audience:** Beginners, intermediate, advanced?
5. **Estimated duration:** Short (<10min), Medium (10-20min), Long (>20min)?
6. **Differentiator:** What makes this video unique?

---

### PHASE 2: Market Research (MANDATORY)

**Before generating titles, ALWAYS execute:**

1. **Competitor title research:**
   ```
   Use WebSearch to search:
   - "[topic] tutorial YouTube"
   - "[tool] how to use YouTube"
   - "[topic] 2024 YouTube"
   ```

2. **Trend analysis:**
   - Check Google Trends for the topic
   - Verify trending videos in the niche
   - Analyze patterns of high-performing titles

3. **Document findings:**
   - Most popular titles found
   - Recurring keywords
   - Formatting patterns

---

### PHASE 3: Title Generation (Maximum 10)

**Technical requirements:**
- Between 50-70 characters (ideal for mobile)
- Include 1-2 relevant emojis (start or end)
- Include 1 main hashtag when appropriate
- Use high-search-volume keywords

**Load formulas from:** `references/title-formulas.md`

**Mandatory style mix:**
1. 2-3 **curiosity** titles (mental trigger)
2. 2-3 **direct benefit** titles (what the viewer gets)
3. 2-3 **urgency/novelty** titles (NEW, 2024, Updated)
4. 2-3 **tutorial/how-to** titles (How to do X)

**Output format:**
```
## 🎯 OPTIMIZED TITLES (Top 10)

1. 🔥 [Title] #hashtag
2. 🚀 [Title]
3. 💡 [Title]
... (up to 10)

**Recommendation:** Title #X
**Justification:** [SEO analysis of recommended title]
```

---

### PHASE 4: Keywords and Tags

**Mandatory research via WebSearch:**
- Estimated search volume
- Competitiveness
- Related keywords

**Tag structure (maximum 500 characters):**

| Category | Quantity | Description |
|-----------|------------|-----------|
| Primary | 3-4 | High volume, main topic |
| Secondary | 5-6 | Medium volume, less competition |
| Long-tail | 4-5 | Specific, low competition |
| Bilingual | 2-3 | Local language + English when relevant |

**Load reference from:** `references/keywords-database.md`

**Output format:**
```
## 🏷️ TAGS (XXX/500 characters)

tag1, tag2, tag3, tag4, tag5, tag6, tag7, tag8, tag9, tag10...

**Analysis:**
- Primary keywords: [list]
- Estimated volume: [high/medium/low]
- Competitiveness: [high/medium/low]
```

---

### PHASE 5: Strategic Hashtags (8-12)

**Mandatory composition:**

| Type | Quantity | Examples |
|------|------------|----------|
| Brand | 2-3 | #ChannelName #BrandTag |
| Topic | 3-4 | Specific to the subject |
| Trending | 2-3 | Trending in the niche |
| CTA | 1-2 | #Tutorial #LearnWithMe |

**Output format:**
```
## #️⃣ HASHTAGS

#ChannelName #BrandTag #tag3 #tag4 #tag5 #tag6 #tag7 #tag8 #tag9 #tag10
```

---

### PHASE 6: Complete Description

**Load links template:** `assets/links-template.md`

**Description structure:**

```markdown
[EMOJI] [HOOK - 1-2 catchy sentences that create curiosity]

📌 In this video you will learn:
• [Benefit 1]
• [Benefit 2]
• [Benefit 3]

⏱️ TIMESTAMPS:
00:00 - Introduction
[Generate based on content if available]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[INSERT CONTENT FROM assets/links-template.md]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 Keywords: [3-5 main keywords]

[HASHTAGS]
```

---

### PHASE 7: Thumbnail Generation (INTERACTIVE - MANDATORY)

**⚠️ IMPORTANT: NEVER generate a thumbnail without first interacting with the user!**

**Load styles from:** `references/thumbnail-styles.md`

**Default style guidelines:**
- Text in 2-3 alternately tilted boxes
- Maximum 6 words total
- Vibrant colors and high contrast
- Blurred or gradient background
- Relevant visual element (icon, logo, screenshot)
- **Aspect Ratio:** 16:9 (YouTube horizontal format)
- **Resolution:** ~1344x768 pixels (1K) - YouTube compatible (recommended: 1280x720)

**Generation process:**

1. **ASK THE USER** before generating:

```
🖼️ Let's create the thumbnail together!

I need you to provide:

1. **Thumbnail text** (maximum 6 words)
   Ex: "MASTER AI IN 10 MIN"

2. **Visual style**:
   - tutorial (learning)
   - review (evaluation)
   - news (novelty/launch)
   - list (top X, best)
   - tips (tips, hacks)
   - viral (impactful)

3. **Main visual element** (optional):
   - Tool logo
   - Screenshot/mockup
   - Representative icons
   - Other element

4. **Color palette**:
   - blue purple gradient (default)
   - orange red gradient (urgent)
   - green cyan gradient (fresh)
   - dark neon (dark background)
   - white black contrast (high contrast)

After receiving the information, show the **PREVIEW** and ask for confirmation before generating.
```

2. **After user confirmation**, call the script:

```bash
python scripts/generate-thumbnail.py \
  "[TEXT]" \
  "[STYLE]" \
  "[VISUAL_ELEMENT]" \
  "[COLORS]" \
  "[FILENAME]"
```

Or use the interactive function:
```bash
python scripts/generate-thumbnail.py --interactive
```

3. **Process the response** and save in `./thumbnails/[video-name].png`

**Output format:**
```
## 🖼️ THUMBNAIL

**Text:** [text chosen by user]
**Style:** [chosen style]
**Visual element:** [chosen element]
**Colors:** [chosen palette]

**Generated prompt:**
[complete prompt sent to API]

**Saved file:** ./thumbnails/[name].png
```

---

### PHASE 8: Final SEO Analysis

**Output format:**
```
## 📊 SEO ANALYSIS

| Metric | Rating | Observation |
|---------|-----------|------------|
| Primary keywords | ⭐⭐⭐⭐⭐ | [comment] |
| Competitiveness | ⭐⭐⭐ | [comment] |
| Ranking potential | ⭐⭐⭐⭐ | [comment] |
| Estimated CTR | ⭐⭐⭐⭐ | [comment] |

**Additional recommendations:**
- [Suggestion 1]
- [Suggestion 2]
```

---

## EXPECTED COMPLETE OUTPUT

At the end of execution, deliver:

```
═══════════════════════════════════════════════════════════
🎬 YOUTUBE CONTENT - [VIDEO TOPIC]
═══════════════════════════════════════════════════════════

## 🎯 OPTIMIZED TITLES (Top 10)
[10 titles with emojis and hashtags]
**Recommendation:** [chosen title + justification]

---

## 📝 COMPLETE DESCRIPTION
[Formatted description with template links]

---

## 🏷️ TAGS (XXX/500 characters)
[Optimized tags]

---

## #️⃣ HASHTAGS
[8-12 strategic hashtags]

---

## 🖼️ THUMBNAIL
[Generated thumbnail information]

---

## 📊 SEO ANALYSIS
[Complete analysis]

═══════════════════════════════════════════════════════════
```

---

## FALLBACKS

**If thumbnail API fails:**
- Generate only detailed textual suggestion
- Provide prompt for manual use
- Suggest alternative tools (Canva, Photoshop)
- Show the error returned by the API for debugging

**If the generated image doesn't open:**
- Check if base64 was extracted correctly
- The Gemini API can return in different formats:
  - `inline_data` with `image_uri`
  - Direct Data URI: `data:image/png;base64,...`
  - JSON in content
- The script already handles these formats, but may need adjustments

**If web search not available:**
- Use internal knowledge base
- Apply proven formulas from `references/title-formulas.md`
- Inform the user that real-time research was not possible

---

## REFERENCE FILES

| File | Function |
|---------|--------|
| `assets/links-template.md` | Channel fixed links (editable) |
| `references/title-formulas.md` | Proven title formulas |
| `references/keywords-database.md` | Keywords by category |
| `references/thumbnail-styles.md` | Styles and prompts for thumbnails |
| `scripts/generate-thumbnail.py` | Script to generate and save thumbnail |

---

## IMPORTANT NOTES

1. **ALWAYS research before generating** - Don't invent based only on internal knowledge
2. **Prioritize organic SEO** in all decisions
3. **Maintain consistent channel visual identity** in thumbnails
4. **70% of audience is mobile** - Titles must be readable on small screens
5. **Links are editable** in `assets/links-template.md`
