# Secureframe MCP Server

This [Model Context Protocol](https://modelcontextprotocol.io/) server provides read-only access to Secureframe's compliance automation platform for AI assistants like Claude and Cursor. Query security controls, monitor compliance tests, and access audit data across SOC 2, ISO 27001, CMMC, FedRAMP, and other frameworks.

⚠️ **Disclaimer**: This MCP server is currently in public beta and grants AI assistants read-only access to your Secureframe compliance data. While the server only performs read operations, always review and validate AI-generated insights before making any compliance or security decisions. You are responsible for ensuring all AI outputs align with your organization's compliance policies and security standards.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Secureframe API credentials ([Get them here](#-obtaining-api-credentials))
- Claude Desktop, Cursor IDE, or any MCP-compatible tool

### Installation

```bash
# Clone and setup
git clone https://github.com/secureframe/secureframe-mcp-server.git
cd secureframe-mcp-server

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure credentials
cp env.example .env
# Edit .env with your API credentials
```

---

## 🔧 Configuration

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "secureframe": {
      "command": "python",
      "args": ["/absolute/path/to/secureframe-mcp-server/main.py"],
      "env": {
        "SECUREFRAME_API_KEY": "your_api_key",
        "SECUREFRAME_API_SECRET": "your_api_secret",
        "SECUREFRAME_API_URL": "https://api.secureframe.com"
      }
    }
  }
}
```

### Cursor IDE

Configure in Cursor's MCP settings:

```json
{
  "mcpServers": {
    "Secureframe": {
      "command": "python",
      "args": ["/absolute/path/to/secureframe-mcp-server/main.py"],
      "env": {
        "SECUREFRAME_API_KEY": "your_api_key",
        "SECUREFRAME_API_SECRET": "your_api_secret",
        "SECUREFRAME_API_URL": "https://api.secureframe.com"
      }
    }
  }
}
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECUREFRAME_API_KEY` | Your Secureframe API key | ✅ |
| `SECUREFRAME_API_SECRET` | Your Secureframe API secret | ✅ |
| `SECUREFRAME_API_URL` | API endpoint (defaults to US region) | ❌ |

**Regional Endpoints:**
- 🇺🇸 US: `https://api.secureframe.com` (default)
- 🇬🇧 UK: `https://api-uk.secureframe.com`

---

## 📋 Available Tools (11 Read-Only Operations)

| Tool | Purpose |
|------|---------|
| **list_controls** | List security controls across frameworks with filtering |
| **list_tests** | List compliance tests with pass/fail status |
| **list_users** | List personnel and their compliance status |
| **list_devices** | List managed devices and security compliance |
| **list_user_accounts** | List user accounts from integrations |
| **list_tprm_vendors** | List third-party risk management vendors |
| **list_vendors** | List vendors (legacy API) |
| **list_frameworks** | List available compliance frameworks |
| **list_repositories** | List code repositories and audit scope |
| **list_integration_connections** | List integration status and connections |
| **list_repository_framework_scopes** | List framework scopes for specific repositories |

---

## 💡 Usage Examples

### Monitor Failing Controls
```python
# Find controls that need attention for SOC 2
list_controls(
    search_query="health_status:unhealthy AND frameworks:soc2_alpha",
    per_page=50
)
```

### Find Failing Tests
```python
# Get top 5 failing tests
list_tests(
    search_query="health_status:fail",
    per_page=5
)
```

### Review High-Risk Vendors
```python
# Find high-risk vendors
list_tprm_vendors(
    search_query="risk_level:High",
    per_page=20
)
```

### Check User Compliance
```python
# Find inactive contractors
list_users(
    search_query="employee_type:contractor AND active:false",
    per_page=100
)
```

---

## 🔍 Search Capabilities

The server supports powerful [Lucene query syntax](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html) for filtering:

### Example Queries

**Find critical failing tests:**
```
health_status:fail AND frameworks:soc2_alpha
```

**Locate inactive users:**
```
active:false AND employee_type:contractor
```

**Search high-risk vendors:**
```
risk_level:High AND archived:false
```

### Common Search Fields

<details>
<summary><strong>Controls & Tests</strong></summary>

- `health_status` - For controls: healthy, unhealthy, draft. For tests: pass, fail, disabled
- `enabled` - true/false
- `test_type` - integration, upload

</details>

<details>
<summary><strong>Personnel</strong></summary>

- `active` - true/false
- `email` - User email address
- `employee_type` - employee, contractor, non_employee, auditor, external
- `in_audit_scope` - true/false

</details>

<details>
<summary><strong>Vendors (TPRM)</strong></summary>

- `risk_level` - Low, Medium, High
- `status` - draft, completed
- `archived` - true/false

</details>

<details>
<summary><strong>Repositories</strong></summary>

- `private` - true/false
- `in_audit_scope` - true/false

</details>

---

## 🛠️ Development

### Debug with MCP Inspector
```bash
npx @modelcontextprotocol/inspector python main.py
```

---

## 📚 Resources

- [Secureframe API Documentation](https://developer.secureframe.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Parameter Reference Guide](PARAMETER_REFERENCE.md)

---

## 🎯 Obtaining API Credentials

1. Log into [Secureframe](https://app.secureframe.com)
2. Navigate to Profile Picture → Company Settings → [API Keys](https://app.secureframe.com/company-settings/api-keys)
3. Click **Create API Key**
4. Save your credentials securely (secret shown only once)

---

## ⚖️ License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
