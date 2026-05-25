/* ═══════════════════════════════════════════════════════════════════
   article-loader.js
   ───────────────────────────────────────────────────────────────────
   This file is what makes the whole "publish-once, appears-everywhere"
   system work.

   It reads ONE file — /en/posts/articles.json — and uses it to build:
     1. The Insights preview cards on the homepage      (two newest)
     2. The article grid on knowledge.html              (all articles)
     3. The featured-article slot on knowledge.html     (one article)
     4. The marquee ticker on knowledge.html            (rotating titles)
     5. The search filter on knowledge.html             (live filtering)

   You DO NOT need to edit this file when you publish a new article.
   You only edit /en/posts/articles.json. That's the whole point.


   HOW IT FINDS WHAT TO BUILD
   The script looks for specific HTML containers on whichever page it's
   loaded into. If the container exists, it fills it. If not, it skips.
   This means the same script runs on the homepage and on knowledge.html
   without any per-page configuration.

   The containers it looks for:
     <div data-articles="homepage-preview">   → fills with 2 newest cards
     <div data-articles="knowledge-grid">     → fills with all cards
     <div data-articles="featured">           → fills with the featured one
     <div data-articles="marquee">            → fills with rotating titles
     <input data-articles-search>             → wires up the search filter

   Place any of these containers on any page. The loader does the rest.


   EDITING
     🟢 Safe: the placeholder/error/empty-state messages near the top
     🟡 Care: the renderer functions (changes affect what cards look like)
     🔴 Don't: the fetch logic and the filter wiring, unless you know JS

   ACCESSIBILITY
     Respects prefers-reduced-motion (the marquee inherits motion.css
     handling, which display:none-s the marquee for reduced-motion users).
     Search input is a real <input> with a label — screen-reader friendly.
═══════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';


  /* ─── Where the manifest lives ─────────────────────────────────────
     The path is RELATIVE to the page that loads this script.
     Both /en/index.html and /en/knowledge.html sit at the same depth,
     so "./posts/articles.json" works from both.
     If you ever move articles.json, update this one line.
  ────────────────────────────────────────────────────────────────── */
  const MANIFEST_PATH = './posts/articles.json';


  /* ─── Messages shown to visitors in edge cases ─────────────────────
     🟢 SAFE TO EDIT: rewrite the wording if you want.
  ────────────────────────────────────────────────────────────────── */
  const ERROR_MESSAGE =
    "Couldn't load articles — check /en/posts/articles.json for syntax errors.";
  const EMPTY_NOTICE =
    "First articles coming soon.";
  // Note: EMPTY_NOTICE is only shown if a page explicitly opts in via
  // data-articles-empty-notice. By default, empty manifest = silent hide.


  /* ─── The manifest, once loaded ────────────────────────────────────
     We fetch it once and reuse it for every container on the page.
     This avoids hitting the network multiple times for the same data.
  ────────────────────────────────────────────────────────────────── */
  let cachedArticles = null;


  /* ═══════════════════════════════════════════════════════════════
     STEP 1 — FETCH THE MANIFEST
     ───────────────────────────────────────────────────────────────
     Loads articles.json from the server. Returns a sorted-newest-first
     array of articles, or null if the file is missing/broken.
  ═══════════════════════════════════════════════════════════════ */

  async function loadManifest() {
    if (cachedArticles !== null) return cachedArticles;

    try {
      const response = await fetch(MANIFEST_PATH, { cache: 'no-cache' });
      if (!response.ok) {
        console.error('article-loader: manifest fetch failed', response.status);
        return null;
      }
      const data = await response.json();
      if (!Array.isArray(data)) {
        console.error('article-loader: manifest is not an array');
        return null;
      }

      // Sort newest first by date. Articles missing a date fall to the end.
      data.sort((a, b) => {
        const da = a.date || '';
        const db = b.date || '';
        return db.localeCompare(da);
      });

      cachedArticles = data;
      return data;
    } catch (err) {
      console.error('article-loader: manifest could not be parsed', err);
      return null;
    }
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 2 — RENDER A SINGLE ARTICLE CARD (the standard one)
     ───────────────────────────────────────────────────────────────
     Used by both the homepage preview and the knowledge.html grid.
     The "withDate" flag controls whether the meta line shows the date.

     This function builds a real DOM element and returns it.
     The caller is responsible for putting it in the right container.
  ═══════════════════════════════════════════════════════════════ */

  function buildCard(article, options) {
    const opts = options || {};
    const withDate = !!opts.withDate;
    const delaySlot = opts.delaySlot;     // 1..6 if a stagger delay is wanted
    const animate = opts.animate !== false; // default true

    const card = document.createElement('article');
    card.className = 'insight-card';
    if (animate) card.setAttribute('data-animate', 'fade-up');
    if (delaySlot) card.setAttribute('data-delay', String(delaySlot));

    // Schema.org microdata — declares each card as an Article entity.
    // Invisible to humans, critical for SEO and AEO. Helps Google and
    // AI answer engines (ChatGPT, Claude, Perplexity) understand that
    // each card represents an article with title, author, and date.
    card.setAttribute('itemscope', '');
    card.setAttribute('itemtype', 'https://schema.org/Article');

    // Meta line. Either "Eyebrow · 8 min read" (homepage)
    //         or "Eyebrow · 20 April 2026 · 8 min read" (knowledge)
    const meta = document.createElement('p');
    meta.className = 'insight-card__meta';
    const metaParts = [];
    if (article.eyebrow) metaParts.push(article.eyebrow);
    if (withDate && article.date) metaParts.push(formatDate(article.date));
    if (article.reading_time) metaParts.push(article.reading_time);
    meta.textContent = metaParts.join(' · ');
    card.appendChild(meta);

    // Hidden microdata — author and date as machine-readable values.
    // These don't appear visually but are read by search-engine crawlers.
    if (article.author) {
      const authorMeta = document.createElement('meta');
      authorMeta.setAttribute('itemprop', 'author');
      authorMeta.setAttribute('content', article.author);
      card.appendChild(authorMeta);
    }
    if (article.date) {
      const dateMeta = document.createElement('meta');
      dateMeta.setAttribute('itemprop', 'datePublished');
      dateMeta.setAttribute('content', article.date);
      card.appendChild(dateMeta);
    }

    // Title — wrapped in a link to the article HTML file.
    const titleEl = document.createElement('h3');
    titleEl.className = 'insight-card__title';
    titleEl.setAttribute('itemprop', 'headline');
    const link = document.createElement('a');
    link.href = './posts/' + article.slug + '.html';
    link.setAttribute('itemprop', 'url');
    link.textContent = article.title || '(untitled)';
    titleEl.appendChild(link);
    card.appendChild(titleEl);

    // Excerpt.
    if (article.excerpt) {
      const excerpt = document.createElement('p');
      excerpt.className = 'insight-card__excerpt';
      excerpt.setAttribute('itemprop', 'description');
      excerpt.textContent = article.excerpt;
      card.appendChild(excerpt);
    }

    return card;
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 3 — RENDER THE FEATURED ARTICLE (the wide variant)
     ───────────────────────────────────────────────────────────────
     A larger, more prominent card. Same data, different presentation.
     Adds the modifier class .insight-card--featured which theme.css
     styles to be wider, with bigger title and visible excerpt.
  ═══════════════════════════════════════════════════════════════ */

  function buildFeaturedCard(article) {
    const card = buildCard(article, { withDate: true, animate: true });
    card.classList.add('insight-card--featured');
    return card;
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 4 — DATE FORMATTING
     ───────────────────────────────────────────────────────────────
     Converts "2026-04-20" into "20 April 2026" for human display.
     Uses the visitor's browser locale settings, so a Thai visitor
     might see different month names. Defaults to English if the
     locale isn't recognised.
  ═══════════════════════════════════════════════════════════════ */

  function formatDate(iso) {
    // iso is "YYYY-MM-DD". Anything else, return as-is.
    if (!iso || typeof iso !== 'string') return '';
    const parts = iso.split('-');
    if (parts.length !== 3) return iso;
    const date = new Date(
      parseInt(parts[0], 10),
      parseInt(parts[1], 10) - 1,
      parseInt(parts[2], 10)
    );
    if (isNaN(date.getTime())) return iso;
    try {
      return date.toLocaleDateString('en-GB', {
        day: 'numeric', month: 'long', year: 'numeric'
      });
    } catch (e) {
      return iso;
    }
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 5 — FILL THE HOMEPAGE PREVIEW CONTAINER
     ───────────────────────────────────────────────────────────────
     Looks for <div data-articles="homepage-preview"> on the page.
     If found, fills it with the two newest articles (no date, no
     stagger conflict — the homepage is light).
  ═══════════════════════════════════════════════════════════════ */

  function fillHomepagePreview(articles) {
    const container = document.querySelector('[data-articles="homepage-preview"]');
    if (!container) return;

    if (!articles || articles.length === 0) {
      hideContainerAndAncestor(container, '.section--insights');
      return;
    }

    container.innerHTML = '';
    const top = articles.slice(0, 2);
    top.forEach((article, idx) => {
      const card = buildCard(article, {
        withDate: false,
        delaySlot: idx + 1   // first card delay-1, second card delay-2
      });
      container.appendChild(card);
    });

    // After insertion, ask the scroll-reveal observer to look at these.
    // animations.js exposes a re-scan hook (we'll add it in Step 3).
    if (window.__rescanScrollReveal) window.__rescanScrollReveal();
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 6 — FILL THE FEATURED SLOT ON KNOWLEDGE.HTML
     ───────────────────────────────────────────────────────────────
     If any article has "featured": true, that one is featured.
     Otherwise the newest article is auto-featured (silent fallback).
  ═══════════════════════════════════════════════════════════════ */

  function fillFeatured(articles) {
    const container = document.querySelector('[data-articles="featured"]');
    if (!container) return;

    if (!articles || articles.length === 0) {
      hideContainerAndAncestor(container, '.knowledge-featured');
      return;
    }

    const explicit = articles.find(a => a.featured === true);
    const chosen = explicit || articles[0];

    container.innerHTML = '';
    container.appendChild(buildFeaturedCard(chosen));

    if (window.__rescanScrollReveal) window.__rescanScrollReveal();
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 7 — FILL THE FULL ARTICLE GRID ON KNOWLEDGE.HTML
     ───────────────────────────────────────────────────────────────
     Renders every article (excluding the one in the featured slot,
     to avoid duplication) as a card with date shown.

     Each card is given a data-search-text attribute containing all
     its searchable text in lowercase, so the search filter (Step 9)
     can match against it without rebuilding the card.
  ═══════════════════════════════════════════════════════════════ */

  function fillKnowledgeGrid(articles) {
    const container = document.querySelector('[data-articles="knowledge-grid"]');
    if (!container) return;

    if (!articles || articles.length === 0) {
      hideContainerAndAncestor(container, '.knowledge-feed');
      return;
    }

    // Figure out which article is in the featured slot, so we can skip it here.
    const explicit = articles.find(a => a.featured === true);
    const featuredSlug = explicit ? explicit.slug : articles[0].slug;
    const remaining = articles.filter(a => a.slug !== featuredSlug);

    container.innerHTML = '';

    if (remaining.length === 0) {
      // Only one article exists, and it's featured. Hide the grid section.
      hideContainerAndAncestor(container, '.knowledge-feed');
      return;
    }

    remaining.forEach((article, idx) => {
      const card = buildCard(article, {
        withDate: true,
        // Stagger the first 6 cards. After that, delays cap (still reveals,
        // just simultaneously) — at 7+ cards the cascade is already visible
        // enough that more delay would feel slow.
        delaySlot: idx < 6 ? idx + 1 : null
      });

      // Attach searchable text for the filter.
      const searchText = [
        article.title || '',
        article.excerpt || '',
        article.eyebrow || ''
      ].join(' ').toLowerCase();
      card.setAttribute('data-search-text', searchText);

      container.appendChild(card);
    });

    if (window.__rescanScrollReveal) window.__rescanScrollReveal();
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 8 — FILL THE MARQUEE
     ───────────────────────────────────────────────────────────────
     The marquee structure (from motion.css) requires items to be
     duplicated twice for the seamless loop. We render the title list
     once, then again, both inside the same .marquee-track element.

     Each title is wrapped in a link so visitors can click it.
     Titles are separated by a small gold dot.
  ═══════════════════════════════════════════════════════════════ */

  function fillMarquee(articles) {
    const container = document.querySelector('[data-articles="marquee"]');
    if (!container) return;

    if (!articles || articles.length === 0) {
      hideContainerAndAncestor(container, '.knowledge-marquee');
      return;
    }

    container.innerHTML = '';

    // Build one full set of items.
    function buildSet() {
      const set = document.createDocumentFragment();
      articles.forEach((article, idx) => {
        const link = document.createElement('a');
        link.className = 'marquee-item';
        link.href = './posts/' + article.slug + '.html';
        link.textContent = article.title || '';
        set.appendChild(link);

        // Gold-dot separator after each item EXCEPT to leave room
        // for the next set. We always emit a dot — even at the end —
        // because the second set immediately follows in the loop and
        // should be separated visually too.
        const dot = document.createElement('span');
        dot.className = 'marquee-dot';
        dot.setAttribute('aria-hidden', 'true');
        dot.textContent = '·';
        set.appendChild(dot);
      });
      return set;
    }

    container.appendChild(buildSet());
    container.appendChild(buildSet());
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 9 — WIRE UP THE SEARCH FILTER
     ───────────────────────────────────────────────────────────────
     Looks for <input data-articles-search>. As the visitor types,
     hides any card in the knowledge grid whose data-search-text
     does not contain the typed string. Empty input = show all.
  ═══════════════════════════════════════════════════════════════ */

  function initSearch() {
    const input = document.querySelector('[data-articles-search]');
    if (!input) return;

    const grid = document.querySelector('[data-articles="knowledge-grid"]');
    if (!grid) return;

    const noMatch = document.querySelector('[data-articles-no-match]');

    input.addEventListener('input', () => {
      const query = input.value.trim().toLowerCase();
      const cards = grid.querySelectorAll('[data-search-text]');
      let visibleCount = 0;

      cards.forEach((card) => {
        const text = card.getAttribute('data-search-text') || '';
        const matches = query === '' || text.indexOf(query) !== -1;
        card.style.display = matches ? '' : 'none';
        if (matches) visibleCount++;
      });

      // Show/hide the "no results" message if one exists on the page.
      if (noMatch) {
        noMatch.style.display = (visibleCount === 0 && query !== '') ? '' : 'none';
      }
    });
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 10 — ERROR DISPLAY
     ───────────────────────────────────────────────────────────────
     If the manifest can't be loaded, we show a single visible error
     message at the top of any container that was supposed to be filled.
     This makes a syntax error in articles.json discoverable rather
     than silent — the user sees the warning and knows where to look.
  ═══════════════════════════════════════════════════════════════ */

  function showErrorIn(selector) {
    const container = document.querySelector(selector);
    if (!container) return;
    const msg = document.createElement('p');
    msg.className = 'articles-error';
    msg.setAttribute('role', 'alert');
    msg.textContent = ERROR_MESSAGE;
    container.innerHTML = '';
    container.appendChild(msg);
  }


  /* ═══════════════════════════════════════════════════════════════
     UTILITY — hide a container AND its ancestor section
     ───────────────────────────────────────────────────────────────
     When the manifest is empty, we don't want a half-empty section
     showing just a heading and no cards. So we walk up to the
     section ancestor and hide that too.
  ═══════════════════════════════════════════════════════════════ */

  function hideContainerAndAncestor(container, ancestorSelector) {
    container.style.display = 'none';
    if (ancestorSelector) {
      const ancestor = container.closest(ancestorSelector);
      if (ancestor) ancestor.style.display = 'none';
    }
  }


  /* ═══════════════════════════════════════════════════════════════
     STEP 11 — INJECT JSON-LD STRUCTURED DATA
     ───────────────────────────────────────────────────────────────
     Builds a <script type="application/ld+json"> block describing
     the page's articles as a schema.org ItemList of Article entities.
     This is the single most important block for AEO — AI answer
     engines (ChatGPT, Claude, Perplexity, Google AI Overview) read
     this to understand what the page contains.

     The page declares its context by setting data-seo-context on the
     body element. Two values are recognised:
       "knowledge-index"  → injects CollectionPage with full ItemList
       "homepage"         → injects a lighter ItemList of recent items

     If no context is declared, no JSON-LD is injected (the page is
     assumed not to want it).

     This script also reads <meta name="site-url"> from the page head
     to build absolute URLs in the structured data, since absolute
     URLs are strongly preferred by search-engine crawlers.
  ═══════════════════════════════════════════════════════════════ */

  function injectStructuredData(articles) {
    const context = document.body.getAttribute('data-seo-context');
    if (!context) return;
    if (!articles || articles.length === 0) return;

    // Read the canonical site URL from a meta tag in the head.
    // Falls back to window.location.origin if not declared.
    const siteUrlMeta = document.querySelector('meta[name="site-url"]');
    const siteUrl = siteUrlMeta
      ? siteUrlMeta.getAttribute('content').replace(/\/$/, '')
      : window.location.origin;

    // Read the firm name from a meta tag, with a sensible fallback.
    const firmNameMeta = document.querySelector('meta[name="firm-name"]');
    const firmName = firmNameMeta
      ? firmNameMeta.getAttribute('content')
      : 'Your Firm Name';

    // Build the list of articles as schema.org Article entities.
    function articleToSchema(article, position) {
      const url = siteUrl + '/en/posts/' + article.slug + '.html';
      const entity = {
        '@type': 'Article',
        'position': position,
        'headline': article.title || '',
        'description': article.excerpt || '',
        'url': url,
        'mainEntityOfPage': url,
        'author': {
          '@type': 'Organization',
          'name': article.author || firmName
        },
        'publisher': {
          '@type': 'Organization',
          'name': firmName
        }
      };
      if (article.date) entity.datePublished = article.date;
      if (article.eyebrow) entity.articleSection = article.eyebrow;
      if (article.keywords && article.keywords.length) {
        entity.keywords = article.keywords.join(', ');
      }
      return entity;
    }

    let payload;

    if (context === 'knowledge-index') {
      // Full CollectionPage — the canonical structured-data shape for
      // an article archive. AI answer engines look for exactly this.
      payload = {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        'name': document.title || 'Insights',
        'url': siteUrl + window.location.pathname,
        'isPartOf': {
          '@type': 'WebSite',
          'name': firmName,
          'url': siteUrl
        },
        'mainEntity': {
          '@type': 'ItemList',
          'itemListElement': articles.map((a, i) => ({
            '@type': 'ListItem',
            'position': i + 1,
            'item': articleToSchema(a, i + 1)
          }))
        }
      };
    } else if (context === 'homepage') {
      // Lighter shape — homepage is mostly a WebSite landing, but it
      // still benefits from declaring the recent articles it links to.
      const recent = articles.slice(0, 3);
      payload = {
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        'name': 'Recent insights',
        'itemListElement': recent.map((a, i) => ({
          '@type': 'ListItem',
          'position': i + 1,
          'item': articleToSchema(a, i + 1)
        }))
      };
    } else {
      return;
    }

    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.setAttribute('data-injected-by', 'article-loader');
    script.textContent = JSON.stringify(payload, null, 2);
    document.head.appendChild(script);
  }


  /* ═══════════════════════════════════════════════════════════════
     INITIALISATION
     ───────────────────────────────────────────────────────────────
     Runs once the DOM is parsed. Loads the manifest, then fills
     every container that asked to be filled, then injects the
     structured data block for SEO/AEO.
  ═══════════════════════════════════════════════════════════════ */

  async function init() {
    const articles = await loadManifest();

    if (articles === null) {
      // Manifest broken or missing.
      showErrorIn('[data-articles="homepage-preview"]');
      showErrorIn('[data-articles="knowledge-grid"]');
      showErrorIn('[data-articles="featured"]');
      return;
    }

    fillHomepagePreview(articles);
    fillFeatured(articles);
    fillKnowledgeGrid(articles);
    fillMarquee(articles);
    initSearch();
    injectStructuredData(articles);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
