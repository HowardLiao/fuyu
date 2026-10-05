# -*- coding: utf-8 -*-
import os
import re

path = '/Users/howardliao/Desktop/HermesAgent/PortFilio/fuyu/generate_dajing_interactive.py'

with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Title and Header
code = re.sub(
    r'<title>.*?</title>',
    '<title>富宇大境（A2 區・6 戶）管理分流・回歸獨立透天雙贏方案專區</title>',
    code
)

old_header = """      <h1>富宇大境（A2 區・6 戶）<br><span>管理分流與資源重整雙贏方案下載專區</span></h1>
      <p class="subtitle">權責相符 ｜ 聚焦治理 ｜ 資源減負 ｜ 促進富宇大地全區長治久安與雙贏互惠</p>
      <div class="reporter-bar">
        <span>提案代表人：<strong>廖倫豪</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>推進路徑：<strong>提請區分所有權人會議特別決議</strong></span>
      </div>"""

new_header = """      <h1>富宇大境（A2 區・6 戶）<br><span>管理分流・回歸獨立透天雙贏方案專區</span></h1>
      <p class="subtitle">終生免繳管理費（每戶年省 $12,000） ｜ 28 萬公款均分退還（每戶約退 $47,455 現金） ｜ 不設繁瑣管委會・完全獨立自理</p>
      <div class="reporter-bar">
        <span>專案代表人：<strong>廖倫豪</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>推進路徑：<strong>市府調處合意分流・不另設管委會</strong></span>
      </div>"""

code = code.replace(old_header, new_header)

# 2. Update Bento Stats
old_bento = """    <!-- 4 Bento Stats (Framed from Win-Win Perspective) -->
    <div class="bento-stats">
      <div class="bento-card">
        <div class="bento-label">全社區雙贏格局</div>
        <div class="bento-val" style="text-align: right;"><span id="cntHouses">235 + 6</span> 戶</div>
        <div class="bento-desc">內部 235 戶聚焦治理，外側 6 戶自理維護</div>
      </div>
      <div class="bento-card highlight">
        <div class="bento-label">大社區營運零衝擊</div>
        <div class="bento-val" style="text-align: right;">$<span id="cntFunds">0</span> 元</div>
        <div class="bento-desc">A2 專款專單立卷移交，不影響大社區營運老本</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">大社區物業管理減負</div>
        <div class="bento-val" style="text-align: right;"><span id="cntDiscount">100</span>% 責任聚焦</div>
        <div class="bento-desc">免除跨越龍社路外側巡查，管理範圍單純化</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">內部公設資源釋放</div>
        <div class="bento-val" style="text-align: right;">+<span id="cntSurplus">100</span>% 空間</div>
        <div class="bento-desc">A2 垃圾門前自理，內部子母車全數留給 235 戶</div>
      </div>
    </div>"""

new_bento = """    <!-- 4 Bento Stats (Framed from Win-Win & No Committee Perspective) -->
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

code = code.replace(old_bento, new_bento)

# 3. Update Simulator
old_sim = """    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><line x1="12" y1="6" x2="12" y2="18"/></svg>
      權責相符與管理效益試算模型
    </div>

    <div class="simulator-card">
      <div class="sim-header">
        <div>
          <h3>💡 權責相符與收支平衡模型：分流管理如何達成雙方財務最適化</h3>
          <p>A2 透天自理外側維護與水電排污，落實收支平衡；大社區管委會亦免除外側管理成本，實現財務權責對等！</p>
        </div>
      </div>"""

new_sim = """    <div class="section-title">
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

code = code.replace(old_sim, new_sim)

old_sim_res = """      <div class="sim-results">
        <div class="sim-res-box">
          <div class="sim-res-lbl">A2 戶均收支平衡調整</div>
          <div class="sim-res-val" id="resFamilySavings">$36,000</div>
          <div class="sim-res-sub">按實際使用服務計費，免除未享用項目之超額分攤</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">A2 專款專戶專管儲備金</div>
          <div class="sim-res-val" id="resHouseholdReserve">$47,455</div>
          <div class="sim-res-sub">大境管委會專戶專款專管，自負門前維護盈虧</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">A2 獨立運作儲備規模</div>
          <div class="sim-res-val" id="resCommunityTotal">$392,731</div>
          <div class="sim-res-sub">專案移交原款與自律結餘，完全獨立自籌</div>
        </div>
      </div>"""

new_sim_res = """      <div class="sim-results">
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

code = code.replace(old_sim_res, new_sim_res)

# 4. Update JS updateSim()
old_js_update_sim = """    function updateSim() {
      const years = parseInt(document.getElementById('simYears').value);
      document.getElementById('simYearsLabel').innerText = years + ' 年';

      const familySavings = years * 7200;
      const householdReserve = Math.round(284731 / 6);
      const communityTotal = 284731 + (years * 21600);

      document.getElementById('resFamilySavings').innerText = '$' + familySavings.toLocaleString();
      document.getElementById('resHouseholdReserve').innerText = '$' + householdReserve.toLocaleString();
      document.getElementById('resCommunityTotal').innerText = '$' + communityTotal.toLocaleString();
    }"""

new_js_update_sim = """    function updateSim() {
      const years = parseInt(document.getElementById('simYears').value);
      document.getElementById('simYearsLabel').innerText = years + ' 年';

      const familySavings = years * 12000;
      const householdReserve = 47455;
      const communityTotal = householdReserve + familySavings;

      document.getElementById('resFamilySavings').innerText = '$' + familySavings.toLocaleString();
      document.getElementById('resHouseholdReserve').innerText = '$' + householdReserve.toLocaleString();
      document.getElementById('resCommunityTotal').innerText = '$' + communityTotal.toLocaleString();
    }"""

code = code.replace(old_js_update_sim, new_js_update_sim)

# 5. Update Item 00 Description
old_item00_desc = """            <h3>臺中市公寓大廈爭議事件調處申請書（免經 241 戶大會・依法直送市府）</h3>
            <p>共 2 頁 ｜ 依據《公寓大廈管理條例》第 59 條之 1 提請臺中市政府都發局調處；調處成立筆錄等同法院確定判決，區公所依法直接受理報備、新光銀行專款移交！</p>"""

new_item00_desc = """            <h3>臺中市公寓大廈爭議事件調處申請書（免開 241 戶大會・不設管委會）</h3>
            <p>共 2 頁 ｜ 依據《公寓大廈管理條例》第 59 條之 1 提請市府調處合意分流退出；回歸獨立透天生活，不另設管委會，28 萬專款均分退還各戶（每戶退約 $47,455 現金）！</p>"""

code = code.replace(old_item00_desc, new_item00_desc)

# 6. Update FAQs for No Committee
old_faqs_block = """    <div class="faq-list">
      <div class="faq-item open">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q1：大境 6 戶透天在法律程序上如何合法推動管理分流？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全依循法定程序，保障全體住戶權益！</strong>依據《公寓大廈管理條例》第 53 條規定，各自獨立使用且共用設施無整體不可分性之集居地區，準用本條例管理。<br>
          A2 大境 6 戶出入直臨公有計畫道路龍社路、水電排污自理、生活垃圾門前等候免費公有清潔隊，具備完整獨立性。實務上將依《條例》第 31 條特別決議程序，正式提案請富宇大地全體區分所有權人會議審議變更規約管理範圍（排除 A2），大會審議通過後依法向主管機關區公所申辦變更報備與大境獨立報備，程序合法、公開透明！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q2：這項分流管理提案，對富宇大地其餘 235 戶住戶有哪些實質雙贏好處？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>全區資源減負、管理更聚焦！</strong><br>
          1. <strong>物業管理聚焦</strong>：解除物業與保全人員跨越公有道路龍社路照應外側住戶之奔波，管理責任單純化，專注封閉式社區 235 戶核心治理。<br>
          2. <strong>公設容量減負</strong>：A2 承諾門前等候市府垃圾車並簽署放棄子母車切結，內部環保室與收費子母車容量 100% 留給 235 戶使用，解決垃圾滿溢壓力。<br>
          3. <strong>消除長期制度隱患</strong>：消弭外側透天未享用內部公設卻需分攤維護費的矛盾，避免未來無休止之行政陳情與爭議，促進全區長治久安。<br>
          4. <strong>財務零衝擊</strong>：A2 定存原即獨立立卷保管，專案移交不侵蝕大社區任何營運公款與既有基金！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q3：A2 分流後，會不會造成大社區管委會財務短缺或需要向住戶調漲管理費？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全不會！大社區財務收支結構不受負面影響。</strong><br>
          A2 6 戶每月繳納之 $6,000 元，經審計按戶數分攤內部垃圾清運費（約 $1,195）與物業經理人事支出（約 $1,751）後，大社區管委會原本投入外側管理所剩無幾；分流後管委會免除了對外側路段的巡檢維護與公電支出，且 A2 原本就未使用內部任何休閒公設，大社區 235 戶之日常營運預算完全穩健自給，絕不需要因而調漲管理費！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q4：關於專案移交之 NT$ 284,731 元款項，如何確保大社區的資產權益不受損？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>帳目獨立清晰，純屬專款原單專案歸位！</strong><br>
          富宇大地管委會於 115 年 5 月與 9 月例會官方財報已明確載明：台中市政府核退之公款分別定存，其中第 2 筆即獨立立卷為「A2 大境定存單 NT$ 220,231 元」專單保管；加上起造人富宇建設交屋管理基金（每戶 1 萬，大境 6 戶共 60,000 元）。該專案款項自始即與大社區其他各區定存單分開保管，移交純屬原款專案歸位，富宇大地 235 戶所屬之悠境、澄境定存、起造人提撥款及日常營運帳戶分毫不受影響！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q5：雙方在程序推動與大會決議期間，管理費與公共事務如何維持平穩運作？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>全程恪遵法規，平穩過渡零衝突！</strong><br>
          在大會特別決議生效前，A2 6 戶住戶全體照常依現制履行管理費繳納義務，絕不採取停繳或對抗手段；A2 住戶門前廢棄物亦維持自行等候市府垃圾車清運，絕不影響大社區內部日常安寧。本案以「協商與雙贏」為唯一準則，共同攜手完成合法合規的分流程序。
        </div>
      </div>
    </div>"""

new_faqs_block = """    <div class="faq-list">
      <div class="faq-item open">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q1：大境 6 戶分流之後，為什麼完全不需要成立管理委員會？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>透天機能獨立，法律上完全不需要成立管委會！</strong><br>
          大境 6 戶緊鄰公有計畫道路龍社路，出入有關自家的獨立鐵捲門、水電瓦斯各自依水電表繳費、生活垃圾每日定時在門前等候台中市環保局免費垃圾車清運、信件包裹由郵差直接投遞。6 戶既沒有內部公用設施、也沒有電梯與保全需求，法律上直接回歸一般自用獨立透天街廓，<strong>免選委員、免開區權大會、免做財務報表與稅籍申報，生活最輕鬆自在！</strong>
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q2：這項「不設管委會、回歸獨立透天」方案，對富宇大地其餘 235 戶有哪些雙贏好處？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>免除對抗與繁瑣點交，大社區管理最單純化！</strong><br>
          1. <strong>管委會零對接負擔</strong>：大境不成立新管委會，富宇大地管委會無需面臨兩會交接、合約分立與公設點交之繁雜公務，只要在規約管理範圍排除 A2，即可專注於封閉式社區 235 戶核心治理。<br>
          2. <strong>公設容量減負</strong>：A2 承諾門前自理垃圾並立切結，內部收費子母車容量 100% 留給內部 235 戶使用，解決垃圾滿溢壓力。<br>
          3. <strong>物業管理聚焦</strong>：解除物業與保全人員跨越公有道路龍社路巡查之奔波，管理動線更集中、行政效能顯著提升。<br>
          4. <strong>財務零衝擊</strong>：A2 定存原即獨立立卷，專案退還不侵蝕大社區任何營運公款與既有基金！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q3：那筆 NT$ 284,731 元的專案公款，不成立管委會要如何處理？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>依戶數全額均分返還給 6 戶區權人（每戶退回約 $47,455 現金）！</strong><br>
          富宇大地管委會 5 月與 9 月例會官方財報已明確載明：第 2 筆獨立立卷為「A2 大境定存單 NT$ 220,231 元」；加上起造人交屋管理基金（每戶 1 萬，6 戶共 60,000 元）。因大境回歸獨立透天不設管委會、亦無公設需管委會維修，在向臺中市政府申請調處時，請求事項直接載明：<strong>由相對人依戶數均分，全額撥還退交本區 6 戶住戶個人帳戶，每戶現領約 NT$ 47,455 元現金！</strong>
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q4：分流後每戶管理費變成 $0 元，平日公共事務與環境如何維持？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>回歸一般透天自律生活，終生免繳任何管理費！</strong><br>
          各家各戶出門直接是公有道路龍社路，門前路燈電費由市府公帑支應；生活垃圾由市府免費清潔隊清運；自家門口各自維護。每戶每年現省 $12,000 元管理費支出，無任何管委會行政與財務包袱！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q5：雙方在程序推動與調處期間，管理費與公共事務如何維持平穩運作？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>全程恪遵法規，平穩過渡零衝突！</strong><br>
          在市府調處成立生效前，A2 6 戶住戶全體照常依現制履行管理費繳納義務；A2 住戶門前廢棄物亦維持自行等候市府垃圾車清運，絕不影響大社區內部日常安寧。本案以「協商與雙贏」為唯一準則，共同攜手完成合法合規的分流程序。
        </div>
      </div>
    </div>"""

code = code.replace(old_faqs_block, new_faqs_block)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dajing_interactive.py successfully updated to 'No Committee / Return to Independent Villas' framework!")
