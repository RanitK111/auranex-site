# Auranex website (kkgmedia.in)

Static website for **Auranex**, an AI receptionist for US HVAC, plumbing, dental, roofing and medspa businesses. Operated by KKG Media. No framework or build step is needed to host it. GitHub Pages serves the `.html` files directly.

## Put it live on GitHub Pages

1. Create a new GitHub repository (for example `auranex-site`), public or private (private Pages needs a paid plan).
2. Upload everything in this folder to the repository root (drag and drop on github.com works), or from a terminal:
   ```bash
   cd auranex-site
   git init
   git add .
   git commit -m "Auranex website"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/auranex-site.git
   git push -u origin main
   ```
3. In the repository go to **Settings → Pages**. Under **Build and deployment** choose **Deploy from a branch**, branch `main`, folder `/ (root)`, then Save.
4. Under **Custom domain** enter `www.kkgmedia.in` and Save. (The `CNAME` file already contains this.) Tick **Enforce HTTPS** once it becomes available.

## DNS records at your domain registrar

| Type  | Host | Value |
|-------|------|-------|
| CNAME | `www` | `YOUR-USERNAME.github.io` |
| A     | `@`   | `185.199.108.153` |
| A     | `@`   | `185.199.109.153` |
| A     | `@`   | `185.199.110.153` |
| A     | `@`   | `185.199.111.153` |

Remove any old A/CNAME records that point `@` or `www` somewhere else (for example the host of the current NeverMiss AI site). DNS can take from a few minutes to 24 hours. GitHub's current IP list is in their docs under "Managing a custom domain for your GitHub Pages site".

## Editing the site

All pages are generated from `tools/build.py` (layout, home, industries, pricing, contact) and `tools/legal.py` (legal pages). Change text or settings there, then run:

```bash
python3 tools/build.py
```

and commit the regenerated `.html` files. Settings at the top of `build.py`: email, Instagram, Calendly link, domain, form address.
Styles are in `assets/css/style.css`.

Preview locally: `python3 -m http.server 8000` and open http://localhost:8000.

## Things to check before launch

- **Contact form** posts to FormSubmit (`formsubmit.co`). The first time anyone submits it, FormSubmit emails `kkgmedia1@gmail.com` a one-time confirmation link. Click it, or the form will not deliver.
- **Calendly** link is `https://calendly.com/kkgmedia1/30min` (same as the old site).
- **Instagram** link is `@auranex.ai`.
- **Legal pages** are sensible drafts, not legal advice. Have a lawyer review them, especially the HIPAA wording for dental and medspa clients, US call-recording and SMS (TCPA) rules, and the India governing-law clause.
- **Search Console**: the Google verification tag from the old site is kept in every page. Submit `https://www.kkgmedia.in/sitemap.xml`.
- Old NeverMiss AI pages used the same file names (`how-it-works.html`, `pricing.html`, `contact.html`, `book-demo.html`, legal pages), so existing links keep working.
