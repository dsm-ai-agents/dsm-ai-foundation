# Collection folder migration

The repository now supports multiple research collections. Existing images, source catalogs, topic IDs, and review records were preserved; image bytes were not changed.

| Previous location | Current location |
| --- | --- |
| Root project brief | [AI Foundations README](../collections/ai-foundations/README.md) |
| `production/` | `collections/ai-foundations/production/` |
| `assets/chapters/` | `collections/ai-foundations/visuals/chapters/` |
| `assets/pilot/` | `collections/ai-foundations/visuals/pilot/` |
| `references/` | `collections/ai-foundations/research/references/` |
| `deliverables/` | `collections/ai-foundations/exports/` |
| `research/100-ai-income-opportunities/` | `collections/ai-income-opportunities/research/` |
| `assets/ai-income/` | `collections/ai-income-opportunities/visuals/` |
| `assets/ai-income/build_gallery.py` | `collections/ai-income-opportunities/production/build_gallery.py` |

Internal navigation and active build scripts use the new layout. Previously shared GitHub paths should be updated using this table; old files remain available in Git history. Keep each collection's folder structure intact when copying it locally. Pull the updated repository normally; this is a regular commit, not a repository rename or a history rewrite.

The existing image galleries remain local HTML. Detailed articles and public educational web pages are future work. Historical generation paths in provenance records may refer to the machine where an image was made; those are not deployment paths or required local inputs.
