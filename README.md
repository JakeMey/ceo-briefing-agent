# CEO Briefing Agent

AI agent that fetches unread emails via Microsoft Graph API and generates a daily briefing using Google Gemini.

## Prerequisites

- Python 3.9+
- Microsoft account (for Graph API)
- Google account (for Gemini API)

## Quick Start

### 1. Clone the repository

git clone https://github.com/JakeMey/ceo-briefing-agent.git
cd ceo-briefing-agent

### 2. Create and activate virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

Mac/Linux:

python -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set up environment variables

cp .env.example .env

Then edit .env and add your actual API keys.

### 5. Run the agent

python agent.py

## Environment Variables

| Variable | Description |
|----------|-------------|
| GEMINI_API_KEY | Google Gemini API key (get from AI Studio) |
| GRAPH_ACCESS_TOKEN | Microsoft Graph temporary token (from Graph Explorer) |

## How to Get API Keys

### Gemini API Key (Free)
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (starts with AIza...)

### Microsoft Graph Token (Temporary)
1. Go to https://developer.microsoft.com/en-us/graph/graph-explorer
2. Sign in with your Microsoft account
3. Click the "Access Token" tab
4. Copy the token (starts with eyJ...)

## Security

- Never commit .env or real tokens to git
- Use .env.example as a template
- Tokens expire in 60 minutes — refresh as needed
- This script processes emails in memory only — no storage

## Project Structure

ceo-briefing-agent/
|-- .gitignore # Excludes secrets, venv, etc.
|-- .env.example # Template for secrets (safe to commit)
|-- LICENSE # MIT license
|-- README.md # This file
|-- requirements.txt # Python dependencies
`-- agent.py # Main agent script

## Sample Output

# CEO Daily Briefing
**Generated:** 2026-05-14 10:30
**Emails analyzed:** 8

## TOP 3 MUST-RESPOND

1. cfo@company.com | Q3 Budget Approval
   WHY: Board approval needed by 3pm today

2. legal@company.com | Contract Review
   WHY: Client waiting on signature

3. sales@company.com | Deal X Pricing
   WHY: $450k deal closes tomorrow

## SUGGESTED ACTIONS

1. Reply to CFO: "Approved, sending to board"
2. Sign contract via DocuSign link
3. Approve pricing in Salesforce

## Troubleshooting

| Error | Solution |
|-------|----------|
| ModuleNotFoundError | Run: pip install -r requirements.txt |
| GEMINI_API_KEY not found | Check that .env file exists and has the key |
| Access token is empty | Paste your Graph token in .env |
| InvalidAuthenticationToken | Token expired — get a fresh one from Graph Explorer |
| No unread emails found | Send yourself a test email and run again |

## Next Steps (Production)

- Add Teams chat integration
- Automate with cron / GitHub Actions
- Deploy to AWS EC2 or Azure
- Switch to OpenAI/Claude per preference

## License

MIT License - Copyright (c) 2026 JakeMey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.