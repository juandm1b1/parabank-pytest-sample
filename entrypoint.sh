#!/bin/bash

echo "========================================="
echo "Starting Phase 1: API and SIT"
echo "========================================="
pytest -m "not ui" -p no:allure_pytest_bdd --alluredir=allure-results --clean-alluredir || true

echo "========================================="
echo "Starting Phase 2: UI (BDD)"
echo "========================================="
pytest -m "ui" -p no:allure_pytest --alluredir=allure-results || true

echo "========================================="
echo "Generating Unified Allure Report"
echo "========================================="
allure generate allure-results --clean -o allure-report
echo "Report successfully generated in /app/allure-report!"