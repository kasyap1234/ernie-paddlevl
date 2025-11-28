# Ernie - OCR Processing Web App

This project uses PaddleOCR-VL to perform OCR on the first 2 pages of the "Attention Is All You Need" paper and displays the results on a web page.

## Features

- OCR processing using PaddleOCR-VL
- Extracts and processes only the first 2 pages of PDFs
- Clean web interface rendering the OCR results
- Automatic deployment to GitHub Pages

## Setup

1. Install dependencies:
   ```bash
   uv install
   ```

2. Run OCR processing:
   ```bash
   uv run main.py
   ```

3. Test the web page locally:
   ```bash
   python3 -m http.server 8000
   ```
   Then visit `http://localhost:8000`

## GitHub Pages Deployment

1. Create a new repository on GitHub
2. Add the remote:
   ```bash
   git remote add origin https://github.com/yourusername/yourrepo.git
   git push -u origin master
   ```

3. Enable GitHub Pages in repository settings:
   - Go to Settings > Pages
   - Select "GitHub Actions" as the source
   - The site will be available at `https://yourusername.github.io/yourrepo/`

## Files

- `main.py` - OCR processing script
- `index.html` - Web page displaying results
- `output.md` - OCR results in markdown format
- `.github/workflows/deploy.yml` - GitHub Pages deployment workflow


# ernie-paddlevl
