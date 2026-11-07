# vinebuzz-media (public, media only)

Public media + GitHub Pages host for VineBUZZ client pages and previews. **No client data, settings, alerts or sources here** — those live in the private vinebuzz-config repo.

| Path | What |
| :-- | :-- |
| `brand/vinedentity/` | Vinedentity logos: `vinedentity-v-icon.png` (1167x1167, transparent), `vinedentity-full-logo-transparent.png` (2576x730, for dark backgrounds), `vinedentity-full-logo-original-white-bg.png` (source, 8000x2284) |
| `brand/partners/` | Authorized partner logos (only with permission noted in the client's Brand-Kit, spec 3.4) |
| `assets/vinebuzz.css` | Shared styles for client pages |
| `templates/client-page/index.html` | [Business] VineBUZZ page template; runs copy it to clients/{page_token}/ with a data.json |
| `clients/` | Per-client page + preview folders, unguessable paths (11.3, 42.2) |
| `robots.txt`, `index.html` | Crawlers blocked; every page carries `noindex` |
| `.nojekyll` | Serve files as-is on GitHub Pages |

Videos are not stored here; they live in each client's VineHUB Media Storage (11.2).
