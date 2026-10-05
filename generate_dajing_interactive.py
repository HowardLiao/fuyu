# -*- coding: utf-8 -*-
import os

html_code = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>富宇大境（A2 區・6 戶）法定獨立分割卷宗與專案報告下載專區</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Noto+Serif+TC:wght@400;600;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-deep: #0B0F19;
      --bg-card: #151B28;
      --bg-card-hover: #1A2233;
      --gold-primary: #D4AF37;
      --gold-bright: #F59E0B;
      --gold-light: #E6D5AC;
      --gold-dark: #B8860B;
      --text-main: #FFFFFF;
      --text-muted: #94A3B8;
      --emerald: #10B981;
      --rose: #E11D48;
      --cyan: #38BDF8;
      --border-gold: rgba(212, 175, 55, 0.35);
      --border-subtle: rgba(255, 255, 255, 0.1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      padding-bottom: 80px;
      overflow-x: hidden;
    }

    /* Ambient Glow */
    .glow-top {
      position: absolute;
      top: -160px;
      left: 50%;
      transform: translateX(-50%);
      width: 900px;
      height: 450px;
      background: radial-gradient(circle, rgba(212, 175, 55, 0.15) 0%, rgba(11, 15, 25, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }

    .container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 1;
    }

    /* Header */
    header {
      padding: 44px 0 28px;
      text-align: center;
      border-bottom: 1px solid var(--border-gold);
    }

    .tag-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid var(--gold-primary);
      border-radius: 9999px;
      color: var(--gold-primary);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 14px;
    }

    h1 {
      font-family: 'Noto Serif TC', serif;
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--text-main);
      margin-bottom: 10px;
      line-height: 1.3;
    }

    h1 span { color: var(--gold-primary); }

    .subtitle {
      color: var(--gold-light);
      font-size: 1.02rem;
      font-weight: 500;
      max-width: 820px;
      margin: 0 auto 18px;
    }

    .reporter-bar {
      display: inline-flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 16px;
      font-size: 0.86rem;
      color: var(--text-muted);
      background: rgba(21, 27, 40, 0.6);
      padding: 8px 20px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
    }

    .reporter-bar strong { color: var(--gold-bright); }

    /* 4-Bento Summary Bar with Counter */
    .bento-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 14px;
      margin: 28px 0 36px;
    }

    .bento-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 18px 20px;
      position: relative;
      overflow: hidden;
      transition: all 0.25s ease;
    }

    .bento-card:hover {
      transform: translateY(-2px);
      border-color: var(--gold-primary);
    }

    .bento-card.highlight {
      border-color: var(--gold-primary);
      box-shadow: 0 0 25px rgba(212, 175, 55, 0.15);
    }

    .bento-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--gold-primary);
      opacity: 0.4;
    }

    .bento-card.highlight::before {
      opacity: 1;
      background: linear-gradient(to bottom, var(--gold-bright), var(--gold-primary));
    }

    .bento-label {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 500;
      margin-bottom: 3px;
      text-align: center;
    }

    .bento-val {
      font-family: 'Cinzel', serif;
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 2px;
      text-align: right;
    }

    .bento-card.highlight .bento-val { color: var(--gold-primary); text-align: right; }

    .bento-desc {
      font-size: 0.78rem;
      color: var(--text-muted);
      text-align: center;
    }

    /* Section Header */
    .section-title {
      font-family: 'Noto Serif TC', serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--gold-primary);
      margin: 38px 0 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .section-title::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--border-subtle);
    }

    /* Dossier List Card */
    .dossier-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .dossier-row {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 20px 24px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      transition: all 0.25s ease;
    }

    .dossier-row:hover {
      background: var(--bg-card-hover);
      border-color: var(--gold-primary);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
    }

    .dossier-row.spotlight {
      background: linear-gradient(135deg, rgba(21, 27, 40, 0.95) 0%, rgba(32, 42, 64, 0.95) 100%);
      border: 1.5px solid var(--gold-primary);
      box-shadow: 0 0 25px rgba(212, 175, 55, 0.18);
    }

    .dossier-meta {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      flex: 1;
      min-width: 280px;
    }

    .dossier-badge {
      background: rgba(212, 175, 55, 0.15);
      color: var(--gold-primary);
      font-weight: 700;
      font-size: 0.78rem;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid rgba(212, 175, 55, 0.3);
      white-space: nowrap;
      margin-top: 2px;
    }

    .dossier-badge.badge-primary {
      background: var(--gold-primary);
      color: #000;
      border-color: var(--gold-bright);
    }

    .dossier-texts h3 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 4px;
    }

    .dossier-texts p {
      font-size: 0.83rem;
      color: var(--text-muted);
      line-height: 1.45;
    }

    .dossier-actions {
      display: flex;
      gap: 10px;
      flex-wrap: nowrap;
    }

    .btn-pdf {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.84rem;
      font-weight: 600;
      padding: 9px 16px;
      border-radius: 6px;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s;
      white-space: nowrap;
      border: none;
    }

    .btn-preview {
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid var(--gold-primary);
      color: var(--gold-bright);
    }

    .btn-preview:hover {
      background: var(--gold-primary);
      color: #000;
      transform: translateY(-1px);
    }

    .btn-download {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
    }

    .btn-download:hover {
      background: rgba(212, 175, 55, 0.2);
      border-color: var(--gold-primary);
      color: var(--gold-primary);
    }

    /* ========================================================================= */
    /* INTERACTIVE MODULE 1: HOUSEHOLD SAVINGS SIMULATOR                         */
    /* ========================================================================= */
    .simulator-card {
      background: linear-gradient(135deg, rgba(21, 27, 40, 0.95) 0%, rgba(26, 36, 54, 0.95) 100%);
      border: 1.5px solid var(--gold-primary);
      border-radius: 16px;
      padding: 26px 30px;
      margin-top: 10px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .sim-header {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 14px;
    }

    .sim-header h3 {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--gold-bright);
    }

    .sim-header p {
      font-size: 0.82rem;
      color: var(--text-muted);
    }

    .sim-controls {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }

    @media (max-width: 768px) {
      .sim-controls { grid-template-columns: 1fr; }
    }

    .control-group label {
      display: block;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--gold-light);
      margin-bottom: 8px;
    }

    .house-selector {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .btn-house {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.82rem;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-house:hover, .btn-house.active {
      background: rgba(212, 175, 55, 0.25);
      border-color: var(--gold-primary);
      color: var(--gold-bright);
      font-weight: 700;
    }

    .slider-container {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    input[type=range] {
      flex: 1;
      accent-color: var(--gold-primary);
      cursor: pointer;
    }

    .slider-val {
      font-family: 'Cinzel', serif;
      font-weight: 700;
      color: var(--gold-bright);
      font-size: 1.15rem;
      min-width: 60px;
    }

    .sim-results {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      background: rgba(11, 15, 25, 0.6);
      border-radius: 10px;
      padding: 18px;
      border: 1px solid var(--border-subtle);
    }

    @media (max-width: 768px) {
      .sim-results { grid-template-columns: 1fr; }
    }

    .sim-res-box {
      border-right: 1px solid var(--border-subtle);
      padding: 6px 14px;
    }

    .sim-res-box:last-child { border-right: none; }

    .sim-res-lbl {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 4px;
      text-align: center;
    }

    .sim-res-val {
      font-family: 'Cinzel', serif;
      font-size: 1.6rem;
      font-weight: 900;
      color: var(--emerald);
      text-align: right;
    }

    .sim-res-sub {
      font-size: 0.74rem;
      color: var(--text-muted);
      margin-top: 2px;
      text-align: center;
    }

    /* ========================================================================= */
    /* INTERACTIVE MODULE 2: BEFORE VS AFTER SWITCHER                            */
    /* ========================================================================= */
    .compare-nav {
      display: flex;
      gap: 10px;
      margin-bottom: 16px;
    }

    .btn-tab {
      flex: 1;
      padding: 10px 16px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      border: 1px solid var(--border-subtle);
      background: var(--bg-card);
      color: var(--text-muted);
      text-align: center;
    }

    .btn-tab.active-tab-before {
      background: rgba(225, 29, 72, 0.15);
      border-color: var(--rose);
      color: #fda4af;
    }

    .btn-tab.active-tab-after {
      background: rgba(16, 185, 129, 0.15);
      border-color: var(--emerald);
      color: #6ee7b7;
    }

    .compare-content {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 22px;
    }

    .compare-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
    }

    .cmp-card {
      background: rgba(11, 15, 25, 0.5);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 16px;
      position: relative;
    }

    .cmp-card.bad { border-left: 4px solid var(--rose); }
    .cmp-card.good { border-left: 4px solid var(--emerald); }

    .cmp-topic {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
    }

    .cmp-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 4px;
    }

    .cmp-desc {
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.45;
    }

    /* ========================================================================= */
    /* INTERACTIVE MODULE 3: 5-STAGE SOP TIMELINE TRACKER                        */
    /* ========================================================================= */
    .timeline-steps {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px;
      margin-bottom: 16px;
    }

    @media (max-width: 860px) {
      .timeline-steps { grid-template-columns: 1fr; }
    }

    .step-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 14px 10px;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .step-btn:hover { border-color: var(--gold-primary); }

    .step-btn.active {
      background: rgba(212, 175, 55, 0.15);
      border-color: var(--gold-primary);
      box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }

    .step-num {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--gold-primary);
      margin-bottom: 2px;
    }

    .step-name {
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .step-detail-card {
      background: var(--bg-card);
      border: 1px solid var(--border-gold);
      border-radius: 12px;
      padding: 22px 26px;
      margin-bottom: 20px;
    }

    .step-det-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 10px;
    }

    .step-det-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--gold-bright);
    }

    .step-det-badge {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid var(--emerald);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
    }

    .step-det-body {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* ========================================================================= */
    /* INTERACTIVE MODULE 4: ACCORDION FAQ                                       */
    /* ========================================================================= */
    .faq-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .faq-item {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      overflow: hidden;
      transition: all 0.2s;
    }

    .faq-item:hover { border-color: var(--gold-primary); }

    .faq-question {
      padding: 16px 20px;
      cursor: pointer;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
    }

    .faq-icon {
      font-size: 1.1rem;
      color: var(--gold-primary);
      transition: transform 0.25s;
    }

    .faq-item.open .faq-icon {
      transform: rotate(45deg);
    }

    .faq-answer {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease-out;
      background: rgba(11, 15, 25, 0.4);
      padding: 0 20px;
      font-size: 0.86rem;
      color: var(--text-muted);
      line-height: 1.6;
    }

    .faq-item.open .faq-answer {
      padding: 0 20px 18px;
      max-height: 250px;
    }

    /* ========================================================================= */
    /* INTERACTIVE MODULE 5: IN-PAGE PDF MODAL VIEWER                            */
    /* ========================================================================= */
    .pdf-modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .pdf-modal-overlay.active { display: flex; }

    .pdf-modal-window {
      background: var(--bg-deep);
      border: 1.5px solid var(--gold-primary);
      border-radius: 16px;
      width: 100%;
      max-width: 1000px;
      height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
    }

    .pdf-modal-header {
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-gold);
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .pdf-modal-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--gold-light);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 70%;
    }

    .pdf-modal-btns {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn-modal-action {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s;
    }

    .btn-modal-action:hover {
      background: var(--gold-primary);
      color: #000;
    }

    .btn-modal-close {
      background: rgba(225, 29, 72, 0.2);
      border: 1px solid var(--rose);
      color: #fda4af;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
    }

    .btn-modal-close:hover {
      background: var(--rose);
      color: #fff;
    }

    .pdf-modal-body {
      flex: 1;
      background: #2D3748;
      position: relative;
    }

    .pdf-modal-body iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    /* Floating Contact Action Button (FAB) */
    .fab-contact {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: linear-gradient(135deg, var(--gold-bright), var(--gold-dark));
      color: #000;
      padding: 12px 20px;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.88rem;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 8px 25px rgba(212, 175, 55, 0.45);
      cursor: pointer;
      z-index: 1000;
      border: none;
      transition: all 0.25s ease;
    }

    .fab-contact:hover {
      transform: translateY(-3px) scale(1.03);
      box-shadow: 0 12px 30px rgba(212, 175, 55, 0.6);
    }

    /* Toast Notification */
    .toast {
      position: fixed;
      bottom: 84px;
      right: 24px;
      background: var(--bg-card);
      border: 1px solid var(--gold-primary);
      color: var(--text-main);
      padding: 12px 20px;
      border-radius: 8px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
      font-size: 0.85rem;
      z-index: 1001;
      display: none;
      align-items: center;
      gap: 8px;
    }

    .toast.show { display: flex; animation: fadeIn 0.3s ease; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .notice-box {
      margin-top: 36px;
      background: rgba(21, 27, 40, 0.5);
      border: 1px dashed var(--gold-dark);
      border-radius: 10px;
      padding: 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.6;
    }

    .notice-box strong { color: var(--gold-light); }

    .back-nav {
      margin-top: 28px;
      text-align: center;
    }

    .back-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: var(--gold-primary);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 600;
      transition: color 0.2s;
    }

    .back-link:hover {
      color: var(--gold-bright);
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="glow-top"></div>

  <div class="container">
    <!-- Header -->
    <header>
      <div class="tag-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        《公寓大廈管理條例》第 53 條、第 31 條管理分流程序 ｜ 專案編號：FY-SPLIT-2026-A2
      </div>
      <h1>富宇大境（A2 區・6 戶）<br><span>法定獨立分割卷宗與專案報告下載專區</span></h1>
      <p class="subtitle">台中市沙鹿區龍社路 593～603 號全體住戶專屬 ｜ 迎回 28 萬自有公款 ｜ 管理費自 $1,000 大降至 $400</p>
      <div class="reporter-bar">
        <span>專案受託召集人：<strong>廖倫豪</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>推進程序：<strong>6 戶連署提請大會審議</strong></span>
      </div>
    </header>

    <!-- 4 Bento Stats -->
    <div class="bento-stats">
      <div class="bento-card">
        <div class="bento-label">專案標的建物</div>
        <div class="bento-val" style="text-align: right;"><span id="cntHouses">6</span> 戶別墅</div>
        <div class="bento-desc">龍社路 593～603 號全體住戶</div>
      </div>
      <div class="bento-card highlight">
        <div class="bento-label">依法迎回自有公款</div>
        <div class="bento-val" style="text-align: right;">$<span id="cntFunds">284,731</span></div>
        <div class="bento-desc">定存 22 萬 ＋ 交屋基金 6 萬 ＋ 結餘</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">每月管理費負擔</div>
        <div class="bento-val" style="text-align: right;">-<span id="cntDiscount">60</span>%</div>
        <div class="bento-desc">每戶由 $1,000 降至 $400（年省 $7,200）</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">年度常態滾存結餘</div>
        <div class="bento-val" style="text-align: right;">+$<span id="cntSurplus">21,600</span></div>
        <div class="bento-desc">扣除門前路燈公電後，老本越滾越多</div>
      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- INTERACTIVE 1: HOUSEHOLD SAVINGS SIMULATOR                              -->
    <!-- ======================================================================= -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><line x1="12" y1="6" x2="12" y2="18"/></svg>
      大境住戶專屬・自主財務效益試算模擬器
    </div>

    <div class="simulator-card">
      <div class="sim-header">
        <div>
          <h3>💡 點選您的門牌，即刻試算分家後的家庭與聚落實質利益</h3>
          <p>每戶每月自 $1,000 調降為 $400，一年實質省下 $7,200 元；且依法享有專屬定存老本儲備！</p>
        </div>
      </div>

      <div class="sim-controls">
        <div class="control-group">
          <label>① 選擇您的戶別門牌：</label>
          <div class="house-selector">
            <button class="btn-house" onclick="selectHouse('593', this)">龍社路 593 號</button>
            <button class="btn-house active" onclick="selectHouse('595', this)">595 號 (A17 廖博士)</button>
            <button class="btn-house" onclick="selectHouse('597', this)">龍社路 597 號</button>
            <button class="btn-house" onclick="selectHouse('599', this)">龍社路 599 號</button>
            <button class="btn-house" onclick="selectHouse('601', this)">龍社路 601 號</button>
            <button class="btn-house" onclick="selectHouse('603', this)">龍社路 603 號</button>
          </div>
        </div>

        <div class="control-group">
          <label>② 預覽未來年限：</label>
          <div class="slider-container">
            <input type="range" id="simYears" min="1" max="10" value="5" oninput="updateSim()">
            <span class="slider-val" id="simYearsLabel">5 年</span>
          </div>
        </div>
      </div>

      <div class="sim-results">
        <div class="sim-res-box">
          <div class="sim-res-lbl">貴戶累計實質省下管理費</div>
          <div class="sim-res-val" id="resFamilySavings">$36,000</div>
          <div class="sim-res-sub">每戶每年實質節省 $7,200 元管理費負擔</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">貴戶享有之自有定存儲備份額</div>
          <div class="sim-res-val" id="resHouseholdReserve">$47,455</div>
          <div class="sim-res-sub">迎回 28 萬公款均分份額，生息有據</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">大境 6 戶全區累計安全老本</div>
          <div class="sim-res-val" id="resCommunityTotal">$392,731</div>
          <div class="sim-res-sub">迎回 28 萬 ＋ 每年淨結餘 $21,600</div>
        </div>
      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- INTERACTIVE 2: BEFORE VS AFTER COMPARISON SWITCHER                      -->
    <!-- ======================================================================= -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/></svg>
      現況「逆向補貼」困境 vs 獨立「自主掌權」對比矩陣
    </div>

    <div class="compare-nav">
      <div id="tabBefore" class="btn-tab active-tab-before" onclick="switchCompare('before')">
        ⚠️ 現況困境：被動合併大社區（241 戶體系）
      </div>
      <div id="tabAfter" class="btn-tab" onclick="switchCompare('after')">
        ✨ 破局方案：依法獨立分割（大境 6 戶自治）
      </div>
    </div>

    <div class="compare-content" id="compareContent">
      <!-- Injected by JavaScript -->
    </div>

    <!-- ======================================================================= -->
    <!-- INTERACTIVE 3: 5-STAGE IMPLEMENTATION SOP TIMELINE                      -->
    <!-- ======================================================================= -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      五大推進階段與標準作業程序（SOP）互動進度看板
    </div>

    <div class="timeline-steps">
      <div class="step-btn active" onclick="selectStep(1, this)">
        <div class="step-num">階段 01</div>
        <div class="step-name">內部連署凝聚</div>
      </div>
      <div class="step-btn" onclick="selectStep(2, this)">
        <div class="step-num">階段 02</div>
        <div class="step-name">管委會正式提案</div>
      </div>
      <div class="step-btn" onclick="selectStep(3, this)">
        <div class="step-num">階段 03</div>
        <div class="step-name">清算協議簽署</div>
      </div>
      <div class="step-btn" onclick="selectStep(4, this)">
        <div class="step-num">階段 04</div>
        <div class="step-name">龍井區公所報備</div>
      </div>
      <div class="step-btn" onclick="selectStep(5, this)">
        <div class="step-num">階段 05</div>
        <div class="step-name">銀行開戶接收</div>
      </div>
    </div>

    <div class="step-detail-card" id="stepDetailCard">
      <!-- Injected by JS -->
    </div>

    <!-- ======================================================================= -->
    <!-- PRESENTATION SPOTLIGHT (PDF ONLY)                                       -->
    <!-- ======================================================================= -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
      高階專案報告簡報
    </div>

    <div class="dossier-list">
      <div class="dossier-row spotlight">
        <div class="dossier-meta">
          <div class="dossier-badge badge-primary">重點簡報</div>
          <div class="dossier-texts">
            <h3>富宇大境 A2 獨立分區管理專案報告（提案說明與協商建議）</h3>
            <p>16 頁全彩高解析高管審計簡報 ｜ 完整收錄法規程序換軌（第 53/31 條）、雙贏效益、28 萬資產移交協商與合規承諾。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <button class="btn-pdf btn-preview" onclick="openPdfModal('富宇大境A2獨立分區管理專案報告.pdf', '富宇大境 A2 獨立分區管理專案報告（16 頁高階簡報）')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </button>
          <a href="富宇大境A2獨立分區管理專案報告.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
          <a href="富宇大境A2獨立分區管理專案報告.pptx" class="btn-pdf" style="background: rgba(212, 175, 55, 0.15); color: #D4AF37; border: 1px solid rgba(212, 175, 55, 0.4);" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            下載 PPTX
          </a>
        </div>
      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- SECTION: 6 LEGAL DOSSIERS (PDF ONLY)                                    -->
    <!-- ======================================================================= -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
      全套法定公文卷宗與全權委任授權書（PDF 印刷檔）
    </div>

    <div class="dossier-list">
      <!-- Item 0: 全權委任授權書 -->
      <div class="dossier-row spotlight" style="border-color: var(--emerald);">
        <div class="dossier-meta">
          <div class="dossier-badge" style="background: rgba(16, 185, 129, 0.2); color: #10B981; border: 1px solid #10B981;">法定授權</div>
          <div class="dossier-texts">
            <h3>富宇大境（A2 區）全體區分所有權人獨立分割全權委任授權書</h3>
            <p>共 1 頁 ｜ 依據《民法》第 528 條委任契約，全體 6 戶專案全權委任 廖倫豪 辦理提案、交涉、迎回 28 萬公款與公所報備；載明排除任何不動產私權處分，保障全體委任人權益。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <button class="btn-pdf btn-preview" onclick="openPdfModal('富宇大境A2獨立分割全權委任授權書.pdf', '法定全權委任授權書：全體 6 戶專案委任 廖倫豪')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </button>
          <a href="富宇大境A2獨立分割全權委任授權書.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 1: 主件 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">法定主件</div>
          <div class="dossier-texts">
            <h3>富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書</h3>
            <p>共 2 頁 ｜ 含主旨說明辦法、管委會提案條款、管理費代收提存共管及第二頁 6 戶親筆連署名冊簽章冊。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <button class="btn-pdf btn-preview" onclick="openPdfModal('富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書.pdf', '法定主件：提案申請書暨全體連署同意書')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </button>
          <a href="富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 2: 附件一 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件一</div>
          <div class="dossier-texts">
            <h3>附件一：法定獨立分割可行性研究報告書</h3>
            <p>共 7 頁 ｜ 援引內政部 86/90 號權威函釋、三大核心王牌、28 萬公款清算試算、五大階段 SOP 及 5% 遲延利息清算協議書範本。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <button class="btn-pdf btn-preview" onclick="openPdfModal('附件一_法定獨立分割可行性研究報告書.pdf', '附件一：法定獨立分割可行性研究報告書')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </button>
          <a href="附件一_法定獨立分割可行性研究報告書.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 3: 附件二 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件二</div>
          <div class="dossier-texts">
            <h3>附件二：富宇大地全區地籍圖及出入證明</h3>
            <p>共 1 頁 ｜ 台中市地政事務所官方地籍套繪圖，白紙黑字證明 A2 大境 6 戶臨接龍社路公有計畫道路獨立出入，無袋地爭議。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <button class="btn-pdf btn-preview" onclick="openPdfModal('附件二_富宇大地全區地籍圖及出入證明.pdf', '附件二：富宇大地全區地籍圖及出入證明')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </button>
          <a href="附件二_富宇大地全區地籍圖及出入證明.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 4: 附件三 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件三</div>
          <div class="dossier-texts">
            <h3>附件三：會議記錄及新光銀行 A2 定存財報存根</h3>
            <p>共 1 頁 ｜ 檢附 115 年 5 月與 9 月例會官方財報，佐證新光銀行定存單第 2 筆獨立立卷「A2 大境定存單 $220,231 元」之專款產權憑證。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <button class="btn-pdf btn-preview" onclick="openPdfModal('附件三_會議記錄及新光銀行A2定存財報存根.pdf', '附件三：會議記錄及新光銀行 A2 定存財報存根')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </button>
          <a href="附件三_會議記錄及新光銀行A2定存財報存根.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 5: 附件四 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件四</div>
          <div class="dossier-texts">
            <h3>附件四：富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書</h3>
            <p>共 1 頁 ｜ 切結水電排污完全物理獨立、自願放棄大社區收費子母車、門前等免費公車型垃圾車，徹底瓦解「公設不可分」之藉口。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <button class="btn-pdf btn-preview" onclick="openPdfModal('附件四_富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書.pdf', '附件四：共用設施無依賴切結與生活垃圾自行清運承諾書')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </button>
          <a href="附件四_富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- INTERACTIVE 4: NEIGHBOR FAQ ACCORDION                                   -->
    <!-- ======================================================================= -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      鄰居最關心的常見法律與財務問答（點擊展開）
    </div>

    <div class="faq-list">
      <div class="faq-item open">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q1：我們大境才 6 戶透天，在法律程序上如何合法獨立成立管委會？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全合於法定程序！</strong>依據《公寓大廈管理條例》第 53 條規定，多數各自獨立使用之建築物，如設施使用無整體不可分性，準用本條例管理。<br>
          大境 6 戶出入臨公有計畫道路龍社路、水電排污自理、生活廢棄物自行等免費清潔隊，客觀上具備完整獨立性。實務上將依《條例》第 31 條特別決議程序，提請富宇大地全體區分所有權人會議審議變更規約第二條管理範圍（排除 A2），大會通過後即可向主管機關區公所申辦變更報備與大境獨立報備！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q2：這筆 NT$ 284,731 元的公款，如何向大社區辦理移交撥還？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>款項來源清楚，依審計公平原則專案協商撥還！</strong>管委會 5 月與 9 月例會官方財報已明確將台中市政府核退之公款獨立開立「A2 大境定存單 NT$ 220,231 元」專單保管；加上起造人富宇建設交屋管理基金（每戶 1 萬，大境 6 戶共 60,000 元）。本區建請大會同意於合意分割後專案撥還移交至大境公庫專戶專管專用。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q3：獨立之後管理費降到 $400，真的夠用嗎？路燈電費會不會付不出來？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>綽綽有餘，甚至年年倒存老本！</strong>大境 6 戶是透天別墅，出門直接是龍社路，我們既沒有電梯維護費、也沒有內部巷道保全，更不用負擔每個月 4.8 萬元的垃圾子母車費用。6 戶月收 $2,400，扣除門前路燈與公電約 $400、行政雜支 $200，<strong>每月常態結餘高達 $1,800，一年還能穩定存下 $21,600 元儲備金</strong>！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q4：我們不使用大社區內部子母車，平日倒垃圾會不會變得很麻煩？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全不會，現況大家本來就是等門前垃圾車！</strong>龍社路本就是台中市環保局定時定點免費清運路線。大境 6 戶出門即投遞，簽訂《切結書》放棄內部子母車，不僅不影響生活，反而替每戶每年省下分攤內部垃圾清運費的冤枉錢！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q5：我們住戶簽了連署書之後，需要自己去跟管委會或公所交涉跑流程嗎？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全不需要！大家只需安心簽名，全權由召集人代辦。</strong>受託召集人 廖倫豪（A17 龍社路 595 號）承諾代表全體 6 戶出席管委會例會提案、與主委簽署分割協議書，並親赴台中市龍井區公所辦理變更備查與新光銀行開戶接收，大家免除一切繁瑣公務負擔！
        </div>
      </div>
    </div>

    <!-- Notice Footer Box -->
    <div class="notice-box">
      <strong>【法定連署與大會提案說明】</strong><br>
      依據《公寓大廈管理條例》第 53 條與第 31 條，本案由 <strong>A2 大境 6 戶（沙鹿區龍社路 593～603 號）全體區權人 100% 簽署連署書與授權書</strong>，正式向管委會提案並協助排入區分所有權人會議審議。<br>
      紙本提案申請書與全權委任授權書正本備於受託召集人 廖倫豪（龍社路 595 號 A17）處，隨時歡迎各位鄰居翻閱完整原件並簽章！
    </div>

    <div class="back-nav">
      <a href="index.html" class="back-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
        返回富宇大地社區線上戰情室總覽
      </a>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- MODAL: IN-PAGE PDF VIEWER                                                 -->
  <!-- ========================================================================= -->
  <div class="pdf-modal-overlay" id="pdfModal">
    <div class="pdf-modal-window">
      <div class="pdf-modal-header">
        <div class="pdf-modal-title" id="pdfModalTitle">PDF 文件預覽</div>
        <div class="pdf-modal-btns">
          <a href="#" id="modalNewTabBtn" class="btn-modal-action" target="_blank">另開新分頁</a>
          <a href="#" id="modalDownloadBtn" class="btn-modal-action" download>下載 PDF</a>
          <button class="btn-modal-close" onclick="closePdfModal()">關閉 ✕</button>
        </div>
      </div>
      <div class="pdf-modal-body">
        <iframe id="pdfFrame" src=""></iframe>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- FLOATING ACTION BUTTON & TOAST                                            -->
  <!-- ========================================================================= -->
  <button class="fab-contact" onclick="openContactModal()">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    聯繫召集人 廖博士
  </button>

  <div class="toast" id="toastBox">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
    <span id="toastMsg">已複製資訊至剪貼簿！</span>
  </div>

  <!-- SCRIPT -->
  <script>
    // 1. PDF Modal Viewer
    function openPdfModal(pdfUrl, title) {
      document.getElementById('pdfModalTitle').innerText = title;
      document.getElementById('pdfFrame').src = pdfUrl;
      document.getElementById('modalNewTabBtn').href = pdfUrl;
      document.getElementById('modalDownloadBtn').href = pdfUrl;
      document.getElementById('pdfModal').classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closePdfModal() {
      document.getElementById('pdfModal').classList.remove('active');
      document.getElementById('pdfFrame').src = '';
      document.body.style.overflow = 'auto';
    }

    // Close on overlay click
    document.getElementById('pdfModal').addEventListener('click', function(e) {
      if (e.target === this) closePdfModal();
    });

    // 2. Household Simulator
    let selectedHouseNum = '595';
    function selectHouse(num, btn) {
      selectedHouseNum = num;
      document.querySelectorAll('.btn-house').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      updateSim();
    }

    function updateSim() {
      const years = parseInt(document.getElementById('simYears').value);
      document.getElementById('simYearsLabel').innerText = years + ' 年';

      const familySavings = years * 7200;
      const householdReserve = Math.round(284731 / 6);
      const communityTotal = 284731 + (years * 21600);

      document.getElementById('resFamilySavings').innerText = '$' + familySavings.toLocaleString();
      document.getElementById('resHouseholdReserve').innerText = '$' + householdReserve.toLocaleString();
      document.getElementById('resCommunityTotal').innerText = '$' + communityTotal.toLocaleString();
    }
    updateSim();

    // 3. Before vs After Compare Switcher
    const compareData = {
      before: [
        { topic: '話語權地位', title: '邊緣化 2.49% 弱勢', desc: '全社區 241 戶，大境僅 6 戶，在 12~18 席管委會中無實質席次，預算動支完全被內部大聚落主導。' },
        { topic: '管理費負擔', title: '每戶每年繳 12,000 元', desc: '6 戶每年繳交 7.2 萬元管理費，全數流入大水庫補貼內部深處巷道與管制作業，門前幾無回饋。' },
        { topic: '垃圾清運費', title: '替他人分攤 4.8 萬/月', desc: '大境位在龍社路自行等公車型垃圾車，卻月月幫內部 235 戶分攤每週兩次 6 桶之收費子母車清運費。' },
        { topic: '物業經理配置', title: '深居貨櫃屋服務歸零', desc: '物業經理（$70,350/月）常駐於內部貨櫃屋，大境郵件信件郵差直送門前，實質服務趨近於零。' }
      ],
      after: [
        { topic: '話語權地位', title: '100% 獨立自主掌權', desc: '成立專管委員會，6 戶全體均為主事核心，每筆預算動支 100% 自主決策，無需看他人臉色。' },
        { topic: '管理費負擔', title: '大幅減輕 60% 至 $400/月', desc: '每戶每年現省 7,200 元；6 戶年收 $28,800 扣除路燈公電後，每年還能穩健存入 $21,600 儲備金！' },
        { topic: '垃圾清運費', title: '費用 NT$ 0 元完全免花費', desc: '出門直接等候台中市環保局免費公有垃圾車，簽署放棄使用切結書，不再幫大社區付一毛清運費！' },
        { topic: '公款儲備掌控', title: '一次迎回 NT$ 284,731 元', desc: '新光銀行 A2 定存單 22 萬與富宇交屋基金 6 萬全額移交大境公庫，平均每戶享有約 4.75 萬老本儲備。' }
      ]
    };

    function renderCompare(mode) {
      const list = compareData[mode];
      const isBad = (mode === 'before');
      let html = '<div class="compare-grid">';
      list.forEach(item => {
        html += `
          <div class="cmp-card ${isBad ? 'bad' : 'good'}" style="text-align: center;">
            <div class="cmp-topic" style="display: flex; justify-content: space-between; align-items: center;">
              <span>${item.topic}</span>
              <span style="text-align: right; font-weight: 700;">${isBad ? '⚠️ 困境' : '✅ 破局'}</span>
            </div>
            <div class="cmp-title" style="text-align: center; margin: 8px 0 6px 0;">${item.title}</div>
            <div class="cmp-desc" style="text-align: center;">${item.desc}</div>
          </div>
        `;
      });
      html += '</div>';
      document.getElementById('compareContent').innerHTML = html;
    }

    function switchCompare(mode) {
      if (mode === 'before') {
        document.getElementById('tabBefore').className = 'btn-tab active-tab-before';
        document.getElementById('tabAfter').className = 'btn-tab';
      } else {
        document.getElementById('tabBefore').className = 'btn-tab';
        document.getElementById('tabAfter').className = 'btn-tab active-tab-after';
      }
      renderCompare(mode);
    }
    renderCompare('before');

    // 4. 5-Stage SOP Interactive Timeline
    const stepsData = {
      1: {
        title: '階段一：A2 大境內部 100% 連署凝聚（共識準備）',
        badge: '進行中・現正發動',
        desc: '• 召開大境 6 戶客廳會，確認共同推選 廖倫豪 為受託召集人兼法定代理人。<br>• 簽署《正式提案申請書》與《專案全權委任授權書》，取得 6 戶區權人 100% 親筆簽章。<br>• 備齊地籍圖、會議記錄與切結書，完成全套法定卷宗立案。'
      },
      2: {
        title: '階段二：向富宇大地管委會正式提案（溝通與審議）',
        badge: '法定公文正式呈送',
        desc: '• 召集人以正式公文向富宇大地第二屆管委會例會提案。<br>• 採取雙贏溝通策略：證明大境定存 22 萬原本就是獨立存單，分割不會影響大社區 760 萬老本；大境退出子母車使用，大社區垃圾容量更充裕；物業經理減少巡護負擔。'
      },
      3: {
        title: '階段三：移交協議簽署與大境管委會成立（法律生效）',
        badge: '法律契約確立',
        desc: '• 管委會例會確認獨立分割，雙方簽署《資產分割清算協議書》，約定新光銀行定存與交屋基金移交條款與 5% 遲延利息保證。<br>• 大境 6 戶依法成立「富宇大境管理委員會」，訂立住戶自治規約，推選幹部。'
      },
      4: {
        title: '階段四：主管機關（台中市龍井區公所）行政報備（法人地位）',
        badge: '官方核發統編',
        desc: '• 檢具全體區權人簽章公文、修正規約、分割協議書、地籍圖向龍井區公所申辦變更備查。<br>• 同步申辦富宇大地變更為 235 戶，大境核發獨立 6 戶報備證明並取得新統一編號。'
      },
      5: {
        title: '階段五：新光銀行開戶接收、資產撥付與外包切割（獨立啟航）',
        badge: '公款撥付・自主營運',
        desc: '• 持公所公文與印鑑至新光銀行沙鹿分行開立「富宇大境管理委員會」專戶。<br>• 28 萬餘元公款一次性匯撥入專戶，終止大社區外包合約連帶責任，正式啟動每月 $400 自主治理！'
      }
    };

    function selectStep(num, btn) {
      document.querySelectorAll('.step-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const data = stepsData[num];
      document.getElementById('stepDetailCard').innerHTML = `
        <div class="step-det-head">
          <div class="step-det-title">${data.title}</div>
          <div class="step-det-badge">${data.badge}</div>
        </div>
        <div class="step-det-body">${data.desc}</div>
      `;
    }
    selectStep(1, document.querySelector('.step-btn.active'));

    // 5. FAQ Accordion Toggle
    function toggleFaq(el) {
      const item = el.parentElement;
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    }

    // 6. Contact Modal / Toast
    function openContactModal() {
      const contactInfo = "受託召集人：廖倫豪 博士 (Howard Liao Ph.D.)\\n門牌：台中市沙鹿區龍社路 595 號 (A17)\\nEmail: liao.howard@gmail.com";
      navigator.clipboard.writeText("廖倫豪 博士 (龍社路 595 號 A17) - liao.howard@gmail.com").then(() => {
        showToast("已複製召集人 廖博士 聯絡資訊至剪貼簿！隨時歡迎來客廳翻閱正本公文！");
      }).catch(() => {
        alert(contactInfo);
      });
    }

    function showToast(msg) {
      const t = document.getElementById('toastBox');
      document.getElementById('toastMsg').innerText = msg;
      t.classList.add('show');
      setTimeout(() => { t.classList.remove('show'); }, 3800);
    }
  </script>
</body>
</html>
"""

out_path = '/Users/howardliao/Desktop/HermesAgent/PortFilio/fuyu/dajing.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_code)

print(f"Generated ultimate interactive Dajing portal: {out_path} ({os.path.getsize(out_path)} bytes)")
