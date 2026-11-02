# Pedro Vega | Technical writing and UX portfolio

[![Portfolio](https://img.shields.io/badge/Live_Portfolio-pvega62.github.io-blue?style=for-the-badge&logo=githubpages)](https://pvega62.github.io/)
[![Software Docs](https://img.shields.io/badge/Software_Docs-Docusaurus-228b22?style=for-the-badge&logo=docusaurus)](https://pvega62.github.io/software)
[![Linted with Vale](https://img.shields.io/badge/Linted_with-Vale-brightgreen?style=for-the-badge)](https://vale.sh)

Welcome to my portfolio. It covers technical writing and UX writing work.

This repo contains the site, the manuals, and the samples. The developer docs are in a separate project. The API reference is in that project too.

---

## 🚀 Live sites and documentation portals

| Portal | Format / Platform | Description | Link |
|:---|:---|:---|:---|
| **Portfolio Homepage** | Custom HTML / CSS / JS | Central hub featuring all samples, background, and navigation. | [pvega62.github.io](https://pvega62.github.io/) |
| **Software Documentation** | Docusaurus (Docs-as-Code) | REST APIs, SDK tutorials, data routing guides, and Algolia AskAI search. | [pvega62.github.io/software](https://pvega62.github.io/software) |
| **Hardware Technical Writing** | Interactive PDF Viewer | Selected commercial, consumer, and medical hardware manuals and guides. | [Hardware Samples](https://pvega62.github.io/technical-writing-hardware) |
| **UX Writing & Content Design** | UI Flows & Microcopy | Microcopy for onboarding, error states, alert copy, and subscription copy. | [UX Writing Samples](https://pvega62.github.io/uxwriting) |
| **Articles** | Publications & Commentary | Technology journalism, humanitarian policy analysis, and reporting. | [Articles](https://pvega62.github.io/articles) |
| **Recordkeeping** | Static Site | Specialized tracking and documentation project. | [Recordkeeping](https://pvega62.github.io/Recordkeeping/) |
| **Resume (PDF)** | Downloadable PDF | Up-to-date resume covering four years of technical writing experience. | [Pedro Vega Resume](https://pvega62.github.io/Pedro%20Vega%20Resume.pdf) |

---

## 📚 Portfolio showcase and documentation samples

### 1. 💻 Software and developer documentation ([Docusaurus portal](https://pvega62.github.io/software))
I took this docs set off a traditional wiki. It now runs as a version-controlled **Docs-as-Code** site on Docusaurus. It runs in seven languages, from English and Spanish to Japanese and Hindi, plus custom Algolia/AskAI search:

* **TypeScript SDK (Sui Blockchain):** complete developer tutorial and API reference for querying object data and constructing transactions with the `SuiClient`.
* **Data Pipelines & Cloud Observability:** step-by-step guides for routing app logs to Datadog log pipelines and tracing LLM app calls with Galileo.
* **Stripe API Documentation:** endpoint reference and walkthrough tutorials for integrating Payment Intents and Refunds, plus the Balance endpoint.
* **Petstore API (OpenAPI / Swagger):** endpoint reference for every schema in the OpenAPI definition with sample request and response payloads.
* **Developer Cookbooks & Tooling:** guides for configuring Postman mock servers and automating editorial linting with Vale. Also covers editing Markdown wiki content in Microsoft Word.

### 2. 🛠️ Hardware technical writing ([Hardware portal](https://pvega62.github.io/technical-writing-hardware))
Selected samples from my work at Felix Storch, Inc. I was Lead Technical Writer there, covering five brands across commercial, consumer, and medical lines:

* **EQTemp Vaccine Storage Refrigerator User Manual:** temperature monitoring and alarm logic for clinical vaccine storage.
* **Frost-Free Warming and Cooling Drawer (SPHC30/SPHC36):** temperature control and Sabbath mode configuration, plus installation steps.
* **ADA Compliance Instructions:** switch installation and refrigerator conversion guides that meet Americans with Disabilities Act standards.
* **InnoGear Aromatherapy Diffuser Manual:** ground-up rewrite of an ambiguous translation, with a redesigned manual layout.
* **MOMCUBE Breast Milk Freezer:** operational protocols and hazard warnings for hospital-grade storage, built to the CDC recommendations for storing breast milk.

### 3. 💬 UX writing and content design ([UX writing portal](https://pvega62.github.io/uxwriting))
Copy that helps users finish a task without friction. The portal shows 18 projects, and every one fits a real character limit:

* **Banking app onboarding (Paymate):** onboarding microcopy for account creation and automated bill payment, written to a 45/100/25 character limit.
* **Error states:** five error messages, from an unknown-cause app crash to an expired card or a rejected email address.
* **Alert copy:** three notification samples including a flight cancellation and a fire alert.
* **Subscription and meta copy:** five pieces spanning subscription page titles and grocery or concert promotions.
* **Content patterns:** the shared voice and tone rules behind those projects.

### 4. 📰 Articles and journalism ([Articles portal](https://pvega62.github.io/articles))
Long-form reporting on tech, aid policy, health, and ethics.

* **Technology journalism:** *"4 Ways to Use Tech Against the Pandemic"* and *"The Samsung Global Goals App."* The second piece explains how the app advances the UN Sustainable Development Goals.
* **The Borgen Project:** investigated international poverty and humanitarian policy across Latin America and the Caribbean.
* **[Pop philosophy](https://pvega62.github.io/software/blog/pop-philosophy):** a 3,000-word essay on the docs blog that reads *Marvel's Civil War* through Kantian deontology and utilitarianism.

---

## 🛠️ Technical skills and workflow

```text
Docs-as-Code Workflow:
[Markdown / TSX] ➔ [Git Branching] ➔ [Vale Linting] ➔ [Docusaurus Build] ➔ [GitHub Pages CI/CD]
```

* Apply docs-as-code workflows, information architecture, single-sourcing, and Agile delivery on every project.
* Write in **Markdown**, HTML5, CSS3, JavaScript, TypeScript, JSON, and YAML.
* Publish with Docusaurus, Git and GitHub, GitLab, Postman, Swagger, Notion, and Confluence.
* Lint prose with Vale, configured for active voice and a 25-word sentence cap.
* Add search with Algolia DocSearch and the AskAI Sidepanel. Automate repeat tasks through the Model Context Protocol (MCP) and the Gemini command-line tool.
* Produce diagrams and screens in Figma and Snagit, plus the Adobe Creative Suite (InDesign, Illustrator, Acrobat).
* Test locally in Docker and from the Linux command line. Edit in VS Code.

---

## 📂 Repository structure

```text
├── /                          # Root portfolio website
│   ├── index.html             # Homepage
│   ├── aboutme.html           # Professional biography and background
│   ├── technical-writing-hardware.html # Hardware documentation showcase
│   ├── uxwriting.html         # UX writing and content design samples
│   ├── articles.html          # Articles and publications
│   ├── search.html            # Algolia DocSearch verification page
│   ├── Pedro Vega Resume.pdf  # Downloadable resume
│   ├── es/ fr/ ar/ hi/ ja/ zh/ # Localized copies of every page, including search.html
│   ├── css/                   # Component and page-specific stylesheets
│   ├── styles/ styles.css     # Shared theme stylesheets
│   ├── js/                    # Search, modal viewers, and navigation scripts
│   ├── fonts/                 # Self-hosted typefaces and flag icons
│   ├── samples/               # PDF documentation samples
│   ├── scripts/               # Local preview server and clean-URL middleware
│   ├── sitemap.xml            # Search engine URL index
│   ├── README.md              # This file
│   └── images/                # Site assets, logos, and previews
└── (External repositories)
    ├── /software              # Docusaurus software documentation portal
    └── /Recordkeeping         # Recordkeeping documentation project
```

---

## 🖥️ Local preview

GitHub Pages serves clean URLs. A request for `/uxwriting` maps to `uxwriting.html`. The preview server does the same on your machine:

```bash
cd pvega62.github.io
node scripts/preview.mjs
```

The server runs at `http://localhost:8080` and reloads the browser after each edit. Set `PORT` to move the port, and set `NO_OPEN=1` to skip the browser launch:

```powershell
$env:PORT="8081"; node scripts/preview.mjs
```

`scripts/clean-urls.js` maps extensionless paths such as `/uxwriting` to the matching `uxwriting.html`. It skips requests that end in `/` or include a file extension.

---

## 🏆 Key accomplishments

* **Authored extensive documentation sets:** wrote and updated hardware manual catalogs and developer quickstarts, plus full API reference sets.
* **40% faster production times:** designed and implemented reusable modular document templates.
* **Global market expansion:** translated 25+ technical guides and UI flows into Spanish and French.
* **Automated editorial quality:** integrated Vale linting into automated local and CI/CD pipelines to enforce active voice and crisp readability.

---

## 📫 Contact

* **email:** [vega.pedro96@gmail.com](mailto:vega.pedro96@gmail.com)
* **LinkedIn:** [linkedin.com/in/pvega62](https://www.linkedin.com/in/pvega62/)
* **Portfolio:** [pvega62.github.io](https://pvega62.github.io/)
* **Software Docs:** [pvega62.github.io/software](https://pvega62.github.io/software)
