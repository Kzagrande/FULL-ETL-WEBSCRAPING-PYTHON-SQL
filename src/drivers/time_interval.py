import os
import sys
project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from datetime import datetime, timedelta
# from run_control_table import PendingAtuomations


def get_current_and_last_hour(pending_automation=None):
       
    if(pending_automation):
        now = pending_automation
        now = now.replace(minute=0, second=0, microsecond=0)
        one_second = timedelta(seconds=1)
        last_second = now - one_second
        format_last_second = last_second.strftime("%Y-%m-%d %H:%M:%S")

        # hora passada
        one_hour = timedelta(hours=1)
        last_hour = now - one_hour
        format_last_hour = last_hour.strftime("%Y-%m-%d %H:%M:%S")

        result = {"last_second": format_last_second, "last_hour": format_last_hour}

        print("last_second", format_last_second)
        print("last_hour", format_last_hour)
        return result
        
    # else:     
    #     print('Não é uma automação pendente')  
    #     now = datetime.now()
    #     now = now.replace(minute=0, second=0, microsecond=0)
    #     one_second = timedelta(seconds=1)
    #     last_second = now - one_second
    #     format_last_second = last_second.strftime("%Y-%m-%d %H:%M:%S")

    #     # hora passada
    #     one_hour = timedelta(hours=1)
    #     last_hour = now - one_hour
    #     format_last_hour = last_hour.strftime("%Y-%m-%d %H:%M:%S")

    #     result = {"last_second": format_last_second, "last_hour": format_last_hour}

    #     print("last_second", format_last_second)
    #     print("last_hour", format_last_hour)
    #     return result