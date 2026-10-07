// PROTOTYPE (#21) — the sample library: 3 section types × 3 presets, in the stored record shape of #13 §3.2.
// build.mjs writes each record to out/library/… as JSON, which is the format under test.

const L = (en, th, zh) => ({ en, th, zh });
const ACTIONS = `<div class="actions">{{#primary}}<a class="btn" href="{{href}}">{{label}}</a>{{/primary}}{{#secondary}}<a class="btn btn--quiet" href="{{href}}">{{label}}</a>{{/secondary}}</div>`;
const EYEBROW = `{{#eyebrow}}<p class="eyebrow">{{eyebrow}}</p>{{/eyebrow}}`;

export const types = {
  hero: {
    schemaVersion: 1, id: 'hero', name: L('Opening', 'ส่วนเปิดหน้า', '开篇'), category: 'opening',
    fields: {
      eyebrow: { kind: 'text', required: false, maxLength: L(60, 50, 24), placeholder: L('Short label above the title', 'ข้อความสั้นเหนือหัวข้อ', '标题上方的短标签') },
      title: { kind: 'text', required: true, maxLength: L(70, 60, 30), placeholder: L('The one thing visitors should remember', 'สิ่งเดียวที่ผู้อ่านควรจำได้', '访客应记住的一件事') },
      lead: { kind: 'text', required: true, maxLength: L(240, 220, 110), placeholder: L('Two sentences on who you help and how', 'สองประโยคว่าคุณช่วยใครและช่วยอย่างไร', '用两句话说明您帮助谁以及如何帮助') },
      primary: { kind: 'link', required: true, placeholder: L('Main action', 'ปุ่มหลัก', '主要按钮') },
      secondary: { kind: 'link', required: false, placeholder: L('Second action', 'ปุ่มรอง', '次要按钮') },
      image: { kind: 'image', required: false },
      figures: { kind: 'list', required: false, min: 2, max: 4, item: { value: { kind: 'text', maxLength: L(8, 10, 6) }, label: { kind: 'text', maxLength: L(48, 44, 20) } } },
    },
  },
  services: {
    schemaVersion: 1, id: 'services', name: L('Services', 'บริการ', '服务'), category: 'services',
    fields: {
      title: { kind: 'text', required: true, maxLength: L(60, 50, 24), placeholder: L('What you offer', 'สิ่งที่คุณให้บริการ', '您提供的服务') },
      intro: { kind: 'text', required: false, maxLength: L(160, 140, 70), placeholder: L('One sentence that frames the list', 'หนึ่งประโยคที่อธิบายภาพรวม', '一句话概括') },
      items: { kind: 'list', required: true, min: 3, max: 6, item: { title: { kind: 'text', maxLength: L(40, 36, 14) }, text: { kind: 'text', maxLength: L(140, 130, 60) } } },
    },
  },
  cta: {
    schemaVersion: 1, id: 'cta', name: L('Contact and conversion', 'ติดต่อและชวนลงมือ', '联系与转化'), category: 'contact',
    fields: {
      title: { kind: 'text', required: true, maxLength: L(60, 50, 24), placeholder: L('What happens next', 'ขั้นต่อไปคืออะไร', '下一步是什么') },
      text: { kind: 'text', required: false, maxLength: L(200, 180, 90), placeholder: L('Why act now, in one or two sentences', 'ทำไมควรติดต่อตอนนี้', '为什么现在行动') },
      primary: { kind: 'link', required: true, placeholder: L('Main action', 'ปุ่มหลัก', '主要按钮') },
      contact: { kind: 'group', required: false, item: { line: { kind: 'text' }, phone: { kind: 'phone' }, email: { kind: 'email' } } },
    },
  },
};

const preset = (id, type, name, purpose, defaults, overrides, markup, css, constraints = {}) => ({
  schemaVersion: 1, id, version: '1.0', type, category: types[type].category, name, purpose,
  changelog: [{ version: '1.0', note: 'First version (#21 sample)' }], tags: [],
  options: defaults, overrides, constraints, markup, css,
});

export const presets = [
  preset('hero-split', 'hero', L('Split with image', 'ข้อความคู่รูป', '图文并排'), L('Title and actions beside one strong photo.', 'หัวข้อและปุ่มเคียงรูปเด่นหนึ่งรูป', '标题与按钮旁配一张主图。'),
    { tone: 'plain', imageSide: 'right' }, ['tone', 'imageSide', 'text', 'image'],
    `<div class="s__in hs hs--img-{{opt.imageSide}}"><div class="hs__text">${EYEBROW}<h1 class="hs__title">{{title}}</h1><p class="lead">{{lead}}</p>${ACTIONS}</div>{{#image}}<figure class="hs__media"><img src="{{src}}" alt="{{alt}}" width="{{w}}" height="{{h}}"></figure>{{/image}}</div>`,
    `.hs{display:grid;gap:var(--space-6);align-items:center}
.hs__text{display:grid;gap:var(--space-4);justify-items:start}
.hs__title{font-size:var(--size-display-1)}
.hs__media{margin:0;aspect-ratio:4/3;overflow:hidden;border-radius:var(--radius-media);background:var(--c-surface)}
.hs__media img{width:100%;height:100%;object-fit:cover;display:block}
@container section (min-width: 48rem){.hs{grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:var(--space-8)}.hs--img-left .hs__media{order:-1}}`,
    { image: 'required' }),

  preset('hero-statement', 'hero', L('Large statement', 'ประโยคใหญ่', '大字标语'), L('A large title with a ruled row for the lead and actions.', 'หัวข้อตัวใหญ่ ใต้เส้นมีคำอธิบายและปุ่ม', '大标题，下方横线后是导语与按钮。'),
    { tone: 'tinted' }, ['tone', 'text'],
    `<div class="s__in hst">${EYEBROW}<h1 class="hst__title">{{title}}</h1><div class="hst__row"><p class="lead hst__lead">{{lead}}</p>${ACTIONS}</div></div>`,
    `.hst{display:grid;gap:var(--space-5)}
.hst__title{font-size:var(--size-display-xl);max-width:16ch}
.hst__row{display:grid;gap:var(--space-5);border-top:1px solid var(--c-rule);padding-top:var(--space-5)}
.hst__lead{max-width:38ch}
@container section (min-width: 48rem){.hst__row{grid-template-columns:minmax(0,38ch) auto;justify-content:space-between;align-items:end}}`),

  preset('hero-figures', 'hero', L('Title with key figures', 'หัวข้อพร้อมตัวเลขสำคัญ', '标题配关键数字'), L('Title and actions above two to four facts in large figures.', 'หัวข้อและปุ่ม ตามด้วยข้อเท็จจริง 2–4 ข้อเป็นตัวเลขใหญ่', '标题与按钮，下方以大号数字展示 2–4 项事实。'),
    { tone: 'plain' }, ['tone', 'text'],
    `<div class="s__in hf"><div class="hf__head">${EYEBROW}<h1 class="hf__title">{{title}}</h1><p class="lead">{{lead}}</p>${ACTIONS}</div><dl class="hf__figs">{{#figures}}<div class="hf__fig"><dt class="hf__label">{{label}}</dt><dd class="hf__value">{{value}}</dd></div>{{/figures}}</dl></div>`,
    `.hf{display:grid;gap:var(--space-7)}
.hf__head{display:grid;gap:var(--space-4);justify-items:start;max-width:40rem}
.hf__title{font-size:var(--size-display-1)}
.hf__figs{display:grid;gap:var(--space-5);margin:0;border-top:1px solid var(--c-rule);padding-top:var(--space-5)}
.hf__fig{display:flex;flex-direction:column-reverse;gap:var(--space-2)}
.hf__value{margin:0;font-family:var(--font-display);font-weight:var(--weight-display);font-size:var(--size-figure);line-height:1;font-variant-numeric:lining-nums tabular-nums;color:var(--c-accent)}
.hf__label{color:var(--c-muted);font-size:var(--size-small)}
@container section (min-width: 40rem){.hf__figs{grid-template-columns:repeat(3,minmax(0,1fr))}}`,
    { figures: 'required' }),

  preset('services-cards', 'services', L('Cards', 'การ์ด', '卡片'), L('Each service on its own card, in two or three columns.', 'แต่ละบริการอยู่บนการ์ดของตัวเอง 2 หรือ 3 คอลัมน์', '每项服务一张卡片，两列或三列。'),
    { tone: 'tinted', columns: '3' }, ['tone', 'columns', 'text'],
    `<div class="s__in sc"><div class="sc__head"><h2 class="sc__title">{{title}}</h2>{{#intro}}<p class="sc__intro">{{intro}}</p>{{/intro}}</div><ul class="sc__grid sc--cols-{{opt.columns}}">{{#items}}<li class="sc__card"><h3 class="sc__name">{{title}}</h3><p class="sc__text">{{text}}</p></li>{{/items}}</ul></div>`,
    `.sc{display:grid;gap:var(--space-6)}
.sc__head{display:grid;gap:var(--space-3);max-width:40rem}
.sc__title{font-size:var(--size-h2)}
.sc__intro{color:var(--c-muted)}
.sc__grid{list-style:none;margin:0;padding:0;display:grid;gap:var(--space-4)}
.sc__card{background:var(--c-surface);border:1px solid var(--c-rule);border-radius:var(--radius-card);padding:var(--space-5);display:grid;gap:var(--space-2);align-content:start}
.sc__name{font-size:var(--size-h3)}
.sc__text{color:var(--c-muted)}
@container section (min-width: 40rem){.sc__grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@container section (min-width: 64rem){.sc--cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}}`),

  preset('services-rows', 'services', L('Ruled rows', 'แถวมีเส้นคั่น', '分隔行'), L('A ruled list: the service name on the left, what it covers on the right.', 'รายการมีเส้นคั่น ชื่อบริการซ้าย รายละเอียดขวา', '带分隔线的列表：左侧服务名称，右侧说明。'),
    { tone: 'plain' }, ['tone', 'text'],
    `<div class="s__in sr"><div class="sr__head"><h2 class="sr__title">{{title}}</h2>{{#intro}}<p class="sr__intro">{{intro}}</p>{{/intro}}</div><dl class="sr__list">{{#items}}<div class="sr__row"><dt class="sr__name">{{title}}</dt><dd class="sr__text">{{text}}</dd></div>{{/items}}</dl></div>`,
    `.sr{display:grid;gap:var(--space-6)}
.sr__head{display:grid;gap:var(--space-3);align-content:start}
.sr__title{font-size:var(--size-h2)}
.sr__intro{color:var(--c-muted);max-width:40ch}
.sr__list{margin:0;border-top:1px solid var(--c-text)}
.sr__row{display:grid;gap:var(--space-2);padding-block:var(--space-4);border-bottom:1px solid var(--c-rule)}
.sr__name{font-family:var(--font-display);font-weight:var(--weight-display);font-size:var(--size-h3)}
.sr__text{margin:0;color:var(--c-muted);max-width:52ch}
@container section (min-width: 48rem){.sr{grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:var(--space-8)}.sr__row{grid-template-columns:minmax(0,2fr) minmax(0,3fr);gap:var(--space-5)}}`),

  preset('services-columns', 'services', L('Open columns', 'คอลัมน์โปร่ง', '开放式分栏'), L('Services in open columns, each under a short accent rule.', 'บริการเรียงเป็นคอลัมน์โปร่ง แต่ละข้อมีเส้นสั้นสีเน้นด้านบน', '服务以开放式分栏排列，每项上方有一条短强调线。'),
    { tone: 'plain' }, ['tone', 'text'],
    `<div class="s__in scol"><h2 class="scol__title">{{title}}</h2>{{#intro}}<p class="lead scol__intro">{{intro}}</p>{{/intro}}<ul class="scol__grid">{{#items}}<li class="scol__item"><h3 class="scol__name">{{title}}</h3><p class="scol__text">{{text}}</p></li>{{/items}}</ul></div>`,
    `.scol{display:grid;gap:var(--space-4)}
.scol__title{font-size:var(--size-h2)}
.scol__intro{color:var(--c-muted);max-width:44ch}
.scol__grid{list-style:none;margin:0;padding:0;display:grid;gap:var(--space-6);padding-top:var(--space-4)}
.scol__item{display:grid;gap:var(--space-2);align-content:start;border-top:2px solid var(--c-accent);padding-top:var(--space-3)}
.scol__name{font-size:var(--size-h3)}
.scol__text{color:var(--c-muted)}
@container section (min-width: 40rem){.scol__grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@container section (min-width: 64rem){.scol__grid{grid-template-columns:repeat(3,minmax(0,1fr))}}`),

  preset('cta-band', 'cta', L('Bold band', 'แถบเข้ม', '深色横幅'), L('A strong band with one clear action.', 'แถบสีเข้มพร้อมปุ่มเดียวที่ชัดเจน', '醒目的横幅，只有一个明确的按钮。'),
    { tone: 'bold' }, ['tone', 'text'],
    `<div class="s__in cb"><div class="cb__text"><h2 class="cb__title">{{title}}</h2>{{#text}}<p class="cb__body">{{text}}</p>{{/text}}</div>{{#primary}}<a class="btn" href="{{href}}">{{label}}</a>{{/primary}}</div>`,
    `.cb{display:grid;gap:var(--space-5);justify-items:start}
.cb__text{display:grid;gap:var(--space-3);max-width:40rem}
.cb__title{font-size:var(--size-h2)}
.cb__body{color:var(--c-muted)}
@container section (min-width: 48rem){.cb{grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:var(--space-8)}}`),

  preset('cta-contact', 'cta', L('Action with contact details', 'ปุ่มพร้อมช่องทางติดต่อ', '按钮与联系方式'), L('Invitation and button beside LINE, phone and email.', 'คำชวนและปุ่ม เคียงกับ LINE โทรศัพท์ และอีเมล', '邀请语与按钮，旁边列出 LINE、电话和邮箱。'),
    { tone: 'tinted' }, ['tone', 'text'],
    `<div class="s__in cc"><div class="cc__text"><h2 class="cc__title">{{title}}</h2>{{#text}}<p class="cc__body">{{text}}</p>{{/text}}{{#primary}}<a class="btn" href="{{href}}">{{label}}</a>{{/primary}}</div>{{#contact}}<dl class="cc__list"><div><dt>{{t.line}}</dt><dd>{{line}}</dd></div><div><dt>{{t.phone}}</dt><dd><a href="tel:{{phoneE164}}">{{phone}}</a></dd></div><div><dt>{{t.email}}</dt><dd><a href="mailto:{{email}}">{{email}}</a></dd></div></dl>{{/contact}}</div>`,
    `.cc{display:grid;gap:var(--space-6)}
.cc__text{display:grid;gap:var(--space-4);justify-items:start;max-width:36rem}
.cc__title{font-size:var(--size-h2)}
.cc__body{color:var(--c-muted)}
.cc__list{margin:0;display:grid;gap:var(--space-4);align-content:start;border-top:1px solid var(--c-rule);padding-top:var(--space-4)}
.cc__list dt{color:var(--c-muted);font-family:var(--font-ui);font-size:var(--size-small)}
.cc__list dd{margin:0;font-size:var(--size-h3);font-variant-numeric:lining-nums}
.cc__list a{color:var(--c-text);text-decoration-color:var(--c-rule);text-underline-offset:.2em}
@container section (min-width: 48rem){.cc{grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:var(--space-8)}.cc__list{border-top:0;padding-top:0;border-left:1px solid var(--c-rule);padding-left:var(--space-6)}}`),

  preset('cta-quiet', 'cta', L('Quiet line', 'บรรทัดเรียบ', '简洁一行'), L('One ruled line with the next step, for the end of a long page.', 'บรรทัดเดียวมีเส้นคั่น บอกขั้นต่อไป สำหรับท้ายหน้ายาว', '一行带分隔线的下一步提示，适合长页面结尾。'),
    { tone: 'plain' }, ['tone', 'text'],
    `<div class="s__in cq"><h2 class="cq__title">{{title}}</h2>{{#primary}}<a class="cq__link" href="{{href}}">{{label}} <span aria-hidden="true">→</span></a>{{/primary}}</div>`,
    `.cq{display:grid;gap:var(--space-3);border-top:1px solid var(--c-rule);padding-top:var(--space-5)}
.cq__title{font-size:var(--size-h3)}
.cq__link{font-family:var(--font-ui);font-weight:var(--weight-ui-strong);color:var(--c-accent);text-decoration:none;justify-self:start}
.cq__link:hover{text-decoration:underline;text-underline-offset:.25em}
@container section (min-width: 40rem){.cq{grid-template-columns:minmax(0,1fr) auto;align-items:baseline}}`),
];

// System strings the generator gives every preset as {{t.*}} (finding: presets need them).
export const strings = {
  en: { line: 'LINE', phone: 'Phone', email: 'Email' },
  th: { line: 'LINE', phone: 'โทรศัพท์', email: 'อีเมล' },
  zh: { line: 'LINE', phone: '电话', email: '电子邮件' },
};

// Instance content for the sample page (real text, not placeholders).
export const content = {
  hero: {
    en: { eyebrow: 'Accounting and tax for Thai companies', title: 'Clear numbers, calm decisions', lead: 'We keep your books, file VAT and withholding tax on time, and explain every figure in plain language.', primary: { label: 'Book a consultation', href: '#contact' }, secondary: { label: 'See our fees', href: '#fees' }, image: { alt: 'Placeholder image: stacked papers on a desk' }, figures: [{ value: '15th', label: 'Books closed by this day, every month' }, { value: '3', label: 'Languages: Thai, English and Chinese' }, { value: '48 h', label: 'Longest wait for a reply' }] },
    th: { eyebrow: 'บัญชีและภาษีสำหรับบริษัทไทย', title: 'ตัวเลขชัดเจน ตัดสิน\u2060ใจได้อย่างมั่นใจ', lead: 'เราดูแลบัญชี ยื่นภาษีมูลค่าเพิ่มและภาษีหัก ณ ที่จ่ายตรงเวลา พร้อมอธิบายทุกตัวเลขด้วยภาษาที่เข้าใจง่าย', primary: { label: 'นัดปรึกษา', href: '#contact' }, secondary: { label: 'ดูค่าบริการ', href: '#fees' }, image: { alt: 'รูปตัวอย่าง: กองเอกสารบนโต๊ะ' }, figures: [{ value: 'วันที่ 15', label: 'ปิดงบให้เสร็จทุกเดือน' }, { value: '3 ภาษา', label: 'ไทย อังกฤษ และจีน' }, { value: '48 ชม.', label: 'ตอบกลับทุกคำถามภายใน' }] },
    zh: { eyebrow: '泰国企业会计与税务', title: '数字清晰，决策从容', lead: '我们负责记账，按时申报增值税与预扣税，并用通俗的语言解释每一个数字。', primary: { label: '预约咨询', href: '#contact' }, secondary: { label: '查看收费', href: '#fees' }, image: { alt: '示例图片：桌上叠放的文件' }, figures: [{ value: '15 日', label: '每月在此日前完成月结' }, { value: '3 种', label: '服务语言：泰语、英语、中文' }, { value: '48 小时', label: '最长回复时间' }] },
  },
  services: {
    en: { title: 'What we do each month', intro: 'Six services, one team, one monthly fee.', items: [
      { title: 'Bookkeeping', text: 'Every sales and purchase document recorded, matched to the bank, and closed by the 15th.' },
      { title: 'VAT', text: 'P.P.30 prepared and filed on time, with a cash forecast for the tax due.' },
      { title: 'Withholding tax', text: 'P.N.D.1, 3 and 53 filed, and a certificate issued to every payee.' },
      { title: 'Payroll and social security', text: 'Salaries, social security contributions and the year-end P.N.D.1 Kor, handled together.' },
      { title: 'Financial statements', text: 'Annual statements under TFRS for NPAEs, ready for your auditor.' },
      { title: 'Advice in plain language', text: 'A monthly call to explain the numbers and what to do next.' }] },
    th: { title: 'งานที่เราทำให้ทุกเดือน', intro: 'หกบริการ ทีมเดียว ค่าบริการรายเดือนเดียว', items: [
      { title: 'ทำบัญชี', text: 'บันทึกเอกสารซื้อขายทุกใบ กระทบยอดกับธนาคาร และปิดงบภายในวันที่ 15' },
      { title: 'ภาษีมูลค่าเพิ่ม', text: 'จัดทำและยื่น ภ.พ.30 ตรงเวลา พร้อมประมาณการเงินสดสำหรับภาษีที่ต้องจ่าย' },
      { title: 'ภาษีหัก ณ ที่จ่าย', text: 'ยื่น ภ.ง.ด.1, 3 และ 53 และออกหนังสือรับรองให้ผู้รับเงินทุกราย' },
      { title: 'เงินเดือนและประกันสังคม', text: 'ดูแลเงินเดือน เงินสมทบประกันสังคม และ ภ.ง.ด.1ก ปลายปีไปพร้อมกัน' },
      { title: 'งบการเงิน', text: 'จัดทำงบการเงินประจำปีตาม TFRS for NPAEs พร้อมส่งผู้สอบบัญชี' },
      { title: 'คำปรึกษาที่เข้าใจง่าย', text: 'โทรคุยทุกเดือนเพื่ออธิบายตัวเลขและสิ่งที่ควรทำต่อ' }] },
    zh: { title: '我们每月为您做什么', intro: '六项服务，一个团队，一笔月费。', items: [
      { title: '记账', text: '记录每一张购销单据，与银行对账，并在 15 日前完成月结。' },
      { title: '增值税', text: '按时编制并申报 P.P.30，并预估应缴税款所需的现金。' },
      { title: '预扣税', text: '申报 P.N.D.1、3 和 53，并为每位收款人开具扣税凭证。' },
      { title: '工资与社会保险', text: '统一处理工资、社会保险缴费以及年末的 P.N.D.1 Kor。' },
      { title: '财务报表', text: '按照 TFRS for NPAEs 编制年度财务报表，供审计师审阅。' },
      { title: '通俗易懂的建议', text: '每月一次通话，解释数字以及下一步该做什么。' }] },
  },
  cta: {
    en: { title: 'Talk to an accountant this week', text: 'Tell us about your business. We reply within two working days with a fixed monthly quote.', primary: { label: 'Book a consultation', href: '#contact' }, contact: { line: '@example-firm', phone: '02 000 0000', phoneE164: '+6620000000', email: 'hello@example.com' } },
    th: { title: 'คุยกับนักบัญชีภายในสัปดาห์นี้', text: 'เล่าเรื่องธุรกิจของคุณให้เราฟัง เราจะตอบกลับภายในสองวันทำการ พร้อมใบเสนอราคารายเดือนแบบคงที่', primary: { label: 'นัดปรึกษา', href: '#contact' }, contact: { line: '@example-firm', phone: '02 000 0000', phoneE164: '+6620000000', email: 'hello@example.com' } },
    zh: { title: '本周就与会计师聊一聊', text: '请介绍一下您的业务。我们会在两个工作日内回复，并提供固定的月度报价。', primary: { label: '预约咨询', href: '#contact' }, contact: { line: '@example-firm', phone: '02 000 0000', phoneE164: '+6620000000', email: 'hello@example.com' } },
  },
};
