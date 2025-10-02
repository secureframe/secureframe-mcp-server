#!/usr/bin/env python3
import os
from typing import Dict, Any, Optional

from fastmcp import FastMCP
from pydantic import BaseModel, Field
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize MCP server
mcp = FastMCP(
    name="Secureframe MCP Server",
    instructions="Read-only access to Secureframe compliance platform data"
)

# Configuration
class SecureframeConfig(BaseModel):
    """Secureframe API configuration"""
    api_key: str
    api_secret: str
    base_url: str = "https://api.secureframe.com"
    
    def __init__(self):
        super().__init__(
            api_key=os.getenv("SECUREFRAME_API_KEY", ""),
            api_secret=os.getenv("SECUREFRAME_API_SECRET", ""),
            base_url=os.getenv("SECUREFRAME_API_URL", "https://api.secureframe.com")
        )
        
        if not self.api_key or not self.api_secret:
            raise ValueError(
                "SECUREFRAME_API_KEY and SECUREFRAME_API_SECRET environment variables must be set"
            )
    
    @property
    def headers(self) -> Dict[str, str]:
        """Authorization headers"""
        return {
            "Authorization": f"{self.api_key} {self.api_secret}",
            "Content-Type": "application/json"
        }

config = SecureframeConfig()

# Helper functions
async def make_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Make API request to Secureframe"""
    url = f"{config.base_url}{endpoint}"
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.request(
                method=method,
                url=url,
                headers=config.headers,
                params=params,
                json=json_data
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API Error {e.response.status_code}: {e.response.text}"}
        except Exception as e:
            return {"error": str(e)}

# Controls Tools (read-only)
@mcp.tool
async def list_controls(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter controls"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List security controls with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/controls", params=params)

# Tests Tools (read-only)
@mcp.tool
async def list_tests(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter tests"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List compliance tests with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/tests", params=params)

# Users Tools (read-only)
@mcp.tool
async def list_users(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter users"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List users with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/users", params=params)

# Devices Tools (read-only)
@mcp.tool
async def list_devices(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter devices"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List devices with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/devices", params=params)

# Frameworks Tools (read-only)
@mcp.tool
async def list_frameworks(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter frameworks"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List compliance frameworks with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/frameworks", params=params)

# Vendors Tools (read-only)
@mcp.tool
async def list_vendors(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter vendors"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List vendors (legacy) with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/vendors", params=params)

# TPRM Vendors Tools (read-only)
@mcp.tool
async def list_tprm_vendors(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter vendors"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List TPRM vendors with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/tprm/vendors", params=params)

# Integration Connections Tools (read-only)
@mcp.tool
async def list_integration_connections(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter connections"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List integration connections with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/integration_connections", params=params)

# Repository Framework Scopes Tools (read-only)
@mcp.tool
async def list_repository_framework_scopes(
    repository_id: str = Field(..., description="ID of the repository"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List framework scopes for a repository"""
    params = {}
    if include_relationships:
        params["include"] = True
    
    return await make_request(
        "GET", 
        f"/repositories/{repository_id}/framework_asset_scopes",
        params=params
    )

# User Accounts Tools (read-only)
@mcp.tool
async def list_user_accounts(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter accounts"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List user accounts with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/user_accounts", params=params)

# Repositories Tools (read-only)
@mcp.tool
async def list_repositories(
    page: int = Field(1, description="Page number for pagination"),
    per_page: int = Field(100, description="Items per page (default: 100)"),
    search_query: Optional[str] = Field(None, description="Lucene search query to filter repositories"),
    include_relationships: bool = Field(False, description="Include relationship data")
) -> Dict[str, Any]:
    """List repositories with filtering support"""
    params = {
        "page": page,
        "per_page": per_page,
        "relationships": include_relationships
    }
    if search_query:
        params["q"] = search_query
    if include_relationships:
        params["include"] = True
    
    return await make_request("GET", "/repositories", params=params)

def main():
    """Run the MCP server"""
    mcp.run()

if __name__ == "__main__":
    main() 