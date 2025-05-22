import pytest
from datetime import datetime
import os


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     # Always use the project root for reports
#     report_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'reports'))
#     os.makedirs(report_dir, exist_ok=True)
#
#     report_gen_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     config.option.htmlpath = os.path.join(report_dir, f"report_{report_gen_time}.html")


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    print('Starting')
    yield
    print('End')

