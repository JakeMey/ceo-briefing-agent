CEO DAILY BRIEFING AGENT – ARCHITECTURE (1-PAGE)
=================================================

PROBLEM STATEMENT
-----------------
CEO receives 100+ emails daily. Needs a daily briefing of:
- Must-respond items (with reasons why)
- Suggested actions for each priority
- KPIs (future scope)

HIGH-LEVEL ARCHITECTURE
-----------------------
[Outlook] -> [Microsoft Graph API] -> [Python Script] -> [Gemini AI] -> [Briefing.md]
              (REST)                  (Agent)           (2.5 Flash)     (Markdown)

SPECIFIC REST ENDPOINTS
-----------------------
Microsoft Graph API (Outlook)
Base URL: https://graph.microsoft.com/v1.0

| Purpose                    | Endpoint                                                    |
|----------------------------|-------------------------------------------------------------|
| Fetch unread emails        | GET /me/messages?$filter=isRead eq false                    |
| Limit to 30 results        | &$top=30                                                    |
| Sort newest first          | &$orderby=receivedDateTime desc                             |
| Select specific fields     | &$select=subject,from,receivedDateTime,bodyPreview          |

Complete working URL:
GET https://graph.microsoft.com/v1.0/me/messages?$filter=isRead eq false&$top=30&$orderby=receivedDateTime desc&$select=subject,from,receivedDateTime,bodyPreview

Authentication Header:
Authorization: Bearer {ACCESS_TOKEN}

Google Gemini API
Model: gemini-2.5-flash
Authentication: API Key via .env file

DATA FLOW (STEP-BY-STEP)
------------------------
1. User runs: python agent.py
2. Script loads API keys from .env file
3. Script calls Graph API with Bearer token
4. Microsoft returns JSON array of unread emails
5. Script extracts: sender, subject, body preview
6. Script formats emails into an LLM prompt
7. Script sends prompt to Gemini API
8. Gemini returns priority analysis (top 3 + actions)
9. Script saves briefing as briefing_YYYY-MM-DD_HH-MM.md
10. User opens markdown file to read daily briefing

REALISTIC MVP SCOPE
-------------------
✅ IN SCOPE (Working Now):
- Outlook email ingestion
- Unread email filter  
- Gemini AI prioritization
- Top 3 urgent items with reasons
- Suggested actions for each
- Markdown output file
- Environment variable config (.env)
- Virtual environment (venv)
- Git version control + GitHub

❌ OUT OF SCOPE (Future Versions):
- Teams chat ingestion
- Real-time listening
- Email delivery to CEO
- Automated daily schedule
- KPI dashboard integration
- Learning from feedback

SECURITY & PRIVACY
------------------
| Concern              | Mitigation                                    |
|----------------------|-----------------------------------------------|
| Email exposure       | Process in memory, no storage                 |
| API keys in code     | .env file + .gitignore                        |
| Graph token expiry   | Fresh token required hourly (temp solution)   |
| Production security  | OAuth 2.0 with refresh token (add in V2)      |
| Data retention       | Briefings stored locally only                 |

COST ESTIMATE (PRODUCTION)
--------------------------
| Service                    | Per Day      | Per Month    |
|----------------------------|--------------|--------------|
| Microsoft Graph API        | $0 (included)| $0           |
| Gemini API (2.5-flash)     | ~$0.001      | ~$0.03       |
| GitHub Actions (CI/CD)     | $0           | $0           |
| Hosting (optional EC2)     | ~$0.01       | ~$0.30       |
| TOTAL                      | ~$0.01       | ~$0.33       |

SUCCESS CRITERIA
----------------
[x] Script runs without errors
[x] Fetches real emails via Graph API
[x] Gemini returns structured priority list
[x] Briefing saved as readable markdown
[x] Tested with 10+ real emails
[ ] CEO validates usefulness (pending feedback)

KEY FILES IN PROJECT
--------------------
| File                    | Purpose                                    |
|-------------------------|--------------------------------------------|
| agent.py                | Main Python script                         |
| .env                    | API keys and tokens (NOT in git)           |
| .env.example            | Template for secrets (in git)              |
| requirements.txt        | Python dependencies                        |
| briefing_*.md           | Generated daily briefings                  |
| ARCHITECTURE.md         | This document                              |

NEXT DEVELOPMENT PRIORITIES
---------------------------
1. Teams chat integration
2. Daily automation via cron/GitHub Actions
3. Email delivery to CEO
4. Production OAuth (no token expiry)

---
Document version: 1.0 | Status: WORKING DEMO | Date: 2026-05-14