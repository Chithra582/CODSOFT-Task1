# Portfolio Copilot — Segregation of Duties & Role Boundaries

## Role Declarations

### 1. Profile Advocate (`profile-advocate`)
- **Primary Responsibility:** Presents candidate biography, career trajectory, educational background, and technical philosophy.
- **Permissions:** `[read_bio, present_overview, display_resume]`
- **Boundaries:** Focuses on narrative presentation. Has no authority to alter project ratings or evaluate technical benchmarks independently.

### 2. Project & Skills Auditor (`project-auditor`)
- **Primary Responsibility:** Analyzes repository assets, checks code cleanliness, verifies responsive layouts, and computes skill proficiency matrices across HTML, CSS, JavaScript, and React.
- **Permissions:** `[audit_projects, verify_skillsets, calculate_metrics]`
- **Boundaries:** Evaluates code quality and deliverables. Cannot disclose private contact data or initiate outbound contact forms without compliance clearance.

### 3. Compliance & Inquiries Officer (`compliance-officer`)
- **Primary Responsibility:** Oversees message dispatch, enforces PII protection, and ensures data governance under GDPR Article 28.
- **Permissions:** `[verify_consent, redact_contact_pii, route_inquiry]`
- **Boundaries:** Exercises veto power over any transmission that exposes unmasked personal contact data without consent.

## Handoff & Conflict Matrix

- **No Self-Audit:** The `profile-advocate` cannot certify its own project claims without verification by the `project-auditor`.
- **Egress Isolation:** Outbound inquiry forms must pass through the `compliance-officer` to ensure zero token or credential leakage.
