# 🎯 Mysung Customer Support System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://cloud.google.com/agent-development-kit)
[![Vertex AI](https://img.shields.io/badge/Vertex-AI-4285F4.svg)](https://cloud.google.com/vertex-ai)

A sophisticated AI-powered customer support system built with Google Agent Development Kit (ADK) and Vertex AI Search, providing intelligent document-based question answering for customer inquiries.

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [System Workflow](#system-workflow)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🤖 **AI Agent** | Intelligent customer support agent powered by Gemini 2 Flash | ✅ Active |
| 🔍 **Vertex AI Search** | Advanced document search and retrieval | ✅ Active |
| 📚 **Document QA** | Context-aware question answering from knowledge base | ✅ Active |
| 🎯 **Smart Routing** | Automatic query routing to appropriate data stores | ✅ Active |
| 🚀 **Fast Responses** | Optimized with Gemini Flash model for quick replies | ✅ Active |
| 📊 **Structured Data** | Organized information retrieval and presentation | ✅ Active |

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        A[Customer Query] --> B[API Gateway]
    end
    
    subgraph "Agent Layer"
        B --> C[LLM Agent]
        C --> D{Query Analysis}
    end
    
    subgraph "Tools Layer"
        D --> E[Vertex AI Search Tool]
        E --> F[Data Store]
    end
    
    subgraph "AI Models"
        C --> G[Gemini 2 Flash Model]
        G --> H[Response Generation]
    end
    
    subgraph "Storage"
        F --> I[(Knowledge Base)]
        F --> J[(Document Store)]
    end
    
    H --> K[Formatted Response]
    K --> B
    B --> L[Customer]
    
    style A fill:#e1f5ff
    style L fill:#e1f5ff
    style C fill:#fff3e0
    style G fill:#f3e5f5
    style F fill:#e8f5e9
```

## 🔄 System Workflow

```mermaid
sequenceDiagram
    participant C as Customer
    participant A as LLM Agent
    participant V as Vertex AI Search
    participant D as Data Store
    participant G as Gemini Model
    
    C->>A: Submit Question
    A->>A: Analyze Intent
    A->>V: Search Query
    V->>D: Retrieve Documents
    D-->>V: Return Results
    V-->>A: Relevant Documents
    A->>G: Generate Response
    G-->>A: AI-Generated Answer
    A->>A: Validate & Format
    A-->>C: Send Response
    
    Note over A,G: If no relevant docs found
    A-->>C: "Information not available"
```

## 🔧 Prerequisites

Before you begin, ensure you have the following installed and configured:

| Requirement | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Runtime environment |
| **Google Cloud Account** | - | Access to GCP services |
| **Vertex AI API** | Enabled | AI/ML capabilities |
| **Vertex AI Search** | Configured | Document search functionality |
| **Google ADK** | Latest | Agent development framework |

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Yash-Kavaiya/mysung-customer-support.git
cd mysung-customer-support
```

### Step 2: Set Up Python Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
cd adk-backend
pip install -r requirements.txt
```

### Step 4: Configure Google Cloud

```bash
# Authenticate with Google Cloud
gcloud auth application-default login

# Set your project
gcloud config set project YOUR_PROJECT_ID
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the `adk-backend` directory:

```env
GOOGLE_CLOUD_PROJECT=your-project-id
DATASTORE_PATH=your-datastore-path
AGENT_NAME_VSEARCH=mysung-support-agent
GEMINI_2_FLASH=gemini-2.0-flash-exp
```

### Configuration Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `DATASTORE_PATH` | String | Vertex AI Search datastore ID | Required |
| `AGENT_NAME_VSEARCH` | String | Name identifier for the agent | `mysung-support-agent` |
| `GEMINI_2_FLASH` | String | Gemini model version | `gemini-2.0-flash-exp` |
| `model` | String | AI model to use | Gemini 2 Flash |
| `instruction` | String | Agent system prompt | Customizable |

### Data Store Setup

1. **Create a Vertex AI Search Data Store:**
   - Go to Google Cloud Console
   - Navigate to Vertex AI Search
   - Create a new data store
   - Upload your knowledge base documents

2. **Update Configuration:**
   - Copy your data store path
   - Update `DATASTORE_PATH` in `agent.py`

## 🚀 Usage

### Starting the Agent

```python
from adk_backend.agent import root_agent

# The agent is ready to use
response = root_agent.query("How do I reset my password?")
print(response)
```

### Example Queries

```python
# Customer support query
response = root_agent.query("What are your business hours?")

# Product information
response = root_agent.query("Tell me about warranty coverage")

# Troubleshooting
response = root_agent.query("My device won't turn on")
```

### Response Flow

```mermaid
flowchart LR
    A[User Query] --> B{Has Context?}
    B -->|Yes| C[Search Documents]
    B -->|No| D[Request Clarification]
    C --> E{Found Info?}
    E -->|Yes| F[Generate Answer]
    E -->|No| G[Return Not Found]
    F --> H[Return Response]
    G --> H
    D --> H
    
    style F fill:#c8e6c9
    style G fill:#ffcdd2
    style H fill:#e1f5ff
```

## 📁 Project Structure

```
mysung-customer-support/
│
├── adk-backend/              # Backend agent implementation
│   ├── __init__.py          # Package initialization
│   ├── agent.py             # Main agent configuration
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables (not in repo)
│
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `agent.py` | Core agent logic with LLM and search tool integration |
| `requirements.txt` | Python package dependencies |
| `__init__.py` | Python package initialization |
| `.env` | Environment configuration (local only) |

## 🛠️ Technology Stack

```mermaid
graph TD
    A[Mysung Customer Support] --> B[Google ADK]
    A --> C[Vertex AI Search]
    A --> D[Gemini 2 Flash]
    
    B --> E[Agent Framework]
    B --> F[Tool Integration]
    
    C --> G[Document Indexing]
    C --> H[Semantic Search]
    
    D --> I[Natural Language Processing]
    D --> J[Response Generation]
    
    style A fill:#4285F4,color:#fff
    style B fill:#34A853,color:#fff
    style C fill:#FBBC04,color:#000
    style D fill:#EA4335,color:#fff
```

### Core Technologies

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Google ADK** | Latest | Agent development framework |
| **Vertex AI Search** | - | Enterprise search solution |
| **Gemini 2 Flash** | Latest | Large language model |
| **Python** | 3.8+ | Programming language |

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Commit with clear messages**
   ```bash
   git commit -m "Add: your feature description"
   ```
5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request**

### Development Workflow

```mermaid
gitGraph
    commit id: "Initial"
    branch feature
    checkout feature
    commit id: "Add feature"
    commit id: "Add tests"
    checkout main
    merge feature
    commit id: "Release"
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues:

- 📧 Email: support@mysung.com
- 🐛 Issues: [GitHub Issues](https://github.com/Yash-Kavaiya/mysung-customer-support/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/Yash-Kavaiya/mysung-customer-support/discussions)

## 🙏 Acknowledgments

- Google Cloud Platform for ADK and Vertex AI
- Gemini team for the powerful language model
- All contributors to this project

---

<div align="center">

**Made with ❤️ by the Mysung Team**

[⬆ Back to Top](#-mysung-customer-support-system)

</div>