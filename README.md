# DeveloperZone AI Model Server

## Project Structure

```
DeveloperZone/
├── launchers/                     # Linux & Windows launch scripts
│   ├── master_launcher.sh
│   ├── master_launcher.bat
│   └── env_setup.py
│
├── server/                        # Backend + MCP + DB
│   ├── app.py
│   ├── config/
│   │   ├── agents/
│   │   ├── providers/
│   │   └── registry.json
│   ├── mcp/
│   │   ├── dispatcher.py
│   │   ├── tools/
│   │   └── config.json
│   ├── admin/
│   │   ├── ui/
│   │   ├── logic/
│   │   └── settings/
│   ├── database/
│   │   ├── init_db.sql
│   │   └── fallback.db
│   ├── audio/
│   │   ├── tts/
│   │   └── stt/
│   └── requirements.txt
│
├── frontend/                      # React/Next.js (public user UI)
│   ├── pages/
│   ├── components/
│   ├── assets/
│   ├── store/
│   └── package.json
│
├── .cursor/                       # Cursor Editor integration
│   └── mcp.json
├── .env.example                   # API KEY placeholders
├── .gitignore
├── README.md                      # Full Setup Guide
└── docs/
    ├── providers.md
    ├── agents.md
    ├── mcp_guide.md
    └── architecture.md
```

## Features
- Modular MCP Server for agent requests
- Configurable agents and providers with fallback
- Public utilities (Wikipedia, Weather, Currency, Recipe, Books)
- Audio integration (Voice Input, TTS)
- Windows & Linux launch scripts
- Database and feature management
- Cursor Editor integration

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/azurebluezone/ai.git
cd ai
```

### 2. Environment Setup
- Copy `.env.example` to `.env` and fill in required API keys.
- (Optional) Use `launchers/env_setup.py` for CLI-based environment setup.

### 3. Install Dependencies
#### Backend
```bash
cd server
pip install -r requirements.txt
```
#### Frontend
```bash
cd ../frontend
npm install
```

### 4. Database Initialization
```bash
cd ../server/database
sqlite3 fallback.db < init_db.sql
```

### 5. Configuration
- Edit `server/config/registry.json` to manage tool/agent fallback.
- Add agent/provider configs in their respective folders.
- Set MCP server port/config in `.cursor/mcp.json`.

### 6. Launch the System
#### Linux
```bash
cd ../../launchers
bash master_launcher.sh
```
#### Windows
```
cd launchers
master_launcher.bat
```

### 7. Access
- MCP Server will be available at the configured port.
- Frontend UI (React/Next.js) will be available at its configured port.
- Cursor Editor can connect to MCP for agent/chat/code features.

## Notes
- All configuration is file-based (JSON, .env). No hardcoding.
- At least 2 agents and 3 provider configs with fallback are recommended.
- Admin panel available for database/settings management.
- Modular, cross-platform, and ready for future updates.

## Contribution
- Upload folder/file structure to the correct GitHub repo.
- Include `.env.example` and `README.md`.
- Test MCP with `.cursor/mcp.json`.
- Check both Windows and Linux launchers.
- Keep all config/logic separate (no hardcoding).

---
For detailed guides, see the `docs/` folder.

