import sys
project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.infra.database_connector import DatabaseConnection
from datetime import datetime
from src.main.main_pipeline import MainPipeline


class PendingAtuomations:
    pending_hour = []
        
    def run_pending_automations(self) -> None:
        sectors = {
            "Sorting_in": MainPipeline.sorting_in,
            "Putaway": MainPipeline.putaway,
            "Picking": MainPipeline.picking,
            "Sorting_out": MainPipeline.sorting_out,
            "Packing": MainPipeline.packing,
            # Adicione aqui as demais funções
        }

        DatabaseConnection.connect()
        cursor = DatabaseConnection.connection.cursor()
        current_time = datetime.now()
        query = "SELECT id, name,scheduled_time FROM ware_ws_shein.control_automations WHERE scheduled_time <= %s AND status = False"
        cursor.execute(query, (current_time,))
        pending_automations = cursor.fetchall()
        print(pending_automations[0][2])

        for automation_id, automation_name, scheduled_time in pending_automations:
            try:
                if automation_name in sectors:
                    sector = sectors[automation_name]
                    # self.pending_hour = []
                    # self.pending_hour.append(automation_id)
                    sector(self)
                else:
                    print(f"No corresponding function found for '{automation_name}'")

                # Mark automation as executed
                MainPipeline.hc(self)
                MainPipeline.procedures(self)

                update_query = "UPDATE automations SET status = 1 WHERE id = %s"
                with DatabaseConnection.connection.cursor() as cursor:
                    cursor.execute(update_query, (automation_id,))
                    DatabaseConnection.connection.commit()

                print(f"Automation '{automation_name}' executed successfully.")

            except Exception as e:
                print(f"Error: {str(e)}")


if __name__ == "__main__":
    pending = PendingAtuomations()
    pending.run_pending_automations()
