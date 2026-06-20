# HAICHI Marketing Site

Static landing page for the HAICHI Windows self-hosted product.

Preview from the repository root:

```powershell
.\.venv\Scripts\python.exe -m http.server 8080
```

Open `http://127.0.0.1:8080/site/`.

Place the current Windows release in `downloads/` for local preview. Before public deployment, replace the local download link in `index.html` with the public release URL and add the production domain as the canonical URL.
