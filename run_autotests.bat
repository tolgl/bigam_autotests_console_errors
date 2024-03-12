rm -r allure_results/*
pytest tests/ --alluredir=allure_results
python send_message_telegram.py
pause