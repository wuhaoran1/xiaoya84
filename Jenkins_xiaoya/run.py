import pytest
import os
from datetime import datetime
from config.path import reports_dir
reports_file = os.path.join(reports_dir,"report-")
ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
reports_name = reports_file + ts
if __name__ == '__main__':
    pytest.main(["--html={}.html".format(reports_name)])
  
