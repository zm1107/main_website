# Weibaba Software · Product Home

#README #Website #Home

[中文](README.md)

<p align="center"><img src="assets/img/logo.png" alt="Weibaba Software logo" width="96" height="96"></p>

**Weibaba Software** is the portfolio home for all software products developed by Weibaba: an entry hub where every product has its own official website.

![Type: static](https://img.shields.io/badge/type-static-blue) ![Privacy: zero-tracking](https://img.shields.io/badge/privacy-zero--tracking-green) ![Languages: zh/en](https://img.shields.io/badge/languages-zh%2Fen-yellow)

> Note: the badge images above are shields.io links used in this README only; the site pages themselves make zero external requests (see `AGENTS.md` for the site red lines).

## About this repository

- Hosts the Weibaba Software product home: six released products (JustForShow, PassGone, PrivarMask, ExifMate, ForceSplit, SourceLens) plus FinFlowScope (in development).
- Pure static, zero tracking, no JavaScript; structure and red lines follow rules/release.md 9.3 and rules/website.md.
- Product wording and design decisions are governed by `docs/site-design.md`; documentation changes come before code changes.

## Site structure

```text
main_website/
├── index.html              # Chinese home
├── en/                     # English version (incl. en/privacy/)
├── privacy/                # Privacy policy (Chinese)
├── assets/
│   ├── style.css           # the only stylesheet
│   └── img/                # logo.png, og.png
├── favicon.ico | favicon.png | apple-touch-icon.png   # all derived by tools/make_icons.py
├── robots.txt | sitemap.xml | _headers | .well-known/security.txt
├── tools/make_icons.py     # icon generator (the single design source)
├── main_website.cmd        # project launch command
├── docs/site-design.md     # requirements, design and decision record (with version table)
└── README.md | README.en.md | AGENTS.md
```

## Run locally

Preferred: run `main_website.cmd` in the repository root (project convention). It starts a local server via the `main_website` conda environment and opens `http://127.0.0.1:8080/`; if the environment is missing it prompts to create one with `conda create -n main_website python=3.13`.

Alternative: `conda run -n main_website --no-capture-output python -m http.server 8080 --bind 127.0.0.1`

## Repository and commit conventions

- Daily work on `dev`; releases merge into `main` with a lightweight tag (global rule 3).
- Commit messages contain only the version number (e.g. `v1.2.0`); changes are recorded in the version table of `docs/site-design.md`.
- Pushing to NAS is unrestricted; GitHub pushes are limited to website repositories with user-confirmed addresses (global rule 15.3).

## Privacy

This site collects nothing: no analytics, no cookies, no forms. See the [privacy policy](privacy/); each product's privacy policy lives at its own website under `/privacy/`.
