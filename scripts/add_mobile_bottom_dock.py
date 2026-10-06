# -*- coding: utf-8 -*-
import os
import re

path = '/Users/howardliao/Desktop/HermesAgent/PortFilio/fuyu/generate_dajing_interactive.py'

with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add Section IDs for anchor scrolling
code = code.replace(
    '<!-- 4 Bento Stats (Framed from Win-Win Perspective for 富宇大地) -->\n    <div class="bento-stats">',
    '<!-- 4 Bento Stats (Framed from Win-Win Perspective for 富宇大地) -->\n    <div class="bento-stats" id="secBento">'
)

code = code.replace(
    '    <!-- ======================================================================= -->\n    <!-- SECTION: 6 LEGAL DOSSIERS (PDF ONLY)                                    -->\n    <!-- ======================================================================= -->\n    <div class="section-title">',
    '    <!-- ======================================================================= -->\n    <!-- SECTION: 6 LEGAL DOSSIERS (PDF ONLY)                                    -->\n    <!-- ======================================================================= -->\n    <div class="section-title" id="secDossiers">'
)

code = code.replace(
    '    <!-- ======================================================================= -->\n    <!-- INTERACTIVE 4: NEIGHBOR FAQ ACCORDION                                   -->\n    <!-- ======================================================================= -->\n    <div class="section-title">',
    '    <!-- ======================================================================= -->\n    <!-- INTERACTIVE 4: NEIGHBOR FAQ ACCORDION                                   -->\n    <!-- ======================================================================= -->\n    <div class="section-title" id="secFaq">'
)

# 2. Add Mobile Bottom Dock CSS before </style>
dock_css = """
    /* ========================================================================= */
    /* MOBILE BOTTOM DOCK NAVIGATION BAR STYLES                                 */
    /* ========================================================================= */
    .mobile-bottom-dock {
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 62px;
      background: rgba(14, 18, 26, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1.5px solid rgba(212, 175, 55, 0.45);
      box-shadow: 0 -6px 25px rgba(0, 0, 0, 0.65);
      z-index: 9995;
      padding: 0 6px;
      padding-bottom: env(safe-area-inset-bottom, 0px);
      align-items: center;
      justify-content: space-around;
    }

    .dock-item {
      background: transparent;
      border: none;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      color: #9E9587;
      cursor: pointer;
      padding: 4px 6px;
      flex: 1;
      transition: all 0.2s;
      -webkit-tap-highlight-color: transparent;
    }

    .dock-item span {
      font-size: 0.72rem;
      font-weight: 600;
      color: #C5BCAD;
      white-space: nowrap;
    }

    .dock-item svg {
      stroke: #C5BCAD;
      transition: all 0.2s;
    }

    .dock-item:active span, .dock-item:active svg {
      color: var(--gold-bright);
      stroke: var(--gold-bright);
    }

    /* Highlight Center Item */
    .dock-item.highlight {
      position: relative;
      top: -10px;
    }

    .dock-icon-circle {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 15px rgba(212, 175, 55, 0.45);
      border: 2px solid #0B0F19;
      margin-bottom: 2px;
    }

    .dock-icon-circle svg {
      stroke: #0B0F19;
      stroke-width: 2.4;
    }

    .dock-item.highlight span {
      color: var(--gold-bright);
      font-weight: 700;
      font-size: 0.72rem;
    }

    @media (max-width: 768px) {
      .mobile-bottom-dock {
        display: flex;
      }
      .fab-contact {
        display: none !important; /* Hide redundant floating button on mobile */
      }
      body {
        padding-bottom: 74px; /* Ensure content is never obscured by mobile dock */
      }
    }
  </style>"""

code = code.replace('  </style>', dock_css)

# 3. Add Mobile Bottom Dock HTML right before modal
dock_html = """  <!-- ========================================================================= -->
  <!-- MOBILE BOTTOM DOCK NAVIGATION BAR (STICKY AT BOTTOM ON MOBILE)           -->
  <!-- ========================================================================= -->
  <nav class="mobile-bottom-dock" id="mobileBottomDock">
    <button class="dock-item" onclick="scrollToSection('secBento')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
      <span>雙贏效益</span>
    </button>
    <button class="dock-item" onclick="scrollToSection('secDossiers')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
      <span>法定卷宗</span>
    </button>
    <button class="dock-item highlight" onclick="openPdfModal('臺中市公寓大廈爭議事件調處申請書.pdf', '臺中市公寓大廈爭議事件調處申請書（2 頁官方版）')">
      <div class="dock-icon-circle">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      </div>
      <span>調處申請</span>
    </button>
    <button class="dock-item" onclick="scrollToSection('secFaq')">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      <span>常見問答</span>
    </button>
    <button class="dock-item" onclick="openContactModal()">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      <span>聯繫主事</span>
    </button>
  </nav>

  <!-- ========================================================================= -->
  <!-- MODAL: IN-PAGE PDF VIEWER                                                 -->
  <!-- ========================================================================= -->"""

code = code.replace(
    '  <!-- ========================================================================= -->\n  <!-- MODAL: IN-PAGE PDF VIEWER                                                 -->\n  <!-- ========================================================================= -->',
    dock_html
)

# 4. Add scrollToSection helper in JS
js_helper = """    function scrollToSection(id) {
      const el = document.getElementById(id);
      if (el) {
        const yOffset = -24;
        const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    }

    // 1. PDF Modal Handler"""

code = code.replace('    // 1. PDF Modal Handler', js_helper)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Mobile Bottom Dock successfully injected into generate_dajing_interactive.py!")
