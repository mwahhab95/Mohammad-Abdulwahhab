const navigation = [
  { id: "home", label: "Home" },
  { label: "Learn Organic Chemistry", children: [
    { id: "learn-organic-chemistry", label: "Overview" },
    { id: "basics-of-organic-chemistry", label: "Basics of Organic Chemistry" },
    { id: "organic-i", label: "Organic-I" },
    { id: "organic-ii", label: "Organic-II" },
    { id: "organic-iii", label: "Organic-III" },
  ]},
  { label: "Apps for Academics", children: [
    { id: "my-apps-for-academics", label: "My Apps for Academics" },
    { id: "mark-list-maker", label: "Mark List Maker" },
    { id: "attendane-export", label: "Grades & Attendance Sync" },
    { id: "sample-key-generator", label: "Sample Key Generator" },
  ]},
  { label: "Apps for Students", children: [
    { id: "woodward-fieser", label: "WoodWard-Fieser λmax Calculator" },
    { id: "nomenclature", label: "Nomenclature" },
    { id: "elemental-analysis", label: "Elemental Analysis" },
  ]},
  { label: "Scientific Research Workshop", children: [
    { id: "scientific-research-workshop", label: "Workshop Overview" },
    { id: "session-1", label: "Session 1" },
    { id: "session-2", label: "Session 2" },
    { id: "session-3", label: "Session 3" },
  ]},
  { id: "ai-index", label: "AI index" },
  { id: "publications", label: "Publications" },
  { id: "highlights", label: "Highlights" },
];

const publications = [
  { title: "Deciphering the groove-binding mode of dolutegravir with salmon sperm DNA through spectroscopic and molecular modelling approaches", authors: "E. Yosrey, M. A. Elmorsy, H. Elmansi, S. Shalan, et al.", journal: "Scientific Reports (2026)", doi: "https://doi.org/10.1038/s41598-026-40136-y" },
  { title: "Developing an Automated Tool for Psychometric Evaluation and Exam Quality Indexing of Multiple-Choice Questions (MCQs): Phase I Study", authors: "M. A. Elmorsy and D. E. Morsi", journal: "Journal of Psychometric Research (2026)", doi: "https://doi.org/10.62425/jopres.1804954" },
  { title: "Targeting TXNIP With Saroglitazar Mitigates Acute Hepatic Injury in Rats Challenged With Thioacetamide", authors: "Elnaghy, F., Saber, S., Abd El-Kader, E. M., Elmorsy, M. A., & Shehatou, G. S. G.", journal: "Archiv der Pharmazie (2025)", doi: "https://doi.org/10.1002/ardp.70179" },
  { title: "Selected recent publications list", authors: "Additional DOI links preserved from the original Google Site.", journal: "2025-2017", doiList: [
    "https://doi.org/10.1007/s11224-025-02621-4","https://doi.org/10.1080/10406638.2024.2447845","https://doi.org/10.21608/joese.2023.245062.1033",
    "https://doi.org/10.1016/j.molstruc.2024.137681","https://doi.org/10.1080/10406638.2022.2038216","https://doi.org/10.3390/antiox11081568",
    "https://doi.org/10.1002/cbf.3686","https://doi.org/10.1007/s11356-021-16427-4","https://doi.org/10.1007/s10812-022-01308-6",
    "https://doi.org/10.1016/j.bpc.2021.106660","https://doi.org/10.3390/molecules26113286","https://doi.org/10.1021/acsomega.0c05793",
    "https://doi.org/10.2147/DDDT.S249093","https://doi.org/10.1016/j.bmc.2020.115373","https://doi.org/10.1111/cbdd.13433",
    "https://doi.org/10.7324/JAPS.2018.8510","https://doi.org/10.1002/ardp.201700403",
  ]},
];

const highlights = [
  "Served as a speaker at the 2nd International Conference of Pharmaceutical Sciences at Mansoura University, held in April 2019.",
  "Participated as a workshop tutor at the 1st International Conference of Pharmaceutical Sciences, MU-PHARM 2017.",
  "Named a JSPS HOPE Fellow for successful participation in The Fifth HOPE Meeting, Tokyo, Japan (2013).",
  'Member of the organizing committee for the "International Workshop on Computational Molecular Modeling & Drug Discovery" at Mansoura University (2012).',
  'Contributed to the "Computer-Based Drug Design" workshop held at Mansoura University in February 2010.',
  "Presented a workshop titled 'Discover How AI Can Transform Your Academic Journey' at the Faculty of Pharmacy, Mansoura University, in February-March 2025.",
  'Presented "The Synergy of AI and NMR: Revolutionizing Drug Discovery" in collaboration with the Pharmacy Center of Scientific Excellence (PCSE), Mansoura University (2025).',
  'Completed the "Introduction to programming using Python" training program certified by Microsoft (2022).',
  "Completed the Microsoft-certified 'Python programming language - Intermediate level' training (2022).",
  "Recognized as a Microsoft Office Specialist for Word 2016 on December 19, 2021.",
  "Achieved Microsoft Office Specialist certification for PowerPoint 2016 on December 28, 2021.",
  "Contributed as a peer reviewer for some reputable Q1 and Q2 scientific journals.",
  "Certificate of Appreciation from the Ministry of Education for achieving 4th rank in the General Secondary Certificate for the 1994/1995 academic year.",
];

const aiServices = [
  ["Claude","Anthropic • USA","Advanced AI assistant with Sonnet and Opus models.","https://claude.ai"],
  ["Grok","xAI • USA","Real-time conversational AI inspired by the Hitchhiker's Guide tone.","https://grok.com"],
  ["Gemini","Google • USA","Multimodal reasoning across text, code, and images.","https://gemini.google.com"],
  ["GLM-4.5","Zhipu AI • China","Multilingual reasoning and strong language-model support.","https://chat.z.ai"],
  ["Qwen-3","Alibaba • China","Versatile LLM platform for broad cloud-based AI workflows.","https://chat.qwen.ai"],
  ["DeepSeek","DeepSeek • China","Strong at code generation and mathematical reasoning.","https://chat.deepseek.com"],
  ["Manus","Manus • China","Foundation models and autonomous AI agents.","https://manus.im/app"],
  ["Skywork","Skywork • Singapore","Enterprise-oriented AI models and agents.","https://skywork.ai"],
  ["Genspark","Genspark • USA","AI-first search and generated knowledge pages.","https://www.genspark.ai"],
  ["Mistral","Mistral AI • France","European AI models and developer tooling.","https://mistral.ai"],
  ["ChatGPT","OpenAI • USA","Conversational AI for writing, coding, and research.","https://chatgpt.com"],
  ["Felo","Felo • Japan","Multilingual communication and translation workflows.","https://felo.ai"],
  ["KIMI","Moonshot AI • China","Very long-context AI assistant.","https://www.kimi.com"],
  ["Copilot","Microsoft • USA","AI assistant integrated into Microsoft products.","https://copilot.microsoft.com"],
  ["Perplexity","Perplexity AI • USA","Cited AI answers with web search.","https://www.perplexity.ai"],
  ["Consensus","Consensus • USA","Scientific evidence search from academic papers.","https://consensus.app"],
  ["SciSpace","SciSpace • International","Literature review and scientific paper understanding.","https://typeset.io"],
];

const app = document.getElementById("app");
const nav = document.getElementById("nav");
const sidebar = document.getElementById("sidebar");
const menuToggle = document.getElementById("menuToggle");

function hero(title, subtitle) { return `<section class="hero"><div class="hero-cover"><div class="hero-copy"><p class="eyebrow">Mohammad Abdulwahhab</p><h2>${title}</h2><p>${subtitle}</p></div></div></section>`; }
function sectionHeader(title, subtitle) { return `<section class="panel"><div class="panel-header"><div><h2 class="panel-title">${title}</h2><p class="lead">${subtitle}</p></div></div></section>`; }
function courseCard(title, text, href) { return `<article class="card"><span class="tag">Course</span><h3>${title}</h3><p>${text}</p><a class="btn btn-primary" href="${href}">Open</a></article>`; }
function resourceCard(title, text, href) { return `<article class="card"><span class="tag">Resource</span><h3>${title}</h3><p>${text}</p><a class="btn btn-primary" href="${href}" target="_blank" rel="noreferrer">Open link</a></article>`; }
function toolPage(title, text, href) { return `${sectionHeader(title, text)}<section class="panel"><p>The original Google Site page is primarily resource- or embed-driven. This rebuilt page preserves it as a direct access point inside the recreated site.</p><div class="button-row"><a class="btn btn-primary" href="${href}" target="_blank" rel="noreferrer">Open original resource</a></div></section>`; }
function videoGalleryPage(title, subtitle, videos) { return `${sectionHeader(title, subtitle)}<section class="card-grid">${videos.map((video, index) => `<article class="embed-card"><h3>Lesson ${index + 1}</h3><iframe class="video-frame" src="${video}" title="${title} lesson ${index + 1}" allowfullscreen></iframe></article>`).join("")}</section>`; }

const pages = {
  home: () => `${hero("Personal website for A. Prof. Mohammad Abdulwahhab","Academia, organic chemistry, scientific research, and custom tools for academics and students.")}<section class="stats-grid"><article><span class="stat-label">Experience</span><div class="stat-value">25+ years</div><p class="muted">Dedicated academic career in pharmaceutical sciences.</p></article><article><span class="stat-label">Focus</span><div class="stat-value">Organic Chemistry</div><p class="muted">Simplifying difficult concepts for pharmacy students.</p></article><article><span class="stat-label">Builds</span><div class="stat-value">Apps + AI</div><p class="muted">Custom Windows tools and practical AI-enabled workflows.</p></article></section><section class="panel"><div class="panel-header"><div><h2 class="panel-title">About Me</h2><p class="lead">Pharmaceutical sciences educator, researcher, and builder of academic productivity tools.</p></div></div><div class="text-columns"><div><p>With over 25 years of experience in academia, I have dedicated my career to the field of pharmaceutical sciences. I graduated from the Faculty of Pharmacy, Mansoura University in 2000, where I also earned both my Master's and PhD degrees.</p><p>My passion lies in making organic chemistry accessible and engaging for pharmacy students. I’m deeply committed to education and strive to simplify complex concepts through clear explanations and interactive learning.</p></div><div><p>My experience encompasses extensive proficiency in various molecular modeling and drug design software, alongside a nascent understanding of Python programming.</p><p>In addition to research and teaching, I develop custom Windows applications tailored to the needs of academics. These tools are designed to enhance productivity, streamline administrative tasks, and support teaching and research activities for myself and fellow faculty members.</p></div></div><div class="button-row"><a class="btn btn-primary" href="https://www.linkedin.com/in/mwahhab95" target="_blank" rel="noreferrer">LinkedIn</a><a class="btn btn-secondary" href="https://www.youtube.com/@mwahhab95" target="_blank" rel="noreferrer">YouTube</a><a class="btn btn-secondary" href="https://t.me/mwahhab95" target="_blank" rel="noreferrer">Telegram</a><a class="btn btn-secondary" href="https://orcid.org/0000-0001-7575-6556" target="_blank" rel="noreferrer">ORCID</a><a class="btn btn-secondary" href="https://scholar.google.com/citations?user=AaoOcAYAAAAJ&hl=en" target="_blank" rel="noreferrer">Google Scholar</a><a class="btn btn-secondary" href="https://www.researchgate.net/profile/Mohammad-Elmorsy?ev=hdr_xprf" target="_blank" rel="noreferrer">ResearchGate</a></div></section><section class="embed-card"><h3>وصايا لطلبة صيدلة الجدد</h3><iframe class="video-frame" src="https://www.youtube.com/embed/HKqgMmBNFIc?start=45" title="وصايا لطلبة صيدلة الجدد" allowfullscreen></iframe></section><section class="panel arabic-block"><p>الدراسة الجامعية في مصر</p><p>أسألكم الدعاء لوالدي بالرحمة و المغفرة ، و لوالدتي بدوام الصحة و العافية ، ولأبنائي بالهداية والنجاح</p><p>اللهم اجعله علما ينتفع به بعد الممات ، تقبل الله منا جميعا صالح الأعمال</p><p><a href="mailto:mwahhab@mans.edu.eg">e-mail: mwahhab@mans.edu.eg</a></p></section>`,
  "learn-organic-chemistry": () => `${sectionHeader("Learn Organic Chemistry","The original site groups the learning material into Basics, Organic-I, Organic-II, and Organic-III.")}<section class="card-grid">${courseCard("Basics of Organic Chemistry","Foundational recorded lessons collected from the original site.","#/basics-of-organic-chemistry")}${courseCard("Organic-I","Course playlist embedded from the original Google Site content.","#/organic-i")}${courseCard("Organic-II","Lecture collection for the second course sequence.","#/organic-ii")}${courseCard("Organic-III","Advanced lecture collection for the third course sequence.","#/organic-iii")}</section>`,
  "basics-of-organic-chemistry": () => videoGalleryPage("Basics of Organic Chemistry","Embedded lesson collection reproduced from the original page.",["https://www.youtube.com/embed/90ujp5xWsLg","https://www.youtube.com/embed/CnxEUKheEMw","https://www.youtube.com/embed/GXakjcJraz0","https://www.youtube.com/embed/--xUdPx-2eQ","https://www.youtube.com/embed/lXI2uvX-SxA","https://www.youtube.com/embed/ZqJhr9Z88AI"]),
  "organic-i": () => videoGalleryPage("Organic-I","A curated subset of the original Organic-I video embeds.",["https://www.youtube.com/embed/2_I8_9yLy7g","https://www.youtube.com/embed/zo2GuxG6y4o","https://www.youtube.com/embed/ZLbGVBCKoaE","https://www.youtube.com/embed/WC66sjrBiwg","https://www.youtube.com/embed/oJKKRrbvH4Y","https://www.youtube.com/embed/buNXJ0cb7b8"]),
  "organic-ii": () => videoGalleryPage("Organic-II","Selected embeds preserved from the original Organic-II page.",["https://www.youtube.com/embed/Z9RJ-UsM06E","https://www.youtube.com/embed/TWIskII3KL8","https://www.youtube.com/embed/XuyR0tj4Bkk","https://www.youtube.com/embed/Bxu6xF_XD3E","https://www.youtube.com/embed/NmwMNsYBxKE","https://www.youtube.com/embed/glUXuy-KF0A"]),
  "organic-iii": () => videoGalleryPage("Organic-III","Selected embeds preserved from the original Organic-III page.",["https://www.youtube.com/embed/gciMDPQpzEM","https://www.youtube.com/embed/T_pCI8Gxpbs","https://www.youtube.com/embed/Sg9ckDOWTBo","https://www.youtube.com/embed/X6-ESnC-8Pc","https://www.youtube.com/embed/ADRwmPsDf3Q","https://www.youtube.com/embed/NEApj9fLuRk"]),
  "my-apps-for-academics": () => `${sectionHeader("My Apps for Academics","Custom tools and companion resources mirrored from the original website.")}<section class="card-grid">${resourceCard("Mark List Maker","Download package","https://app.box.com/s/lbrqatzgq249pr7i4j4w0w4dapww00sy")}${resourceCard("Grades & Attendance Sync","Download package","https://app.box.com/s/dwm64al7jzudsnnc9en6607f7keeuui4")}${resourceCard("Sample Key Generator","Download package","https://app.box.com/s/b090zt6ev7lhspmwdk6xxpu45pokk9re")}${resourceCard("Supporting resource","Box link","https://app.box.com/s/627kk5oznfyd3exbelayi9vjc86fuesf")}${resourceCard("Supporting resource","Box link","https://app.box.com/s/fzswdp5ijdd1uwei9w3hys63h6kh6bkm")}${resourceCard("Supporting resource","Box link","https://app.box.com/s/exqw0oy8lfjmm9frpzdnukbzneot26li")}${resourceCard("Supporting resource","Box link","https://app.box.com/s/2nesgbttb7xlbxwjlnjbtbe9bivxilgy")}${resourceCard("Supporting resource","Box link","https://app.box.com/s/8e4rw1qfd6l2c95ugyknmp42fnym9lo1")}${resourceCard("Supporting resource","Box link","https://app.box.com/s/k25zmmd2h27c5hnqpva7iu5m5djov8dr")}${resourceCard("Zenodo record","Persistent archive","https://doi.org/10.5281/zenodo.15769051")}</section><section class="embed-card"><h3>Important workshop about the use of AI in Academia</h3><p class="muted">Two recorded talks embedded on the original Apps for Academics page.</p><div class="card-grid"><iframe class="video-frame" src="https://www.youtube.com/embed/1gS4SNrr54A" title="Using AI in Academia" allowfullscreen></iframe><iframe class="video-frame" src="https://www.youtube.com/embed/VvLpkwOjKZM" title="From Code to Convenience" allowfullscreen></iframe></div></section>`,
  "mark-list-maker": () => toolPage("Mark List Maker","Part of the academic software collection on the original site.","https://app.box.com/s/lbrqatzgq249pr7i4j4w0w4dapww00sy"),
  "attendane-export": () => toolPage("Grades & Attendance Sync","Part of the academic software collection on the original site.","https://app.box.com/s/dwm64al7jzudsnnc9en6607f7keeuui4"),
  "sample-key-generator": () => toolPage("Sample Key Generator","Part of the academic software collection on the original site.","https://app.box.com/s/b090zt6ev7lhspmwdk6xxpu45pokk9re"),
  "woodward-fieser": () => toolPage("WoodWard-Fieser λmax Calculator","Student-focused calculator page preserved as a direct resource entry.","https://sites.google.com/view/mohammad-abdulwahhab/apps-for-students/woodward-fieser-%CE%BBmax-calculator"),
  nomenclature: () => toolPage("Nomenclature","Student learning resource preserved from the original Google Site.","https://sites.google.com/view/mohammad-abdulwahhab/apps-for-students/nomenclature"),
  "elemental-analysis": () => toolPage("Elemental Analysis","Student learning resource preserved from the original Google Site.","https://sites.google.com/view/mohammad-abdulwahhab/apps-for-students/elemental-analysis"),
  "scientific-research-workshop": () => `${sectionHeader("Scientific Research Workshop","The workshop page on the original site links to three sessions on digital research, decoding research, and sharing science.")}<section class="card-grid">${courseCard("Session 1","The Everyday Researcher: From Digital Noise to Trusted Source.","#/session-1")}${courseCard("Session 2","Decoding Research: From Question to Publication.","#/session-2")}${courseCard("Session 3","Making an Impact: How to Share Your Science.","#/session-3")}</section>`,
  "session-1": () => `${sectionHeader("Session 1","The Everyday Researcher: From Digital Noise to Trusted Source.")}<section class="panel"><ul class="clean-list"><li>Spot fake news with SIFT: Stop and Think, Investigate the Source, Find Better Coverage, Trace to the Original.</li><li>Key digital sources: PubMed, Google Scholar, Scopus, EKB, UpToDate, Medscape, WHO, FDA, EDA.</li><li>AI tools listed on the original page: Gemini, Perplexity, and Grok.</li><li>Responsible AI use: always verify AI-generated content.</li></ul></section><section class="embed-card"><iframe class="video-frame" src="https://www.youtube.com/embed/C-tyG_jYNL8" title="Session 1" allowfullscreen></iframe></section>`,
  "session-2": () => `${sectionHeader("Session 2","Decoding Research: From Question to Publication.")}<section class="panel"><ul class="clean-list"><li>FINER research idea checklist: Feasible, Interesting, Novel, Ethical, Relevant.</li><li>Journal quality ladder: Q1, Q2, Q3, Q4.</li><li>Hallmarks of a good reference: peer-reviewed, recent, relevant, and cited by others.</li></ul></section><section class="embed-card"><iframe class="video-frame" src="https://www.youtube.com/embed/h_gb8iu8Zps" title="Session 2" allowfullscreen></iframe></section>`,
  "session-3": () => `${sectionHeader("Session 3","Making an Impact: How to Share Your Science.")}<section class="panel"><ul class="clean-list"><li>The 12-12-24 presentation rule: 12 slides, 12 minutes, 24+ point font.</li><li>Great presentation keys: master your content, design for clarity, and engage with a story.</li><li>Poster advice: logical flow, powerful title, prioritize visuals, and add a QR code.</li></ul></section><section class="embed-card"><iframe class="video-frame" src="https://www.youtube.com/embed/yxlS9r-hmyo" title="Session 3" allowfullscreen></iframe></section>`,
  "ai-index": () => `${sectionHeader("AI index","A reproduced directory of AI platforms and tools listed on the original site.")}<section class="service-grid">${aiServices.map(([name, meta, desc, url]) => `<article class="service-card"><h4>${name}</h4><p class="service-meta">${meta}</p><p>${desc}</p><a class="btn btn-secondary" href="${url}" target="_blank" rel="noreferrer">Visit ${name}</a></article>`).join("")}</section>`,
  publications: () => `${sectionHeader("Research Portfolio","Publications and DOI links reproduced from the original website.")}<section class="publication-list">${publications.map((item) => item.doiList ? `<article class="publication-item"><h3>${item.title}</h3><p class="muted">${item.authors} • ${item.journal}</p><div class="button-row">${item.doiList.map((doi) => `<a class="btn btn-secondary" href="${doi}" target="_blank" rel="noreferrer">${doi.replace("https://doi.org/", "DOI ")}</a>`).join("")}</div></article>` : `<article class="publication-item"><h3>${item.title}</h3><p>${item.authors}</p><p class="muted">${item.journal}</p><a class="btn btn-primary" href="${item.doi}" target="_blank" rel="noreferrer">Open DOI</a></article>`).join("")}</section>`,
  highlights: () => `${sectionHeader("Highlights","Professional milestones, workshops, recognitions, and certifications.")}<section class="highlight-list">${highlights.map((item, index) => `<article class="highlight-item"><span class="tag">Highlight ${index + 1}</span><p>${item}</p></article>`).join("")}</section>`,
};

function renderNav() {
  nav.innerHTML = navigation.map((item) => item.children ? `<div class="nav-group"><button type="button">${item.label}</button><div class="nav-children">${item.children.map((child) => `<a class="nav-link" data-page="${child.id}" href="#/${child.id}">${child.label}</a>`).join("")}</div></div>` : `<a class="nav-link" data-page="${item.id}" href="#/${item.id}">${item.label}</a>`).join("");
}
function getCurrentPage() { const id = window.location.hash.replace("#/", "") || "home"; return pages[id] ? id : "home"; }
function renderPage() {
  const current = getCurrentPage();
  app.innerHTML = pages[current]();
  document.querySelectorAll(".nav-link").forEach((link) => link.classList.toggle("active", link.dataset.page === current));
  if (window.innerWidth <= 1100) sidebar.classList.remove("open");
}

menuToggle.addEventListener("click", () => sidebar.classList.toggle("open"));
window.addEventListener("hashchange", renderPage);
window.addEventListener("resize", () => { if (window.innerWidth > 1100) sidebar.classList.remove("open"); });
renderNav();
renderPage();
