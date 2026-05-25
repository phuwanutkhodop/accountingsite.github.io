═══════════════════════════════════════════════════════════════════════════
ARTICLES.JSON — HOW IT WORKS
═══════════════════════════════════════════════════════════════════════════

This folder holds two kinds of files:

  1. The HTML article files       (e.g. thai-company-setup.html)
  2. articles.json                ← the LIST of all articles in this folder

Every page on the website that mentions an article — the homepage Insights
preview, the knowledge.html grid, the marquee — reads from articles.json.

So: when you publish a new article, you do TWO things:
  Step 1.  Save the article HTML in this folder.
  Step 2.  Add an entry for it to articles.json.

That's the whole workflow. Don't edit the homepage. Don't edit knowledge.html.
Don't edit the marquee. Just edit this one file.


───────────────────────────────────────────────────────────────────────────
HOW TO ADD A NEW ARTICLE TO articles.json
───────────────────────────────────────────────────────────────────────────

1. Open articles.json
2. Add a new block at the TOP of the list (so newest is first)
3. Save

A new block looks like this — copy this template, change the values:

  {
    "slug": "your-article-filename-without-html",
    "title": "The article's full headline",
    "excerpt": "A short two-sentence summary that appears on the card.",
    "eyebrow": "Tax",
    "date": "2026-06-15",
    "reading_time": "7 min read",
    "author": "Your Firm Name",
    "keywords": ["topic one", "topic two", "topic three"]
  },

The comma at the end is important — it separates this entry from the next
one. The LAST entry in the list does NOT get a comma.


───────────────────────────────────────────────────────────────────────────
WHAT EACH FIELD MEANS
───────────────────────────────────────────────────────────────────────────

slug
    The article's filename WITHOUT the .html on the end.
    If your file is "thai-company-setup.html", the slug is
    "thai-company-setup".  This becomes the link target.
    Use only lowercase letters, numbers, and hyphens. No spaces.

title
    The article's full headline. Same as the <h1> at the top of the
    article HTML file.

excerpt
    The short summary that shows on the card on knowledge.html and the
    homepage. Aim for about 25-40 words. Two sentences works well.

eyebrow
    The small gold label above the title. This is editorial signalling —
    it tells the reader what topic this article is about. Common values:
    "Tax", "Legal", "Onboarding", "Audit", "Bangkok". You can use any
    short label you want. Keep it under 20 characters.

date
    The publication date, in YYYY-MM-DD format. Used to sort articles
    newest-first. Example: 2026-06-15 means 15 June 2026.

reading_time
    Hand-typed by you. Calculate: total words divided by 200, rounded.
    Format: "8 min read" or "5 min read" — keep the format consistent.

author
    OPTIONAL. The name of the article's author. If you skip this field,
    the firm name is used as a default. Mainly matters for SEO and AEO —
    Google and AI answer engines like ChatGPT/Claude/Perplexity use the
    author field to attribute the article and build trust signals.
    Example: "Your Firm Name" or "Jane Doe, Senior Tax Advisor"

keywords
    OPTIONAL. A list of 2-5 short topic phrases that describe what the
    article covers. Mainly matters for SEO and AEO — these become part
    of the page's structured data, helping search engines and AI engines
    understand what topics the article addresses. Skip this field if you
    don't want to think about keywords; the article still works fine.
    Example: ["VAT Thailand", "Revenue Department", "tax registration"]
    Format: a list inside square brackets, each value in double quotes,
    separated by commas.

featured
    OPTIONAL. Add "featured": true to the article you want shown in
    the wide featured slot at the top of knowledge.html.
    Only ONE article should have this at any time. To change which
    article is featured: remove it from the old one, add it to the new.
    If NO article has featured: true, the newest article is shown there
    automatically.


───────────────────────────────────────────────────────────────────────────
THE THREE RULES OF JSON SYNTAX (the only thing to be careful about)
───────────────────────────────────────────────────────────────────────────

JSON is strict. If you break any of these, the file won't load and the
articles will disappear from the site until you fix it.

Rule 1.  Every text value must be in DOUBLE quotes.
         CORRECT:    "title": "Setting up a Thai company"
         WRONG:      "title": 'Setting up a Thai company'
         WRONG:      "title": Setting up a Thai company

Rule 2.  Each entry inside the [ ] list is separated by a comma.
         The LAST entry has NO comma after its closing }.

         CORRECT:
           [
             { "slug": "first" },
             { "slug": "second" },
             { "slug": "third" }              ← no comma here
           ]

         WRONG:
           [
             { "slug": "first" }              ← missing comma
             { "slug": "second" },
             { "slug": "third" },             ← extra comma at end
           ]

Rule 3.  No comments are allowed inside the JSON file itself.
         No // single-line comments.
         No /* multi-line */ comments.
         (That's why this README is a separate file.)


───────────────────────────────────────────────────────────────────────────
IF SOMETHING BREAKS
───────────────────────────────────────────────────────────────────────────

If you save articles.json and the article cards disappear from the
website, you've probably broken one of the three rules above. Two ways
to find the problem:

  1. The website itself.  knowledge.html will display a message like
     "Couldn't load articles — check articles.json for syntax errors"
     near the top of the page. That tells you the file is broken.

  2. JSONLint.  Visit https://jsonlint.com, paste in your full
     articles.json content, click "Validate JSON". It will tell you
     exactly which line and which character has the problem.

After you fix the typo and re-save, the articles re-appear on the next
page load.


───────────────────────────────────────────────────────────────────────────
WHAT IF articles.json IS EMPTY?
───────────────────────────────────────────────────────────────────────────

An empty manifest looks like this:    [ ]

When the manifest is empty, the website hides the entire article-related
sections of knowledge.html (the marquee, the search bar, the article grid)
and the homepage Insights section disappears too. The page still shows
the header, the page heading, and the contact CTA. Nothing looks broken.

This is intentional — it means you can ship the site before you have
any articles, and visitors won't see empty containers.


═══════════════════════════════════════════════════════════════════════════
END OF README
═══════════════════════════════════════════════════════════════════════════
