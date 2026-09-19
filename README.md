# My Personal AI Stack

Hey, thanks for stopping by.
This is just my small home setup for playing with AI tools in one place.
Nothing fancy here. I built it to learn and to make daily work a bit easier.
Feel free to copy it and change it to fit your own needs.

## Why this exists

I wanted chat and search and voice to live together without too much setup.
I also wanted something I can turn off and on with one command.
So I put everything in one compose file and shared it here.

## What lives here

- open-webui on 3000 for chat
- openai-edge-tts on 5050 for voice
- searxng on 8081 for private search
- jina-reader on 8090 for reading web pages
- jina-adapter on 8091 to connect chat to reader
- open-terminal for file browsing
- scrapling on 8000 as MCP for scraping
- hostinger-mcp on 8100 as MCP for Hostinger
- indeepcleaning-dev on 3001 for my web project

## How it fits together

The chat UI is the main door. You talk there.
When you ask for web content, the chat calls the adapter.
The adapter calls the reader and returns clean text.
For search, the chat can use private search.
For voice, the chat can use the voice tool.
The MCP tools just wait on their ports until they are called.

## Quick start

You need Docker plus the compose plugin.
You also need Ollama on your host if you want local models.

- copy env example to env
- fill in your tokens in the new env file
- run compose up
- open localhost 3000 in your browser

```sh
cp .env-example .env
docker compose up
docker compose ps
docker compose logs
docker compose down
```

## Ports

- 3000 for chat UI
- 5050 for voice
- 8081 for private search
- 8090 for reader
- 8091 for adapter
- 8000 for scraper MCP
- 8100 for Hostinger MCP
- 3001 for dev app

## Env vars

These live in your env file. The example file has empty values.

- OPEN_TERMINAL_API_KEY for file browser
- SCRAPLING_MCP_AUTH_TOKEN for scraper auth
- HOSTINGER_API_TOKEN for Hostinger access

## Folders

- openwebui holds chat data
- jina-adapter holds a tiny python adapter
- hostinger-mcp holds the Hostinger MCP build
- searxng holds search settings

## Common issues

If the chat cannot reach Ollama, check that Ollama is running on your host.
If the reader feels slow, try again with a simpler page.
If a port is busy, stop the other app that uses that port and try again.

## Notes

This is for local use and learning. It is not hardened for public servers.
I still tweak it from time to time. Thanks for reading.
