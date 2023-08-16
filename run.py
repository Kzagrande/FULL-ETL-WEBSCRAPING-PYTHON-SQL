import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.main import main_pipeline

if __name__ == "__main__":
    main_pipeline.run_pipeline()