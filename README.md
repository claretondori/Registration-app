#  University Course Registration Engine

A production-ready, asynchronous academic course registration backend engine engineered with FastAPI, SQLAlchemy, and PostgreSQL using the Repository-Service software design pattern.

---

##  Core Technologies
*   **Framework:** FastAPI (Asynchronous Python Web Framework)
*   **Database ORM:** SQLAlchemy (Asyncio Execution Mode)
*   **Data Validation:** Pydantic V2 (Data Transfer Objects)
*   **Architecture Pattern:** Repository-Service / Layered Architecture

---

##  System Domain & Academic Logic

This system functions as the administrative backbone for university operations, managing course constraints, student enrollments, faculty profiles, and schedule assignments while ensuring strict relational data invariants.

###  Core System Responsibilities

*   **Student Lifecycle Gateway (`student.py`):** Coordinates academic enrollment tracking, profile attributes, and course registration validation pipelines.
*   **Faculty Allocation Engine (`teacher.py`):** Manages instructor assignments, teaching rosters, department bounds, and catalog allocation.
*   **Academic Catalog Ledger (`course.py`):** Enforces course parameters, capacities, student roster limits, and curriculum relations.
*   **Decoupled Multi-Tier Processing:** Isolates incoming HTTP API routing (`routers/`) from application workflows (`services/`), database actions (`repositories/`), and storage models (`models/`).

---

##  Architectural Topology

The application enforces strict isolation of concerns so infrastructure changes do not alter domain business rules:

```text
app/
├── core/             # System infrastructure configurations & security constants
├── models/           # Data Layer: Declarative SQLAlchemy relational entities (Student, Teacher, Course)
├── schemas/          # Boundary Layer: Strict Pydantic serialization schemas and input DTOs
├── repositories/     # Data Access Layer: Encapsulated SQL generation and entity CRUD rules
├── services/         # Business Logic Layer: Handles cross-entity rules (e.g., enrolling a student in a course)
├── routers/          # Presentation Layer: FastAPI REST endpoint handlers and status lifecycle mappings
├── database.py       # Asynchronous session context manager and database connection engine
└── main.py           # Application bootstrap gateway
```

---

##  System Domain Layer Matrix

The application coordinates an interconnected matrix of transactional administrative modules:

| Sub-Domain Layer | Core Model | Architectural Responsibility | Inter-dependencies |
| :--- | :--- | :--- | :--- |
| **Registrar Space** | `Student` | Profiles, enrollment tracks, course rosters | `Course` |
| **Faculty Space** | `Teacher` | Staff registries, department mapping, course distribution | `Course` |
| **Catalog Space** | `Course` | Capacity guardrails, schedules, database relationship mapping | `Student`, `Teacher` |

---

##  Local Infrastructure Setup

### Prerequisite Dependencies
*   **Python Engine:** `v3.11+`
*   **Database Engine:** `PostgreSQL 15+` (or alternative target relational DB)

### 1. Workspace Isolation
Clone the layout structure to your workstation and establish your virtual execution runtime environment:
```bash
git clone https://github.com
cd academic-registration-engine

# Initialize runtime container
python3 -m venv env
source env/bin/activate
```

### 2. Dependency Ingestion
Compile and bind the core infrastructure dependencies directly into your application space:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Application Launch
Spin up the ASGI web server engine with development monitors enabled:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
*   **Interactive OpenAPI Documentation (Swagger UI):** `http://localhost:8000/docs`
*   **Alternative Schema Interface (ReDoc):** `http://localhost:8000/redoc`

---

##  Platform Scalability Targets
*   **Concurrency Locks:** Implement distributed transaction locks to prevent race conditions when two students attempt to claim the final open seat in a course simultaneously.
*   **Data Migrations:** Integrate Alembic migration timelines to execute safe production database schema updates without transaction loss.
