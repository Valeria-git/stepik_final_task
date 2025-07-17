# Stepik Final Task

This is the final project for the Stepik Selenium course.

## How to run tests

To run any test file, use the following command:

```bash
pytest -v --tb=line --language=en FILE_NAME.py
```

If you are reviewing this project, please use the following command to run the key tests marked with `@pytest.mark.need_review`:

```bash
pytest -v --tb=line --language=en -m need_review
```

## Project structure

The structure of this project differs slightly from the one suggested in the original task:

- `/utils/` – contains helper functions for generating random emails and passwords.
- `test_data.py` – stores links and test-related constants.

## Notes
If you have issues with running my test, try to change imports paths/delete __init__.py files/change version of pytest and selenium