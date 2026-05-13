# CEO Briefing Agent

AI agent that fetches unread emails via Microsoft Graph API and generates a daily briefing using Google Gemini.

## Prerequisites

- Python 3.9+
- Microsoft account (for Graph API)
- Google account (for Gemini API)

## Quick Start

1. Clone the repository
2. Create virtual environment:
   \\\ash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   \\\
3. Install dependencies:
   \\\ash
   pip install -r requirements.txt
   \\\
4. Copy \.env.example\ to \.env\ and add your keys:
   \\\ash
   cp .env.example .env
   # Edit .env with your actual API keys
   \\\
5. Run the agent:
   \\\ash
   python agent.py
   \\\

## Environment Variables

| Variable | Description |
|----------|-------------|
| \GEMINI_API_KEY\ | Google Gemini API key (get from AI Studio) |
| \GRAPH_ACCESS_TOKEN\ | Microsoft Graph temporary token (from Graph Explorer) |

## Security

- Never commit \.env\ or real tokens
- Use \.env.example\ as a template
- Tokens expire — refresh as needed

## License

MIT - For demonstration purposes only
