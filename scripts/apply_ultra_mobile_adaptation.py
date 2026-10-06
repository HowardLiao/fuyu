# -*- coding: utf-8 -*-
import os
import re

path = '/Users/howardliao/Desktop/HermesAgent/PortFilio/fuyu/generate_dajing_interactive.py'

with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Viewport
code = code.replace(
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">'
)

# 2. Add Mobile Notice in Modal & Table Hint
modal_body_old = """      <div class="pdf-modal-body">
        <iframe id="pdfFrame" src=""></iframe>
      </div>"""

modal_body_new = """      <div class="mobile-pdf-notice">
        📱 手機用戶提示：若內嵌預覽無法完整上下滑動，請點擊上方<strong>【另開新分頁】</strong>或<strong>【下載 PDF】</strong>以原生全螢幕檢視！
      </div>
      <div class="pdf-modal-body">
        <iframe id="pdfFrame" src=""></iframe>
      </div>"""

code = code.replace(modal_body_old, modal_body_new)

# Table scroll hint
tbl_hint_old = """      <h3 style="color: #D4AF37; margin: 0 0 14px 0; font-size: 15px; font-weight: 700;">📋 全案「真正必要之 7 份核心文件」規格對照表</h3>
      
      <div style="overflow-x: auto;">"""

tbl_hint_new = """      <h3 style="color: #D4AF37; margin: 0 0 8px 0; font-size: 15px; font-weight: 700;">📋 全案「真正必要之 7 份核心文件」規格對照表</h3>
      <div class="table-scroll-hint">👉 手機用戶可左右滑動查看完整規格表格，或點擊每列右側「預覽」按鈕直接檢視！</div>
      <div style="overflow-x: auto; -webkit-overflow-scrolling: touch;">"""

code = code.replace(tbl_hint_old, tbl_hint_new)

# 3. Add Mobile CSS Rules before </style>
mobile_css = """
    /* ========================================================================= */
    /* ULTRA MOBILE ADAPTATION & RESPONSIVENESS ENHANCEMENTS                     */
    /* ========================================================================= */
    .mobile-pdf-notice {
      display: none;
      background: rgba(212, 175, 55, 0.15);
      border-bottom: 1px solid var(--gold-dark);
      color: var(--gold-bright);
      font-size: 0.8rem;
      padding: 8px 14px;
      text-align: center;
      line-height: 1.45;
    }

    .table-scroll-hint {
      display: none;
      font-size: 0.8rem;
      color: var(--gold-light);
      margin-bottom: 10px;
      padding: 4px 8px;
      background: rgba(212, 175, 55, 0.08);
      border-radius: 4px;
    }

    @media (max-width: 768px) {
      .mobile-pdf-notice { display: block; }
      .table-scroll-hint { display: block; }

      .container {
        padding: 16px 12px 60px;
        width: 100%;
        max-width: 100%;
      }

      header {
        margin-bottom: 20px;
      }

      h1 {
        font-size: 1.4rem;
        line-height: 1.35;
      }

      h1 span {
        font-size: 1.12rem;
      }

      .subtitle {
        font-size: 0.86rem;
        line-height: 1.55;
        padding: 0 4px;
        margin-bottom: 14px;
      }

      .tag-badge {
        font-size: 0.74rem;
        padding: 6px 10px;
        white-space: normal;
        text-align: center;
        line-height: 1.4;
      }

      .reporter-bar {
        flex-direction: column;
        align-items: stretch;
        gap: 6px;
        padding: 10px 14px;
        font-size: 0.82rem;
        text-align: center;
      }

      .bento-stats {
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin: 18px 0 24px;
      }

      .bento-card {
        padding: 12px 14px;
      }

      .bento-label {
        font-size: 0.72rem;
      }

      .bento-val {
        font-size: 1.25rem;
      }

      .bento-desc {
        font-size: 0.7rem;
        line-height: 1.35;
      }

      .section-title {
        font-size: 1.15rem;
        margin: 28px 0 14px;
        gap: 8px;
      }

      .simulator-card {
        padding: 16px 14px;
      }

      .house-selector {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 6px;
      }

      .btn-house {
        padding: 10px 4px;
        font-size: 0.8rem;
        text-align: center;
        min-height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      .sim-results {
        grid-template-columns: 1fr;
        gap: 10px;
        padding: 14px;
      }

      .sim-res-val {
        font-size: 1.4rem;
      }

      .dossier-row {
        flex-direction: column;
        align-items: stretch;
        padding: 16px 14px;
        gap: 14px;
      }

      .dossier-meta {
        flex-direction: column;
        gap: 8px;
        min-width: 0;
        width: 100%;
      }

      .dossier-badge {
        align-self: flex-start;
      }

      .dossier-texts h3 {
        font-size: 1rem;
        line-height: 1.4;
      }

      .dossier-texts p {
        font-size: 0.82rem;
        line-height: 1.5;
      }

      .dossier-actions {
        width: 100%;
        display: flex;
        flex-direction: row;
        gap: 8px;
      }

      .btn-pdf {
        flex: 1;
        justify-content: center;
        padding: 12px 8px;
        font-size: 0.88rem;
        min-height: 44px;
      }

      .compare-nav {
        flex-direction: column;
        gap: 8px;
      }

      .btn-tab {
        padding: 12px 14px;
        font-size: 0.88rem;
        text-align: center;
        min-height: 44px;
      }

      .timeline-steps {
        grid-template-columns: 1fr;
        gap: 8px;
      }

      .step-btn {
        padding: 12px;
        min-height: 44px;
      }

      .faq-question {
        padding: 14px 16px;
        font-size: 0.9rem;
        min-height: 44px;
      }

      .faq-answer {
        font-size: 0.84rem;
        line-height: 1.6;
      }

      .faq-item.open .faq-answer {
        padding: 0 16px 14px;
        max-height: 450px;
      }

      .pdf-modal-overlay {
        padding: 4px;
      }

      .pdf-modal-window {
        height: 98vh;
        border-radius: 10px;
      }

      .pdf-modal-header {
        padding: 10px 12px;
      }

      .pdf-modal-title {
        max-width: 48%;
        font-size: 0.84rem;
      }

      .btn-modal-action {
        padding: 8px 10px;
        font-size: 0.78rem;
        min-height: 36px;
        display: flex;
        align-items: center;
      }

      .btn-modal-close {
        padding: 8px 10px;
        font-size: 0.8rem;
        min-height: 36px;
      }

      .fab-contact {
        bottom: 16px;
        right: 16px;
        padding: 12px 18px;
        font-size: 0.84rem;
        min-height: 44px;
      }

      .toast {
        bottom: 74px;
        right: 14px;
        left: 14px;
        font-size: 0.82rem;
        padding: 12px 14px;
        justify-content: center;
      }
    }

    @media (max-width: 480px) {
      .bento-stats {
        grid-template-columns: 1fr;
      }
      .house-selector {
        grid-template-columns: 1fr;
      }
      .dossier-actions {
        flex-direction: column;
      }
      .btn-pdf {
        width: 100%;
      }
    }
  </style>"""

code = code.replace('  </style>', mobile_css)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dajing_interactive.py successfully injected with Ultra Mobile Adaptation CSS!")
