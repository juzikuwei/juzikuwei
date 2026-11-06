# Profile artwork

The profile uses an original citrus/workbench identity derived from `juzikuwei`, with a warm paper, terracotta, and brown palette requested by the owner. Artwork is repository-local SVG; no remote fonts, scripts, or image-generation services are required.

## References studied

- https://github.com/innng/innng — a personal visual motif carried through the introduction.
- https://github.com/anuraghazra/anuraghazra — an introduction grounded in actual work.
- https://github.com/adamalston/adamalston — a custom visual composition rather than a badge collection.
- https://github.com/MaxRohowsky/best-github-profile-readme — discovery gallery.

These informed the approach; no artwork or copy was reused.

## Editing

Run `python scripts/build-profile-assets.py` to regenerate the header, project illustrations, and process panels in both languages. Colors and type roles are defined in the script. The older mental-model diagrams are maintained separately.

The README keeps descriptions and links as native text so the page remains useful at narrow widths, with images unavailable, or with a screen reader. SVG text uses system font fallbacks. GitHub controls the surrounding page theme; the warm background is contained within the artwork.

## Validation

Check SVG XML, local image references, Markdown rendering through GitHub's API, and rendered artwork for text collisions. Keep visual QA outputs outside the repository.
