## Plan: Repository Pattern and SQLAlchemy Integration

Introduce a clean abstraction layer for model metadata using the Repository pattern, transitioning from JSON files to a structured database approach starting with an in-memory implementation.

### Phase 1: Repository Pattern implementation
1. Create the `model_registry/repository/` directory with `__init__.py`.
2. Define the abstract base class `BaseRepository` in `model_registry/repository/base.py` using `abc.ABC`. It should include methods: `create`, `get_by_name`, `update`, and `list_all`.
3. Create a Pydantic schema or Dataclass for `ModelMetadata` in `model_registry/repository/models.py` to standardize the metadata structure (name, total_features, artifact_path, etc.).
4. Implement `InMemoryRepository` in `model_registry/repository/in_memory.py` to store metadata in a dictionary, allowing the system to run without a real database for now.
5. Refactor `ModelRegistry` in `model_registry/model_registry.py` to accept a repository instance in its constructor, decoupling it from direct filesystem JSON operations.

### Phase 2: Dependency Management
1. Update `pyproject.toml` to include `sqlalchemy` and `psycopg2-binary` (PostgreSQL driver) under `[project.dependencies]`.
2. (Optional but recommended) Create a `model_registry/database.py` file to hold the SQLAlchemy `engine` and `session` configuration, preparing for the future PostgreSQL implementation.

### Phase 3: Verification and Testing
1. Create `tests/model_registry/test_repository.py` to specifically test the `InMemoryRepository` implementation.
2. Update existing tests in `tests/model_registry/test_model_registry.py` to inject the `InMemoryRepository` into the `ModelRegistry` class.
3. Ensure that model artifacts (the `.pkl` files) are still correctly managed on the filesystem while their metadata moves to the repository.

**Relevant files**
- `model_registry/model_registry.py` — Refactor to use the new repository for metadata operations.
- `pyproject.toml` — Add `sqlalchemy` and `psycopg2-binary`.
- `model_registry/repository/base.py` — New ABC for the repository.
- `model_registry/repository/in_memory.py` — New in-memory implementation.
- `model_registry/repository/models.py` — New metadata schema definition.

**Verification**
1. Run `pytest tests/model_registry/` to ensure all existing functionality is preserved.
2. Verify that metadata is correctly stored and retrieved from the `InMemoryRepository` during test execution.
3. Run `pip install .` (or equivalent) to verify that new dependencies are correctly resolved.

**Decisions**
- **Metadata vs. Artifacts**: The model artifacts (the `.pkl` files) will remain on the filesystem for now, while only the metadata (JSON fields) is moved to the Repository pattern.
- **In-Memory First**: The `InMemoryRepository` will be the default implementation used by `ModelRegistry` to maintain current functionality without requiring a running PostgreSQL instance immediately.

**Further Considerations**
1. Would you like the `ModelMetadata` to be defined using **SQLAlchemy Declarative Base** immediately, or should I start with a simple **Pydantic** model that can later be mapped? (I recommend starting with Pydantic for the `InMemory` version).
2. Should we implement an `Async` version of the repository, or stay with `Sync` for now? (The current implementation is sync).
