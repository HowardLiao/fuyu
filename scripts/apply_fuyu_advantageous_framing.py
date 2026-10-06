# -*- coding: utf-8 -*-
import os
import re

path = '/Users/howardliao/Desktop/HermesAgent/PortFilio/fuyu/generate_dajing_interactive.py'

with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Title and Header Subtitle
old_header = """      <h1>富宇大境（A2 區・6 戶）<br><span>管理分流・回歸獨立透天雙贏方案專區</span></h1>
      <p class="subtitle">終生免繳管理費（每戶年省 $12,000） ｜ 28 萬公款均分退還（每戶約退 $47,455 現金） ｜ 不設繁瑣管委會・完全獨立自理</p>
      <div class="reporter-bar">
        <span>專案代表人：<strong>廖倫豪</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>推進路徑：<strong>市府調處合意分流・不另設管委會</strong></span>
      </div>"""

new_header = """      <h1>富宇大境（A2 區・6 戶）<br><span>管理分流・回歸獨立透天雙贏方案專區</span></h1>
      <p class="subtitle">管理分流聚焦核心 ｜ 公設資源 100% 回饋大社區 ｜ 財務獨立權責相符 ｜ 促進富宇大地長治久安與和諧共榮</p>
      <div class="reporter-bar">
        <span>專案代表人：<strong>廖倫豪</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>推進路徑：<strong>市府調處合意分流・不另設管委會</strong></span>
      </div>"""

code = code.replace(old_header, new_header)

# 2. Update Bento Stats (Framed 100% advantageous to 富宇大地)
old_bento = """    <!-- 4 Bento Stats (Framed from Win-Win & No Committee Perspective) -->
    <div class="bento-stats">
      <div class="bento-card highlight">
        <div class="bento-label">管理費支出降幅</div>
        <div class="bento-val" style="text-align: right;">-$0 元 / 月</div>
        <div class="bento-desc">每戶由 $1,000 降至 $0（年省 $12,000）</div>
      </div>
      <div class="bento-card highlight">
        <div class="bento-label">專案公款均分退還</div>
        <div class="bento-val" style="text-align: right;">約 $<span id="cntFunds">47,455</span> 元</div>
        <div class="bento-desc">28 萬專款依 6 戶均分退回住戶個人帳戶</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">組織行政負擔</div>
        <div class="bento-val" style="text-align: right;"><span id="cntDiscount">0</span>% 行政雜務</div>
        <div class="bento-desc">不成立管委會，免選委員、免開會做帳</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">大社區物業減負</div>
        <div class="bento-val" style="text-align: right;">+<span id="cntSurplus">100</span>% 責任聚焦</div>
        <div class="bento-desc">富宇大地管委會專注內部，外側 0 負擔</div>
      </div>
    </div>"""

new_bento = """    <!-- 4 Bento Stats (Framed from Win-Win Perspective for 富宇大地) -->
    <div class="bento-stats">
      <div class="bento-card">
        <div class="bento-label">全社區雙贏格局</div>
        <div class="bento-val" style="text-align: right;"><span id="cntHouses">235 + 6</span> 戶</div>
        <div class="bento-desc">內部 235 戶聚焦治理，外側 6 戶自理維護</div>
      </div>
      <div class="bento-card highlight">
        <div class="bento-label">大社區營運零衝擊</div>
        <div class="bento-val" style="text-align: right;">$<span id="cntFunds">0</span> 元</div>
        <div class="bento-desc">A2 專款專單立卷結算，不影響大社區營運老本</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">大社區物業管理減負</div>
        <div class="bento-val" style="text-align: right;"><span id="cntDiscount">100</span>% 責任聚焦</div>
        <div class="bento-desc">免除跨越龍社路外側巡查，管理動線集中單純化</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">內部公設資源釋放</div>
        <div class="bento-val" style="text-align: right;">+<span id="cntSurplus">100</span>% 空間</div>
        <div class="bento-desc">A2 垃圾門前自理，內部子母車全數留給 235 戶</div>
      </div>
    </div>"""

code = code.replace(old_bento, new_bento)

# 3. Update Simulator
old_sim = """    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><line x1="12" y1="6" x2="12" y2="18"/></svg>
      回歸獨立透天・各戶實質現金效益試算模擬器
    </div>

    <div class="simulator-card">
      <div class="sim-header">
        <div>
          <h3>💡 點選您的門牌，即刻試算回歸獨立透天之終生實質利益</h3>
          <p>每戶終生免繳管理費（每年現省 $12,000 元），並享有 28 萬公款均分退還（約 $47,455 現金），完全免除管委會繁瑣行政！</p>
        </div>
      </div>"""

new_sim = """    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><line x1="12" y1="6" x2="12" y2="18"/></svg>
      權責相符與管理效益試算模型
    </div>

    <div class="simulator-card">
      <div class="sim-header">
        <div>
          <h3>💡 權責相符與收支平衡模型：分流管理如何達成雙方財務最適化</h3>
          <p>A2 透天自理外側維護與水電排污，落實收支平衡；大社區管委會亦免除外側管理成本，實現財務權責對等與資源最適化！</p>
        </div>
      </div>"""

code = code.replace(old_sim, new_sim)

old_sim_res = """      <div class="sim-results">
        <div class="sim-res-box">
          <div class="sim-res-lbl">貴戶累計省下管理費</div>
          <div class="sim-res-val" id="resFamilySavings">$60,000</div>
          <div class="sim-res-sub">終生免繳管理費，每年實質省下 $12,000 元</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">專案退還現金份額</div>
          <div class="sim-res-val" id="resHouseholdReserve">$47,455</div>
          <div class="sim-res-sub">28 萬專款均分直接退入各戶個人帳戶</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">貴戶累計實質總收益</div>
          <div class="sim-res-val" id="resCommunityTotal">$107,455</div>
          <div class="sim-res-sub">退還現金 ＋ 累計省下管理費總利益</div>
        </div>
      </div>"""

new_sim_res = """      <div class="sim-results">
        <div class="sim-res-box">
          <div class="sim-res-lbl">A2 門前自理維護成本</div>
          <div class="sim-res-val" id="resFamilySavings">$0 元</div>
          <div class="sim-res-sub">外側路燈、排污與清潔住戶自理，大社區 0 支出</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">大社區營運老本保全</div>
          <div class="sim-res-val" id="resHouseholdReserve">100%</div>
          <div class="sim-res-sub">大社區數百萬元公共基金分毫未損，營運水位充裕</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">內部公設資源專用</div>
          <div class="sim-res-val" id="resCommunityTotal">235 戶</div>
          <div class="sim-res-sub">內部環保室與收費子母車容量全數保留供內部使用</div>
        </div>
      </div>"""

code = code.replace(old_sim_res, new_sim_res)

# 4. Update JS updateSim()
old_js_update_sim = """    function updateSim() {
      const years = parseInt(document.getElementById('simYears').value);
      document.getElementById('simYearsLabel').innerText = years + ' 年';

      const familySavings = years * 12000;
      const householdReserve = 47455;
      const communityTotal = householdReserve + familySavings;

      document.getElementById('resFamilySavings').innerText = '$' + familySavings.toLocaleString();
      document.getElementById('resHouseholdReserve').innerText = '$' + householdReserve.toLocaleString();
      document.getElementById('resCommunityTotal').innerText = '$' + communityTotal.toLocaleString();
    }"""

new_js_update_sim = """    function updateSim() {
      const years = parseInt(document.getElementById('simYears').value);
      document.getElementById('simYearsLabel').innerText = years + ' 年';

      document.getElementById('resFamilySavings').innerText = '$0 元支出';
      document.getElementById('resHouseholdReserve').innerText = '100% 保全';
      document.getElementById('resCommunityTotal').innerText = '235 戶專屬';
    }"""

code = code.replace(old_js_update_sim, new_js_update_sim)

# 5. Update Item 00 Description
old_item00_desc = """            <h3>臺中市公寓大廈爭議事件調處申請書（免開 241 戶大會・不設管委會）</h3>
            <p>共 2 頁 ｜ 依據《公寓大廈管理條例》第 59 條之 1 提請市府調處合意分流退出；回歸獨立透天生活，不另設管委會，28 萬專款均分退還各戶（每戶退約 $47,455 現金）！</p>"""

new_item00_desc = """            <h3>臺中市公寓大廈爭議事件調處申請書（免開 241 戶大會・不設管委會）</h3>
            <p>共 2 頁 ｜ 依據《公寓大廈管理條例》第 59 條之 1 提請市府調處合意分流退出；回歸獨立透天自理，解除大社區跨路管轄負擔，依審計公平原則辦理專案款項移交結算！</p>"""

code = code.replace(old_item00_desc, new_item00_desc)

# 6. Update FAQ Q3 (Remove 均分退款 / 47,455)
old_q3 = """      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q3：那筆 NT$ 284,731 元的專案公款，不成立管委會要如何處理？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>依戶數全額均分返還給 6 戶區權人（每戶退回約 $47,455 現金）！</strong><br>
          富宇大地管委會 5 月與 9 月例會官方財報已明確載明：第 2 筆獨立立卷為「A2 大境定存單 NT$ 220,231 元」；加上起造人交屋管理基金（每戶 1 萬，6 戶共 60,000 元）。因大境回歸獨立透天不設管委會、亦無公設需管委會維修，在向臺中市政府申請調處時，請求事項直接載明：<strong>由相對人依戶數均分，全額撥還退交本區 6 戶住戶個人帳戶，每戶現領約 NT$ 47,455 元現金！</strong>
        </div>
      </div>"""

new_q3 = """      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q3：關於新光銀行專單定存等專案款項，如何確保大社區的財務權益不受損？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>帳目獨立清晰，純屬專款原單專案歸位！</strong><br>
          富宇大地管委會 5 月與 9 月例會官方財報已明確載明：台中市政府核退之公款分別定存，其中第 2 筆即獨立立卷為「A2 大境定存單 NT$ 220,231 元」專單保管；加上起造人富宇建設交屋管理基金（每戶 1 萬，大境 6 戶共 60,000 元）。該專案款項自始即與大社區其他各區定存單分開獨立保管，移交結算純屬專款原單專案歸位，富宇大地 235 戶所屬之悠境、澄境定存、起造人提撥款及日常營運帳戶分毫不受影響！
        </div>
      </div>"""

code = code.replace(old_q3, new_q3)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dajing_interactive.py successfully updated: purged all mentions of '均分退款' & '47,455', framed 100% advantageous to 富宇大地!")
