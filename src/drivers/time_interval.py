import os
import sys
project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from datetime import datetime, timedelta
# from run_control_table import PendingAtuomations


def get_current_and_last_hour():
        
    # if PendingAtuomations:
    #     pending_class = PendingAtuomations
    #     pending_hour = pending_class.pending_hour 
    #     print(pending_hour)
        # hora atual tirando um milisegundo
    
    
    now = datetime.now()
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


        # cursor = DatabaseConnection.connection.cursor()
        # current_time = datetime.now()
        # query = "SELECT id, name FROM control_automations WHERE scheduled_time <= %s AND status = False"
        # cursor.execute(query, (current_time,))
        # pending_automations = cursor.fetchall()
        # for automation_id, automation_name in pending_automations:
        #     try:
        #         if automation_name in sectors:
        #             sector = sectors[automation_name]
        #             sector() 
        #         else:
        #             print(
        #                 f"Nenhuma função correspondente encontrada para '{automation_name}'"
        #             )

        #         # Marcar a automação como executada
        #         self.hc()
        #         self.procedure()
        #         update_query = "UPDATE automations SET status = 1 WHERE id = %s"
        #         cursor.execute(update_query, (automation_id,))
        #         DatabaseConnection.connection.commit()

        #         print(f"Automação '{automation_name}' executada com sucesso.")
        #     except Exception as e:
        #         print(f"Erro ao executar a automação '{automation_name}': {str(e)}")