#!/usr/bin/env python3
"""
CEO Daily Briefing Agent - Email Only Demo
Fetches unread emails from Outlook, prioritizes with Gemini (new SDK)
"""

import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from google import genai
from google.genai import types

load_dotenv()

# Configuration
GRAPH_API_URL = "https://graph.microsoft.com/v1.0/me/messages"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ACCESS_TOKEN = os.getenv("GRAPH_ACCESS_TOKEN")

def fetch_unread_emails(token, limit=20):
    """Fetch unread emails from Outlook"""
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "$filter": "isRead eq false",
        "$top": limit,
        "$orderby": "receivedDateTime desc",
        "$select": "subject,from,receivedDateTime,bodyPreview"
    }
    
    print(f"📧 Fetching up to {limit} unread emails...")
    response = requests.get(GRAPH_API_URL, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        print(response.json())
        return []
    
    emails = response.json().get("value", [])
    print(f"✅ Found {len(emails)} unread emails")
    return emails

def prioritize_with_gemini(emails):
    """Send emails to Gemini for prioritization using new SDK"""
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # Format emails for prompt
    email_text = ""
    for i, email in enumerate(emails, 1):
        sender = email['from']['emailAddress']['address']
        subject = email['subject']
        preview = email.get('bodyPreview', 'No preview')[:200]
        email_text += f"\n{i}. From: {sender}\n   Subject: {subject}\n   Preview: {preview}\n"
    
    prompt = f"""You are an executive briefing agent. Below are {len(emails)} unread emails.

Output:
1. TOP 3 MUST-RESPOND - List the 3 most urgent emails.
   For each: [Sender] | [Subject] | WHY respond (1 sentence)

2. SUGGESTED ACTIONS - One action for each of the top 3.

EMAILS:
{email_text}"""
    
    print("🤖 Sending to Gemini for prioritization...")
    
    # Use gemini-2.0-flash (fast, efficient, widely available)
    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=prompt
    )
    
    print("✅ Prioritization complete")
    return response.text

def save_briefing(briefing, email_count):
    """Save briefing to markdown file"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"briefing_{timestamp}.md"
    
    with open(filename, "w") as f:
        f.write(f"# CEO Daily Briefing\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Emails analyzed:** {email_count}\n\n")
        f.write("---\n\n")
        f.write(briefing)
    
    print(f"💾 Saved to {filename}")
    return filename

def main():
    print("\n" + "="*50)
    print("🤖 CEO BRIEFING AGENT (EMAIL ONLY)")
    print("="*50 + "\n")
    
    if not GEMINI_API_KEY:
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print("Add: GEMINI_API_KEY=your_key_here")
        return
    
    if not ACCESS_TOKEN or ACCESS_TOKEN == "PASTE_YOUR_GRAPH_EXPLORER_TOKEN_HERE":
        print("❌ Error: GRAPH_ACCESS_TOKEN not configured")
        print("Get a fresh token from Graph Explorer")
        return
    
    emails = fetch_unread_emails(ACCESS_TOKEN)
    
    if not emails:
        print("No unread emails found. Send yourself a test email and try again.")
        return
    
    briefing = prioritize_with_gemini(emails)
    
    print("\n" + "="*50)
    print("📋 BRIEFING")
    print("="*50 + "\n")
    print(briefing)
    
    save_briefing(briefing, len(emails))
    print("\n✅ Demo complete!")

if __name__ == "__main__":
    main()    
