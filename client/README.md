# AI-Powered Journal

AI-Powered Journal is a Svelte-based web application that allows users to create, edit, analyze, and manage journal entries. This app integrates AI-powered sentiment analysis and text generation to enhance journal writing.

---

## Features

- **Create Journals**: Add new journal entries.
- **Edit Journals**: Modify existing journal content.
- **AI Text Generation**: Generate text suggestions while editing journal entries.
- **AI Sentiment Analysis**: Analyze the sentiment of journal entries with confidence scores.
- **Delete Journals**: Remove unwanted journal entries.
- **User Authentication**: Secure login/logout functionality.

---

## Installation

Follow these steps to set up the application locally:

### Prerequisites
- Node.js (v14+)
- npm or yarn package manager

### Clone the Repository
```bash
git clone <repository-url>
cd ai-powered-journal


## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```
## Usage
    Log In: Enter your credentials to access the app.
    Add Journal: Click on Add new Journal to create a new entry.
    Edit Journal:
    Click the Edit button next to a journal entry to make changes.
    Once in edit mode, an AI Text Generation button will appear. Click it to let AI suggest text for the entry.
    Save or cancel the changes as needed.
    Analyze with AI: Click Analyze with AI next to an entry to get sentiment insights.
    Delete Entry: Click Delete to remove a journal entry.

## API Endpoints
    The app communicates with the backend using the following API endpoints:

    GET /journal/entries - Retrieve all journal entries.
    POST /journal/entries - Add a new journal entry.
    PUT /journal/entries/:id - Update a journal entry.
    DELETE /journal/entries/:id - Delete a journal entry.
    POST /journal/analyze - Perform sentiment analysis on journal content.
    POST /journal/generate - Generate text based on a prompt.


## This version explicitly states that the **AI Text Generation** button is visible only when a journal entry is in **Edit** mode. Let me know if you’d like further adjustments!
