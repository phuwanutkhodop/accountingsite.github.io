/* ═══════════════════════════════════════════════════════════════════
   animations.js
   ───────────────────────────────────────────────────────────────────
   This file powers all interactive motion on the site.

   It contains five independent helpers, each in its own labelled
   section. They do not depend on each other — you can delete any
   one block and the rest will keep working.

   THE FIVE HELPERS
     1. Scroll-trigger reveal    → fades elements in as they scroll
                                    into view. Looks for elements with
                                    data-animate="…"
     2. Cursor glow on buttons   → a soft gold glow follows the mouse
                                    inside .btn--glow buttons
     3. Hero headline parallax   → the italic word drifts gently as
                                    the mouse moves. Looks for
                                    data-cursor-parallax
     4. Scroll progress bar      → fills the gold line at the top of
                                    the page as you scroll. Looks for
                                    #scrollProgress
     5. Stats counter            → counts numbers up from 0 when they
                                    enter the viewport. Looks for
                                    data-counter

   EDITING
     🟢 Safe: numeric tuning values (marked with comments)
     🟡 Care: the "init" calls at the bottom
     🔴 Don't: the IntersectionObserver blocks themselves, unless you
        know what you're doing

   ACCESSIBILITY
     The whole file respects `prefers-reduced-motion`. If the visitor
     has that OS setting on, all five helpers either disable themselves
     or fall back to an instant/no-motion version.
═══════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ─── Accessibility gate ─────────────────────────────────────────
     If the user has turned on "reduce motion" at the OS level,
     we disable everything except scroll reveals, and even those
     become instant (no fade, no slide). This is not optional —
     some users get motion sickness from parallax.
  ──────────────────────────────────────────────────────────────── */
  const prefersReducedMotion = window.matchMedia(
    '(prefers-reduced-motion: reduce)'
  ).matches;


  /* ═══════════════════════════════════════════════════════════════
     HELPER 1 — SCROLL-TRIGGER REVEAL
     ───────────────────────────────────────────────────────────────
     Finds every element with a data-animate="…" attribute and
     gives it a CSS class when it scrolls into view. The CSS in
     motion.css handles the actual fade/slide — this script just
     flips the switch.

     HTML usage:
       <h2 data-animate="fade-up">Hello</h2>
       <p data-animate="fade-up" data-animate-delay="2">World</p>

     🟢 SAFE TO EDIT: the threshold and rootMargin values below.
  ═══════════════════════════════════════════════════════════════ */

  function initScrollReveal() {
    const animatedEls = document.querySelectorAll('[data-animate]');
    if (animatedEls.length === 0) return;

    // If reduced motion: just reveal everything immediately, no observer.
    if (prefersReducedMotion) {
      animatedEls.forEach(el => el.classList.add('is-revealed'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const el = entry.target;
            const delay = el.getAttribute('data-animate-delay');

            // Apply delay class if specified (e.g. data-animate-delay="2" → delay-2)
            if (delay) {
              el.classList.add(`delay-${delay}`);
            }

            el.classList.add('is-revealed');
            observer.unobserve(el); // only fire once
          }
        });
      },
      {
        // 🟢 EDIT: how much of the element must be visible before revealing.
        //    0.15 = 15% visible. Raise for later reveals, lower for earlier.
        threshold: 0.15,

        // 🟢 EDIT: shrinks the viewport for the calculation.
        //    "0px 0px -10% 0px" means "trigger 10% before bottom of screen."
        rootMargin: '0px 0px -10% 0px'
      }
    );

    animatedEls.forEach((el) => observer.observe(el));
  }


  /* ═══════════════════════════════════════════════════════════════
     HELPER 2 — CURSOR GLOW ON BUTTONS
     ───────────────────────────────────────────────────────────────
     For any button with class .btn--glow, a soft gold radial
     gradient follows the mouse cursor *inside* the button.
     It uses CSS custom properties (--glow-x, --glow-y) so the
     actual glow is styled in motion.css.

     🟢 SAFE TO EDIT: selector below if you want to apply this
        effect to other elements too.
  ═══════════════════════════════════════════════════════════════ */

  function initCursorGlow() {
    if (prefersReducedMotion) return; // no glow if motion is reduced

    const glowEls = document.querySelectorAll('.btn--glow');
    if (glowEls.length === 0) return;

    glowEls.forEach((el) => {
      el.addEventListener('mousemove', (e) => {
        const rect = el.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        el.style.setProperty('--glow-x', `${x}%`);
        el.style.setProperty('--glow-y', `${y}%`);
      });

      // Reset when the cursor leaves, so glow fades back to centre
      el.addEventListener('mouseleave', () => {
        el.style.setProperty('--glow-x', '50%');
        el.style.setProperty('--glow-y', '50%');
      });
    });
  }


  /* ═══════════════════════════════════════════════════════════════
     HELPER 3 — HERO HEADLINE PARALLAX
     ───────────────────────────────────────────────────────────────
     The word wrapped in <span data-cursor-parallax> drifts a few
     pixels in the direction opposite to the mouse. Creates a
     subtle "floating serif" feel in the hero.

     🟢 SAFE TO EDIT: MAX_OFFSET (how far the word can drift).
  ═══════════════════════════════════════════════════════════════ */

  function initHeroParallax() {
    if (prefersReducedMotion) return; // no parallax for reduced motion

    const parallaxEls = document.querySelectorAll('[data-cursor-parallax]');
    if (parallaxEls.length === 0) return;

    // 🟢 EDIT: maximum drift in pixels. 12–18 feels editorial; 24+ feels playful.
    const MAX_OFFSET = 14;

    // Smoothing: we lerp (linearly interpolate) toward the target each frame
    // so the movement feels liquid, not jerky. 🟢 EDIT 0.08 to taste (lower = smoother/slower).
    const SMOOTHING = 0.08;

    let targetX = 0, targetY = 0;
    let currentX = 0, currentY = 0;
    let rafId = null;

    // Track the mouse relative to the centre of the viewport
    window.addEventListener('mousemove', (e) => {
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      // Normalised -1..1, then multiplied by MAX_OFFSET.
      // Negative sign → word drifts *away* from cursor (opposite direction).
      targetX = -((e.clientX - cx) / cx) * MAX_OFFSET;
      targetY = -((e.clientY - cy) / cy) * MAX_OFFSET;

      if (!rafId) tick();
    });

    function tick() {
      currentX += (targetX - currentX) * SMOOTHING;
      currentY += (targetY - currentY) * SMOOTHING;

      parallaxEls.forEach((el) => {
        el.style.transform =
          `translate3d(${currentX.toFixed(2)}px, ${currentY.toFixed(2)}px, 0)`;
      });

      // Keep animating until we've settled within half a pixel of target
      if (
        Math.abs(targetX - currentX) > 0.5 ||
        Math.abs(targetY - currentY) > 0.5
      ) {
        rafId = requestAnimationFrame(tick);
      } else {
        rafId = null;
      }
    }
  }


  /* ═══════════════════════════════════════════════════════════════
     HELPER 4 — SCROLL PROGRESS BAR
     ───────────────────────────────────────────────────────────────
     Updates the width of #scrollProgress based on how far down
     the page the visitor has scrolled. 0% at top, 100% at bottom.

     Uses requestAnimationFrame + a "ticking" flag to avoid firing
     on every single scroll event (which would be wasteful).
  ═══════════════════════════════════════════════════════════════ */

  function initScrollProgress() {
    const bar = document.getElementById('scrollProgress');
    if (!bar) return;

    let ticking = false;

    function update() {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight =
        document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      bar.style.width = `${pct}%`;
      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(update);
        ticking = true;
      }
    }, { passive: true });

    update(); // set initial value on load
  }


  /* ═══════════════════════════════════════════════════════════════
     HELPER 5 — STATS COUNTER
     ───────────────────────────────────────────────────────────────
     Any element with data-counter and data-target="NUMBER" will
     count up from 0 to that number when it scrolls into view.
     Used for the About section stats.

     Example HTML:
       <span data-counter data-target="140">0</span>

     🟢 SAFE TO EDIT: DURATION_MS (how long the count-up takes).
  ═══════════════════════════════════════════════════════════════ */

  function initStatsCounter() {
    const counters = document.querySelectorAll('[data-counter]');
    if (counters.length === 0) return;

    // 🟢 EDIT: total duration of the count-up in milliseconds.
    //    1600 = 1.6 seconds. Feels dignified. Faster feels frantic.
    const DURATION_MS = 1600;

    // If reduced motion: just set the final number immediately.
    if (prefersReducedMotion) {
      counters.forEach((el) => {
        const target = parseInt(el.getAttribute('data-target'), 10) || 0;
        el.textContent = target;
      });
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target'), 10) || 0;
          animateCount(el, target);
          observer.unobserve(el);
        });
      },
      { threshold: 0.5 } // count when element is halfway visible
    );

    counters.forEach((el) => observer.observe(el));

    function animateCount(el, target) {
      const start = performance.now();

      function step(now) {
        const elapsed = now - start;
        const progress = Math.min(elapsed / DURATION_MS, 1);
        // Ease-out cubic — starts fast, settles softly on the final number
        const eased = 1 - Math.pow(1 - progress, 3);
        const value = Math.round(target * eased);
        el.textContent = value;
        if (progress < 1) {
          requestAnimationFrame(step);
        }
      }

      requestAnimationFrame(step);
    }
  }


  /* ═══════════════════════════════════════════════════════════════
     INITIALISATION
     ───────────────────────────────────────────────────────────────
     🟡 EDIT WITH CARE: these are the calls that actually wire
     everything up. Comment out a line to disable that helper.
  ═══════════════════════════════════════════════════════════════ */

  function init() {
    initScrollReveal();     // 1. Fade-in-on-scroll
    initCursorGlow();       // 2. Gold glow on buttons
    initHeroParallax();     // 3. Headline drift
    initScrollProgress();   // 4. Progress bar
    initStatsCounter();     // 5. About section counters
  }

  // Run once the DOM is parsed. We use DOMContentLoaded rather than
  // `load` so the site feels responsive even before images finish.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
