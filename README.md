# Mohammad Abdulwahhab Academic Website

A modern rebuilt version of the academic website for Mohammad Abdulwahhab. The project keeps the original page structure, preserves the bilingual academic tone, and lifts embedded apps, videos, and resource links into a cleaner static site that can be deployed on free hosting.

## Folder structure

```text
mohammad-abdulwahhab-site/
|-- assets/
|   |-- site.css
|   `-- site.js
|-- embeds/
|   `-- generated interactive mini-apps and workshop materials
|-- home/
|   `-- index.html
|-- learn-organic-chemistry/
|   |-- index.html
|   |-- basics-of-organic-chemistry/
|   |   `-- index.html
|   |-- organic-i/
|   |   `-- index.html
|   |-- organic-ii/
|   |   `-- index.html
|   `-- organic-iii/
|       `-- index.html
|-- apps-for-academics/
|   |-- index.html
|   |-- my-apps-for-academics/
|   |   `-- index.html
|   |-- mark-list-maker/
|   |   `-- index.html
|   |-- attendane-export/
|   |   `-- index.html
|   `-- sample-key-generator/
|       `-- index.html
|-- apps-for-students/
|   |-- index.html
|   |-- woodward-fieser-lmax-calculator/
|   |   `-- index.html
|   |-- nomenclature/
|   |   `-- index.html
|   `-- elemental-analysis/
|       `-- index.html
|-- publications/
|   `-- index.html
|-- scientific-research-workshop/
|   |-- index.html
|   |-- session-1/
|   |   `-- index.html
|   |-- session-2/
|   |   `-- index.html
|   `-- session-3/
|       `-- index.html
|-- ai-index/
|   `-- index.html
|-- highlights/
|   `-- index.html
|-- scripts/
|   `-- generate_site.py
|-- index.html
|-- package.json
`-- vite.config.js
```

## Local setup

1. Make sure Python 3 is available as `py -3`.
2. Regenerate the site if needed:

```bash
py -3 scripts/generate_site.py
```

3. Optional local dev server with Vite:

```bash
npm install
npm run dev
```

If you do not want Node tooling, you can also serve the folder directly with any static server.

## Build steps

```bash
npm install
npm run build
```

Vite outputs the production build into `dist/`.

## Deployment

### Vercel

1. Import the repository into Vercel.
2. Use `npm run build`.
3. Set the output directory to `dist`.

### Netlify

1. Connect the repository.
2. Build command: `npm run build`
3. Publish directory: `dist`

### GitHub Pages

1. Run `npm run build`.
2. Publish the contents of `dist/` to your Pages branch.
3. Because the site is multi-page static HTML instead of a client-side SPA, no special 404 router workaround is needed.

## How to update content later

1. Refresh or recrawl the source into the raw HTML dump directory.
2. Run:

```bash
py -3 scripts/generate_site.py --source ../mohammad-site-raw
```

3. Review the generated `embeds/` files if the embedded HTML changed.

## How embeds and links are handled

- YouTube videos are rebuilt as responsive iframes.
- Embedded mini-apps and workshop materials stored inside `data-code` blocks are written into standalone files under `embeds/` and loaded through iframes.
- External live tools discovered via `data-url` attributes are embedded with sandboxing and also exposed with an `Open in new tab` button.
- The original private visitor counter on the home page is intentionally omitted.

## Migration checklist

- [x] Home
- [x] Learn Organic Chemistry
- [x] Basics of Organic Chemistry
- [x] Organic-I
- [x] Organic-II
- [x] Organic-III
- [x] Apps for Academics
- [x] Mark List Maker
- [x] Grades & Attendance Sync
- [x] Sample Key Generator
- [x] My Apps for Academics
- [x] Apps for Students
- [x] WoodWard-Fieser λmax Calculator
- [x] Nomenclature
- [x] Elemental Analysis
- [x] Publications
- [x] Scientific Research Workshop
- [x] Session 1
- [x] Session 2
- [x] Session 3
- [x] AI index
- [x] Highlights
- [x] Social/profile links
- [x] Download links
- [x] YouTube embeds
- [x] Embedded apps or closest working reconstruction
