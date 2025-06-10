# Secureframe MCP Server - Parameter Reference Guide

This document provides common examples of parameter values that can be used in the Secureframe MCP Server.

## Table of Contents
- [User & Personnel](#user--personnel)
- [Vendors & Risk Management](#vendors--risk-management)
- [Controls & Tests](#controls--tests)
- [Repositories](#repositories)
- [Search Query Examples](#search-query-examples)

---

## User & Personnel

### Employee Types
```
employee_type:
  - employee
  - contractor
  - non_employee
  - auditor
  - external
```

---

## Vendors & Risk Management

### Vendor Status
```
status: draft | completed
risk_level: Low | Medium | High
archived: true | false
```

---

## Controls & Tests

### Control Attributes
```
health_status: healthy | unhealthy | draft
implementation_status: implemented | not_implemented
```

### Tests Attributes
```
health_status: pass | fail | disabled
test_type: integration | upload
```


### Test Domain Examples
```
test_domain:
  - Network Security
  - Data Security
  - Identity and Access Management
  - Vulnerability Management
  - Governance
```

### Framework Examples
```
framework keys:
  - soc2_alpha
  - iso27001
  - iso27001_2022
  - CIS_IG1
  - hipaa
  - cmmc_l2
  - FedRAMP_Low
  - FedRAMP_Moderate
  - FedRAMP_High
  - FedRAMP_20x
```

---

## Repositories

### Repository Attributes
```
vendor_name: Github | Gitlab | Bitbucket
private: true | false
in_audit_scope: true | false
```

---

## Search Query Examples

### Controls
```lucene
# Find unhealthy controls
health_status:unhealthy

# Find unimplemented SOC2 controls
implementation_status:not_implemented AND frameworks:soc2_alpha

# Find custom controls
custom:true AND health_status:draft
```

### Tests
```lucene
# Find failing tests
health_status:fail

# Find disabled integration tests
health_status:disabled AND test_type:integration

# Find upload tests that need evidence
test_type:upload AND health_status:fail
```

### Users
```lucene
# Find inactive contractors
employee_type:contractor AND active:false

# Find users not in audit scope
in_audit_scope:false AND active:true

# Find external auditors
employee_type:auditor
```

### Vendors
```lucene
# Find high-risk vendors
risk_level:High

# Find archived vendors
archived:true

# Find draft vendors
status:draft AND archived:false
```

### Repositories
```lucene
# Find private GitHub repositories
vendor_name:Github AND private:true

# Find public repositories in audit scope
private:false AND in_audit_scope:true
```

---

## Notes

1. **Case Sensitivity**: Most parameter values are case-sensitive as shown above.
2. **Boolean Values**: Use lowercase `true` or `false` for boolean fields.
3. **Date Formats**: Use ISO8601 format for dates (e.g., `2024-01-15` or `2024-01-15T10:30:00Z`).
4. **Lucene Syntax**: Search queries support full Lucene query syntax including AND, OR, NOT, wildcards (*), and field grouping.