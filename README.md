# TalentLens

AI-powered resume screening and ranking system for recruiters.

## Architecture

- `app/`: FastAPI API, resume parsing, ranking pipeline, and recruiter dashboard
- PostgreSQL: candidate, job, and screening persistence
- ChromaDB: embeddings and semantic retrieval
- API-based LLM: skill extraction and explanation layer
- Docker Compose: local orchestration for the complete stack

## Run locally

### Application

```powershell
cd "AI-Powered Resume Screening & Ranking System"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000 for the recruiter dashboard.
API docs are available at http://localhost:8000/docs.

### Verify the installation

With the server running in one terminal, run these commands in another:

```powershell
python test_pipeline.py
python test_api.py
```

The first pipeline run downloads the `all-MiniLM-L6-v2` embedding model and caches it locally.

Resume uploads are limited to 200 MB per file. Files over that limit are rejected before parsing.

The health endpoint can be checked with:

```powershell
Invoke-WebRequest http://localhost:8000/health -UseBasicParsing
```

### Docker

```powershell
docker compose up --build
```

Set `LLM_API_KEY` in the shell or a `.env` file when connecting the production LLM adapter.
