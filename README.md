# ParaBank Automation Framework - Bill Payment Flow

This repository contains a robust QA Automation Framework designed to test the **Bill Payment** flow (simulating a "Payer" experience). The system under test (SUT) is [ParaBank](https://parabank.parasoft.com), a demo banking application.

The project demonstrates the implementation of modern testing practices, including **Data-Driven Testing**, **Contract Testing**, **System Integration Testing (SIT)**, and the **Screenplay Pattern** for UI automation.

## 🛠️ Tech Stack

*   **Language:** Python 3.12
*   **Test Runner:** Pytest 8.3
*   **API Testing:** Requests
*   **Contract Testing:** JSON Schema (`jsonschema`)
*   **UI Testing:** Playwright + ScreenPy (Screenplay Pattern)
*   **BDD:** Pytest-BDD
*   **Reporting:** Pytest-HTML

## 📂 Project Architecture

The framework is structured by testing layers to ensure maintainability and execution speed:

```text
├── features/               # Gherkin feature files (UI / E2E)
├── payloads/               # External JSON payloads for API requests
├── schemas/                # JSON Schemas for Contract Testing
├── screenplay/             # Screenplay Pattern (Tasks, Questions, Abilities)
├── step_defs/              # BDD step definitions for UI
└── tests/
    ├── api/                # Isolated API & Contract tests (Fast feedback)
    └── sit/                # System Integration Tests (Business flows)