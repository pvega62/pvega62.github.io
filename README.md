# Pedro Vega | Technical Writer and UX Writer

[![Portfolio](https://img.shields.io/badge/Portfolio-pvega62.github.io-1f3a5f?style=flat-square)](https://pvega62.github.io/)
[![Software Docs](https://img.shields.io/badge/Software_Docs-Docusaurus-228b22?style=flat-square)](https://pvega62.github.io/software)
[![Languages](https://img.shields.io/badge/Languages-7-5b5b5b?style=flat-square)](https://pvega62.github.io/)
[![Linted with Vale](https://img.shields.io/badge/Linted_with-Vale-brightgreen?style=flat-square)](https://vale.sh)
![Updated](https://img.shields.io/badge/Updated-November_2026-6b7280?style=flat-square)

I write software documentation, hardware manuals, and product copy. This repo contains the portfolio site and the work behind it. The Docusaurus portal and the Sweepy docs have their own repos.

---

## Live sites

| Site | What it covers | Link |
|:--|:--|:--|
| **Portfolio homepage** | Every project, the background pages, and contact details. | [pvega62.github.io](https://pvega62.github.io/) |
| **Software documentation** | Docusaurus portal with nine docs sets, Algolia DocSearch, and AskAI. Serves 7 languages. | [pvega62.github.io/software](https://pvega62.github.io/software) |
| **Blog** | Posts on documentation, AI tooling, and pop culture. | [pvega62.github.io/software/blog](https://pvega62.github.io/software/blog) |
| **Hardware manuals** | Commercial, consumer, and medical manuals in an interactive PDF viewer. | [Technical writing samples](https://pvega62.github.io/technical-writing-hardware) |
| **UX writing** | Microcopy projects, content patterns, and two bonus print designs. | [UX writing samples](https://pvega62.github.io/uxwriting) |
| **Articles** | Published pieces on technology, aid policy, and health. | [Articles](https://pvega62.github.io/articles) |
| **Recordkeeping** | Vinyl catalog built from scratch in HTML, CSS, and JavaScript. | [Recordkeeping](https://pvega62.github.io/Recordkeeping/) |
| **Resume** | Two-page PDF. | [Pedro Vega Resume](https://pvega62.github.io/Pedro%20Vega%20Resume.pdf) |

---

## Documentation sets

The software portal runs on Docusaurus. Markdown sits in Git, Vale checks style on each change, and GitHub Actions deploys the build.

| Documentation set | Pages | What it covers |
|:--|--:|:--|
| **Automated job search with Sweepy** | 14 | Setup, YAML profiles, scoring rules, the command and configuration reference, developer reference, the MCP tool reference, and a scoring case study. |
| **Blüdhaven Pets API** | 14 | An OpenAPI 3.1 reference for intake, licensing, veterinary clearances, and adoption holds. Includes a Scalar console that sends live requests or runs a browser demo. |
| **Stripe API** | 21 | Payment Intents, Refunds, Balance, webhooks, idempotency, expansion, pagination, and test mode. |
| **Sui TypeScript SDK, end to end** | 6 | `SuiClient` concepts, object queries, owned objects, and a transaction walkthrough. |
| **Log and LLM observability** | 5 | Routing app logs to Datadog pipelines and tracing LLM calls in Galileo. Also covers Postman mock servers. |
| **Commit and PR write-ups** | 2 | Worked examples on NumPy memory order and JAX reductions. |

### Short sets

* **Ask Artie AI assistant case study.** The page shows the retrieval pipeline behind Ask Artie, the docs assistant.
* **Google Chrome theme installation.** A step-by-step guide, also published in Spanish.
* **Microsoft Word to GitHub wiki workflow.** Editors write wiki Markdown in Word through Writage.

### Build pipeline

Every change follows one path.

```text
Markdown ➔ Git branch ➔ Vale lint ➔ Docusaurus build ➔ GitHub Pages deploy
```

The portal runs in seven languages. Diagrams show how Sweepy moves a job post through five stages. Search matches the page language, with AI answers on top.

---

## Hardware technical writing

The hardware library collects my manuals from Felix Storch, Inc., where I was Lead Technical Writer. The set spans five brands across commercial, consumer, and medical lines.

* **EQTemp vaccine storage refrigerator.** Temperature monitoring and warning logic for clinical vaccine storage.
* **MOMCUBE freezer.** Operational protocols and hazard warnings for storing breast milk in a hospital setting. The manual follows CDC storage recommendations.
* **Frost-Free warming and cooling drawer (SPHC30/SPHC36).** Covers temperature control and Sabbath mode setup. Includes installation steps.
* **ADA compliance set.** Covers the ADRD18H34 conversion, handle installation, remote switch wiring, and ADA range hood instructions.
* **InnoGear aromatherapy diffuser.** A ground-up rewrite of an ambiguous translation, with a new manual layout.
* **PNR installation instructions.** Install steps and safety copy for commercial kitchen equipment.
* **Instant wardrobe changing sliding pole.** A bonus installation guide for the sliding pole accessory.

Seven of these manuals also appear in Spanish. Source Word files sit beside the PDFs.

---

## UX writing and content design

The UX section collects microcopy projects that fit real character limits. Each project pairs the copy with a rationale and an outcome.

* **Banking app onboarding (Paymate).** Account creation and automated bill payment, written to 45/100/25 character limits.
* **Error states.** The set covers an unknown app crash, crash recovery, an expired card, a rejected email, and a fake-name rejection.
* **Notification copy.** Notices cover a flight cancellation, a building fire, and a truck delay.
* **Subscription and meta copy.** Covers a subscription page for contact lenses, a grocery subscription, a sports fan app, a concert, and a rivalry score update.
* **Permission copy.** A car buying site asks for location access with one short prompt.
* **Content patterns.** The voice and tone rules behind every project.
* **Classroom hall passes.** Custom passes pair vintage comic art with a two-tone print layout, plus a working prototype.

---

## Articles and journalism

The articles page collects nine pieces on tech, aid policy, and health.

<!-- Microsoft.Vocab stays off for these titles. "Against" is part of a published headline. -->
<!-- vale Microsoft.Vocab = NO -->

* **Technology.** *4 Ways to Use Tech Against the Pandemic* and *The Samsung Global Goals App*, which explains how the app advances the UN Sustainable Development Goals.
* **The Borgen Project.** Reporting on poverty, hunger, gender equality, healthcare, and homelessness across the Dominican Republic, Puerto Rico, and Guyana.
* **Pop philosophy.** A 3,000-word essay that reads *Marvel's Civil War* through Kantian deontology and utilitarianism.
* **Docs blog.** *What building an AI documentation assistant taught me about technical writing*, plus four shorter posts.

<!-- vale Microsoft.Vocab = YES -->

---

## Skills and workflow

| Area | Tools and practice |
|:--|:--|
| **Documentation** | Docs-as-code, information architecture, single-sourcing, REST and OpenAPI, MCP integration, quickstarts, SOPs |
| **Authoring** | Markdown, HTML5, CSS3, JavaScript, TypeScript, JSON, YAML, React, Node.js, Bootstrap, Mermaid |
| **Publishing** | Docusaurus, GitHub and GitLab, Postman, Swagger, Notion, Confluence, Algolia |
| **Quality** | Vale with a custom style guide, active voice, a 25-word sentence cap, WCAG accessibility checks |
| **AI tooling** | Gemini and Claude for prompt design, MCP for localization and tooling, DeepL and Lara translation memory, Galileo, PyMuPDF, ReportLab |
| **Design** | Figma, Snagit, Adobe InDesign, Illustrator, and Acrobat |
| **Environment** | Git, Linux command line, Docker, VS Code |

---

## Repository layout

```text
pvega62.github.io/
├── index.html                    # Homepage
├── aboutme.html                  # Background, skills, and experience
├── technical-writing-hardware.html
├── uxwriting.html
├── articles.html
├── search.html                   # Algolia DocSearch verification
├── es/ fr/ ar/ hi/ ja/ zh/       # Localized copies of all six pages
├── css/                          # Shared, page-specific, and interactive styles
├── js/                           # Search, PDF viewer, navigation, transitions
├── fonts/                        # Self-hosted typefaces and flag icons
├── images/                       # Logos, icons, and previews
├── samples/
│   ├── articles-and-essays/      # Published article PDFs
│   ├── technical-writing/        # Hardware manuals, Spanish editions, Word sources
│   └── ux-writing/               # UX spec PDFs
├── scripts/                      # Local preview server and clean-URL middleware
├── .vale/ + .vale.ini            # Style packages and configuration
├── .github/workflows/            # Repository sync jobs
├── sitemap.xml
└── README.md
```

### Companion repositories

| Repository | Contents |
|:--|:--|
| [software-docs](https://github.com/pvega62/software-docs) | Docusaurus source for the software portal |
| [sweepy](https://github.com/pvega62/sweepy) | Job search engine written in Python, MIT license |
| [Recordkeeping](https://github.com/pvega62/Recordkeeping) | Vinyl collection catalog |

---

## Local preview

GitHub Pages serves clean URLs, so `/uxwriting` maps to `uxwriting.html`. The preview server does the same on your machine.

```bash
cd pvega62.github.io
node scripts/preview.mjs
```

The server runs at `http://localhost:8080` and reloads the browser after each edit. Change the port with `PORT`, and skip the browser launch with `NO_OPEN=1`.

```powershell
$env:PORT="8081"; node scripts/preview.mjs
```

`scripts/clean-urls.js` maps extensionless paths to the matching `.html` file. It skips requests that end in a slash or include a file extension.

---

## Selected results

* **Production time.** Modular document templates cut production time by 40 percent.
* **Global reach.** I translated 25+ technical guides and UI flows into Spanish and French. The portfolio now runs in 7 languages.
* **Editorial automation.** Vale gates enforce active voice and a 25-word sentence cap in local and CI pipelines.
* **Coverage.** I wrote API reference sets, SDK guides, hardware catalogs, and a product docs suite of 14 pages.

---

## Contact

Reach me at [vega.pedro96@gmail.com](mailto:vega.pedro96@gmail.com), or connect on [LinkedIn](https://www.linkedin.com/in/pvega62/). The live site is [pvega62.github.io](https://pvega62.github.io/), and the docs portal is [pvega62.github.io/software](https://pvega62.github.io/software).
