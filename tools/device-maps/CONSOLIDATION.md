# One public browsing hub

`docs/modbus-device-maps/index.md` is the public browsing hub. The retired `products/xpf/device-maps/index.md` path is owned by the exact redirect in `mkdocs.yml`; its descendant guides keep their URLs.

The source of public previews is the separate `Modbus-Monitor/modbus-device-maps` repository. Do not maintain a second catalog or copy private CSV sources into this repository. Refresh generated Markdown using:

```sh
python tools/device-maps/build_public_previews.py --catalog-root ../modbus-device-maps
mkdocs build --strict
python tools/device-maps/validate_consolidation.py --site-dir site
```

The generator preserves established guide paths and sample tables, adds public JSON provenance, and creates preview-only pages for entries without a published guide. It records source SHA-256 values and exact redirect destinations in `consolidation-manifest.json`. Generated pages are committed so regular MkDocs builds work offline. Review changes against the source catalog before copying the manifest to `html-redirects.json` in the public data repository.

Preview count and unique guide count are separate, overlapping inventories. Neither establishes a complete in-app inventory. Model display names and IDs are preserved even where the source names need later review.

The older private-CSV guide generator still creates device guides, but no longer writes either browsing hub. After publishing a guide batch, explicitly refresh this public catalog view; do not automatically infer a new catalog ID from a display name.

Deploy docs first. The public data repository's Pages workflow checks every live docs destination before applying source redirects. The organization homepage is a third repository and should be deployed last. See the private pre-commit report for live baseline evidence, release order, external-site link changes and remaining runtime checks.
